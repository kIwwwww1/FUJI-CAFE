from sqlalchemy.ext.asyncio import AsyncSession

from backend.book_service.src.domain.entities import AbstractBookRepository, Book


class PostgresBookRepository(AbstractBookRepository):
    """
    Реальная рабочая база данных на PostgreSQL для книг
    """

    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def create(self, book: Book) -> None:

        # Переводим чистый датакласс в ORM-модель
        orm_book = "..."
        self.session.add(orm_book)
        await self.session.commit()

    # async def get_by_id(self, id: int) -> Book | None:
    #     stmt = select(...)
    #     self.session.execute()
