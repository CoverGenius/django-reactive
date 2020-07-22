from typing import Optional, List

from pydantic import BaseModel, Field, constr, validator


class RegistrationSchema(BaseModel):
    email: str = Field(title="Email")
    password1: str = Field(title="Password")
    password2: str = Field(title="Confirm Password")
    first_name: str = Field(title="First name")
    last_name: str = Field(title="Last name")
    age: Optional[int] = Field(title="Age")
    bio: Optional[str] = Field(title="Bio")
    password: Optional[constr(min_length=3)] = Field(title="Password")
    telephone: Optional[constr(min_length=10)] = Field(title="Telephone")

    @validator("password2")
    def passwords_match(cls, v, values, **kwargs):
        if "password1" in values and v != values["password1"]:
            raise ValueError("passwords do not match")
        return v


class Item(BaseModel):
    name: str = Field(title="Name of the item", description="Namss")
    details: Optional[str] = Field(
        title="Task details", description="Enter the task details"
    )
    done: bool = Field(title="Done?", default=False)


class Task(BaseModel):
    name: str = Field(title="Name of the task", description="Test")
    items: Optional[List[Item]] = None

    class Config:
        title = "A list of items"


class TaskListSchema(BaseModel):
    name: str = Field(title="Name of the task list")
    tasks: Optional[List[Task]] = Field(
        None, title="Tasks", description="A list of tasks"
    )

    class Config:
        title = "A list of tasks"
