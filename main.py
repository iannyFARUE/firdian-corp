from transformers import pipeline
# from core.weather_agent import agent
from core.general_agent_v2 import agent
from rag.index import  load_file, chunk_text, embed_and_save
def main():
   

    classifier = pipeline("sentiment-analysis")
    classifier(
        [
            "i I AM EXCITED TO BUILD AN AGENT",
            "I hate MCpS this so much!",
        ]
    )


if __name__ == "__main__":
    chunks = chunk_text(load_file())
    embed_and_save(url="http://localhost:6333",docs=chunks, collection_name="ian_cv")
