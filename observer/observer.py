from abc import ABC, abstractmethod
from .observable import Observable

class Observer(ABC):

  @abstractmethod
  def update(self, observable: Observable):
    print("updated from observable")