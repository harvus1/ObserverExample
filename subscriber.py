import abc

class Subscriber(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, publisher: Publisher):
        raise NotImplementedError