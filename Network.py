import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.43.51"
        self.port = 1234
        self.add = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.add)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print (e)

    def send(self, data):
        try:
            self.client.send(str(data).encode())

        except socket.error as e:
            print(e)

    def recv(self):
        try:
            return pickle.loads(self.client.recv(2048 * 2))
        except socket.error as e:
            print(e)