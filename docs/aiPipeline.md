# AI Pipeline

This document describes how RAGdoll processes documents and generates grounded responses using Retrieval-Augmented Generation (RAG).

---

# Overview

RAGdoll answers questions by retrieving relevant information from uploaded documents before generating a response with a language model.

Unlike a traditional chatbot, responses are grounded in user-provided documents rather than relying solely on the model's internal knowledge.

---

# Document Processing Pipeline

When a document is uploaded, it passes through several processing stages before becoming searchable.

```
Upload PDF
      │
      ▼
Extract Text
      │
      ▼
Split into Chunks
      │
      ▼
Generate Embeddings
      │
      ▼
Store in ChromaDB
```

---

## Step 1 – Upload

The user uploads a supported document through the web interface.

Current supported format:

- PDF

Future versions may support:

- DOCX
- Markdown
- Plain text

---

## Step 2 – Text Extraction

The AI service extracts readable text from each page of the document while preserving page numbers.

Example:

```
Page 1
Introduction...

Page 2
Operating systems...
```

---

## Step 3 – Chunking

Documents are divided into smaller sections called **chunks**.

Chunking improves retrieval accuracy because language models perform better when provided with focused context instead of entire documents.

Example:

```
Document

Page 1
-----------------
Chunk 1

Chunk 2

Chunk 3
-----------------

Page 2
-----------------
Chunk 4

Chunk 5
-----------------
```

Each chunk keeps metadata including:

- Document ID
- Page number
- Chunk number

---

## Step 4 – Embedding Generation

Each chunk is converted into a vector embedding using an embedding model.

Embeddings capture the semantic meaning of text, allowing similar concepts to be matched even when different words are used.

Example:

```
"The CPU schedules processes."

↓

[0.172, -0.441, ...]
```

These vectors are stored in ChromaDB.

---

# Question Answering Pipeline

When the user asks a question, the following pipeline is executed.

```
User Question
      │
      ▼
Generate Question Embedding
      │
      ▼
Semantic Search
      │
      ▼
Retrieve Top Chunks
      │
      ▼
Build Prompt
      │
      ▼
Language Model
      │
      ▼
Answer + Citations
```

---

## Step 1 – User Question

Example:

```
How does process scheduling work?
```

---

## Step 2 – Question Embedding

The question is converted into an embedding using the same embedding model.

This allows similarity comparisons against stored document chunks.

---

## Step 3 – Semantic Retrieval

ChromaDB compares the question embedding with every stored document embedding.

The most relevant chunks are returned.

Example:

```
Question

↓

Top 5 matching chunks

• Page 17
• Page 42
• Page 43
• Page 87
• Page 91
```

---

## Step 4 – Prompt Construction

The retrieved chunks are combined with the user's question to create the final prompt.

Example structure:

```
Context

Chunk A

Chunk B

Chunk C

Question

How does process scheduling work?
```

---

## Step 5 – Response Generation

The language model generates a response using only the retrieved context.

This significantly reduces hallucinations and produces answers grounded in the uploaded documents.

---

## Step 6 – Source Citations

Each response includes references to the document pages used during retrieval.

Example:

```
Answer...

Sources

Operating Systems.pdf
Page 42

Operating Systems.pdf
Page 43
```

---

# Why Retrieval-Augmented Generation?

Traditional language models rely on information learned during training.

RAG improves this process by supplying relevant external knowledge at inference time.

Benefits include:

- More accurate responses
- Reduced hallucinations
- Up-to-date knowledge
- Answers grounded in user documents
- Explainable responses through citations

---

# Future Improvements

Potential enhancements include:

- Hybrid keyword + semantic search
- Query rewriting
- Automatic document summaries
- OCR for scanned documents
- Re-ranking retrieved chunks
- Streaming responses
- Multi-document reasoning