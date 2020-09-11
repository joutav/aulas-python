from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self) -> None:
        self.jao = Usuario("Joao", 500)
        self.lance_do_jao = Lance(self.jao, 100.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        gui = Usuario('Gui', 500)
        lance_do_gui = Lance(gui, 150.0)



        self.leilao.propoe(self.lance_do_jao)
        self.leilao.propoe(lance_do_gui)


        menor_valor_esperado = 100
        maior_valor_esperado = 150

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_lances_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            gui = Usuario('Gui', 500)
            lance_do_gui = Lance(gui, 150.0)

            self.leilao.propoe(lance_do_gui)
            self.leilao.propoe(self.lance_do_jao)



    def test_deve_retornar_o_mesmo_valor_para_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        self.leilao.propoe(self.lance_do_jao)



        menor_valor_esperado = 100
        maior_valor_esperado = 100

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_o_leilao_tiver_tres_lances(self):
        jorge = Usuario("Jorge", 500)
        gui = Usuario('Gui', 500)

        lance_do_gui = Lance(gui, 150.0)
        lance_do_jorge = Lance(jorge, 200.0)

        self.leilao.propoe(self.lance_do_jao)
        self.leilao.propoe(lance_do_gui)
        self.leilao.propoe(lance_do_jorge)



        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se o leilao nao tiver lances, permite propor

    def test_deve_permitir_propor_lance_caso_leilao_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_jao)


        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebido)

    # se o usuario for diferente do ultimo lance, permite propor
    def test_deve_permitir_propor_lance_caso_o_ultimo_usuario_seja_diferente(self):
        gui = Usuario('gui', 500)
        lance_do_gui = Lance(gui, 200)

        self.leilao.propoe(self.lance_do_jao)
        self.leilao.propoe(lance_do_gui)

        quantidade_de_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebido)

    # se o usuario for igual ao do ultimo lance, não permite propor
    def test_nao_deve_permitir_propo_lance_caso_usuario_seja_o_mesmo(self):
        lance_do_jao200 = Lance(self.jao, 200)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_jao)
            self.leilao.propoe(lance_do_jao200)


