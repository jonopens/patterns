from __future__ import annotations
from abc import ABC, abstractmethod
from .observer import Observer  

class Observable(ABC):

  @abstractmethod
  def subscribe(self, observer: Observer):
    # internals
    print(f"subscribe {observer}")
  
  @abstractmethod
  def unsubscribe(self, observer):
    print(f"unsubscribe {observer}")

  @abstractmethod
  def publish(self):
    print("publish a message to observers of a topic/channel/subject")
