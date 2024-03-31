from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    text = item.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Input text cannot be empty or contain only whitespace characters.")

    try:
        result = classifier(text)[0]
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the input text: {str(e)}")
