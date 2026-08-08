# Database Design

RAGdoll uses two storage systems:

- A relational database for application data.
- ChromaDB for vector embeddings and semantic retrieval.

This separation keeps structured application data independent from AI-specific data.

---

# Relational Database

## Documents

Stores metadata for uploaded documents.

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary key |
| filename | TEXT | Original filename |
| pages | INTEGER | Number of pages |
| uploaded_at | TIMESTAMP | Upload timestamp |

---

## Conversations

Stores chat sessions.

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary key |
| title | TEXT | Conversation title |
| created_at | TIMESTAMP | Creation timestamp |

---

## Messages

Stores chat history.

| Column | Type | Description |
|---------|------|-------------|
| id | UUID | Primary key |
| conversation_id | UUID | Parent conversation |
| role | TEXT | user / assistant |
| content | TEXT | Message text |
| created_at | TIMESTAMP | Timestamp |

---

# Entity Relationship Diagram

```
Documents

id (PK)
filename
pages
uploaded_at


Conversations

id (PK)
title
created_at


Messages

id (PK)
conversation_id (FK)
role
content
created_at
```

Relationship:

```
Conversation
      │
      │ 1
      │
      ▼
Messages (Many)
```

Documents are independent of conversations. A conversation may reference one or more documents during retrieval, but no direct foreign key relationship is required.

---

# ChromaDB

ChromaDB stores document embeddings used for semantic search.

Each stored chunk contains:

- Chunk text
- Embedding vector
- Document ID
- Page number
- Chunk index

Example metadata:

```json
{
  "document_id": "abc123",
  "page": 17,
  "chunk": 8
}
```

The vector itself is managed internally by ChromaDB and is not stored in the relational database.

---

# Storage Responsibilities

## Relational Database

Stores:

- Document metadata
- Conversation metadata
- Chat messages

## ChromaDB

Stores:

- Text chunks
- Embeddings
- Chunk metadata

---

# Design Principles

- Normalize structured application data.
- Store vector embeddings separately.
- Avoid duplicate information.
- Keep AI retrieval independent from application state.
- Allow either storage system to evolve without affecting the other.