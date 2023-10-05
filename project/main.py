from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/", response_model=list[schemas.User])
async def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/users/{username}", response_model=schemas.User)
def get_user(username: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=username)
    if not db_user :
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/users/", response_model=schemas.User)
async def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="User already exists")   
    return crud.create_user(db, user=user)

@app.put("/users/")
async def update_user(user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated_user = crud.update_user(db, username=user.username,
                                    first_name=user.first_name, last_name=user.last_name, gender=user.gender, email=user.email)
    return {"message": "User updated"}
                      


@app.delete("/users/{username}")
async def delete_user(username: str, db:Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == username)
    fdb_user = db_user.first()
    if not fdb_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.delete(synchronize_session=False)
    db.commit()
    return {"message": f"{username} is deleted"}

