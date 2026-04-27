from langchain_community.document_loaders import PyPDFLoader
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv()
embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
)

qdrant = QdrantVectorStore.from_existing_collection(
        embedding=embeddings,
        url='localhost:6333',
        prefer_grpc=False,
        collection_name="ian_cv",
    )

def process_query(query: str):
    search_results = qdrant.similarity_search(query=query)
    context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

    SYSTEM_PROMPT = f"""
        You are a helpful AI Assistant who answers user query based on the available
        context retrieved from a PDF file along with page_contents and page number.

        You should only ans the user based on the following context 
        and navigate the user to open the right page to know more.

        Context:
        {context} 
        """
    client = OpenAI()
    response = client.chat.completions.create(
                model="gpt-5.4-nano",
                messages=[
                    {"role":"system","content":SYSTEM_PROMPT},
                    {"role":"user","content":query}
                ]
            )
    
    return response.choices[0].message.content
