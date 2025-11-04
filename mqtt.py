import socket
import time



class MQTTSocketClient:
    def __init__(self, host, port, tls=False, keepalive=60, timeout=10):
        self.host = host
        self.port = port
        self.tls = tls
        self.keepalive = keepalive
        self.timeout = timeout
        self.sock: socket.socket | None = None
        self.last_rx = time.time()
        self.last_tx = time.time()
        self.packet_id = 1

    def connect(self):
        pass
    def disconnect(self):
        pass
    def ping(self):
        pass
    def publish(self):
        pass
    def subscribe(self):
        pass