from fastapi import FastAPI
from pydantic import BaseModel
from utils import gemini_response


app = FastAPI()
@app.get('/')
async def read_root():
    return {"message": "Welcome to the Gemini API Caller."}




class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/gemini")
async def generate_response_endpoint(request: PromptRequest):
    try:
        response = gemini_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calling Gemini API: {e}")
