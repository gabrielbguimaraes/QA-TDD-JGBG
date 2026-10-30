# QA-TDD-JGBG

Implementação dos 3 exercícios práticos de Qualidade de Software e TDD em Python, com testes unitários via `pytest` e relatório de cobertura via `pytest-cov`.

## Estrutura do Projeto

- `src/exercicio1/` e `tests/exercicio1/`: Classificação de triângulos e validação de desigualdade triangular.
- `src/exercicio2/` e `tests/exercicio2/`: Cadastro e validação de dados (`Person`, `Email`, `PersonDAO`).
- `src/exercicio3/` e `tests/exercicio3/`: Calculadora de salário líquido com descontos por cargo e faixa salarial.

## Como Executar

### 1. Criar e ativar o ambiente virtual

No Windows (PowerShell):
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Linux / macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Executar os testes com cobertura

Execução geral:
```bash
pytest --cov=src --cov-report=term-missing
```

Execução por exercício:
```bash
pytest tests/exercicio1 --cov=src/exercicio1 --cov-report=term-missing
pytest tests/exercicio2 --cov=src/exercicio2 --cov-report=term-missing
pytest tests/exercicio3 --cov=src/exercicio3 --cov-report=term-missing
```

## Evidências de Cobertura

### Exercício 1 (Triângulos)
```text
Name                          Stmts   Miss Branch BrPart  Cover   Missing
-------------------------------------------------------------------------
src\exercicio1\__init__.py        2      0      0      0   100%
src\exercicio1\triangulo.py      17      0      8      0   100%
-------------------------------------------------------------------------
TOTAL                            19      0      8      0   100%
```

### Exercício 2 (Validação de Cadastro)
```text
Name                         Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------------------
src\exercicio2\__init__.py       2      0      0      0   100%
src\exercicio2\models.py        36      0     14      0   100%
------------------------------------------------------------------------
TOTAL                           38      0     14      0   100%
```

### Exercício 3 (Calculadora de Salário)
```text
Name                                    Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------------------
src\exercicio3\__init__.py                  2      0      0      0   100%
src\exercicio3\calculadora_salario.py      28      0      8      0   100%
-----------------------------------------------------------------------------------
TOTAL                                      30      0      8      0   100%
```

### Relatório Geral Consolidado
```text
Name                                    Stmts   Miss Branch BrPart  Cover   Missing
-----------------------------------------------------------------------------------
src\__init__.py                             0      0      0      0   100%
src\exercicio1\__init__.py                  2      0      0      0   100%
src\exercicio1\triangulo.py                17      0      8      0   100%
src\exercicio2\__init__.py                  2      0      0      0   100%
src\exercicio2\models.py                   36      0     14      0   100%
src\exercicio3\__init__.py                  2      0      0      0   100%
src\exercicio3\calculadora_salario.py      28      0      8      0   100%
-----------------------------------------------------------------------------------
TOTAL                                      87      0     30      0   100%
```