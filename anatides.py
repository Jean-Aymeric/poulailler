from volaille import Volaille


class Anatides(Volaille):
    def chanter(self) -> str:
        return "Couin Couin"

    def manger(self) -> str:
        return "..."

    def getAsciiArt(self) -> str:
        return "     \n" \
               "=.)  \n" \
               "(  >)\n" \
               "^  ^ "
