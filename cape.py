from decoratorasciiart import DecoratorAsciiArt
from volaille import Volaille


class Cape(DecoratorAsciiArt):
    def __init__(self, volaille: Volaille):
        DecoratorAsciiArt.__init__(self, volaille)

    def decorateAsciiArt(self, asciiart:str):
        return asciiart[0:9] + '\\' + asciiart[10:16] + '\\' + asciiart[17:]
