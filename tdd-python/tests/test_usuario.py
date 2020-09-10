from src.leilao.dominio import Usuario, Leilao
import pytest


@pytest.fixture
def vini():
    return Usuario('Vini', 100)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50.0)

    assert vini.carteira == 50.0


def test_deve_permitir_propor_lance_quando_valor_eh_menor_que_saldo_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1)

    assert vini.carteira == 99


def test_deve_permitir_propor_lance_quando_valor_eh_igual_que_saldo_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100)

    assert vini.carteira == 0


def test_nao_deve_permitir_propor_lance_quando_valor_eh_maior_que_saldo_da_carteira(vini, leilao):
    with pytest.raises(ValueError):

        vini.propoe_lance(leilao, 101)

