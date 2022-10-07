from fastapi import FastAPI
from translator.google import GoogleTranslate
from translator.constant import GOOGLE_LANGUAGES_TO_CODES


app = FastAPI()


@app.get("/translate/")
def translate(text: str, tl: str, sl: str):
    gt = GoogleTranslate(text=text, target=tl, source=sl)
    translated = gt.translate()
    return translated


@app.get("/languages/support/")
def languages_support():
    return GOOGLE_LANGUAGES_TO_CODES
