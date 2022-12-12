from anatides import Anatides
from cape import Cape
from femelle import Femelle
from gallusgallusdomesticus import GallusGallusDomesticus
from iron import Iron
from male import Male
from nongenre import NonGenre
from poulailler import Poulailler
from roux import Roux

poule = NonGenre(Femelle(Femelle(GallusGallusDomesticus())))
coq = Cape(Iron(Roux(NonGenre(Anatides()))))
poulailler = Poulailler()
poulailler.addVolaille(poule)
poulailler.addVolaille(coq)

poulailler.display()
poulailler.removeVolaille(coq)
coq = Male(coq)
poulailler.addVolaille(coq)
poulailler.display()
