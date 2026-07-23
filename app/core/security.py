from argon2 import PasswordHasher

from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os
from jose import jwt

load_dotenv()


ph = PasswordHasher()


def hash_password(password:str):
    return ph.hash(password)

def verify_password(hashed_password:str , simple_password:str):
    return ph.verify(hashed_password,simple_password)

def create_access_token(data:dict,expires_minutes:int= int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES'))):
    to_encode =data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    print(expire)
    to_encode.update({"exp":expire})
    SECRET_KEY = os.getenv('ACCESS_TOKEN_SECRET')
    algorithm = os.getenv('ALGORITHM')
    return jwt.encode(to_encode,SECRET_KEY , algorithm)

def create_refresh_token(data:dict,expires_minutes:int= int(os.getenv('REFRESH_TOKEN_EXPIRE_MINUTES'))):
    to_encode =data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp":expire})
    SECRET_KEY = os.getenv('REFRESH_TOKEN_SECRET')
    algorithm = os.getenv('ALGORITHM')
    return jwt.encode(to_encode,SECRET_KEY , algorithm)


