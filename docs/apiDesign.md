# API Design

This document defines the REST API used by RAGdoll. The Express backend serves as the application's primary API and communicates with the AI service when AI-related processing is required.

---

# Base URL

```
/api
```

---

# Health

## GET /health

Checks whether the backend is running.

### Response

```json
{
  "status": "OK"
}
```

---

# Documents

## POST /documents

Uploads a new document for processing.

### Request

```
multipart/form-data
```

| Field | Type | Required |
|-------|------|----------|
| file | File | Yes |

### Response

```json
{
  "message": "Document uploaded successfully.",
  "documentId": "abc123"
}
```

---

## GET /documents

Returns all uploaded documents.

### Response

```json
[
  {
    "id": "abc123",
    "filename": "Operating Systems.pdf",
    "pages": 218,
    "uploadedAt": "2026-08-08T09:00:00Z"
  }
]
```

---

## GET /documents/:id

Returns metadata for a specific document.

### Response

```json
{
  "id": "abc123",
  "filename": "Operating Systems.pdf",
  "pages": 218,
  "uploadedAt": "2026-08-08T09:00:00Z"
}
```

---

## DELETE /documents/:id

Deletes a document and its associated embeddings.

### Response

```json
{
  "message": "Document deleted successfully."
}
```

---

# Chat

## POST /chat

Submits a question to the AI.

### Request

```json
{
  "conversationId": "conv001",
  "question": "Explain process scheduling."
}
```

### Response

```json
{
  "answer": "Process scheduling determines which process executes next...",
  "sources": [
    {
      "document": "Operating Systems.pdf",
      "page": 42
    }
  ]
}
```

---

# Conversations

## GET /conversations

Returns all conversations.

### Response

```json
[
  {
    "id": "conv001",
    "title": "Operating Systems",
    "createdAt": "2026-08-08T09:15:00Z"
  }
]
```

---

## GET /conversations/:id

Returns a conversation and its messages.

### Response

```json
{
  "id": "conv001",
  "messages": [
    {
      "role": "user",
      "content": "Explain process scheduling."
    },
    {
      "role": "assistant",
      "content": "Process scheduling..."
    }
  ]
}
```

---

## DELETE /conversations/:id

Deletes a conversation.

### Response

```json
{
  "message": "Conversation deleted successfully."
}
```

---

# Error Format

All errors follow a consistent format.

```json
{
  "error": {
    "message": "Document not found."
  }
}
```

---

# Status Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Resource created |
| 400 | Invalid request |
| 404 | Resource not found |
| 500 | Internal server error |

---

# Notes

- The Express backend acts as the single entry point for all client requests.
- AI processing is delegated to the FastAPI service.
- Uploaded documents are processed asynchronously before becoming available for querying.
- Future versions may introduce authentication and authorization.