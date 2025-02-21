import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain.vectorstores import FAISS
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

# extract text from pdf function
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# split text into chunks function
def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks = text_splitter.split_text(text)
    return chunks

# vector embeddings and storing them into vectorDB FIASS
def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store

# Function to create a conversational retrieval chain
# def get_conversational_chain(vector_store):
#     llm = GoogleGenerativeAI(model="gemini-pro")  # Use Gemini Pro model
#     memory = ConversationBufferMemory(
#         memory_key="chat_history", return_messages=True
#     )
#     conversation_chain = ConversationalRetrievalChain.from_llm(
#         llm=llm, retriever=vector_store.as_retriever(), memory=memory
#     )
#     return conversation_chain

#explain + QnA 
def get_conversational_chain(vector_store):
    llm = GoogleGenerativeAI(model="gemini-pro")  
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm, retriever=vector_store.as_retriever(), memory=memory
    )
    return conversation_chain


def generate_questions_and_answers(topic):
    """Generates an explanation along with related questions and answers."""
    llm = GoogleGenerativeAI(model="gemini-pro")

    explanation_prompt = f"Explain the topic '{topic}' in simple terms."
    explanation = llm.invoke(explanation_prompt)

    qa_prompt = f"Generate 3 related questions and their answers on the topic '{topic}'. Format: Q1: ..., A1: ... Q2: ..., A2: ... Q3: ..., A3: ..."
    qa_response = llm.invoke(qa_prompt)

    return explanation, qa_response
