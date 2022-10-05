from fastapi import FastAPI
from translator.google import GoogleTranslate


app = FastAPI()


@app.get("/{text}/")
def translate(text: str):
    gt = GoogleTranslate(text)
    s = gt.translate()
    return s