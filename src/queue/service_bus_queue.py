from abc import ABC, abstractmethod


class ServiceBusQueueSender(ABC):
    @abstractmethod
    def send_message(self):
        pass


class ServiceBusQueueReceiver(ABC):
    @abstractmethod
    def receive_message(self):
        pass


class ServiceBusQueueSenderFactory(ABC):
    @abstractmethod
    def create_sender(self):
        pass

    @abstractmethod
    def create_receiver(self):
        pass