from .exceptions import LanguageNotSupportedException
from .constant import GOOGLE_LANGUAGES_TO_CODES as gls


class BaseTranslate:
    def __init__(self, text: str, target: str, source: str):
        self.text = text
        self.source = source
        self._check_language_support(target=target)

    def _check_language_support(self, target: str):
        """
        check if target language supported or not
        """
        if target in gls.values():
            self.target = target
        else:
            raise LanguageNotSupportedException(target)