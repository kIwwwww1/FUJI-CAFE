import logging

from backend.book_service.src.domain import BookAlreadyExistsError
from backend.book_service.src.domain.entities import Book
from backend.book_service.src.domain.interfaces.repositories.book_repository import (
    AbstractBookRepository,
)
from backend.book_service.src.infrastructure.web.schemas import BookCreateDTO

logger = logging.getLogger("book_service")


class CreateBookUseCase:
    def __init__(self, book_repo: AbstractBookRepository) -> None:
        self.book_repo = book_repo

    async def execute(self, book_dto: BookCreateDTO) -> Book:

        logger.info("Попытка создать книгу с ISBN: %s", book_dto.isbn)

        existing_book = await self.book_repo.get_by_isbn(book_dto.isbn)

        if existing_book is not None:
            logger.warning(
                "Ошибка создания: книга с ISBN %s уже существует", book_dto.isbn
            )
            raise BookAlreadyExistsError(f"Книга с ISBN {book_dto.isbn} уже существует")

        book = Book(**book_dto.model_dump())
        await self.book_repo.create(book)
        logger.info("Книга '%s' успешно сохранена в базу данных", book.title_ru)
        return book
