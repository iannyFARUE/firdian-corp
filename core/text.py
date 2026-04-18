from openai import OpenAI
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()


def prompt_open_ai():
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5.4",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response)
    print(response.output_text)

def prompt_gemini_ai():
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
            config=types.GenerateContentConfig(
        system_instruction="You are a maths expert and only answer math related questions. If the query is not related to maths. Just say sorry and do not answer that."),
          contents="How are you"
    )
    print(response.text)

def prompt_genai_via_openai():
    import os
    key = os.environ.get("GEMINI_API_KEY")
    client = OpenAI(
        api_key=key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        messages=[
            {   "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": "Explain to me how AI works"
            }
        ]
    )

    print(response.choices[0].message.content)

def main():
    prompt_genai_via_openai()

if __name__ == '__main__':
    #1. Zero-shot Prompting: The model is given a direct question or task without prior examples
    #2. Few Shot Prompting: Directly giving the instruction to the model and few example to the model
    main()