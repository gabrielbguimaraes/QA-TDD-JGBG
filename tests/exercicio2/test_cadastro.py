"""Casos de teste para o Exercício 2: Validação de Cadastro com TDD."""
import pytest
from src.exercicio2.models import Email, Person, PersonDAO


@pytest.fixture
def dao() -> PersonDAO:
    """Fixture que instancia o PersonDAO limpo para cada teste."""
    return PersonDAO()


@pytest.fixture
def valid_person() -> Person:
    """Fixture que cria uma pessoa totalmente válida."""
    return Person(
        id=1,
        name="Carlos Silva",
        age=30,
        emails=[Email(id=1, name="carlos@email.com")],
    )


# --- Teste de Pessoa Válida ---


def test_pessoa_totalmente_valida(dao: PersonDAO, valid_person: Person):
    """Pessoa com todos os campos válidos não deve apresentar erros."""
    errors = dao.isValidToInclude(valid_person)
    assert errors == []


def test_pessoa_com_multiplos_emails_validos(dao: PersonDAO):
    """Pessoa com múltiplos e-mails válidos deve ser aceita."""
    p = Person(
        id=1,
        name="Maria Santos",
        age=25,
        emails=[
            Email(id=1, name="maria@pessoal.com"),
            Email(id=2, name="maria@trabalho.org"),
        ],
    )
    assert dao.isValidToInclude(p) == []


# --- Testes de Validação do Nome ---


def test_nome_com_apenas_uma_parte(dao: PersonDAO):
    """Nome com apenas uma palavra deve ser recusado."""
    p = Person(id=1, name="Silva", age=25, emails=[Email(1, "silva@mail.com")])
    errors = dao.isValidToInclude(p)
    assert len(errors) == 1
    assert "ao menos duas partes" in errors[0]


def test_nome_vazio(dao: PersonDAO):
    """Nome em branco ou vazio deve ser recusado."""
    p1 = Person(id=1, name="", age=25, emails=[Email(1, "teste@mail.com")])
    p2 = Person(id=2, name="   ", age=25, emails=[Email(1, "teste@mail.com")])

    assert len(dao.isValidToInclude(p1)) == 1
    assert len(dao.isValidToInclude(p2)) == 1


def test_nome_com_numeros(dao: PersonDAO):
    """Nome contendo dígitos deve ser recusado."""
    p = Person(id=1, name="Carlos 123", age=25, emails=[Email(1, "carlos@mail.com")])
    errors = dao.isValidToInclude(p)
    assert len(errors) == 1
    assert "apenas letras" in errors[0]


def test_nome_com_caracteres_especiais(dao: PersonDAO):
    """Nome contendo caracteres especiais/símbolos deve ser recusado."""
    p = Person(id=1, name="Carlos @Silva", age=25, emails=[Email(1, "carlos@mail.com")])
    errors = dao.isValidToInclude(p)
    assert len(errors) == 1
    assert "apenas letras" in errors[0]


# --- Testes de Análise de Valor Limite (AVL) para Idade [1, 200] ---


def test_idade_limite_inferior_invalido_zero(dao: PersonDAO):
    """Idade 0 (imediatamente abaixo do limite inferior 1) deve ser inválida."""
    p = Person(id=1, name="Carlos Silva", age=0, emails=[Email(1, "c@mail.com")])
    errors = dao.isValidToInclude(p)
    assert any("intervalo fechado de 1 a 200" in err for err in errors)


def test_idade_limite_inferior_valido_um(dao: PersonDAO):
    """Idade 1 (limite inferior) deve ser válida."""
    p = Person(id=1, name="Carlos Silva", age=1, emails=[Email(1, "c@mail.com")])
    assert dao.isValidToInclude(p) == []


def test_idade_limite_superior_valido_duzentos(dao: PersonDAO):
    """Idade 200 (limite superior) deve ser válida."""
    p = Person(id=1, name="Carlos Silva", age=200, emails=[Email(1, "c@mail.com")])
    assert dao.isValidToInclude(p) == []


def test_idade_limite_superior_invalido_duzentos_e_um(dao: PersonDAO):
    """Idade 201 (imediatamente acima do limite superior 200) deve ser inválida."""
    p = Person(id=1, name="Carlos Silva", age=201, emails=[Email(1, "c@mail.com")])
    errors = dao.isValidToInclude(p)
    assert any("intervalo fechado de 1 a 200" in err for err in errors)


