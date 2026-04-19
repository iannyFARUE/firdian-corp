from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import json

def prompt_open_ai():
    client = OpenAI()

# Few shot prompting: Directly giving instructions to the mddel and few examples to the model
    SYSTEM_PROMPT = """
You're an expert AI Assistant in resolving user queries using chain of thought
You work on START, PLAN and OUTPUT steps.
You need to first PLAN what needs to be done. The PLAN can be multiple steps.
Once you think enough PLAN has been done, finally you can give an OUTPUT

Rule:
- Strictly follow the given JSON output format
- Only run one step at a time
- The sequence of steps is START (where user gives an input), PLAN 
(That can be multiple times) and finally OUTPUT (which is going to be displayed to the user)

Output JSON Format:
{"step": "START" | "PLAN" | "OUTPUT", "content":"string"}


Examples:
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
"""

    print("\n\n\n")
    message_history = [
        {"role":"system", "content": SYSTEM_PROMPT }
    ]

    USER_QUERY  = input(">>")
    message_history.append({"role":"user","content":USER_QUERY})

    while True:
        response = client.responses.parse(
        model="gpt-4o",
        text ={"format":{"type":"json_object"}},
        input=message_history
        )
        raw_result = response.output_text
        message_history.append({"role":"assistant","content":raw_result})

        parsed_result = json.loads(raw_result)

        if parsed_result.get("step") == "START":
            print("<<",parsed_result.get("content"),">>")
            continue

        if parsed_result.get("step") == "PLAN":
            print("...",parsed_result.get("content"),"....")
            continue

        if parsed_result.get("step") == "OUTPUT":
            print("||", parsed_result.get("content"),"||")
            break
if __name__ == "__main__":
    prompt_open_ai()
    print("\n\n\n")


