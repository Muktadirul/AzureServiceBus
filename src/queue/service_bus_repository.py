from abc import ABC, abstractmethod
from asyncio import Queue


class ServiceBusRepository(ABC):
    @abstractmethod
    def get_queue_sender(self, queue_name: str) -> Queue:
        pass

    @abstractmethod
    def get_queue_receiver(self, queue_name: str) -> Queue:
        pass


class Repository(ServiceBusRepository):
    def __init__(self):
        pass

    def get_queue_sender(self , queue_name: str) -> Queue:
        pass

    def get_queue_receiver(self, queue_name: str) -> Queue:
        pass

