# Real-Time-Multimodal-Data-Processing

This repository contains a real-time multimodal data processing pipeline built with Pathway, Docling, and the OpenAI API. 
The system monitors a folder for incoming PDF documents, parses them, extracts content, generates embeddings, and prepares the data for use in retrieval-augmented generation (RAG) applications such as a chatbot.

## Overview

The project demonstrates:

- Real-time ingestion of PDFs using Pathway’s streaming engine
- Document parsing using Docling
- Text chunking and embeddings generated via the OpenAI API
- A pipeline that updates automatically whenever new documents are added
- A foundation for building a chatbot that can answer questions about uploaded PDFs

## Current Capabilities

- Detects new or updated PDF files in the `data/` directory
- Parses documents and extracts structured content
- Generates text embeddings using OpenAI
- Stores embeddings and prepares them for retrieval
- Exposes a local HTTP server on port `8000` for future endpoints
