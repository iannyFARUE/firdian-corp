from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader


def load_file(path:str = Path(__file__).parent.parent / "IanResume.pdf"):

    # Loading this file in python program
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs
