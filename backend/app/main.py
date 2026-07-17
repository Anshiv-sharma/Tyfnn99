from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.schemas import UserCreate
from app.models import User 

app = FastAPI()

@app.get("/")
def home(db: Session = Depends(get_db_session)):
    return{"message": "TYFN99 Backend Running"}

@app.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db_session)
):
    print(user)
    return{"message": "Registeration request received!"}