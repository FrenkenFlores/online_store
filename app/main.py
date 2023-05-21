from fastapi import FastAPI, status, HTTPException
from database import connect_mongodb
from models import User
from hashlib import sha512

app = FastAPI()
client = connect_mongodb()
db = client["OnlineStore"]
users_collection = db["users"]
category_collection = db["category"]
products_collection = db["products"]
cart_collection = db["cart"]


@app.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"data": ""}


@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
def add_new_user(user: User):
    if users_collection.find_one(user.dict()):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")
    new_user = User(username=user.username,
                    password=sha512(user.password.encode("utf-8")).hexdigest(),
                    role=user.role,
                    is_active=user.is_active)
    users_collection.insert_one(new_user.dict())
    return new_user


@app.get("/users", status_code=status.HTTP_200_OK)
def add_new_user():
    return {"data": [{"username": row["username"],
                      "password": row["password"],
                      "is_active": row["is_active"],
                      "role": row["role"]} for row in users_collection.find()]}


client.close()
