from decoratorasciiart import DecoratorAsciiArt
from volaille import Volaille


class Male(DecoratorAsciiArt):
    def __init__(self, volaille: Volaille):
        DecoratorAsciiArt.__init__(self, volaille)

    def decorateAsciiArt(self, asciiart:str):
        return asciiart[0] + 'M' + asciiart[2:10] + '!' + asciiart[11:]
