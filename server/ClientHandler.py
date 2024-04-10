import logging

from server.logger import setup_logger


class ClientHandler:
    def __init__(self, client_socket, client_address):
        setup_logger()
        self.client_socket = client_socket
        self.client_address = client_address

    def handle_client(self):
        try:
            logging.info("Connection established from %s", self.client_address)

            data = self.client_socket.recv(1024)
            logging.info("Received data: %s", data.decode())

            http_response = "HTTP/1.1 200 OK"

            self.client_socket.sendall(http_response.encode())
        finally:
            self.client_socket.close()
