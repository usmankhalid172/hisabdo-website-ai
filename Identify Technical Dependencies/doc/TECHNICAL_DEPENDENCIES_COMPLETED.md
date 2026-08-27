# HisabDo — Identify Technical Dependencies
## Completed Technical Dependency Document & Environment Setup Plan

**Task status:** COMPLETED  
**Core stack:** React + Node.js/Express.js + Python + FastAPI + Ollama + Sentence Transformers + FAISS + MongoDB  
**Future vector migration:** Qdrant

---

## 1. Executive Summary

HisabDo is planned as an AI-enabled application with a React frontend, a Node.js/Express integration layer, a Python/FastAPI AI service, MongoDB for application data, Ollama for local LLM inference, Sentence Transformers for embeddings, and FAISS for the initial RAG prototype.

The dependency plan below covers all requested technical areas: frontend, backend integration, Python/FastAPI, LLM runtime, embeddings, vector search, FAISS, future Qdrant migration, database/API dependencies, authentication, environment variables, local-AI hardware, model RAM/storage, optional cloud networking, logging/monitoring, version compatibility, and external services.

---

## 2. Core Technical Stack

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | React | User interface |
| Frontend tooling | Vite + npm | Build/dev tooling |
| Integration/API | Node.js + Express.js | API gateway/integration where required |
| AI backend | Python + FastAPI | AI/RAG REST service |
| LLM runtime | Ollama | Local model inference |
| Embeddings | Sentence Transformers | Semantic vector generation |
| Initial vector store | FAISS | Local similarity search |
| Application database | MongoDB | Users, app data, metadata |
| Future vector DB | Qdrant | Scalable persistent vector search |

---

## 3. Required Frontend Dependencies — COMPLETED

### Runtime
- Node.js 20 LTS target
- npm 10+ target

### Packages
- `react`
- `react-dom`
- `react-router-dom`
- `axios`

### Development
- `vite`
- `@vitejs/plugin-react`
- `eslint`

### Frontend responsibilities
- Responsive UI
- Login/authentication screens
- API communication
- AI chat/assistance UI
- Loading and error states
- Displaying recommendations and retrieved context where required
- Never exposing private server secrets

---

## 4. Backend Integration Requirements — COMPLETED

Node.js/Express.js can serve as the frontend-facing integration layer when required.

### Responsibilities
1. Route frontend requests.
2. Handle authentication/session integration.
3. Forward AI requests to FastAPI.
4. Apply CORS/security policy.
5. Centralize API error handling.
6. Keep provider credentials on the server.
7. Provide a consistent API contract to React.

### Recommended flow

`React → Node/Express → FastAPI → MongoDB / FAISS / Ollama`

For a simpler deployment, React may call FastAPI directly for suitable endpoints; the architecture should keep this configurable.

---

## 5. Python Environment Requirements — COMPLETED

### Target
- Python 3.11.x
- `venv` virtual environment
- pip

### Setup

Windows:
```powershell
python -m venv venv
.env\Scripts\Activate.ps1
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

---

## 6. FastAPI Requirements — COMPLETED

Core packages:
- FastAPI
- Uvicorn
- Pydantic 2.x
- python-dotenv
- httpx
- PyMongo

### Recommended service responsibilities
- REST endpoints
- Request/response validation
- Authentication dependencies
- MongoDB access
- RAG orchestration
- Embedding generation
- FAISS retrieval
- Ollama calls
- Health checks
- Error handling
- Structured logging

### Suggested endpoints
```text
GET  /health
GET  /health/database
GET  /health/llm
GET  /health/vector-store
POST /api/auth/login
POST /api/rag/query
```

Run locally:
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 7. Ollama / LLM Runtime Requirements — COMPLETED

### Selected initial runtime
Ollama for local LLM inference.

### Required configuration
```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
```

The model name is intentionally configurable. A smaller model can be selected for lower RAM machines; a larger model can be selected when more resources are available.

### Requirements
- Ollama installed
- Local model downloaded
- Enough RAM/storage for selected model
- Local service reachable from FastAPI
- Model tested with a simple prompt before RAG integration

---

## 8. Embedding Model Requirements — COMPLETED

### Initial embedding technology
Sentence Transformers.

### Recommended prototype model
```text
sentence-transformers/all-MiniLM-L6-v2
```

### Requirements
- Model downloaded/available to the Python environment
- Same embedding model used for indexing and querying
- Consistent text preprocessing
- Rebuild index if the embedding model changes

### Purpose
Convert documents and user queries into numerical vectors for semantic retrieval.

---

## 9. Vector Database Requirements — COMPLETED

### Initial choice
FAISS.

### Future choice
Qdrant.

### Why
FAISS is practical for a local RAG prototype. Qdrant becomes more useful when persistent collections, metadata filtering, multiple services/users, or scalable deployment is needed.

---

## 10. FAISS Requirements for Initial RAG Prototype — COMPLETED

### Pipeline
```text
Documents
   ↓
Cleaning
   ↓
Chunking
   ↓
Sentence Transformer
   ↓
Embeddings
   ↓
FAISS Index
   ↓
User Query
   ↓
Query Embedding
   ↓
Top-K Similarity Search
   ↓
Retrieved Context
   ↓
Ollama LLM
   ↓
