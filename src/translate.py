from fastapi import FastAPI, Query
from typing import Annotated
from transformers import pipeline
from pydantic import BaseModel
app = FastAPI()

class data(BaseModel):
    language:str
    text:str
    
@app.post("/text")
async def main(data:data):
    if data.language == "Arabic":
        pipe = pipeline("translation", model="Helsinki-NLP/opus-mt-tc-big-ar-en")
        other_language = "English"

    elif data.language == "English":
        pipe = pipeline("translation", model="marefa-nlp/marefa-mt-en-ar")
        other_language = "Arabic"
    return {"blog":data.text, other_language:pipe(data.text)[0]["translation_text"]}