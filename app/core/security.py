import os
from datetime import datetime, timedelta, timezone

from argon2 import PasswordHasher
from dotenv import load_dotenv
from jose import jwt

from app.config.settings import ALGORITHM

load_dotenv()


ph = PasswordHasher()


def hash_password(password:str)->str:
    """This function is used to hash password"""
    return ph.hash(password)

def verify_password(hashed_password:str , simple_password:str)->bool:
    """This function is used to verify the password"""
    return ph.verify(hashed_password,simple_password)


def create_token(data:dict , expires_minutes : int , SECRET_KEY:str )->str:
    """This is a common function which is used to create both access and refresh tokens"""
    to_encode =data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expires_minutes)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY,ALGORITHM)


