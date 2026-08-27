# HisabDo Environment Setup

## Prerequisites
1. Python 3.11
2. Node.js 20 LTS
3. Git
4. MongoDB local or MongoDB Atlas
5. Ollama
6. VS Code (recommended)
7. Docker Desktop (optional)

## Backend
```bash
python -m venv venv
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Linux/macOS:
source venv/bin/activate

python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

## Frontend
```bash
cd frontend
npm install
npm run dev
```

## Environment
Copy `config/.env.example` to a local `.env` and change secrets/configuration.

## Local services
Start MongoDB and Ollama before FastAPI.

## Validation
- `/health`
- MongoDB connection
- Ollama response
- embedding model load
- FAISS index load
- sample RAG query
