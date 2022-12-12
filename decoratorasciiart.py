from abc import ABC, abstractmethod

from volaille import Volaille


class DecoratorAsciiArt(Volaille, ABC):
    __volaille: Volaille

    def __init__(self, volaille: Volaille):
        self.__volaille = volaille

    def chanter(self) -> str:
        return self.__volaille.chanter()

    def manger(self) -> str:
        return self.__volaille.manger()

    def getAsciiArt(self) -> str:
        return self.decorateAsciiArt(self.__volaille.getAsciiArt())

    @abstractmethod
    def decorateAsciiArt(self, asciiart:str):
        pass
