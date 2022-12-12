from volaille import Volaille


class Poulailler:
    __volailles: [Volaille]

    def __init__(self):
        self.__volailles = []

    def addVolaille(self, volaille: Volaille) -> None:
        self.__volailles.append(volaille)

    def removeVolaille(self, volaille: Volaille) -> None:
        self.__volailles.remove(volaille)

    def display(self) -> None:
        asciiArts = []
        for volaille in self.__volailles:
            asciiArts.append(volaille.getAsciiArt().split("\n"))
        for i in range(len(asciiArts[0])):
            line = ""
            for asciiArt in asciiArts:
                line += asciiArt[i] + " "
            print(line)
        for volaille in self.__volailles:
            print(volaille.chanter())
