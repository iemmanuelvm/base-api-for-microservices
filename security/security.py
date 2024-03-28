from datetime import datetime, timedelta
from typing import Optional
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, APIRouter, HTTPException, status

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return bcrypt_context.hash(password)

def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)



