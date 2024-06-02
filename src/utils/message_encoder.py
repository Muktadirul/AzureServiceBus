import base64


class MessageEncoder:
    def __init__(self):
        pass

    def encoder(self, message: str) -> str:
        try:
            encoded_bytes = base64.b64encode(message.encode('utf-8'))
            encoded_strings = encoded_bytes.decode('utf-8')
            return encoded_strings

        except Exception as e:
            return f"Error encoding base64 string: {str(e)}"


if __name__ == "__main__":
    encoded_string = "This is a base64 encoding string"
    encoder = MessageEncoder()
    print("Decoded string:", encoder.encoder(encoded_string))