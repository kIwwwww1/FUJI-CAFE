

from backend.book_service.src.domain.interfaces.book_repository import AbstractBookRepository


class CreateBookUseCase:
    def __init__(self, book_repo: AbstractBookRepository) -> None:
        self.book_repo = book_repo

    def execute(self, book_data: ):
        self.book_repo.create()
