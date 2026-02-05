from fastapi import FastAPI
from pydantic import BaseModel
from app.ai.summarizer import summarize_text  # works now

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/summarize")
async def summarize(request: TextRequest):
    summary = await summarize_text(request.text)
    return {"summary": summary}
