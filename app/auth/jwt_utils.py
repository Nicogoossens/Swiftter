import time
import jwt

SECRET = "dev-secret-replace-in-prod"

def create_token(data: dict, exp_seconds: int = 3600):
    payload = data.copy()
    payload.update({"exp": int(time.time()) + exp_seconds})
    return jwt.encode(payload, SECRET, algorithm="HS256")

def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=["HS256"])
    except Exception:
        return None
