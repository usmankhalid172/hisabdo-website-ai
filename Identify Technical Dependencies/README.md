# HisabDo – Technical Dependencies & Environment Setup

## Project Overview

HisabDo is an AI-powered application designed with a modern web architecture. The system uses a React frontend, Node.js/Express.js integration layer, Python/FastAPI AI backend, MongoDB database, Ollama for local LLM inference, Sentence Transformers for embeddings, and FAISS for the initial RAG prototype.

This README provides the complete technical dependency analysis and environment setup plan for the HisabDo project.

---

## Core Technical Stack

- React
- Node.js / Express.js
- Python
- FastAPI
- Ollama
- Sentence Transformers
- FAISS
- MongoDB
- Qdrant (Future Migration)

---

## 1. Frontend Dependencies

### Required Technologies

- React
- React DOM
- React Router DOM
- Axios
- Vite
- ESLint
- Node.js 20 LTS
- npm 10+

### Frontend Responsibilities

- User interface
- Navigation
- Authentication screens
- API communication
- AI assistant interface
- Displaying AI-generated responses
- Loading and error states
- Responsive user experience

Private API keys, database credentials, JWT secrets, and other sensitive information must never be exposed in frontend code.

---

## 2. Backend Integration Requirements

Node.js and Express.js are used as the backend integration layer where required.

### Responsibilities

- API routing
- Frontend/backend communication
- Authentication integration
- Request validation
- FastAPI communication
- Error handling
- CORS configuration
- Secure API communication

### Recommended Architecture

```text
React
  ↓
Node.js / Express.js
  ↓
FastAPI
  ↓
MongoDB / FAISS / Ollama
```

---

## 3. Python Environment Requirements

Python is required for the AI and RAG components.

### Recommended Version

**Python 3.11.x**

### Virtual Environment

Windows:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

Using a virtual environment prevents dependency conflicts between projects.

---

## 4. FastAPI Requirements

FastAPI is used for the AI/RAG backend service.

### Main Dependencies

- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
- httpx
- PyMongo

### Responsibilities

- REST API development
- Request/response validation
- Authentication
- Database communication
- RAG processing
- Embedding generation
- FAISS search
- Ollama communication
- Health checks
- Error handling
- Logging

### Recommended API Endpoints

```text
GET  /health
GET  /health/database
GET  /health/llm
GET  /health/vector-store
POST /api/auth/login
POST /api/rag/query
```

### Run FastAPI

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 5. Ollama / LLM Runtime Requirements

Ollama is selected as the initial local LLM runtime.

### Configuration

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
```

The model remains configurable so different models can be selected depending on available RAM, storage, and performance requirements.

### Requirements

- Ollama installed
- Local LLM model downloaded
- Sufficient RAM
- Sufficient storage
- FastAPI able to communicate with Ollama
- Model tested before RAG integration

---

## 6. Embedding Model Requirements

Sentence Transformers is used for generating semantic embeddings.

### Recommended Prototype Model

```text
sentence-transformers/all-MiniLM-L6-v2
```

### Purpose

The embedding model converts documents, knowledge-base content, and user queries into numerical vectors that can be searched using a vector database.

### Important Requirement

The same embedding model must be used for:

1. Document indexing
2. User query embedding

If the embedding model changes, the existing vector index should be rebuilt.

---

## 7. Vector Database Requirements

### Initial Vector Store

**FAISS**

### Future Vector Store

**Qdrant**

FAISS is recommended for the initial local RAG prototype because it is lightweight and suitable for local similarity search.

Qdrant can be introduced later when the application requires:

- Persistent vector collections
- Metadata filtering
- Larger datasets
- Multiple services
- Scalable deployment
- Production-grade vector search

---

## 8. FAISS Requirements for Initial RAG Prototype

### RAG Pipeline

```text
Knowledge Documents
        ↓
Text Cleaning
        ↓
Document Chunking
        ↓
Sentence Transformers
        ↓
Embeddings
        ↓
FAISS Index
        ↓
User Query
        ↓
Query Embedding
        ↓
Similarity Search
        ↓
Top-K Retrieved Context
        ↓
Ollama LLM
        ↓
