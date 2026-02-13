# Protogrid Response

A lightweight, standardized API response tool for Python web frameworks. zero-dependencies by default!

## Features

- **Standardized Structure**: Every response follows the same `success`, `message`, `data`, `error`, `meta` pattern.
- **Zero Dependencies**: Uses Python standard library (`dataclasses`, `enum`, `http`).
- **Flexible Inputs**: Pass status as `APIStatus.OK`, `"ok"`, `200`, or `"200"`.
- **Framework Support**: Built-in support for FastAPI and Flask.

## Installation

```bash
pip install protogrid-response
```

## Usage

### Simple Python

You can use `make_response` (aliased as `create_response`) with flexible inputs:

```python
from api_response import make_response

# Success with string code
res = make_response(status="ok", data={"id": 1})

# Success with integer code
res = make_response(status=201, message="Created Successfully")

# Error with string code matches
err = make_response(status="not_found", message="User missing")
```

### FastAPI Integration

```python
from fastapi import FastAPI
from api_response import make_response

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    # Returns a standard response dictionary that FastAPI serializes
    return make_response(
        status=200,
        data={"user_id": user_id}
    ).to_dict()
```

_Note: If you use the integration helper `fastapi_response`, it handles the `JSONResponse` wrapper for you._

### Flask Integration

```python
from flask import Flask
from api_response.integrations.flask import flask_response

@app.get("/users/<int:user_id>")
def get_user(user_id):
    return flask_response(
        status="ok",
        data={"id": 1}
    )
```