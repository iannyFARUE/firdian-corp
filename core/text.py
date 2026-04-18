from openai import OpenAI
from dotenv import load_dotenv
from google import genai

def prompt_open_ai():

    load_dotenv()
    client = OpenAI()

    response = client.responses.create(
        model="gpt-5.4",
        input="Write a one-sentence bedtime story about a unicorn."
    )
    print(response)
    print(response.output_text)

def prompt_gemini_ai():
    load_dotenv()
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents="Explain how AI works in a few words"
    )
    print(response.text)

def main():
    prompt_gemini_ai()

if __name__ == '__main__':
    main()