Grounded AI Response
```

### Required FAISS Components

- FAISS index
- Document IDs
- Chunk IDs
- Metadata mapping
- Embedding model configuration

### RAG Quality Controls

- Top-K retrieval
- Similarity threshold
- Source metadata
- Insufficient-context handling
- Grounded prompts
- Protection against unsupported AI claims

---

## 9. Future Qdrant Migration Requirements

Qdrant is planned as a future scalable vector database.

### Migration Plan

1. Keep document IDs independent from FAISS.
2. Create a vector-store abstraction.
3. Implement FAISS vector-store adapter.
4. Implement Qdrant vector-store adapter.
5. Re-index the knowledge base.
6. Validate retrieval quality.
7. Switch the vector-store configuration.

### Future Environment Variables

```env
VECTOR_STORE=qdrant
QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION=hisabdo_documents
```

The frontend should not require changes when migrating from FAISS to Qdrant.

---

## 10. Database / API Dependencies

MongoDB is used as the application database.

### Possible Data

- Users
- Application records
- Expenses
- User preferences
- Document metadata
- Conversations where required
- Feedback
- Other application data

### Python Dependency

```text
pymongo
```

### MongoDB Configuration

```env
MONGODB_URI=mongodb://localhost:27017/hisabdo
MONGODB_DB=hisabdo
```

Database credentials must remain on the backend and must never be exposed to the React frontend.

---

## 11. Authentication Dependencies

Authentication should use JWT or the project's existing authentication mechanism.

### Recommended Dependencies

- PyJWT
- Passlib
- Bcrypt

### Authentication Requirements

- Secure password hashing
- Expiring access tokens
- Protected API endpoints
- Authentication middleware/dependencies
- Authorization checks
- Secure JWT secret
- Server-side secret management

Example:

```env
JWT_SECRET=CHANGE_THIS_IN_LOCAL_ENV
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

## 12. Required Environment Variables

The project should use environment variables instead of hard-coded configuration.

### Example

```env
APP_NAME=HisabDo
ENVIRONMENT=development
DEBUG=true

API_HOST=0.0.0.0
API_PORT=8000

VITE_API_BASE_URL=http://localhost:8000

MONGODB_URI=mongodb://localhost:27017/hisabdo
MONGODB_DB=hisabdo

JWT_SECRET=CHANGE_THIS_IN_LOCAL_ENV
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

VECTOR_STORE=faiss

FAISS_INDEX_PATH=./data/faiss/index.faiss
FAISS_METADATA_PATH=./data/faiss/metadata.json

QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION=hisabdo_documents

CORS_ORIGINS=http://localhost:5173
```

### Security Rule

Never commit the real `.env` file to Git.

Only commit:

```text
.env.example
```

---

## 13. Hardware Requirements for Local AI

### Minimum Prototype Requirements

- 64-bit CPU
- 4 CPU cores
- 8 GB RAM
- SSD recommended

### Recommended Development Machine

- 64-bit CPU
- 4–8+ CPU cores
- 16 GB RAM
- SSD
- At least 20 GB free storage

### GPU

A GPU is optional for the initial prototype. GPU acceleration can improve local LLM performance when supported by the selected model/runtime and hardware.

---

## 14. Model RAM and Storage Requirements

Model requirements depend on:

- Model size
- Quantization
- Context length
- Number of concurrent requests
- CPU/GPU hardware

### General Planning

| Model Class | Recommendation |
|---|---|
| 1B–4B | Recommended starting point |
| 7B–8B | Requires more RAM |
| Larger Models | High RAM/GPU requirements |

Storage is also required for:

- Ollama models
- Sentence Transformer model
- Python packages
- Node.js packages
- MongoDB data
- FAISS indexes
- Logs

---

## 15. Network Dependencies for Optional Cloud AI Services

The local prototype can operate mainly without cloud AI services after the required models and packages have been downloaded.

Internet may be required for:

- npm packages
- Python packages
- Ollama model downloads
- Embedding model downloads
- MongoDB Atlas
- Qdrant Cloud
- Optional cloud LLM APIs
- Cloud monitoring services

### Production Requirements

Cloud communication should use:

- HTTPS
- Secure API keys
- Restricted network access
- Timeouts
- Retry policies
- Secure environment variables

---

## 16. Logging and Monitoring Requirements

### Logging

The system should record:

- Timestamp
- Service name
- API endpoint
- HTTP status
- Response duration
- Error type
- Request/correlation ID

### Monitoring

Monitor:

