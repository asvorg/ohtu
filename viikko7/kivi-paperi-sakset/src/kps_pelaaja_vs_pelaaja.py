from tuomari import Tuomari


class KPSPelaajaVsPelaaja:
    def _toisen_pelaajan_siirto(self, *siirrot): 
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
