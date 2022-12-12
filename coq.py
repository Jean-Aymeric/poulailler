from volaille import Volaille


class Coq(Volaille):
    def chanter(self) -> str:
        return "CocoriCOOOO"

    def manger(self) -> str:
        return "..."

    def getAsciiArt(self) -> str:
        return " M   \n" \
               "<.) !\n" \
               "(  >)\n" \
               "^  ^ "