- API uptime
- API response time
- API error rate
- MongoDB health
- Ollama availability
- Embedding model status
- FAISS/Qdrant retrieval status
- CPU usage
- RAM usage
- Disk usage

### Sensitive Data

Never log:

- Passwords
- JWT secrets
- API keys
- Access tokens
- Unnecessary financial information
- Sensitive user information

---

## 17. Version Compatibility

| Component | Target Version |
|---|---|
| Python | 3.11.x |
| Node.js | 20 LTS |
| npm | 10+ |
| React | 18.x compatible baseline |
| FastAPI | 0.115+ |
| Uvicorn | 0.30+ |
| Pydantic | 2.x |
| Sentence Transformers | 3.x |
| FAISS CPU | 1.8.x compatible |
| PyMongo | 4.x |
| Ollama | Current stable release |
| MongoDB | 7.x / 8.x compatible |

Exact versions should be locked for production/release builds. Dependency upgrades should be followed by smoke testing.

---

## 18. External Service Dependencies

### Required / Local

- MongoDB
- Ollama
- Sentence Transformers
- FAISS

### Optional / Future

- MongoDB Atlas
- Qdrant
- Qdrant Cloud
- Cloud LLM provider
- Monitoring/observability platform

External services should be configurable so that the application is not tightly coupled to one provider.

---

## 19. Recommended System Architecture

```text
                    ┌──────────────────┐
                    │  React Frontend  │
                    │      + Vite      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Node.js /        │
                    │ Express.js       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Python / FastAPI │
                    │    AI Service    │
                    └─────┬────┬────┬──┘
                          │    │    │
              ┌───────────┘    │    └───────────┐
              ▼                ▼                ▼
          MongoDB           FAISS             Ollama
       Application DB     RAG Search          Local LLM
                               ▲
                               │
                    Sentence Transformers
                         Embeddings
```

### Future

FAISS can be replaced or complemented by Qdrant when production scale requires it.

---

## 20. Environment Setup Plan

### Step 1 — Install Prerequisites

Install:

- Python 3.11
- Node.js 20 LTS
- Git
- MongoDB
- Ollama
- VS Code

Optional:

- Docker Desktop
- Postman
- MongoDB Compass

### Step 2 — Setup Backend

```bash
python -m venv venv
```

Activate the environment and run:

```bash
pip install -r backend/requirements.txt
```

### Step 3 — Setup Frontend

```bash
cd frontend
npm install
npm run dev
```

### Step 4 — Configure Environment

Create a local `.env` file using:

```text
config/.env.example
```

### Step 5 — Start Services

Recommended order:

```text
1. MongoDB
2. Ollama
3. FastAPI
4. Node.js / Express.js
5. React
```

---

## 21. Docker Support

The project can use:

```text
config/docker-compose.yml
```

It provides local containers for:

- MongoDB
- Qdrant

Qdrant is included for future vector-database migration and testing.

---

## 22. Completion Checklist

- [x] Required frontend dependencies identified
- [x] Backend integration requirements identified
- [x] Python environment requirements defined
- [x] FastAPI requirements identified
- [x] Ollama / LLM runtime requirements identified
- [x] Embedding model requirements identified
- [x] Vector database requirements identified
- [x] FAISS requirements for the initial RAG prototype defined
- [x] Future Qdrant migration requirements defined
- [x] Database/API dependencies defined
- [x] Authentication dependencies identified
- [x] Required environment variables identified
- [x] Hardware requirements for local AI models identified
- [x] Model RAM and storage requirements identified
- [x] Network dependencies for optional cloud AI services identified
- [x] Logging and monitoring requirements identified
- [x] Version compatibility documented
- [x] External service dependencies identified

---

## 23. Expected Output

### Complete Technical Dependency Document and Environment Setup Plan

**STATUS: COMPLETED**

The HisabDo technical dependency analysis covers the complete requested technology stack, environment configuration, local AI requirements, RAG architecture, FAISS implementation, future Qdrant migration, database/API dependencies, authentication, security, hardware, networking, monitoring, external services, and version compatibility.

---

## Final Status

**Task: Identify Technical Dependencies**

**Status: COMPLETED**

### Core Stack

```text
React
+
Node.js / Express.js
+
Python
+
FastAPI
+
Ollama
+
Sentence Transformers
+
FAISS
+
MongoDB
```

### Future

```text
Qdrant
```

**Deliverable: Complete**
