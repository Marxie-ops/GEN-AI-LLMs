import os
import streamlit as st
import pickle
import time
import langchain
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import faiss


# Access the variables
secret_key = "your_api_key"     
# Set the OpenAI API key
os.environ['OPENAI_API_KEY'] = secret_key

# Initialize LLM (ChatOpenAI)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", 
                 temperature=0.7, 
                 max_tokens=500)

# Set up the URL loader for Kenyan business news
loaders = UnstructuredURLLoader(
    urls=[
        "https://www.businessdailyafrica.com",
        "https://nation.africa/kenya/business",
        "https://www.standardmedia.co.ke/business"
    ]
)

# Load data from the URLs
data = loaders.load()

# Split the data into chunks
text_splitter = RecursiveCharacterTextSplitter(
    separators=[" "],
    chunk_size=1000,
    chunk_overlap=200
)
docs = text_splitter.split_documents(data)

# Clean the documents
from langchain.docstore.document import Document  # Import the Document class

cleaned_docs = []

for doc in docs:
    cleaned_content = doc.page_content.replace("\n\n", " ").strip()
    cleaned_doc = Document(
        metadata=doc.metadata, 
        page_content=cleaned_content
    )
    cleaned_docs.append(cleaned_doc)

# Create the embeddings for the chunks using OpenAIEmbeddings
embeddings = OpenAIEmbeddings()

# Pass the documents and embeddings to create FAISS vector index
vectorindex_openai = FAISS.from_documents(cleaned_docs, embeddings)

# Save the FAISS index
#faiss_index = vectorindex_openai.index  # Extract the FAISS index from the LangChain wrapper
file_path = "vector1_index.index"
#faiss.write_index(faiss_index, file_path)

# Load the FAISS index
loaded_faiss_index = faiss.read_index(file_path)

# Recreate the LangChain FAISS vector store with the loaded index
docstore = vectorindex_openai.docstore  # Get the docstore
index_to_docstore_id = vectorindex_openai.index_to_docstore_id  # Get the index-to-docstore mapping

# Recreate the LangChain FAISS vector store with the loaded index
loaded_vectorstore = FAISS(embedding_function=embeddings, 
                           index=loaded_faiss_index, 
                           docstore=docstore, 
                           index_to_docstore_id=index_to_docstore_id)

# Create the chain using the loaded vector store
chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=loaded_vectorstore.as_retriever())

# Streamlit UI to get the user input for search query
st.title("Kenyan Business Search Tool")
query = st.text_input("Enter your search query related to Kenyan business:", "")

# Check if a query is provided by the user
if query:
    # Display the user's query and process it when the search button is clicked
    st.write(f"Your question: {query}")

    # Execute search when the user clicks the "Search" button
    if st.button("Search"):
        with st.spinner('Searching...'):
            # Query the chain with the user's input
            response = chain.invoke({"question": query}, return_only_outputs=True)
            
            # Display the answer and sources
            st.subheader("Answer")
            st.write(response["answer"])
            
            st.subheader("Sources")
            st.write(response["sources"])

# Optionally, you can include additional information such as FAQ or help instructions in the sidebar
st.sidebar.header("How it works")
st.sidebar.write("""
1. Enter a query related to Kenyan business news.
2. The model will search the content of multiple Kenyan business websites.
3. The results will include relevant answers and sources.
""")
