PDF-Based RAG Application



Overview



This project is a basic Retrieval-Augmented Generation (RAG) application that allows users to interact with PDF documents using natural language queries.



The application loads PDF files from the data folder, extracts and splits the text into smaller chunks, generates embeddings, and stores them in a vector database.



When a user submits a query, the application converts it into embeddings, performs semantic similarity search against the stored vectors, retrieves relevant document chunks, and uses an LLM to generate a context-aware response.



Features

Load PDF documents from the data folder.

Extract and chunk text from PDF files.

Generate embeddings for document chunks.

Store embeddings in a vector database.

Perform semantic search based on user queries.

Generate context-aware answers using an LLM.



How It Works

Load PDF documents from the data folder.

Extract text and split it into smaller chunks.

Generate embeddings for each chunk.

Store embeddings in a vector database.

Embed the user's query and search for relevant chunks.

Pass the retrieved context to an LLM.

Generate a relevant response based on the retrieved information.



Use Cases

PDF document question answering.

Searching and retrieving information from documents.

Building knowledge-based AI applications.

