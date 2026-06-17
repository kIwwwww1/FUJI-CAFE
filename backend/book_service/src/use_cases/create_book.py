from backend.book_service.src.domain.entities import Book
from backend.book_service.src.domain.interfaces.book_repository import (
    AbstractBookRepository,
)
from backend.book_service.src.infrastructure.web.schemas import BookCreateDTO


class CreateBookUseCase:
    def __init__(self, book_repo: AbstractBookRepository) -> None:
        self.book_repo = book_repo

    async def execute(self, book_dto: BookCreateDTO) -> Book:
        book = Book(**book_dto.model_dump())

        await self.book_repo.create(book)
        return book
