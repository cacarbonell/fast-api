#Python
from typing import Optional
from enum import Enum
#Pydantic
from pydantic import BaseModel, Field
#FastAPI
from fastapi import FastAPI, Body, Query, Path

app = FastAPI()

# Models

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str = Field(
        min_length=1,
        max_length=50,
        example="Pitalito"
    )
    state: str = Field(
        min_length=1,
        max_length=50,
        example="Huila"
    )
    country: str = Field(
        min_length=1,
        max_length=50,
        example="Colombia"
    )

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Cristhian"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Carbonell",
    )
    age: int = Field(
        ...,
        gt=0,
        le=70,
        example=34
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="black"
    )
    is_married: Optional[bool] = Field(
        default=None
    )
    password: str = Field(
        ...,
        min_length=8
    )

    # class Config:
    #     schema_extra = {
    #         "example": {
    #             "fist_name": "Cristhian",
    #             "last_name": "Carbonell",
    #             "age": 34,
    #             "hair_color": "black",
    #             "is_married": True
    #         },
    #     }

class PersonOut(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Cristhian"
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Carbonell",
    )
    age: int = Field(
        ...,
        gt=0,
        le=70,
        example=34
    )
    hair_color: Optional[HairColor] = Field(
        default=None,
        example="black"
    )
    is_married: Optional[bool] = Field(
        default=None
    )


@app.get("/")
def home():
    return {"Hello": "World"}

# request and response body

@app.post("/person/new", response_model=PersonOut)
def create_person(person: Person = Body(...)):
    return person

# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="Tony"
    ),
    age: str = Query(
        ...,
        title="Persona age",
        description="This is the person age. It's required",
        example=45
    )
):
    return {name: age}

# Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Persona id",
        description="This is the person id, It's required",
        example=45
    )
):
    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person (
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=34
    ),
    person: Person = Body(
        ...
    ),
    location: Location = Body(
        ...
    )
): 
    results = person.dict()
    results.update(location.dict())
    return results
