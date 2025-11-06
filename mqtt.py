import socket
import time
import struct
from threading import Event
import json
import ssl
from enum import IntEnum, auto

IP = "192.168.1.119"
PORT = 1883
CLIENTID = "TEST"

STOP = Event()

class ControlHeaderType(IntEnum):
    CONNECT     = 0x10  # Client → Server
    CONNACK     = 0x20  # Server → Client
    PUBLISH     = 0x30  # Client or Server
    PUBACK      = 0x40
    PUBREC      = 0x50
    PUBREL      = 0x60
    PUBCOMP     = 0x70
    SUBSCRIBE   = 0x80
    SUBACK      = 0x90
    UNSUBSCRIBE = 0xA0
    UNSUBACK    = 0xB0
    PINGREQ     = 0xC0
    PINGRESP    = 0xD0
    DISCONNECT  = 0xE0

class MQTTFlags(IntEnum):
    RETAIN          = 0x01  # RETAIN = 1 (for PUBLISH)
    QOS1            = 0x02  # QoS level 1
    QOS2            = 0x04  # QoS level 2
    DUP             = 0x08  # DUP flag
    SUBSCRIBE_FLAG  = 0x02  # SUBSCRIBE requires QoS1 (0b0010)

# CONNECT flags bitfield (MQTT v3.1.1)
class MQTTConnectFlags(IntEnum):
    RESERVED       = 0x01            # must be 0
    CLEAN_SESSION  = 0x02            # bit 1
    WILL_FLAG      = 0x04            # bit 2
    WILL_RETAIN    = 0x20            # bit 5
    PASSWORD       = 0x40            # bit 6
    USERNAME       = 0x80            # bit 7

class HeaderType(IntEnum):
    CONNECT = 0

class MQTTWillQoS(IntEnum):
    QOS0    = (0 & 0x03) << 3   # Little hack to push the numbers in to bits 3 and 4
    QOS1    = (1 & 0x03) << 3
    QOS2    = (2 & 0x03) << 3



class MQTTProtocolLevel(IntEnum):
    V3_1_1 = 0x04


def constructControlHeader(self, packetType: ControlHeaderType, flags: MQTTFlags, variableHeaderSize: int, payloadSize: int) -> bytearray:
    fixedHeader = bytearray()

    fixedHeader += ControlHeaderType.CONNECT
    remainingLength = variableHeaderSize + payloadSize
    fixedHeader += struct.pack("!H", remainingLength)

    return fixedHeader

def constructVariableHeader(self, headerFlags: bytes = 0) -> bytearray:

    '''
    Protocol Name Length 2x bytes
    Protocol Name
    Protocol Level i.e. version
    Content Flag 1x bytes
    Keep Alive
    '''

    variableHeader = bytearray()

    # Variable Header Boiler Plate

    protocolName = "MQTT".encode("utf-8")

    variableHeader += protocolName
    variableHeader += bytes(MQTTProtocolLevel.V3_1_1)
    variableHeader += headerFlags

    return variableHeader

def constructPayload(self) -> bytearray:
    pass


class MQTTSocketClient:
    def __init__(self, clientID: str, username: str, password: str, host: str, port: int, tls=True, keepalive=60, timeout=10):
        self.clientID = clientID
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.tls = tls
        self.keepalive = keepalive
        self.timeout = timeout
        self.sock: socket.socket | None = None
        self.last_receive = time.time()
        self.last_send = time.time()
        self.connectionTime = None
        self.packet_id = 1

    def __handle_tls(self):
        tlsHandler = ssl.create_default_context()
        return tlsHandler.wrap_socket(self.sock, server_hostname=self.host)

    def __receive_packet(self) -> tuple[IntEnum, bytes]:
        msg = self.sock.recv(1024)

        fixedHeaderBytes = msg[:2]
        if fixedHeaderBytes & ControlHeaderType.CONNACK:
            return ControlHeaderType.CONNACK, bytes(0)

    def __constructConnectPacket(self,  client_id: str, keepalive: int, username: str | None, password: str | None, will_topic: bytes | None, will_payload: bytes | None, will_retain: bool = True, clean_start: bool = True, will_qos: MQTTWillQoS = MQTTWillQoS.AT_MOST_ONCE) -> bytes:

        # Construct CONNECT Packet Variable Header flags
        variableFlags = 0
        if clean_start:
            variableFlags |= MQTTConnectFlags.CLEAN_SESSION

        if username is not None:
            variableFlags |= MQTTConnectFlags.USERNAME

        if password is not None:
            variableFlags |= MQTTConnectFlags.PASSWORD

        willExists = (will_topic is not None) and (will_payload is not None)

        if willExists:
            variableFlags |= MQTTConnectFlags.WILL_FLAG
            variableFlags |= will_qos

            if will_retain:
                variableFlags |= MQTTConnectFlags.WILL_RETAIN


        variableHeader = constructVariableHeader(variableFlags)

        # Add the keep alive timer
        variableHeader += struct.pack("!H", keepalive)


        # Construct Payload
        payload = bytearray()
        payload += client_id.encode("utf-8")

        if willExists:
            payload += will_topic.encode("utf-8")
            payload += will_payload

        if username is not None:
            payload += username.encode("utf-8")

        if password is not None:
            payload += password.encode("utf-8")


        # Construct Fixed Header
        fixedHeader = constructControlHeader(ControlHeaderType.CONNECT, len(variableHeader), len(payload))

        return fixedHeader + variableHeader + payload

    def __constructDisconnectPacket(self) -> bytes:
        return bytes([ControlHeaderType.DISCONNECT, 0])

    def __constructPingReqPacket(self) -> bytes:
        return bytes([ControlHeaderType.PINGREQ, 0])

    def __connect(self):

        self.sock = socket.create_connection((self.host, self.port), self.timeout)

        if self.tls:
            self.sock = self.__handle_tls()

        self.sock.settimeout(self.timeout)

        connectPacket = self.__constructConnectPacket(self.clientID, self.keepalive, self.username, self.password, b"home/bme680/status", b"offline")

        self.sock.sendall(connectPacket)
        self.last_send = time.time()
        self.connectionTime = self.last_send

        # Confirm The Connection

        packetType = self.__receive_packet()[0] # The first index is the packet type, for a connack there is no payload, only thing we care about is that it is a connack

        if packetType != ControlHeaderType.CONNACK:
            print("Connected But No CONNACK Packet Received")
            raise socket.error


    def __disconnect(self):
        self.sock.sendall(self.__constructDisconnectPacket())
        self.sock.close()
        self.sock = None

    def ping(self):
        pass
    def publish(self):
        pass
    def subscribe(self):
        pass

    def run(self):
        try:
            self.__connect()
        except socket.error:
            print(f"Failed to connect to MQTT server at {self.host}:{self.port}")
            self.sock.close()

        print("connection succeeded")

        self.__disconnect()




if __name__ == '__mqtt__':
    MQTTSocketClient("testingSetup", "user", "password")