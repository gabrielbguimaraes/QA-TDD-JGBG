"""Casos de teste para o Exercício 1: Classificação de Triângulos."""
import pytest
from src.exercicio1.triangulo import Triangulo, classificar_triangulo


def test_ct01_triangulo_escaleno_valido():
    """CT01: Triângulo escaleno válido (ex: 3, 4, 5)."""
    assert classificar_triangulo(3, 4, 5) == "Escaleno"


def test_ct02_triangulo_isosceles_valido():
    """CT02: Triângulo isósceles válido (ex: 5, 5, 4)."""
    assert classificar_triangulo(5, 5, 4) == "Isosceles"


def test_ct03_triangulo_equilatero_valido():
    """CT03: Triângulo equilátero válido (ex: 5, 5, 5)."""
    assert classificar_triangulo(5, 5, 5) == "Equilatero"


def test_ct04_1_isosceles_permutacao_a_igual_b():
    """CT04 (Caso 1): Isósceles com permutação dos valores - a == b (5, 5, 3)."""
    assert classificar_triangulo(5, 5, 3) == "Isosceles"


def test_ct04_2_isosceles_permutacao_a_igual_c():
    """CT04 (Caso 2): Isósceles com permutação dos valores - a == c (5, 3, 5)."""
    assert classificar_triangulo(5, 3, 5) == "Isosceles"


def test_ct04_3_isosceles_permutacao_b_igual_c():
    """CT04 (Caso 3): Isósceles com permutação dos valores - b == c (3, 5, 5)."""
    assert classificar_triangulo(3, 5, 5) == "Isosceles"


def test_ct05_um_valor_zero():
    """CT05: Um valor zero (ex: 0, 4, 5)."""
    assert classificar_triangulo(0, 4, 5) == "Invalido"


def test_ct05_permutacoes_com_zero():
    """CT05 complementar: Permutações com zero nas outras posições."""
    assert classificar_triangulo(4, 0, 5) == "Invalido"
    assert classificar_triangulo(4, 5, 0) == "Invalido"


def test_ct06_um_valor_negativo():
    """CT06: Um valor negativo (ex: -2, 4, 5)."""
    assert classificar_triangulo(-2, 4, 5) == "Invalido"


def test_ct06_permutacoes_com_negativo():
    """CT06 complementar: Permutações com negativo nas outras posições."""
    assert classificar_triangulo(4, -2, 5) == "Invalido"
    assert classificar_triangulo(4, 5, -2) == "Invalido"


def test_ct07_08_soma_dois_lados_igual_terceiro_permutacao_1():
    """CT07/CT08 Permutação 1: a + b == c -> 2 + 3 == 5."""
    assert classificar_triangulo(2, 3, 5) == "Invalido"


def test_ct07_08_soma_dois_lados_igual_terceiro_permutacao_2():
    """CT07/CT08 Permutação 2: a + c == b -> 2 + 3 == 5 (2, 5, 3)."""
    assert classificar_triangulo(2, 5, 3) == "Invalido"


def test_ct07_08_soma_dois_lados_igual_terceiro_permutacao_3():
    """CT07/CT08 Permutação 3: b + c == a -> 2 + 3 == 5 (5, 2, 3)."""
    assert classificar_triangulo(5, 2, 3) == "Invalido"


def test_ct09_10_soma_dois_lados_menor_terceiro_permutacao_1():
    """CT09/CT10 Permutação 1: a + b < c -> 2 + 3 < 6 (2, 3, 6)."""
    assert classificar_triangulo(2, 3, 6) == "Invalido"


def test_ct09_10_soma_dois_lados_menor_terceiro_permutacao_2():
    """CT09/CT10 Permutação 2: a + c < b -> 2 + 3 < 6 (2, 6, 3)."""
    assert classificar_triangulo(2, 6, 3) == "Invalido"


def test_ct09_10_soma_dois_lados_menor_terceiro_permutacao_3():
    """CT09/CT10 Permutação 3: b + c < a -> 2 + 3 < 6 (6, 2, 3)."""
    assert classificar_triangulo(6, 2, 3) == "Invalido"


def test_ct11_tres_valores_iguais_a_zero():
    """CT11: Os três valores iguais a zero (0, 0, 0)."""
    assert classificar_triangulo(0, 0, 0) == "Invalido"


def test_classe_triangulo_instanciacao_e_metodo_classificar():
    """Verifica comportamento orientado a objetos da classe Triangulo."""
    t_equilatero = Triangulo(5, 5, 5)
    assert t_equilatero.a == 5
    assert t_equilatero.b == 5
    assert t_equilatero.c == 5
    assert t_equilatero.classificar() == "Equilatero"

    t_invalido = Triangulo(1, 2, 10)
    assert t_invalido.classificar() == "Invalido"
