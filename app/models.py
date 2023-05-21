# This package will hold the data structures for the web store components. Every data structure will represent
# a table in MongoDB.
from pydantic import BaseModel
from enum import Enum


class Roles(str, Enum):
    client = "client"
    admin = "admin"


class User(BaseModel):
    """The User class will represent the user table."""
    username: str
    password: str
    is_active: bool
    role: Roles = Roles.client
