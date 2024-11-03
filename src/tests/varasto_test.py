import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_voi_ottaa_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(6)

        maara = self.varasto.ota_varastosta(8)

        self.assertAlmostEqual(maara, 6)

    def test_ei_voi_laittaa_enemman_kuin_tilaa(self):
        self.varasto.lisaa_varastoon(20)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ei_lisata_negatiivista_tilaa(self):
        self.varasto.lisaa_varastoon(-5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_oteta_negatiivista_tilaa(self):
        maara = self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(maara, 0.0)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ei_luoda_negatiivista_varastoa(self):
        self.negvarasto = Varasto(-5, -5)

        self.assertAlmostEqual(self.negvarasto.tilavuus, 0)
        self.assertAlmostEqual(self.negvarasto.saldo, 0)

    def test_ei_luoda_ylitse_tayttyvaa_varastoa(self):
        self.ylivarasto = Varasto(5, 10)

        self.assertAlmostEqual(self.ylivarasto.saldo, 5)

    def test_tulostaa_oikein(self):
        self.assertAlmostEqual(str(self.varasto), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")


