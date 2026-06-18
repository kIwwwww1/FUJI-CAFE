class DomainError(Exception):
    """Базовое исключение для всего нашего домена"""

    pass


class BookAlreadyExistsError(DomainError):
    """Ошибка, если книга уже есть в системе"""

    pass
