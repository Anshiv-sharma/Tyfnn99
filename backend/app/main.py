from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.schemas import UserCreate
from app.models import User 
from app.utils import hash_password

app = FastAPI()

@app.get("/")
def home(db: Session = Depends(get_db_session)):
    return{"message": "TYFN99 Backend Running"}

@app.post("/register")
def register(
    user: UserCreate,
    db: Session = Depends(get_db_session)
):

    # checking if the email alr exists
    existing_email = db.query(User).filter(User.email == user.email).first()

    if existing_email:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # checking if the phone no. alr exists
    existing_phone = db.query(User).filter(User.phone == user.phone).first()

    if existing_phone:
        raise HTTPException(
            status_code=400,
            detail="Phone number already registered"
        )
    
    # creating a new user
    new_user = User(
        name = user.name,
        email = user.email,
        phone = user.phone,
        password_hash = hash_password(user.password)
    )

    #save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return{
        "message": "User registered successfully!",
        "user_id": new_user.id
        }