def test_idade_negativa(dao: PersonDAO):
    """Idade negativa deve ser inválida."""
    p = Person(id=1, name="Carlos Silva", age=-15, emails=[Email(1, "c@mail.com")])
    errors = dao.isValidToInclude(p)
    assert any("intervalo fechado de 1 a 200" in err for err in errors)


def test_idade_nula(dao: PersonDAO):
    """Idade None deve ser tratada como inválida."""
    p = Person(id=1, name="Carlos Silva", age=None, emails=[Email(1, "c@mail.com")])  # type: ignore
    errors = dao.isValidToInclude(p)
    assert any("intervalo fechado de 1 a 200" in err for err in errors)


# --- Testes de Associação de E-mail ---


def test_pessoa_sem_emails_associados_lista_vazia(dao: PersonDAO):
    """Pessoa com lista vazia de e-mails deve retornar erro."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[])
    errors = dao.isValidToInclude(p)
    assert any("ao menos um e-mail" in err for err in errors)


def test_pessoa_sem_emails_associados_nulo(dao: PersonDAO):
    """Pessoa com e-mails nulos (None) deve ser inicializada/rejeitada."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=None)
    errors = dao.isValidToInclude(p)
    assert any("ao menos um e-mail" in err for err in errors)

    p.emails = None  # type: ignore
    errors_nulo = dao.isValidToInclude(p)
    assert any("ao menos um e-mail" in err for err in errors_nulo)


# --- Testes de Formato de E-mail (_____@____._____) ---


def test_email_sem_arroba(dao: PersonDAO):
    """E-mail sem o caractere '@' deve ser recusado."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[Email(1, "usuario.dominio.com")])
    errors = dao.isValidToInclude(p)
    assert any("formato do e-mail" in err for err in errors)


def test_email_sem_ponto(dao: PersonDAO):
    """E-mail sem o caractere '.' deve ser recusado."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[Email(1, "usuario@dominio")])
    errors = dao.isValidToInclude(p)
    assert any("formato do e-mail" in err for err in errors)


def test_email_com_primeira_parte_vazia(dao: PersonDAO):
    """E-mail com parte antes do '@' vazia deve ser recusado."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[Email(1, "@dominio.com")])
    errors = dao.isValidToInclude(p)
    assert any("formato do e-mail" in err for err in errors)


def test_email_com_segunda_parte_vazia(dao: PersonDAO):
    """E-mail com parte entre '@' e '.' vazia deve ser recusado."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[Email(1, "usuario@.com")])
    errors = dao.isValidToInclude(p)
    assert any("formato do e-mail" in err for err in errors)


def test_email_com_terceira_parte_vazia(dao: PersonDAO):
    """E-mail com parte após o '.' vazia deve ser recusado."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[Email(1, "usuario@dominio.")])
    errors = dao.isValidToInclude(p)
    assert any("formato do e-mail" in err for err in errors)


def test_email_com_nome_vazio(dao: PersonDAO):
    """E-mail com string vazia deve ser recusado."""
    p = Person(id=1, name="Carlos Silva", age=30, emails=[Email(1, "")])
    errors = dao.isValidToInclude(p)
    assert any("formato do e-mail" in err for err in errors)


# --- Testes de Operação e Persistência do PersonDAO.save ---


def test_persondao_salvar_pessoa_valida(dao: PersonDAO, valid_person: Person):
    """PersonDAO deve salvar com sucesso uma pessoa com dados válidos."""
    assert len(dao.saved_persons) == 0
    dao.save(valid_person)
    assert len(dao.saved_persons) == 1
    assert dao.saved_persons[0] == valid_person


def test_persondao_salvar_pessoa_invalida_lanca_excecao(dao: PersonDAO):
    """PersonDAO deve lançar ValueError ao tentar salvar uma pessoa inválida."""
    invalid_person = Person(id=2, name="Invalido", age=0, emails=[])
    with pytest.raises(ValueError) as exc_info:
        dao.save(invalid_person)

    assert "Não é possível salvar pessoa inválida" in str(exc_info.value)
    assert len(dao.saved_persons) == 0


def test_atributos_model_email_e_person():
    """Garante integridade e inicialização dos atributos de Email e Person."""
    e = Email(10, "teste@dominio.com")
    assert e.id == 10
    assert e.name == "teste@dominio.com"

    p = Person(20, "Ana Paula", 40, [e])
    assert p.id == 20
    assert p.name == "Ana Paula"
    assert p.age == 40
    assert len(p.emails) == 1
    assert p.emails[0] == e
