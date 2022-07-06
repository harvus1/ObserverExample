import abc
from subscriber import Subscriber

class Publisher(metaclass=abc.ABCMeta):
    @abstractmethod
    def subscribe(self, s:Subscriber):
        raise NotImplementedError

    @abstractmethod
    def unsubsribe(self, s:Subscriber):
        raise NotImplementedError

    @abstractmethod
    def send_message(self):
        raise NotImplementedError