# Gemini Code Review Mini Project

Tech stack:
- Frontend: React + Vite
- Backend: Python FastAPI
- AI: Google Gemini (via google-generativeai)

## Quick Start

### 1. Backend

```bash
cd backend
python -m venv venv
# Windows:
venv\\Scripts\\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

Set your Gemini API key in `.env`:

```env
GEMINI_API_KEY=YOUR_ACTUAL_KEY_HERE
```

Run server:

```bash
uvicorn main:app --reload --port 8000
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173 and start reviewing code!