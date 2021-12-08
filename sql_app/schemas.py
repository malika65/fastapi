from pydantic import BaseModel
from typing import Optional, List


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    # provide configurations to Pydantic
    class Config:
        # True : read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes)
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    # provide configurations to Pydantic
    class Config:
        # True : read the data even if it is not a dict,
        # but an ORM model (or any other arbitrary object with attributes)
        orm_mode = True




    