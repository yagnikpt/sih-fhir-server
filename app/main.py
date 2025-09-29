from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers.conceptmap import router as conceptmap_router

_ = load_dotenv()
app = FastAPI()

app.include_router(conceptmap_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
