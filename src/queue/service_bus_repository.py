from abc import ABC, abstractmethod
from asyncio import Queue
from azure.servicebus.aio import ServiceBusClient
from azure.servicebus.aio._servicebus_sender_async import ServiceBusSender
from azure.servicebus.aio._servicebus_receiver_async import ServiceBusReceiver
class ServiceBusRepository(ABC):
    @abstractmethod
    def get_queue_sender(self, queue_name: str) -> Queue:
        pass

    @abstractmethod
    def get_queue_receiver(self, queue_name: str) -> Queue:
        pass


class ServiceBusQueueRepository(ServiceBusRepository):
    def __init__(self, connection_string: str, queue_name: str):
        self._queue_name = queue_name
        self._connection = ServiceBusClient.from_connection_string(conn_str=connection_string)

    def get_queue_sender(self, queue_name: str) -> ServiceBusSender:
        return self._connection.get_queue_sender(queue_name=self._queue_name)

    def get_queue_receiver(self, queue_name: str) -> ServiceBusReceiver:
        return self._connection.get_queue_receiver(queue_name=self._queue_name)

