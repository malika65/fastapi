from typing import Optional, final, List

from fastapi import FastAPI, Body, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
import schemas, models, crud
models.Base.metadata.create_all(bind=engine)
from cbfa import ClassBased

app = FastAPI()

wrapper = ClassBased(app)


#Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@wrapper('/items')
class ItemCreateView:

    def get(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
        items = crud.get_items(db, skip=skip, limit=limit)
        return items

    def post(
        user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
    ):
        return crud.create_user_item(db=db, item=item, user_id=user_id)





# compare plain and hashed passwords
@app.post("/compare_pass/")
def compare_pass(plainpass: str, hashpass: str):
    return crud.verify_password(plainpass, hashpass)
