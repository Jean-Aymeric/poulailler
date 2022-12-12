from decoratorasciiart import DecoratorAsciiArt
from volaille import Volaille


class Roux(DecoratorAsciiArt):
    def __init__(self, volaille: Volaille):
        DecoratorAsciiArt.__init__(self, volaille)

    def decorateAsciiArt(self, asciiart:str):
        return asciiart[0:13] + '##' + asciiart[15:]
