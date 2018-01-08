from abc import ABCMeta
from abc import abstractmethod
class AbstractDuck(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass

class Duck(AbstractDuck):
    def quack(self):
        print("[Duck] Quack")

duck= Duck()
duck.quack()