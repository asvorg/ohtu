from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class LuoPeli:
    def luo_peli(self, choice):
        choices = {"a": KPSPelaajaVsPelaaja,
                    "b": KPSTekoaly,
                    "c": KPSParempiTekoaly
                    }
        return choices[choice]()