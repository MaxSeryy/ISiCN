import uvicorn
from fastapi import FastAPI, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()

# for FastAPI using bearer token
security = HTTPBearer()

users_db = {
    "token_student_123": {"user_id": 1, "role": "student"},
    "token_admin_999": {"user_id": 2, "role": "admin"}
}

def get_current_user(credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials 
    user = users_db.get(token)
    
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized: invalid token.")
    return user

@app.get("/admin/logs")
# check the role 
def get_admin_logs(user: dict = Security(get_current_user)):
    
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Forbidden: Only for administrators.")
    
    return {"message": "Secret system logs", "logs": ["log1", "log2"]}

if __name__ == "__main__":
    uvicorn.run("T1:app", host="127.0.0.1", port=8000, reload=True)