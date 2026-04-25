from transformers import pipeline
# from core.weather_agent import agent
from core.general_agent_v2 import agent
from rag.index import  load_file
def main():
   

    classifier = pipeline("sentiment-analysis")
    classifier(
        [
            "i I AM EXCITED TO BUILD AN AGENT",
            "I hate MCpS this so much!",
        ]
    )


if __name__ == "__main__":
    print(load_file())
