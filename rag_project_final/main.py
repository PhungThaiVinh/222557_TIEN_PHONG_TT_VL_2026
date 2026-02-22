import os
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA

# Load biến môi trường
load_dotenv()

# 1. Load dữ liệu
with open("data.txt", "r", encoding="utf-8") as f:
    texts = f.readlines()

# 2. Tạo Embedding
embeddings = OpenAIEmbeddings()

# 3. Tạo Vector Database (FAISS)
db = FAISS.from_texts(texts, embeddings)

# 4. Tạo LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")

# 5. Tạo RAG chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=db.as_retriever()
)

# 6. Query
query = "LangChain là gì?"
result = qa.run(query)

print("Câu hỏi:", query)
print("Trả lời:", result)
