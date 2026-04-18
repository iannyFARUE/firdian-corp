from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

def prompt_open_ai():
    client = OpenAI()

# Few shot prompting: Directly giving instructions to the mddel and few examples to the model
    SYSTEM_PROMPT = """
You should only answer the coding related questions. Do not answer anything else. Your name is Firdah. If user asks something other than coding, just say sorry

Rule:
- Strictly follow the output in JSON format

Output Format:
{{
"code": "string" or None,
"isCodingQuestion": boolean
}}


Examples:
Q. Can you explain the a+ b whole square ?
A. {{'code':None, 'isCodingQuestion':false}}

Q. Hey write a code in python for adding two numbers.
A: {{'code': 'def add(a:int, b:int)->int:
        return a + a','isCodingQuestion':true }}
"""

    response = client.responses.create(
        model="gpt-5.4",
        input=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": "implemement factorial function in python"
            }
        ]
    )
    print(response)
    print(response.output_text)

if __name__ == "__main__":
    prompt_open_ai()