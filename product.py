from publisher import Publisher
from subscriber import Subscriber


class Product(Publisher):
    def __init__(self, name, category, price):
        self.name: str = name
        self.category: str = category
        self.price: float = price

    _clients: List[Subscriber] = []

    def subscribe(self, s: Subscriber):
        self._clients.append(s)

    def unsubsribe(self, s: Subscriber):
        self._clients.remove(s)

    def send_message(self):
        for clients_list in self._clients:
            clients_list.update(self)

    def someLogicalProcess(self):
        pass
