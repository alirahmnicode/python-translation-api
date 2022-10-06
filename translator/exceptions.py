class BaseError(Exception):
    """
    base error class
    """

    def __init__(self, val, message):
        self.val = val
        self.message = message
        super().__init__()

    def __str__(self):
        return "{} --> {}".format(self.val, self.message)


class LanguageNotSupportedException(BaseError):
    """
    exception thrown if the user uses a language that is not supported by the deep_translator
    """
    
    def __init__(self, val, message="There is no support for the chosen language"):
        super().__init__(val, message)