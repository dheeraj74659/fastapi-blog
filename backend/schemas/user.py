"""
pydantic model for user.
"""
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import Field


# properties required during user creation
class UserCreate(BaseModel):
    """pydantic class for user creation."""

    email: EmailStr
    password: str = Field(..., min_length=4)


class ShowUser(BaseModel):
    """
    Pydantic class for returning user details."""

    id: int
    email: EmailStr
    is_active: bool

    # tells pydnatic to convert even non dict object to json
    class Config:
        orm_mode = True
