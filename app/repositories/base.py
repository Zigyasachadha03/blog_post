from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def delete(self, id):
        pass
    
    @abstractmethod
    def update(self, id, entity):
        pass