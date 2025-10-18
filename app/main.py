from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI(title="Swiftter API")
oauth2 = OAuth2PasswordBearer(tokenUrl="/token")

class GenerateRequest(BaseModel):
    prompt: str

@app.get("/health")
def health():
    return {"ok": True, "service": "Swiftter"}

@app.post("/generate")
def generate(payload: GenerateRequest, token: str = Depends(oauth2)):
    # DEV stub: in production forward to modelserver or cloud API
    return {"result": f"ECHO: {payload.prompt}"}

@app.post("/token")
def token():
    # DEV stub: return a dev token
    return {"access_token": "dev-token", "token_type": "bearer"}
