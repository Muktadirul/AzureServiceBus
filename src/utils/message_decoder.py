import base64


class MessageDecoder:
    def decode(self, message:str):
        try:
            decoded_bytes = base64.b64decode(message)
            decoded_string = decoded_bytes.decode('utf-8')
            return decoded_string
        except Exception as e:
            return f"Error decoding base64 string: {str(e)}"


if __name__ == "__main__":
    encoded_string = "VGhpcyBpcyBhIGJhc2U2NCBlbmNvZGluZyBzdHJpbmc="
    decoded = MessageDecoder()
    print("Decoded string:", decoded.decode(encoded_string))