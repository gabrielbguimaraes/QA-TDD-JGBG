"""Módulo contendo as classes Email, Person e PersonDAO para o Exercício 2."""
from __future__ import annotations

import re


class Email:
    """Representa um e-mail associado a uma pessoa."""

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class Person:
    """Representa uma pessoa com id, nome, idade e uma lista de e-mails."""

    def __init__(
        self,
        id: int,
        name: str,
        age: int,
        emails: list[Email] | None = None,
    ) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.emails = emails if emails is not None else []


class PersonDAO:
    """Data Access Object para a entidade Person com regras de validação."""

    def __init__(self) -> None:
        self.saved_persons: list[Person] = []

    def isValidToInclude(self, p: Person) -> list[str]:
        """Valida o objeto Person e retorna uma lista de mensagens de erro.

        Regras:
        1. Nome: Composto por ao menos 2 partes contendo exclusivamente letras.
        2. Idade: No intervalo fechado [1, 200].
        3. Associação de Email: Pelo menos um objeto Email associado.
        4. Formato do Email: Formato "_____@____._____" com ao menos 1 caractere em cada parte.
        """
        errors: list[str] = []

        # Validação do Nome
        if not p.name or not p.name.strip():
            errors.append(
                "O nome deve ser composto por ao menos duas partes contendo apenas letras."
            )
        else:
            parts = p.name.strip().split()
            if len(parts) < 2 or not all(part.isalpha() for part in parts):
                errors.append(
                    "O nome deve ser composto por ao menos duas partes contendo apenas letras."
                )

        # Validação da Idade [1, 200]
        if p.age is None or p.age < 1 or p.age > 200:
            errors.append("A idade deve estar no intervalo fechado de 1 a 200 anos.")

        # Validação de Associação de Email
        if not p.emails or len(p.emails) == 0:
            errors.append("A pessoa deve possuir ao menos um e-mail associado.")
        else:
            email_regex = re.compile(r"^[^@\s]+@[^@.\s]+\.[^@.\s]+$")
            for email in p.emails:
                if not email.name or not email_regex.match(email.name):
                    errors.append(
                        f"O formato do e-mail '{email.name}' é inválido (deve ser parte1@parte2.parte3)."
                    )

        return errors

    def save(self, p: Person) -> None:
        """Salva a pessoa após validar os dados; levanta ValueError se inválida."""
        errors = self.isValidToInclude(p)
        if errors:
            raise ValueError(
                f"Não é possível salvar pessoa inválida: {'; '.join(errors)}"
            )
        self.saved_persons.append(p)
