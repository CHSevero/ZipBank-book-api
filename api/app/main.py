from fastapi import FastAPI

app = FastAPI()


@app.get("/", tags=["Book-API"])
def root():
    return {"message": "Book-API alive!"}