import json
from typing import Optional

from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from tools.weather import get_weather
from tools.cmd import run_command
load_dotenv()

client = OpenAI()

def agent():

    available_tools = {
        "get_weather":get_weather,
        "run_command": run_command
    }
    SYSTEM_PROMPT = """
        You're an expert AI Assistant in resolving user queries using chain of thought
        You work on START, PLAN and OUTPUT steps.
        You need to first PLAN what needs to be done. The PLAN can be multiple steps.
        Once you think enough PLAN has been done, finally you can give an OUTPUT
        You can also call a tool if required from the list of available tools
        For every tool call wait for the observe step which is the output from the tool call

        Rule:
        - Strictly follow the given JSON output format
        - Only run one step at a time
        - The sequence of steps is START (where user gives an input), PLAN 
        (That can be multiple times) and finally OUTPUT (which is going to be displayed to the user)

        Output JSON Format:
        {"step": "START" | "PLAN" | "OUTPUT" | "TOOL", "content":"string","tool":"string", "input":"string" }

        Available tools:
        - get_weather(city: str): Takes city name as an input string and returns the weather info about the city
        - run_command(cmd: str): Takes a system linux command as string and executes the command on user's system and returns the output from that command


        Example 1:
        START: Can you solve 2 + 3 * 5 / 10
        PLAN {"STEPS":"PLAN", "content": "Seems like user is interested in math problem"}
        PLAN {"STEPS":"PLAN", "content": "looking at the problem, we should solve this using BODMAS method"}
        PLAN {"STEPS":"PLAN", "content": "Yes, BODMAS is correct thing to be done here"}
        PLAN {"STEPS":"PLAN", "content": "first we must multiply 3 * 5 which is 15"}
        PLAN {"STEPS":"PLAN", "content": "Now the new equation is 2 + 15 /  10"}
        PLAN {"STEPS":"PLAN", "content": "We must perform division that is 15 / 10 = 1.5"}
        PLAN {"STEPS":"PLAN", "content": "Now the new equation is 2 + 1.5"}
        PLAN {"STEPS":"PLAN", "content": "Now finally lets perform the add to get 3.5"
        PLAN {"STEPS":"PLAN", "content": "Great, we have solved and finally left with 3.5 as the answer"}
        OUTPUT {"STEPS":"OUTPUT", "content": "3.5"}

        Example 2:
        START: What is the weather of Harare
        PLAN {"STEPS":"PLAN", "content": "Seems like user is interested in getting weather of Harare in Zimbabwe"}
        PLAN {"STEPS":"PLAN", "content": "Lets see if we have any available tool from the list of available tools"}
        PLAN {"STEPS":"PLAN", "content": "Great, we have get_weather tool available for this query"}
        PLAN {"STEPS":"PLAN", "content": "I need to call get_weather tool for Harare as input for city"}
        PLAN {"STEPS":"TOOL", "tool":"get_weather,"input": "Harare"}
        PLAN {"STEPS":"OBSERVE","tool":"get_weather", "output": "The weather in Harare is Partly cloudy +57Â°F"}
        PLAN {"STEPS":"PLAN", "content": "Great, i got the weather info about Harare"}
        OUTPUT {"STEPS":"OUTPUT", "content": "The current weather in Harare is 30 C with Partly cloudy"}
        """
    print("\n\n\n")
    message_history = [
        {"role":"system", "content": SYSTEM_PROMPT }
    ]

    class MyOutputFormat(BaseModel):
        step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, TOOL, etc")
        content: Optional[str] = Field(None, description="The optional string content for the step")
        tool: Optional[str] = Field(None, description="The ID of the tool to call.")
        input: Optional[str] = Field(None, description="The input params for the tool")



    while True:
        USER_QUERY  = input("> ")
        message_history.append({"role":"user","content":USER_QUERY})

        while True:
            response = client.chat.completions.parse(
            model="gpt-4o",
            response_format=MyOutputFormat,
            messages=message_history
            )
            raw_result = response.choices[0].message.content
            message_history.append({"role":"assistant","content":raw_result})

            parsed_result = response.choices[0].message.parsed

            if parsed_result.step == "START":
                print("<<",parsed_result.content,">>")
                continue

            if parsed_result.step == "TOOL":
                tool_to_call = parsed_result.tool
                tool_input = parsed_result.input
                print(f"..calling {tool_to_call}({tool_input})")
                tool_response = available_tools[tool_to_call](tool_input)
                print(f"..calling {tool_to_call}({tool_input}) = {tool_response}")

                message_history.append({
                    "role":"developer", "content": json.dumps({
                        "step":"OBSERVE","tool":tool_to_call,"input":tool_input,"output":tool_response
                    })
                })

                continue

            if parsed_result.step == "PLAN":
                print("...",parsed_result.content,"....")
                continue

            if parsed_result.step == "OUTPUT":
                print("||", parsed_result.content,"||")
                break


if __name__ == "__main__":
    agent()
    print("\n\n\n")