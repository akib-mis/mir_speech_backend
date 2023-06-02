import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transcribe.app import app_router

app = FastAPI(title="Mir_speech", version="2023.06.02")
origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://mirspeech.ergov.com/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(app_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Mir_speech",
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
