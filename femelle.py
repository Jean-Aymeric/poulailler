from decoratorasciiart import DecoratorAsciiArt
from volaille import Volaille


class Femelle(DecoratorAsciiArt):
    def __init__(self, volaille: Volaille):
        DecoratorAsciiArt.__init__(self, volaille)

    def decorateAsciiArt(self, asciiart:str):
        return asciiart
