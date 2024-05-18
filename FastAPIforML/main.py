from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from ml import obtain_image

import io
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}


# app.get("/")(read_root) # this is equivalent to to @app.get("/")

# run by "uvicorn main:app"  command


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "Message": "Hello"}


# run by "uvicorn main:app --reload" to restart the server automatically

# navigate base_url/docs for swagger ui

"""fastapi is build on top of Starlette and Pydantic.
Starlette for all the web part and Pydantic for all the data part"""


class Item(BaseModel):
    name: str
    price: float
    tags: list[str] = []


@app.post("/items/")
def create_items(item: Item):
    return item


@app.get("/generate")
def generate_image(prompt: str):
    image = obtain_image(prompt, num_inference_steps=5, seed=1024)
    image.save("image.png")
    return FileResponse("image.png")


# Streaming the response instead of saving
@app.get("/generate")
def generate_image(prompt: str):
    image = obtain_image(prompt, num_inference_steps=5, seed=1024)
    memory_stream = io.BytesIO()
    image.save(memory_stream, format="PNG")
    memory_stream.seek(0)
    return StreamingResponse(memory_stream, media_type="image/png")


# with specific parameter value
@app.get("/generate_specific")
def generate_image(
    prompt: str,
    *,
    seed: int | None = None,
    num_inference_steps: int = 50,
    guidance_scale: float = 7.5,
):
    image = obtain_image(
        prompt,
        num_inference_steps=num_inference_steps,
        seed=seed,
        guidance_scale=guidance_scale,
    )
    image.save("image.png")
    return FileResponse("image.png")


# run by "uvicorn main:app" cause we dont want to restart the server for every changes
