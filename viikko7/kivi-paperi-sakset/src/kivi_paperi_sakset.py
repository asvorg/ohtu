from tuomari import Tuomari
from luo_peli import LuoPeli

class KiviPaperiSakset:

    def __init__(self, tyyppi: str = "a") -> None:
        self._toinen_pelaaja = LuoPeli().luo_peli(tyyppi)

    def pelaa(self):
        tuomari = Tuomari()

        ensimmaisen_siirto = self._ensimmaisen_siirto()
        toka_siirto = self._toisen_siirto(ensimmaisen_siirto)

        while self._onko_ok_siirto(ensimmaisen_siirto) and self._onko_ok_siirto(toka_siirto):
            tuomari.kirjaa_siirto(ensimmaisen_siirto, toka_siirto)
            print(tuomari)

            ensimmaisen_siirto = self._ensimmaisen_siirto()
            toka_siirto = self._toka_siirto(ensimmaisen_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        return self._toinen_pelaaja._toisen_pelaajan_siirto(ensimmaisen_siirto)
    
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"