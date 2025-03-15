from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def player(self,type):
        self.type = type