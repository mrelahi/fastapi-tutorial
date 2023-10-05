from sqlalchemy.orm import Session
import models, schemas
from passlib.context import CryptContext

from passlib.hash import pbkdf2_sha256

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(username=user.username, password=pbkdf2_sha256.hash(user.password),
                          first_name=user.first_name, last_name=user.last_name, gender=user.gender, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, username:str, first_name:str, last_name:str, gender:str, email:str):
    user = get_user_by_username(db=db, username=username)
    user.first_name = first_name
    user.last_name = last_name
    user.gender = gender
    user.email = email
    db.commit()
    db.refresh(user)
    return user