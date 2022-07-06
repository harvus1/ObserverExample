from publisher import Publisher
from subscriber import Subscriber


class Sales(Publisher):

    _clients: List[Subscriber] = []
    _workers: List[Subscriber] = []

    def subscribe(self, s: Subscriber) -> None:
         self._clients.append(s)
         self._workers.append(s)


    def unsubsribe(self, s: Subscriber):
         self._clients.remove(s)
         self._workers.remove(s)

    def send_message(self):
         for clients_list in self._clients:
             clients_list.update(self)

         for workers_list in self._workers:
             workers_list.update(self)

    def sale_released(self):
         pass