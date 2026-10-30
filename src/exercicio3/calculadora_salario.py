"""Módulo contendo a calculadora de salário e modelos para o Exercício 3."""
from enum import Enum


class Cargo(str, Enum):
    """Cargos disponíveis na organização."""

    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


class Funcionario:
    """Representa um funcionário com nome, e-mail, salário base e cargo."""

    def __init__(
        self,
        nome: str,
        email: str,
        salario_base: float,
        cargo: Cargo,
    ) -> None:
        self.nome = nome
        self.email = email
        self.salario_base = float(salario_base)
        self.cargo = cargo


class CalculadoraSalario:
    """Calculadora responsável por apurar o salário líquido com base no cargo e salário base."""

    @staticmethod
    def calcular_salario_liquido(funcionario: Funcionario) -> float:
        """Calcula o salário líquido de um funcionário de acordo com as regras de desconto.

        Regras de Desconto:
        - DESENVOLVEDOR:
            20% se salario_base >= 3000.00;
            10% caso contrário.
        - DBA:
            25% se salario_base >= 2000.00;
            15% caso contrário.
        - TESTADOR:
            25% se salario_base >= 2000.00;
            15% caso contrário.
        - GERENTE:
            30% se salario_base >= 5000.00;
            20% caso contrário.
        """
        salario = funcionario.salario_base
        cargo = funcionario.cargo

        if cargo == Cargo.DESENVOLVEDOR:
            taxa_desconto = 0.20 if salario >= 3000.00 else 0.10
        elif cargo == Cargo.DBA:
            taxa_desconto = 0.25 if salario >= 2000.00 else 0.15
        elif cargo == Cargo.TESTADOR:
            taxa_desconto = 0.25 if salario >= 2000.00 else 0.15
        elif cargo == Cargo.GERENTE:
            taxa_desconto = 0.30 if salario >= 5000.00 else 0.20
        else:
            raise ValueError(f"Cargo não suportado: {cargo}")

        salario_liquido = salario * (1.0 - taxa_desconto)
        return round(salario_liquido, 2)
