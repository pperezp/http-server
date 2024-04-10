import socket
import time
import logging

from server.ClientHandler import ClientHandler
from ServerConfService import ServerConfService
from server.logger import setup_logger


class Server:

    start_time = None

    def __init__(self):
        setup_logger()

        Server.start_time = time.time()
        ServerConfService.load()
        self.PORT = ServerConfService.get_int("port")

        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', self.PORT))
        self.server_socket.listen(socket.SOMAXCONN)

    def run(self):
        elapsed_time = time.time() - Server.start_time

        logging.info("http://localhost:%d", self.PORT)
        logging.info("Started in %f s.", elapsed_time)
        try:
            while True:
                client_socket, client_address = self.server_socket.accept()

                client_handler = ClientHandler(client_socket, client_address)
                client_handler.handle_client()
        finally:
            self.server_socket.close()
            logging.info("Server socket closed")
