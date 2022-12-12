from decoratorasciiart import DecoratorAsciiArt
from volaille import Volaille


class Iron(DecoratorAsciiArt):
    def __init__(self, volaille: Volaille):
        DecoratorAsciiArt.__init__(self, volaille)

    def decorateAsciiArt(self, asciiart:str):
        return asciiart[0:18] + '/\\ /\\' + asciiart[23:]
