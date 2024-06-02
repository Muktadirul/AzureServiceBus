import logging
from abc import ABC, abstractmethod
from azure.servicebus.management import ServiceBusAdministrationClient
from azure.servicebus import ServiceBusClient, ServiceBusMessage


class ServiceBusRepository(ABC):
    @abstractmethod
    def send_list_of_messages(self, msg_chunks:list[str]):
        pass

    @abstractmethod
    def get_list_of_messages(self):
        pass


class ServiceBusQueueRepository(ServiceBusRepository):
    def __init__(self, connection_string: str, queue_name: str):
        self._queue_name = queue_name
        self._connection = ServiceBusClient.from_connection_string(conn_str=connection_string)

    def send_list_of_messages(self, msg_chunks:list[str]):
        with self._connection as client:
            with client.get_queue_sender(queue_name=self._queue_name) as sender:
                for chunk in msg_chunks:
                    message = ServiceBusMessage(chunk)
                    sender.send_messages(message)
                logging.info('All messages send successful')

    def get_list_of_messages(self):
        received_chunks = []
        with self._connection as client:
            with client.get_queue_receiver(queue_name=self._queue_name, max_wait_time=5) as receiver:
                for msg in receiver:
                    logging.info("Received %s ",msg)
                    receiver.complete_message(msg)
        return received_chunks
