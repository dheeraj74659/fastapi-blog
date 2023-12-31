"""
Contains security related functions.
"""
from datetime import datetime
from datetime import timedelta
from typing import Optional

from core.config import settings
from jose import jwt


def create_access_token(
    data: dict[str:str], expires_delta: Optional[timedelta] = None
) -> str:
    """
    Method to generate JWT access token.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt
