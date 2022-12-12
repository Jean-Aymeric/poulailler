from abc import ABC,abstractmethod


class Volaille(ABC):
    @abstractmethod
    def chanter(self) -> str:
        pass

    @abstractmethod
    def manger(self) -> str:
        pass

    @abstractmethod
    def getAsciiArt(self) -> str:
        pass