Grounded Answer
```

### Required artifacts
- FAISS index file
- Metadata mapping file
- Document/chunk IDs
- Embedding model configuration

### RAG controls
- Top-K retrieval
- Similarity threshold
- Source metadata
- Insufficient-context response
- Prompt guardrails against unsupported claims

---

## 11. Future Qdrant Migration Requirements — COMPLETED

Migration should not require rewriting the frontend.

### Migration plan
1. Keep document/chunk IDs independent from FAISS.
2. Create a vector-store abstraction.
3. Implement `FAISSVectorStore`.
4. Implement `QdrantVectorStore`.
5. Re-index/re-embed the knowledge base.
6. Validate retrieval quality.
7. Switch configuration using `VECTOR_STORE`.

Future configuration:
```env
VECTOR_STORE=qdrant
QDRANT_URL=
QDRANT_API_KEY=
QDRANT_COLLECTION=hisabdo_documents
```

---

## 12. Database / API Dependencies — COMPLETED

### MongoDB
Use MongoDB for application data such as:
- users
- expenses/records
- application metadata
- support conversations where required
- document metadata
- feedback

### Python database dependency
`pymongo`

### Connection
```env
MONGODB_URI=mongodb://localhost:27017/hisabdo
MONGODB_DB=hisabdo
```

The frontend must never connect directly using database credentials.

---

## 13. Authentication Dependencies — COMPLETED

### Recommended approach
JWT-based authentication or the project's existing authentication mechanism.

### Python dependencies
- PyJWT
- Passlib/Bcrypt when password hashing is handled by the service

### Requirements
- Passwords must be securely hashed
- Access tokens should expire
- Protected endpoints require authentication
- Authorization/role checks should be applied where needed
- Secrets remain in environment/deployment secret storage

---

## 14. Required Environment Variables — COMPLETED

Use `config/.env.example` as the template.

Main variables:
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

**Security rule:** never commit a real `.env` file or secret values.

---

## 15. Hardware Requirements for Local AI — COMPLETED

### Minimum prototype target
- 64-bit CPU
- 4 CPU cores
- 8 GB RAM
- SSD preferred

### Recommended development machine
- 64-bit CPU
- 4–8+ CPU cores
- 16 GB RAM
- SSD
- 20+ GB free space initially

### GPU
GPU is optional for the prototype. It can improve local inference speed when the selected runtime/model and drivers support acceleration.

---

## 16. Model RAM & Storage Requirements — COMPLETED

Exact resource use depends on model size, quantization and context length.

### Practical planning
| Model class | General planning |
|---|---|
| 1B–4B | Most practical for ordinary development machines |
| 7B–8B | More RAM required; performance depends strongly on quantization/hardware |
| Larger models | High RAM/GPU requirements; not recommended for the basic prototype |

Also reserve storage for:
- Ollama model files
- Sentence Transformer model
- Python packages
- Node modules
- MongoDB data
- FAISS index
- logs

---

## 17. Network Dependencies for Optional Cloud AI — COMPLETED

The core local prototype can operate without a cloud LLM after models/packages have been downloaded.

Internet may be needed for:
- npm package installation
- Python package installation
- downloading embedding models
- downloading Ollama models
- optional cloud LLM APIs
- MongoDB Atlas
- Qdrant Cloud
- external monitoring

Production cloud services require:
- HTTPS
- outbound firewall rules
- API-key protection
- timeout/retry policies
- restricted service-to-service access

---

## 18. Logging & Monitoring Requirements — COMPLETED

### Minimum logging
Record:
- timestamp
- service
- endpoint
- HTTP status
- response duration
- error type
- request/correlation ID

### Monitor
- API uptime
- API latency
- error rate
- MongoDB connection
- Ollama availability
- embedding loading
- vector-store retrieval
- CPU/RAM/disk usage

### Never log
- passwords
- JWT secrets
- API keys
- access tokens
- unnecessary sensitive financial information

---

## 19. Version Compatibility — COMPLETED

| Component | Target baseline |
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
| MongoDB | 7.x/8.x compatible |

For release builds, pin/lock exact versions and run smoke tests after upgrades.

---

## 20. External Service Dependencies — COMPLETED

### Required/local
- MongoDB (local or managed)
- Ollama
- Sentence Transformers model
- FAISS

### Optional/future
- MongoDB Atlas
- Qdrant/Qdrant Cloud
- Cloud LLM provider
- Monitoring/observability platform

External providers should be accessed through service abstractions/configuration so they can be replaced without redesigning the UI.

---

## 21. Environment Setup Plan — COMPLETED

### Startup order
1. MongoDB
2. Ollama
3. FastAPI
4. Node/Express (if used)
5. React

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
python -m venv venv
# activate venv
pip install -r backend/requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Docker support
`config/docker-compose.yml` provides local MongoDB and Qdrant containers.

---

## 22. Acceptance / Completion Checklist

- [x] Required frontend dependencies identified
- [x] Backend integration requirements identified
- [x] Python environment defined
- [x] FastAPI requirements defined
- [x] Ollama/LLM runtime requirements defined
- [x] Embedding model requirements defined
- [x] Vector database requirements defined
- [x] FAISS initial RAG requirements defined
- [x] Future Qdrant migration defined
- [x] Database/API dependencies defined
- [x] Authentication dependencies defined
- [x] Environment variables defined
- [x] Local AI hardware requirements defined
- [x] Model RAM/storage planning defined
- [x] Optional cloud network dependencies defined
- [x] Logging/monitoring requirements defined
- [x] Version compatibility documented
- [x] External services documented
- [x] Environment setup plan completed

**Expected Output:** A complete technical dependency document and environment setup plan — DELIVERED.
