from argon2 import PasswordHasher

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
import jwt

load_dotenv()


ph = PasswordHasher()


def hash_password(password:str):
    return ph.hash(password)

def verify_password(hashed_password:str , simple_password:str):
    return ph.verify(hash_password,simple_password)

def create_access_token(data:dict,expires_minutes:int= os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')):
    to_encode =data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp":expire})
    SECRET_KEY = os.getenv('16edccd79dd6c09de6a2c7ffe80b6d9e1400313ad337584b8fdbfc65e2514dc2ee15e3bfbed54155853f38e55e0e4d702fcea201414b88f7fd5ccccd719dfb90')
    algorithm = os.getenv('ALGORITHM')
    return jwt.encode(to_encode,SECRET_KEY , algorithm)
