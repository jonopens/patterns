from .observable import Observable
from .observer import Observer
from datetime import datetime, date
from typing import List

class DeploymentTopic(Observable):
  # whatever state needed to be passed in the message to the observers
  _current_sha: str = ""
  _timestamp: datetime.datetime = datetime(date.today())
  _observers: List[Observer] = []

  def subscribe(self):
    print()

  def unsubscribe(self):
    print()

  def publish(self):
    for observer in self._observers:
      observer.update(self)

  def deploy(self):
    # do some deploy stuff

    self.publish()