"""
Pydantic schemas related to token.
"""
from pydantic import BaseModel


class Token(BaseModel):
    """pydantic schema to return token."""

    access_token: str
    token_type: str
