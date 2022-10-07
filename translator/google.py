import requests
from bs4 import BeautifulSoup
from .translate import BaseTranslate
from .constant import BASE_URL
from .exceptions import TranslationNotFound


    
class GoogleTranslate(BaseTranslate):
    """
    use google for translate
    """
    def __init__(self, text: str, target: str = "en", source: str = "auto"):
        self.element_tag = "div",
        self.element_query = {"class": "t0"},
        self._alt_element_query = {"class": "result-container"}
        super().__init__(text, target, source)

    def translate(self):
        r = requests.get(url=BASE_URL, params=self.get_params())
        s = BeautifulSoup(r.text, 'html.parser')
        element = s.find(self.element_tag, self.element_query)
        if not element:
            element = s.find(self.element_tag, self._alt_element_query)
            if not element:
                raise TranslationNotFound(self.text)
        return element.get_text(strip=True)

    def get_params(self):
        text = self.text.strip()
        params = dict()
        params['tl'] = self.target
        params['sl'] = self.source
        params['q'] = text
        return params
