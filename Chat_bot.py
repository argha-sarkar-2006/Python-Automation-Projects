# # Import ONLY LLM
# from langchain_groq import ChatGroq
# import os 
# GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# # Import ONLY vector store
# from langchain_chroma import Chroma

# from langchain_community.embeddings import HuggingFaceEmbeddings
# # Import ONLY the splitter
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.document_loaders import WebBaseLoader

print("- Loading website content -")
loader = WebBaseLoader(web_paths=["https://celoref.mintlify.app/overview/use-cases"])
docs = loader.load()

# PRINTING OUTPUT
print(f"Successfully loaded {len(docs)} document(s).")
print(f"Content Preview (First 500 chars):\n{docs[0].page_content[:500]}...")
print("Splitting text into chunks ")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,   # Size of each piece
    chunk_overlap=20  # How much previous text to repeat
)
splits = text_splitter.split_documents(docs)

# PRINTING OUTPUT
print(f"Original Documents: {len(docs)}")
print(f"Total Split Chunks: {len(splits)}")

print("\n  Chunk #1  ")
print(splits[0].page_content)

# print("\n Chunk #2 (Check the start  it should repeat the end of Chunk #1) ")
# print(splits[1].page_content)
# print("--- Initializing Embedding Model ---")
# embeddings = HuggingFaceEmbeddings(
#     model_name="sentence-transformers/all-MiniLM-L6-v2"
# )
# print("✅ Model loaded: sentence-transformers/all-MiniLM-L6-v2")


# # This creates the database in-memory (RAM) automatically
# vectorstore = Chroma.from_documents(
#     documents=splits,
#     embedding=embeddings
# )

# print("✅ Vector Store created successfully.")

# # PRINTING COLLECTION DETAILS
# print("\n--- Inspecting Chroma Collection ")
# # .get() allows us to look inside the database
# collection_data = vectorstore.get()

# print(f"Total items in collection: {len(collection_data['ids'])}")
# print(f"Sample ID: {collection_data['ids'][0]}")
# # Note: The actual vectors are hidden for efficiency, but the data is there.
# print("--- Initializing LLM ---")
# llm = ChatGroq(
#     model="openai/gpt-oss-20b", # Standard Groq Model
#     temperature=0,
#     api_key=GROQ_API_KEY
# )
# print("✅ LLM Ready.")
# # Import ONLY Chain components
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.output_parsers import StrOutputParser

# # -------------------------------
# # Define Prompt
# # -------------------------------
# template = """
# Answer ONLY from this context:

# {context}

# Question: {question}
# """

# prompt = ChatPromptTemplate.from_template(template)


# # -------------------------------
# # Setup Retriever
# # -------------------------------
# retriever = vectorstore.as_retriever()   # <-- your vectorstore must be defined earlier


# # -------------------------------
# # Helper: Format docs
# # -------------------------------
# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)


# # -------------------------------
# # Build RAG Chain (using Groq LLM)
# # -------------------------------
# rag_chain = (
#     {"context": retriever | format_docs, "question": RunnablePassthrough()}
#     | prompt
#     | llm                     # <-- your ChatGroq LLM inserted here
#     | StrOutputParser()
# )


# # -------------------------------
# # Run Query
# # -------------------------------
# query = "how to implement celoref sdk"

# print(f"Query: {query}\n")
# print("-" * 50)

# response = rag_chain.invoke(query)
# print(response)
