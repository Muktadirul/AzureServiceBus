from abc import ABC, abstractmethod
from src.queue.service_bus_repository import ServiceBusQueueRepository
from src.utils.message_encoder import MessageEncoder
from src.utils.message_decoder import MessageDecoder
from src.utils.message_spliter import split_message


class ServiceBusQueueSender(ABC):
    @abstractmethod
    def send_message(self, message: str) -> bool:
        pass


class ServiceBusQueueReceiver(ABC):
    @abstractmethod
    def receive_message(self):
        pass


class QueueSender(ServiceBusQueueSender):
    def __init__(self,
                 client: ServiceBusQueueRepository,
                 encoder: MessageEncoder,
                 ):
        self._client = client
        self._encoder = encoder

    def send_message(self, message) -> bool:
        message_chunks = split_message(message=message, chunk_size=1024)
        decoded_list =[self._encoder.encoder(message=msg) for msg in message_chunks]
        self._client.send_list_of_messages(msg_chunks=decoded_list)


class QueueReceiver(ServiceBusQueueReceiver):
    def __init__(self,
                 client: ServiceBusQueueRepository,
                 decoder: MessageDecoder,
                 ):
        self._client = client
        self._decoder = decoder

    def receive_message(self) -> str:
        encoded_messages = self._client.get_list_of_messages()
        decoded_messages = [self._decoder.decode(message=msg) for msg in encoded_messages]
        full_message = " ".join(decoded_messages)
        print(full_message)
        return full_message


if __name__ == "__main__":
    import os
    connection_string = os.getenv("CONNECTION_STRING")
    encder = MessageEncoder()
    decder = MessageDecoder()
    service_bus_queue_repository = ServiceBusQueueRepository(connection_string=connection_string, queue_name='queue1')
    sender = QueueSender(client=service_bus_queue_repository, encoder=encder)
    sender.send_message("A"*10*100*3)
    receiver = QueueReceiver(client=service_bus_queue_repository, decoder=decder)
    receiver.receive_message()