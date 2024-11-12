from .observable import Observable
from .observer import Observer
from datetime import date


class Consumer(Observer):
  _last_update: date = date(2021, 11, 11)

  def update(self, topic: Observable):
    if topic._timestamp > self._last_update:
      self._last_update = topic._timestamp