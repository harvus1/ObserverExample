from publisher import Publisher
from subscriber import Subscriber


class Inventory(Publisher):
    def __init__(self):
        self.name

    _workers: List[Subscriber] = []

    def subscribe(self, s: Subscriber):
        self._workers.append(s)

    def unsubsribe(self, s: Subscriber):
        self._workers.remove(s)

    def send_message(self):
        for workers_list in self._workers:
            workers_list.update(self)

    def someLogicalProcess(self):
        pass