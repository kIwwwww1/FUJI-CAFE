from abc import ABC, abstractmethod

class AbstractUserRepository(ABC):

    @abstractmethod
    async def create(self, ...) -> None:
        '''Создание пользователя'''
        pass

    @abstractmethod
    async def get(self, ...) -> None:
        '''Получение пользователя'''
        pass
    
    @abstractmethod
    async def delete(self, ...) -> None:
        '''Удаление пользователя'''
        pass
    
