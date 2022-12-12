from volaille import Volaille


class GallusGallusDomesticus(Volaille):
    def chanter(self) -> str:
        return "Cot cot cot codet"

    def manger(self) -> str:
        return "..."

    def getAsciiArt(self) -> str:
        return "     \n" \
               "<.)  \n" \
               "(  >)\n" \
               "^  ^ "
