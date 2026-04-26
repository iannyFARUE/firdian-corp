from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings



def load_file(path:str = Path(__file__).parent.parent / "IanResume.pdf"):

    # Loading this file in python program
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs


def chunk_text(document, chunk: int = 100, chunk_overlap: int = 0):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    return texts


def embed_and_save(url:str, docs, collection_name:str):


    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
)
    
    qdrant = QdrantVectorStore.from_documents(
        docs,
        embeddings,
        url=url,
        prefer_grpc=True,
        collection_name=collection_name,
    )
    print("Index of documents done...")