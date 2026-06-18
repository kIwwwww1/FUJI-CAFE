from abc import ABC, abstractmethod

from backend.book_service.src.domain.entities import Book


class AbstractBookRepository(ABC):
    """
    Абстрактный класс по работе с базой книг
    """

    @abstractmethod
    async def create(self, book_data: Book) -> None:
        """Создание книги"""
        pass

    @abstractmethod
    async def get_by_id(self, id: int) -> Book | None:
        """Получение книги по id в бд"""
        pass

    @abstractmethod
    async def get_by_isbn(self, isbn: str) -> Book | None:
        """Найти книгу по ISBN. Если не найдена — вернуть None"""
        pass

    # @abstractmethod
    # async def get_by_title(self, title: str) -> None:
    #     """Получение книги по названию"""
    #     pass

    @abstractmethod
    async def delete(self, id: int) -> None:
        """Удаление книги"""
        pass

    # @abstractmethod
    # async def change_quantity(self, id: int) -> None:
    #     """Изменение количества книг"""
    #     pass
