"""
Contains pydantic schema related to blog.
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic import root_validator


class CreateBlog(BaseModel):
    """
    Pydantic schema to create new blog.
    """

    title: str
    slug: str
    content: Optional[str] = None

    @root_validator(pre=True)
    def generate_slug(cls, values: dict[str]) -> str:
        if "title" in values:
            values["slug"] = values.get("title").replace(" ", "-").lower()
        return values


class ShowBlog(BaseModel):
    """
    Pydantic schema for returning blog details.
    """

    title: str
    content: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


class UpdateBlog(CreateBlog):
    """Pydnatic schema to update a blog."""

    pass
