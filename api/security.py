from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

USERNAME = ""
PASSWORD = ""

def verificar_usuario(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != USERNAME or credentials.password != PASSWORD:
        raise HTTPException(status_code=401, detail="Usuario o contraseña incorrectos")