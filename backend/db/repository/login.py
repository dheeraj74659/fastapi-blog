"""
Contains repository function related to login functionality.
"""
from db.models.user import User
from sqlalchemy.orm import Session


def get_user(email: str, db: Session):
    """
    Repository function to get user provided email id.
    """
    user = db.query(User).filter(User.email == email).first()
    return user
