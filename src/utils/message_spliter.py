from azure.servicebus import ServiceBusMessage
def split_message(message, chunk_size):
    chunks = [message[i:i+chunk_size] for i in range(0, len(message), chunk_size)]
    return chunks