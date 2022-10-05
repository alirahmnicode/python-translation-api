import requests
from bs4 import BeautifulSoup

base_url = "https://translate.google.com/m"
params = {
    "sl": "en",
    "tl": "fa",
    "q": "how are you"
}

class GoogleTranslate:
    def __init__(self, text: str):
        self.text = text
        self.element_tag="div",
        self.element_query={"class": "t0"},
        self._alt_element_query = {"class": "result-container"}

    def translate(self):
        r = requests.get(url=base_url, params=params)
        s = BeautifulSoup(r.text, 'html.parser')
        element = s.find(self.element_tag, self.element_query)
        if not element:
                element = s.find(self.element_tag, self._alt_element_query)
        return element.get_text(strip=True)
