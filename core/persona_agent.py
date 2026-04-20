from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import json

def prompt_open_ai():
    client = OpenAI()

# Few shot prompting: Directly giving instructions to the mddel and few examples to the model
    SYSTEM_PROMPT = """
You are an AI persona Assistant named Mai Farai.
You are acting on behalf of Mai Farai my mother who passed away on March 1 2020, a loving and gentle soul.
Your background is born in Zimbabwe and christian who is also a single mother with 2 boys Ian and Honest.

Examples:
Q. Makadii Mhamha
A: Ndamuka
"""

    print("\n\n\n")
    response = client.responses.parse(
    model="gpt-5.4",
    input=[
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":"Ndakusuwai Mama"}
    ]
    )
    raw_result = response.output_text
    print(raw_result)
if __name__ == "__main__":
    prompt_open_ai()
    print("\n\n\n")


