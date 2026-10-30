"""Casos de teste para o Exercício 3: Calculadora de Salário com TDD."""
import pytest
from src.exercicio3.calculadora_salario import (
    CalculadoraSalario,
    Cargo,
    Funcionario,
)

# --- Testes de DESENVOLVEDOR (Limite: 3000.00 | >= 20%, < 10%) ---


def test_desenvolvedor_salario_abaixo_do_limite():
    """Desenvolvedor com salário abaixo de 3000.00 deve ter 10% de desconto."""
    func = Funcionario("Alice Dev", "alice@empresa.com", 2500.00, Cargo.DESENVOLVEDOR)
    # 2500.00 - 10% = 2250.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 2250.00


def test_desenvolvedor_salario_exatamente_no_limite():
    """Desenvolvedor com salário exatamente 3000.00 deve ter 20% de desconto."""
    func = Funcionario("Bob Dev", "bob@empresa.com", 3000.00, Cargo.DESENVOLVEDOR)
    # 3000.00 - 20% = 2400.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 2400.00


def test_desenvolvedor_salario_acima_do_limite():
    """Desenvolvedor com salário acima de 3000.00 deve ter 20% de desconto."""
    func = Funcionario("Carol Dev", "carol@empresa.com", 4500.00, Cargo.DESENVOLVEDOR)
    # 4500.00 - 20% = 3600.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 3600.00


def test_desenvolvedor_fronteira_imediatamente_abaixo():
    """Desenvolvedor com 2999.99 deve ter 10% de desconto."""
    func = Funcionario("Dev Fronteira", "dev@empresa.com", 2999.99, Cargo.DESENVOLVEDOR)
    # 2999.99 * 0.9 = 2699.991 -> 2699.99
    assert CalculadoraSalario.calcular_salario_liquido(func) == 2699.99


# --- Testes de DBA (Limite: 2000.00 | >= 25%, < 15%) ---


def test_dba_salario_abaixo_do_limite():
    """DBA com salário abaixo de 2000.00 deve ter 15% de desconto."""
    func = Funcionario("Daniel DBA", "daniel@empresa.com", 1500.00, Cargo.DBA)
    # 1500.00 - 15% = 1275.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 1275.00


def test_dba_salario_exatamente_no_limite():
    """DBA com salário exatamente 2000.00 deve ter 25% de desconto."""
    func = Funcionario("Eduarda DBA", "eduarda@empresa.com", 2000.00, Cargo.DBA)
    # 2000.00 - 25% = 1500.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 1500.00


def test_dba_salario_acima_do_limite():
    """DBA com salário acima de 2000.00 deve ter 25% de desconto."""
    func = Funcionario("Fabio DBA", "fabio@empresa.com", 3000.00, Cargo.DBA)
    # 3000.00 - 25% = 2250.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 2250.00


def test_dba_fronteira_imediatamente_abaixo():
    """DBA com 1999.99 deve ter 15% de desconto."""
    func = Funcionario("DBA Fronteira", "dba@empresa.com", 1999.99, Cargo.DBA)
    # 1999.99 * 0.85 = 1699.9915 -> 1699.99
    assert CalculadoraSalario.calcular_salario_liquido(func) == 1699.99


# --- Testes de TESTADOR (Limite: 2000.00 | >= 25%, < 15%) ---


def test_testador_salario_abaixo_do_limite():
    """Testador com salário abaixo de 2000.00 deve ter 15% de desconto."""
    func = Funcionario("Gisele QA", "gisele@empresa.com", 1600.00, Cargo.TESTADOR)
    # 1600.00 - 15% = 1360.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 1360.00


def test_testador_salario_exatamente_no_limite():
    """Testador com salário exatamente 2000.00 deve ter 25% de desconto."""
    func = Funcionario("Hugo QA", "hugo@empresa.com", 2000.00, Cargo.TESTADOR)
    # 2000.00 - 25% = 1500.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 1500.00


def test_testador_salario_acima_do_limite():
    """Testador com salário acima de 2000.00 deve ter 25% de desconto."""
    func = Funcionario("Igor QA", "igor@empresa.com", 2800.00, Cargo.TESTADOR)
    # 2800.00 - 25% = 2100.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 2100.00


def test_testador_fronteira_imediatamente_abaixo():
    """Testador com 1999.99 deve ter 15% de desconto."""
    func = Funcionario("QA Fronteira", "qa@empresa.com", 1999.99, Cargo.TESTADOR)
    # 1999.99 * 0.85 = 1699.9915 -> 1699.99
    assert CalculadoraSalario.calcular_salario_liquido(func) == 1699.99


# --- Testes de GERENTE (Limite: 5000.00 | >= 30%, < 20%) ---


def test_gerente_salario_abaixo_do_limite():
    """Gerente com salário abaixo de 5000.00 deve ter 20% de desconto."""
    func = Funcionario("Julia Gerente", "julia@empresa.com", 4000.00, Cargo.GERENTE)
    # 4000.00 - 20% = 3200.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 3200.00


def test_gerente_salario_exatamente_no_limite():
    """Gerente com salário exatamente 5000.00 deve ter 30% de desconto."""
    func = Funcionario("Lucas Gerente", "lucas@empresa.com", 5000.00, Cargo.GERENTE)
    # 5000.00 - 30% = 3500.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 3500.00


def test_gerente_salario_acima_do_limite():
    """Gerente com salário acima de 5000.00 deve ter 30% de desconto."""
    func = Funcionario("Mariana Gerente", "mariana@empresa.com", 7000.00, Cargo.GERENTE)
    # 7000.00 - 30% = 4900.00
    assert CalculadoraSalario.calcular_salario_liquido(func) == 4900.00


def test_gerente_fronteira_imediatamente_abaixo():
    """Gerente com 4999.99 deve ter 20% de desconto."""
    func = Funcionario("Gerente Fronteira", "gf@empresa.com", 4999.99, Cargo.GERENTE)
    # 4999.99 * 0.8 = 3999.992 -> 3999.99
    assert CalculadoraSalario.calcular_salario_liquido(func) == 3999.99


# --- Testes de Casos Especiais, Erros e Inicialização ---


def test_cargo_invalido_lanca_excecao():
    """Cargo desconhecido/inválido deve lançar ValueError."""
    func = Funcionario("Desconhecido", "desc@empresa.com", 2500.00, "ESTAGIARIO")  # type: ignore
    with pytest.raises(ValueError) as exc_info:
        CalculadoraSalario.calcular_salario_liquido(func)

    assert "Cargo não suportado" in str(exc_info.value)


def test_instanciacao_calculadora_e_atributos_funcionario():
    """Verifica atributos de Funcionario e chamada via instância da CalculadoraSalario."""
    calc = CalculadoraSalario()
    func = Funcionario("Teste", "teste@empresa.com", 1000, Cargo.DESENVOLVEDOR)
    assert func.nome == "Teste"
    assert func.email == "teste@empresa.com"
    assert func.salario_base == 1000.0
    assert func.cargo == Cargo.DESENVOLVEDOR

    assert calc.calcular_salario_liquido(func) == 900.00
