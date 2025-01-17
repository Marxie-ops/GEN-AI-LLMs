# GENERATIVE AI SOLUTIONS POWERED BY OPENAI
## *Problem*
The primary problem addressed by this project is the need for efficient and accurate search tools for Kenyan business news. In Kenya, accessing and filtering through vast amounts of business-related information from multiple sources (websites, news articles, etc.) is challenging. Many businesses, investors, and professionals struggle to find relevant and up-to-date business news. Additionally, the vast amounts of unstructured data make it difficult to get specific answers related to business trends, market analysis, and industry reports.

## *Impact*
The impact of this project is twofold:

Improved Access to Information: By creating an easy-to-use search tool, users can quickly access and filter through large volumes of Kenyan business news. This significantly reduces the time spent on manual searches and improves decision-making processes by providing instant access to relevant business insights.

Enhanced Decision-Making for Business and Professionals: This tool allows business owners, investors, and professionals to stay up-to-date with trends, news, and analysis in the Kenyan business sector, making it easier to make informed decisions about investments, partnerships, and strategies.

## *Steps Used to Build the Tool*
Setting Up the Environment:

Set up the development environment by installing necessary Python packages like streamlit, langchain, openai, faiss, and others.
Set the OpenAI API key either directly in the code or through a .env file to authenticate API requests.
Data Collection:

Loaded business-related data from Kenyan news websites using the UnstructuredURLLoader class from LangChain.
Specified the URLs of multiple Kenyan business news sources.
Data Processing:

Split the content of the documents into smaller chunks using RecursiveCharacterTextSplitter to make the information manageable and improve the efficiency of document retrieval.
Cleaned the data by removing extra line breaks and ensuring a consistent format for each document.
Creating Embeddings:

Generated embeddings of the processed documents using OpenAI’s OpenAIEmbeddings. Embeddings are numerical representations of the documents that allow for semantic search.
Building the Vector Store:

Created a FAISS vector index using the embeddings to enable fast similarity search.
The FAISS index is stored in a file (e.g., vector1_index.index) for efficient retrieval of relevant documents during user queries.
Query Processing and Model Setup:

Set up a RetrievalQAWithSourcesChain from LangChain, which allows for querying the loaded documents and retrieving both answers and source references.
Integrated OpenAI's GPT-3.5 model for generating natural language responses based on the retrieved documents.
Streamlit User Interface:

Developed an interactive Streamlit UI for the app. This UI allows users to input a query and see the generated answer along with the sources used for the answer.
The app processes the user's input, queries the document store, and displays relevant answers and sources.
Saving and Loading the FAISS Index:

The FAISS vector index is saved to disk for persistence and later use. This prevents reprocessing the documents every time the app is used.
The index is reloaded from the file when the app is restarted, ensuring the tool is efficient and scalable.
Deployment and Usage:

The tool is made accessible locally via Streamlit for users to interact with the tool and retrieve business information from Kenyan business websites.
Documentation:

Created comprehensive documentation for the tool, outlining installation steps, usage, and troubleshooting, making it easy for others to use or contribute to the project.
Conclusion
This tool effectively addresses the challenge of accessing, processing, and querying Kenyan business news in a structured and efficient way. The use of AI-powered document retrieval and natural language processing helps provide meaningful insights to users quickly. The system can be scaled or adapted to other regions or industries as needed, offering significant potential for expanding its use.


# *Documentation*
## ***Kenyan Business Search Tool***
This project leverages LangChain, OpenAI, and FAISS to create a powerful search tool that allows users to query Kenyan business news websites. The tool retrieves relevant information from multiple sources and presents answers based on the latest data. It's built using Streamlit to provide an interactive user interface.

## *Features*
* Query-based search to retrieve information from Kenyan business websites.
* Integration with LangChain for efficient natural language processing (NLP) and document retrieval.
* Use of OpenAI's GPT-3.5 turbo model to generate answers.
* Embedding-based search powered by FAISS for efficient document search and retrieval.
* Streamlit UI for interactive querying and result presentation.
## *Installation*
To set up the project on your local machine, follow the steps below:

Clone the repository:
bash
Copy
Edit
git clone <your-repository-url>
cd <your-project-directory>
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up OpenAI API key:

Create a .env file in the project directory and add your OpenAI API key:

makefile
Copy
Edit
OPENAI_API_KEY=your_api_key_here
Or, you can set the key directly in your code:

python
Copy
Edit
import os
os.environ['OPENAI_API_KEY'] = 'your_api_key_here'
Install FAISS:

For FAISS to work, ensure that the appropriate FAISS package is installed. You can install the CPU version using:

bash
Copy
Edit
pip install faiss-cpu
Or, for GPU support, install:

bash
Copy
Edit
pip install faiss-gpu
Usage
Running the app locally:

* Once the environment is set up, you can run the app using Streamlit:

bash
Copy
Edit
streamlit run business_search_tool.py
User interface:

The app will launch in your browser. You can then:

Enter a query in the input field about Kenyan business topics.
Click the "Search" button to get a relevant answer from the data collected from Kenyan business websites.
View the answer and sources on the app’s interface.
## *How it works:*

The app uses LangChain to load data from various Kenyan business websites, splits the content into manageable chunks, and generates embeddings using OpenAI. The FAISS vector store is used to perform efficient search and retrieval. The app then queries the OpenAI model to generate a relevant response.

## *Example search flow:*

User enters a query like: "What are the latest trends in the Kenyan real estate market?"
The system retrieves relevant documents from the sources, performs search using embeddings, and provides the answer with references.
Code Overview
Business Search Tool: The main functionality of the app is implemented in the business_search_tool.py file.

Document Processing: The UnstructuredURLLoader is used to load data from various URLs related to Kenyan business news.

Text Splitting and Cleaning: The documents are split into chunks using RecursiveCharacterTextSplitter and cleaned for consistent formatting.

FAISS Vector Store: The FAISS vector index is created from the processed documents and used for efficient similarity search.

LangChain Retrieval Chain: The RetrievalQAWithSourcesChain is used to combine the document retrieval and response generation using the OpenAI model.

Project Structure
bash
Copy
Edit
.
├── business_search_tool.py         # Main script for the Streamlit app
├── requirements.txt                # List of project dependencies
├── .env                            # Contains your OpenAI API key (if needed)
├── vector1_index.index             # FAISS index file for fast searching (generated during runtime)
└── README.md                       # Project documentation
Troubleshooting
If you encounter any issues, consider the following:

Ensure your OpenAI API key is set up correctly.
Verify that the required libraries are installed by running pip install -r requirements.txt.
If FAISS installation fails, check that the correct version (CPU or GPU) is installed for your system.
Contributing
Feel free to fork the project, make improvements, and create pull requests. Contributions are welcome!



Make sure to replace placeholders like <your-repository-url> and your_api_key_here with the appropriate values for your project. This README.md will give users a clear understanding of how to set up and use your Kenyan Business Search Tool.

## Video Link to see how the tool works.








