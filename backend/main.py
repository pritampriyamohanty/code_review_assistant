# import os
# import json
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import google.generativeai as genai

# # Load env
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# if not GEMINI_API_KEY:
#     raise RuntimeError("GEMINI_API_KEY missing in .env")

# genai.configure(api_key=GEMINI_API_KEY)

# # Use correct model for v0.8.5
# model = genai.GenerativeModel("gemini-1.5-flash")

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ReviewRequest(BaseModel):
#     language: str
#     code: str


# SYSTEM_PROMPT = """
# You are a strict but helpful senior software engineer.

# Your tasks:
# 1. Detect syntax / logic errors.
# 2. Suggest improved formatted code.
# 3. Return JSON ONLY in this format:

# {
#   "hasErrors": true/false,
#   "errors": "string",
#   "improvedCode": "string",
#   "comments": "string"
# }
# """


# @app.post("/review")
# async def review_code(payload: ReviewRequest):

#     # Build full prompt as ONE string (required for v0.8.5)
#     prompt = f"""
# {SYSTEM_PROMPT}

# Language: {payload.language}

# Code:
# ```{payload.language}
# {payload.code}

# """

#this is the working code 
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel

# app = FastAPI(title="Code Review STUB")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ReviewRequest(BaseModel):
#     language: str
#     code: str

# @app.get("/")
# async def root():
#     return {"message": "Stub API running"}

# @app.post("/review")
# async def review_code(payload: ReviewRequest):
#     # 👉 ALWAYS returns a dict – no Gemini, no magic
#     return {
#         "hasErrors": False,
#         "errors": "",
#         "improvedCode": payload.code,
#         "comments": f"Code in {payload.language} looks fine (stub).",
#     }


# import os
# import json
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import google.generativeai as genai

# # =============== ENV + GEMINI SETUP ==================
# load_dotenv()  # reads .env in backend folder

# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# if not GEMINI_API_KEY:
#     raise RuntimeError("GEMINI_API_KEY is not set. Put it in .env")

# genai.configure(api_key=GEMINI_API_KEY)

# # Use a Gemini 1.5 model (works with google-generativeai 0.8.5)
# model = genai.GenerativeModel("gemini-1.5-flash")
# # You could also try: model = genai.GenerativeModel("gemini-1.5-pro")

# # =============== FASTAPI APP ==================
# app = FastAPI(title="Gemini Code Review API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173", "*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # =============== DATA MODELS ==================
# class ReviewRequest(BaseModel):
#     language: str
#     code: str


# SYSTEM_PROMPT = """
# You are a strict but helpful senior software engineer.

# Your tasks:
# 1. Detect syntax and logic errors.
# 2. Suggest a cleaner, improved version of the code.
# 3. Explain what is wrong (if anything).
# 4. If the code is correct, say it clearly.

# Always respond ONLY in VALID JSON with this shape:

# {
#   "hasErrors": true or false,
#   "errors": "string describing errors or empty if none",
#   "improvedCode": "string with improved or same code",
#   "comments": "extra review comments"
# }
# """

# # =============== ROUTES ==================
# @app.get("/")
# async def root():
#     return {"message": "Gemini Code Review API running"}


# @app.post("/review")
# async def review_code(payload: ReviewRequest):
#     """
#     Returns JSON with:
#       hasErrors: bool
#       errors: str
#       improvedCode: str
#       comments: str
#     """

#     # ---------- Build prompt ----------
#     prompt = f"""
# {SYSTEM_PROMPT}

# Language: {payload.language}

# Code:
# ```{payload.language}
# {payload.code}
# """




#this is the final code 


# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import ast

# app = FastAPI(title="Simple Code Review API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173", "*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class ReviewRequest(BaseModel):
#     language: str
#     code: str


# @app.get("/")
# async def root():
#     return {"message": "Simple Code Review API running"}


# def review_python(code: str):
#     """
#     Very simple Python syntax check using ast.parse.
#     """
#     try:
#         ast.parse(code)
#         return {
#             "hasErrors": False,
#             "errors": "",
#             "improvedCode": code,
#             "comments": "Python code looks syntactically correct.",
#         }
#     except SyntaxError as e:
#         line = e.lineno or 0
#         col = e.offset or 0
#         msg = f"SyntaxError: {e.msg} at line {line}, column {col}."
#         return {
#             "hasErrors": True,
#             "errors": msg,
#             "improvedCode": code,  # we don't auto-fix, just return original
#             "comments": "Please fix the syntax error and try again.",
#         }


# def review_javascript(code: str):
#     """
#     Super simple JS checks with some basic suggestions.
#     This is NOT a real compiler, just a demo.
#     """
#     issues = []

#     # Example checks
#     if "==" in code and "===" not in code:
#         issues.append("Use '===' instead of '==' for strict equality.")

#     if "console.log(" in code and not code.strip().endswith(");"):
#         issues.append("JS console.log usually ends with ');'.")

#     has_errors = len(issues) > 0
#     errors_text = "\n".join(issues)

#     # simple 'improvement': replace '==' with '==='
#     improved = code.replace("==", "===") if "==" in code else code

#     if not has_errors:
#         comments = "JavaScript code looks okay based on simple checks."
#     else:
#         comments = "Some potential issues were found."

