"""Módulo de classificação de triângulos para o Exercício 1."""


def classificar_triangulo(a: int, b: int, c: int) -> str:
    """Classifica um triângulo a partir do comprimento de seus três lados inteiros.

    Regras:
    - Todos os lados devem ser estritamente maiores que zero.
    - A soma de quaisquer dois lados deve ser estritamente maior que o terceiro lado
      (desigualdade triangular: a + b > c, a + c > b, b + c > a).
    - Se qualquer condição for violada, retorna "Invalido".
    - Caso válido:
        - "Equilatero": 3 lados iguais.
        - "Isosceles": 2 lados iguais.
        - "Escaleno": 3 lados diferentes.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalido"

    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalido"

    if a == b == c:
        return "Equilatero"

    if a == b or a == c or b == c:
        return "Isosceles"

    return "Escaleno"


class Triangulo:
    """Representa um triângulo com 3 lados inteiros."""

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    def classificar(self) -> str:
        """Retorna a classificação do triângulo."""
        return classificar_triangulo(self.a, self.b, self.c)
