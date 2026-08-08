# RAGdoll Architecture

## Overview

RAGdoll follows a modular, service-oriented architecture that separates the user interface, application logic, and AI processing into independent components.

```
                 ┌────────────────────────┐
                 │        React UI        │
                 └──────────┬─────────────┘
                            │ HTTP Requests
                            ▼
                 ┌────────────────────────┐
                 │    Express Backend     │
                 └──────────┬─────────────┘
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
          ▼                                   ▼
 ┌──────────────────┐              ┌──────────────────┐
 │ Application Data │              │  FastAPI Service │
 │   (SQLite/DB)    │              └─────────┬────────┘
 └──────────────────┘                        │
                                             ▼
                                   ┌──────────────────┐
                                   │ PDF Processing   │
                                   │ Text Chunking    │
                                   │ Embeddings       │
                                   │ ChromaDB         │
                                   │ Language Model   │
                                   └──────────────────┘
```

---

# Components

## React Frontend

Responsible for the user interface.

Responsibilities:

- Upload documents
- Display uploaded documents
- Chat interface
- Display AI responses
- Display document citations
- Manage conversations

The frontend communicates only with the Express backend.

---

## Express Backend

Acts as the central API for the application.

Responsibilities:

- Handle client requests
- Store application data
- Manage uploaded files
- Manage conversations
- Communicate with the AI service
- Return responses to the frontend

The backend does not perform AI processing directly.

---

## FastAPI AI Service

Handles all AI-related functionality.

Responsibilities:

- Extract text from PDFs
- Split documents into chunks
- Generate embeddings
- Store embeddings in ChromaDB
- Retrieve relevant document context
- Generate AI responses

Separating AI logic from the main backend keeps the system modular and allows AI components to be updated independently.

---

# Data Flow

## Document Upload

1. User uploads a PDF.
2. React sends the file to the Express backend.
3. Express stores the document.
4. Express forwards the file to the AI service.
5. The AI service extracts text.
6. Text is divided into chunks.
7. Embeddings are generated.
8. Embeddings are stored in ChromaDB.

---

## Question Answering

1. User submits a question.
2. React sends the question to Express.
3. Express forwards the request to the AI service.
4. The AI service generates an embedding for the question.
5. ChromaDB retrieves the most relevant chunks.
6. Retrieved chunks are combined with the user's question.
7. The language model generates a grounded response.
8. Express returns the response to the frontend.

---

# Design Principles

- Modular architecture
- Separation of concerns
- Service independence
- Maintainable codebase
- Scalable AI pipeline
- Privacy-conscious document processing

---

# Future Improvements

- User authentication
- Multiple AI providers
- Additional document formats
- Streaming responses
- Cloud object storage
- Distributed vector databases