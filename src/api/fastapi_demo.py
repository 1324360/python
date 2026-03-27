# FastAPI Demo

This is a simple FastAPI application.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```