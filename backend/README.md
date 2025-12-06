# Backend (FastAPI + Gemini)

## Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   cd backend
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Gemini API key:

   - Open `.env` and put your key:

     ```env
     GEMINI_API_KEY=YOUR_ACTUAL_KEY_HERE
     ```

4. Run the server:

   ```bash
   uvicorn main:app --reload --port 8000
   ```

API will be available at: http://localhost:8000