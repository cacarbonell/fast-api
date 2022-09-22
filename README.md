# FastAPI: Basics, Path Operations and Validations

![fastapi](https://user-images.githubusercontent.com/60154657/191849551-99056de8-b486-4f38-ad90-d51086c1012e.png)

## Basics of FastAPI

### What is Fast API?
It is a modern, fast⚡ framework for web development with Python. Focused on making APIs, it is the fastest in terms of server speed, surpassing NodeJS and GO. It was created by Sebastián Ramírez, it is open source and is found on Github, and it is used by companies such as Uber, Windows, Netflix and Office.

### FastAPI's location in the Python ecosystem

FastAPI uses other Frameworks within itself to function
* ```Uvicorn:``` It is a Python library that works as a server, that is, it allows any computer to become a server.
* ```Starlette:``` It is a low-level web development framework, to develop applications, you require extensive knowledge of Python, FastAPI is responsible for adding functionalities on top of it so that it can be used easily.
* ```Pydantic:``` It is a Framework that allows you to work with data similar to pandas, but it allows you to use models which will take advantage of FastAPI to create the API

### Hello World: Creating the development environment

Creation of the virtual environment
```bash
python3 -m venv venv
```

Activation of the environment
```bash
source venv/bin/activate
```

Then we install FastAPI and uvicorn
```bash
pip3 install fastapi uvicorn
```

We create a main.py file where we will enter the code to create our API.
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Hello": "World"}
```

first we import FastAPI then we create an app instance and we create with a decorator the path operations @app.get(”/”) this is equivalent when we enter the main url it will show us what we are returning from the function and we create the function home which returns a dictionary

Then we run the server with ```uvicorn```
```bash
uvicorn main:app --reload
```

main of the Python file that refers to the app instance we add a —reload flag allows changes to be made to the Python file, the application is reloaded without stopping it and we can see the changes reflected

### Interactive documentation of an API

FastAPI also stands on the shoulders of OpenAPI, which is a set of rules that allows you to define how to describe, create, and display APIs. It is a set of rules that allow us to say that an API is well defined.

**OpenAPI** needs software, which is Swagger, which is a set of software that allows you to work with APIs. FastAPI works on top of a Swagger program which is Swagger UI, which allows you to display the documented API.

Access Interactive Documentation with Swagger UI: In the Browser

```{localhost}/docs - http://127.0.0.1:8000/docs```

Access interactive documentation with Redoc:

```{localhost}/redoc - http://127.0.0.1/redoc```

## Disassembling the Framework

### Path Operations
A path operations is the combination of routes and http methods.

![path-operations](https://user-images.githubusercontent.com/60154657/191851262-d8c9dee3-55e7-4493-a46e-058bf87afee7.png)

### Path Parameters
Path parameters are variable parts of a URL path. They are typically used to point to a specific resource within a collection, such as a user identified by ID. A URL can have multiple path parameters.

![path-parameters PNG](https://user-images.githubusercontent.com/60154657/191851401-aa3d96a4-b796-47e4-8342-d801b031850b.png)

### Query Parameters
A query parameters is a set of optional elements which are added at the end of the route, in order to define content or actions in the URL, these elements are added after a ? to add more query parameters we use ampersand &

![query-parameters](https://user-images.githubusercontent.com/60154657/191851578-1de9f610-0cfd-4709-b68c-6a6b8cd2fbb2.png)

### Request Body and Response Body
Under the HTTP protocol there is a communication between the user and the server. This communication is made up of headers and a body. For the same reason, there are two directions in the communication between the client and the server and they are defined as follows:

* **Request:** When the client requests data from the server
* **Response:** When the server responds to the client

**Request Body →** With the aforementioned, it becomes the body of a request from the client to the server.

**Response Body →** With the above mentioned, it becomes the body of a response from the server to the client.

![requets-and-response-body](https://user-images.githubusercontent.com/60154657/191852015-263728c9-64a4-444e-b4a4-99493b46149c.png)

### Models

A model is the representation of an entity in code, at least in a descriptive way.

To create a model we are going to use the **Pydantic** library with a class called BaseModel

```python
from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Body
# Models
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None
```
Then we create a path parameters

```python
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
```

Which sends a request body
```json
{
  "first_name": "Cristhian",
  "last_name": "Carbonell",
  "age": 34,
  "hair_color": "black",
  "is_married": false
}
```
and the server responds with a response body
```json
{
  "first_name": "Cristhian",
  "last_name": "Carbonell",
  "age": 34,
  "hair_color": "black",
  "is_married": false
}
```
## Validations

### Validations: Query Parameters

To validate the **query parameters** we are going to need that the user cannot enter less than 50 characters in the name parameter and that it be greater than 1 character and we avoid cases that pass empty or pass numbers with values ​​of a million.

![validations-query](https://user-images.githubusercontent.com/60154657/191852819-812be3c9-2369-4f94-94a4-729397b1dcec.png)

```python
from fastapi import FastAPI, Body, Query
# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(name: Optional[str] = Query(None, min_length=1, max_length=50),
                age: str = Query(...)):
    return {name: age}
```
The name parameter is optional and of type string, and it is a query parameter by default if no argument is passed, it is None and has a minimum length of 1 and a maximum length of 50, in addition the age parameter is mandatory when we pass three points ... to Query(...) and return a dictionary the key is name and value is age

### Validations: exploring more parameters

To specify the validations, we must pass as parameters to the **Query** function what we need to validate.

For **str** data types:
- **max_length:** To specify the maximum length of the string
- **min_length:** To specify the minimum length of the string
- **regex:** To specify regular expressions

For data types **int:**

- **ge:** (greater or equal than ≥) to specify that the value must be greater than or equal to
- **le:** (less or equal than ≤) to specify that the value must be less than or equal to
- **gt:** (greater than >) to specify that the value should be greater
- **lt:** (less than <) to specify that the value should be less

It is possible to provide more context to our documentation. The **title** and **description parameters must be used.**

- **title:** To define a title to a parameter
- **description:** To specify a description to the parameter

![validations-parameters](https://user-images.githubusercontent.com/60154657/191853289-1a52aea0-fc6f-4f74-a064-347002f1fbc1.png)

### Validations: Path Parameters

We import **Path** to validate the path parameters, we add two title and description parameters to both the query and the path parameters, which helps us in the documentation to have more information about each parameter, we create an endpoint **/person/detail/{person_id}** which receives an integer as path parameters and we define it as mandatory with three dots in the **Path(...)** method, we also append the parameter **gt=0** that tells us that it has to pass integers greater than zero and we return a dictionary with the key person_id and the value that the id exists.

```python
from fastapi import FastAPI, Body, Query, Path
# Validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
    ),
    age: str = Query(
        ...,
        title="Persona age",
        description="This is the person age. It's required"
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
        description="This is the person id, It's required"
    )
):
    return {person_id: "It exists!"}
```
### Validations: Request Body

For the validation of **Request Body** we create a new models called **Location**, we create the new route **/person/{person_id}** that receives a mandatory **path parameters** and receives two parameters mandatory **person and location** which are the models and the user must share them by **request body,** for which the concatenation of the two dictionaries is returned.

```python
# Models

class Location(BaseModel):
    city: str
    state: str
    country: str

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person (
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
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
```

### Validations: Models

We import the **Enum** class from the enum module which will allow us to enumerate some objects, we import the Field class from the pydantic module which is similar to Body, Query and Path from the fastapi module and allows us to validate the attributes of a models, we create a new class called **HairColor** which inherits from Enum and has 5 attributes, which will be selected by the user, if you enter another value that does not correspond to the attributes, it will show us an error, then in the Person class we perform the attribute validations with Field.

```python
from enum import Enum

from pydantic import Field

class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
    )
    age: int = Field(
        ...,
        gt=0,
        le=70
    )
    hair_color: Optional[HairColor] = Field(
        default=None
    )
    is_married: Optional[bool] = Field(
        default=None
    )

@app.put("/person/{person_id}")
def update_person (
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0
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
```

### Special data types

![special-data-types](https://user-images.githubusercontent.com/60154657/191854039-6a2fb1ec-1293-44ff-b00c-4571a3c2a32d.png)

## Examples

### Creating automatic Request Body examples

One way to use request body examples is by using a Config class where we can create a dictionary with the example key and appending the attributes that will be sent through a request body

```python
class Config:
        schema_extra = {
            "example": {
                "fist_name": "Cristhian",
                "last_name": "Carbonell",
                "age": 34,
                "hair_color": "black",
                "is_married": True
            },
        }
```

The other way that is better is by appending the example attribute of the Field Class where we add what we want to see in the example

```python
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
        example="Carbonell"
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
```

![example 1](https://user-images.githubusercontent.com/60154657/191854431-82455ae4-eb9a-4c5b-bfaf-a21ea5fefed2.png)


### Creating examples of automatic Path and Query parameters

```python
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
```

To add examples in both the query and path parameters, we append the example attribute which will store the data that we write and display it

![example-2](https://user-images.githubusercontent.com/60154657/191854635-2c012c46-a15a-4960-8e50-f63d76960b93.png)

![example-3](https://user-images.githubusercontent.com/60154657/191854713-660dca7d-5ee9-4429-87f8-7f609b9ae28b.png)

**Author:** Cristhian Carbonell🏋️‍♂️
