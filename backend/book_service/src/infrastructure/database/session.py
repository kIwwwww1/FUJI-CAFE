import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

logger = logging.getLogger(__name__)

DATABASE_URL = "..."

engine = create_async_engine(
    url=DATABASE_URL,
)

# pool_size=20,          # Максимальное количество постоянных соединений с БД
# max_overflow=10,       # Сколько дополнительных соединений можно временно создать сверх pool_size
# pool_timeout=30,       # Сколько секунд ждать свободное соединение из пула, прежде чем выкинуть ошибку
# pool_recycle=1800,     # Автоматически обновлять соединения каждые 30 минут (защита от разрывов со стороны Postgres)
# pool_pre_ping=True,    # Проверять «живо» ли соединение перед отправкой

async_session_factory = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Инжектирует асинхронную сессию базы данных в роуты FastAPI.
    Гарантирует автоматическое закрытие сессии после завершения запроса
    """

    async with async_session_factory() as session:
        try:
            # Если запрос прошел успешно, SQLAlchemy сама сделает commit,
            # либо мы сделаем его вручную в Репозитории.

            yield session

        except SQLAlchemyError:
            # Если внутри запроса упал любой SQL-запрос, принудительно откатываем изменения

            logger.error(
                "Запрос в базу произошел с ошибкой, ьаза вернулась в прошлое состояние"
            )

            await session.rollback()
            raise

        finally:
            # Блок 'async with' автоматически закроет сессию при выходе (session.close()),
            # возвращая соединение обратно в пул, освобождая оперативную память.

            pass


@asynccontextmanager
async def get_db_context() -> AsyncGenerator[AsyncSession, None]:
    """
    Контекстный менеджер для работы с БД в обычных Python функциях и фоновых задачах
    """

    async with async_session_factory() as session:
        try:
            yield session

        except SQLAlchemyError:
            logger.error(
                "Запрос в базу произошел с ошибкой, ьаза вернулась в прошлое состояние"
            )

            await session.rollback()
            raise