#     return {
#         "hasErrors": has_errors,
#         "errors": errors_text,
#         "improvedCode": improved,
#         "comments": comments,
#     }


# def review_generic(language: str, code: str):
#     """
#     Fallback for other languages: just say it looks fine.
#     """
#     return {
#         "hasErrors": False,
#         "errors": "",
#         "improvedCode": code,
#         "comments": f"{language} code looks fine (basic check only).",
#     }


# @app.post("/review")
# async def review_code(payload: ReviewRequest):
#     lang = payload.language.lower()

#     if lang == "python":
#         return review_python(payload.code)
#     elif lang in ("javascript", "js"):
#         return review_javascript(payload.code)
#     else:
#         return review_generic(payload.language, payload.code)

#last code before

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# import ast
# import esprima


# # ----------------- FASTAPI APP -----------------
# app = FastAPI(title="Simple Code Review API")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:5173", "*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# # ----------------- REQUEST MODEL -----------------
# class ReviewRequest(BaseModel):
#     language: str
#     code: str


# # ----------------- HELPERS -----------------
# def review_python(code: str):
#     """
#     Simple Python syntax check using ast.parse.
#     """
#     try:
#         ast.parse(code)
#         return {
#             "hasErrors": False,
#             "errors": "",
#             "improvedCode": code,
#             "comments": "Python code looks syntactically correct.",
#         }
#     except SyntaxError as e:
#         line = e.lineno or 0
#         col = e.offset or 0
#         msg = f"SyntaxError: {e.msg} at line {line}, column {col}."
#         return {
#             "hasErrors": True,
#             "errors": msg,
#             "improvedCode": code,
#             "comments": "Please fix the syntax error and try again.",
#         }


# def review_javascript(code: str):
#     """
#     JavaScript syntax checking using esprima.
#     This catches real JS syntax errors.
#     """
#     try:
#         # Will raise an exception if there is a syntax error
#         esprima.parseScript(code)

#         return {
#             "hasErrors": False,
#             "errors": "",
#             "improvedCode": code,
#             "comments": "JavaScript code is syntactically correct.",
#         }
#     except Exception as e:
#         msg = str(e)
#         return {
#             "hasErrors": True,
#             "errors": msg,
#             "improvedCode": code,
#             "comments": "Please fix the JavaScript syntax error.",
#         }


# def review_generic(language: str, code: str):
#     """
#     Fallback for other languages: only a basic message.
#     """
#     return {
#         "hasErrors": False,
#         "errors": "",
#         "improvedCode": code,
#         "comments": f"{language} code looks fine based on basic checks (no deep analysis).",
#     }


# # ----------------- ROUTES -----------------
# @app.get("/")
# async def root():
#     return {"message": "Simple Code Review API running"}


# @app.post("/review")
# async def review_code(payload: ReviewRequest):
#     """
#     Returns JSON with:
#       hasErrors: bool
#       errors: str
#       improvedCode: str
#       comments: str
#     """
#     lang = payload.language.lower()

#     if lang == "python":
#         return review_python(payload.code)
#     elif lang in ("javascript", "js"):
#         return review_javascript(payload.code)
#     else:
#         return review_generic(payload.language, payload.code)



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import ast
import esprima



# ---------------- FASTAPI SETUP ----------------
app = FastAPI(title="Python + JavaScript Code Review API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------- REQUEST MODEL ----------------
class ReviewRequest(BaseModel):
    language: str
    code: str


# ---------------- PYTHON REVIEW ----------------
def review_python(code: str):
    """
    Real Python syntax validation using AST.
    """
    try:
        ast.parse(code)
        return {
            "hasErrors": False,
            "errors": "",
            "improvedCode": code,
            "comments": "Python code is syntactically correct.",
        }
    except SyntaxError as e:
        msg = f"SyntaxError: {e.msg} (line {e.lineno}, col {e.offset})"
        return {
            "hasErrors": True,
            "errors": msg,
            "improvedCode": code,
            "comments": "Please correct the Python syntax error.",
        }


# ---------------- JAVASCRIPT REVIEW ----------------
def review_javascript(code: str):
    """
    JavaScript syntax validation using esprima.
    """
    try:
        esprima.parseScript(code)
        return {
            "hasErrors": False,
            "errors": "",
            "improvedCode": code,
            "comments": "JavaScript code is syntactically correct.",
        }
    except Exception as e:
        return {
            "hasErrors": True,
            "errors": str(e),
            "improvedCode": code,
            "comments": "Fix the JavaScript syntax error.",
        }


# ---------------- FALLBACK ----------------
def review_generic(language: str, code: str):
    return {
        "hasErrors": False,
        "errors": "",
        "improvedCode": code,
        "comments": f"No deep checks available for '{language}'.",
    }


# ---------------- ROUTES ----------------
@app.get("/")
async def root():
    return {"message": "Python + JS Code Review API running"}


@app.post("/review")
async def review_code(payload: ReviewRequest):
    lang = payload.language.lower()

    if lang == "python":
        return review_python(payload.code)

    elif lang in ("javascript", "js"):
        return review_javascript(payload.code)

    else:
        return review_generic(payload.language, payload.code)
