from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


users = {}


@app.post("/users/", response_model=User)
def create_user(user: User):
    """Create a new user"""
    if user.id in users:
        raise HTTPException(status_code=400, detail="User already exists")
    users[user.id] = user
    return user


@app.get("/users/{user_id}", response_model=User)
def read_user(user_id: int):
    """Get a user by id"""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]


@app.get("/users/", response_model=List[User])
def read_users():
    """Get all users"""
    return list(users.values())


@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: User):
    """Update a user by id"""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = user
    return user


@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    """Delete a user by id"""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users.pop(user_id)