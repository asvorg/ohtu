class IntJoukko:
    KAPASITEETTI = 5
    OLETUSKASVATUS = 5

    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti or self.KAPASITEETTI
        self.kasvatuskoko = kasvatuskoko or self.OLETUSKASVATUS
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def _luo_lista(self, koko):
        return [0] * koko

    def kuuluu(self, n):
        return n in self.ljono[:self.alkioiden_lkm]

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.ljono.extend(self._luo_lista(self.kasvatuskoko))

            return True
        return False

    def poista(self, n):
        if self.kuuluu(n):
            kohta = self.ljono.index(n)
            self.ljono.pop(kohta)
            self.alkioiden_lkm -= 1
            return True
        return False

    def kopioi_lista(self, a, b):
        b.extend(a)

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.ljono[:self.alkioiden_lkm]

    @staticmethod
    def _yhdiste_tai_leikkaus(a, b, yhdista):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            tulos.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            if yhdista or a.kuuluu(b_taulu[i]):
                tulos.lisaa(b_taulu[i])

        return tulos

    @staticmethod
    def yhdiste(a, b):
        return IntJoukko._yhdiste_tai_leikkaus(a, b, True)

    @staticmethod
    def leikkaus(a, b):
        return IntJoukko._yhdiste_tai_leikkaus(a, b, False)

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()
        a_taulu = a.to_int_list()

        for i in range(0, len(a_taulu)):
            if not b.kuuluu(a_taulu[i]):
                tulos.lisaa(a_taulu[i])

        return tulos

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        return "{" + ", ".join(map(str, self.ljono[:self.alkioiden_lkm])) + "}"
