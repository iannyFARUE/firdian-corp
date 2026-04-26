from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter



def load_file(path:str = Path(__file__).parent.parent / "IanResume.pdf"):

    # Loading this file in python program
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs


def chunk_text(document, chunk: int = 100, chunk_overlap: int = 0):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    return texts
