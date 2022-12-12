from decoratorasciiart import DecoratorAsciiArt
from volaille import Volaille


class NonGenre(DecoratorAsciiArt):
    def __init__(self, volaille: Volaille):
        DecoratorAsciiArt.__init__(self, volaille)

    def decorateAsciiArt(self, asciiart:str):
        return asciiart[0:10] + '!' + asciiart[11:]
