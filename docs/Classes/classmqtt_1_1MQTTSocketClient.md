---
title: mqtt::MQTTSocketClient
summary: MQTT Client Class. 

---

# mqtt::MQTTSocketClient



MQTT Client Class.  [More...](#detailed-description)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[init](Classes/classmqtt_1_1MQTTSocketClient.md#function-init)**(self self, str clientID, str username =None, str password =None, str host ="homeassistant", int port =1883, [tls](Classes/classmqtt_1_1MQTTSocketClient.md#variable-tls) tls =False, [keepalive](Classes/classmqtt_1_1MQTTSocketClient.md#variable-keepalive) keepalive =60, [timeout](Classes/classmqtt_1_1MQTTSocketClient.md#variable-timeout) timeout =10)<br>[MQTTSocketClient](Classes/classmqtt_1_1MQTTSocketClient.md) Constructor.  |
| | **[handle_tls](Classes/classmqtt_1_1MQTTSocketClient.md#function-handle-tls)**(self self)<br>Function to handle TLS wrapping.  |
| bytes | **[receiveAmountOfBytes](Classes/classmqtt_1_1MQTTSocketClient.md#function-receiveamountofbytes)**(self self, int n)<br>Function to receive a packet byte by byte.  |
| tuple[int, bytes] | **[receive_packet](Classes/classmqtt_1_1MQTTSocketClient.md#function-receive-packet)**(self self)<br>Function to receive an entire packet.  |
| bytes | **[constructConnectPacket](Classes/classmqtt_1_1MQTTSocketClient.md#function-constructconnectpacket)**(self self, str client_id, int keepalive, str username, str password, bytes will_topic, bytes will_payload, bool will_retain =True, bool clean_start =True, [MQTTWillQoS](Classes/classmqtt_1_1MQTTWillQoS.md) will_qos =[MQTTWillQoS.QOS1](Classes/classmqtt_1_1MQTTWillQoS.md#variable-qos1))<br>Function to create a MQTT CONNECT Packet.  |
| bytes | **[constructDisconnectPacket](Classes/classmqtt_1_1MQTTSocketClient.md#function-constructdisconnectpacket)**(self self)<br>Function to create a MQTT DISCONNECT Packet.  |
| bytes | **[constructPingReqPacket](Classes/classmqtt_1_1MQTTSocketClient.md#function-constructpingreqpacket)**(self self)<br>Function to create a MQTT PINGREQ Packet.  |
| bytes | **[constructPublishPacket](Classes/classmqtt_1_1MQTTSocketClient.md#function-constructpublishpacket)**(self self, str topic, str payloadIn, [MQTTFlags](Classes/classmqtt_1_1MQTTFlags.md) qosLevel, int qosPacketIdentifier, bool duplicate =False)<br>Function to construct a PUBLISH Packet.  |
| bytes | **[constructPubRelPacket](Classes/classmqtt_1_1MQTTSocketClient.md#function-constructpubrelpacket)**(self self)<br>Function to create a MQTT PUBREL Packet.  |
| | **[connect](Classes/classmqtt_1_1MQTTSocketClient.md#function-connect)**(self self)<br>Function to create a connection to a MQTT Broker.  |
| | **[disconnect](Classes/classmqtt_1_1MQTTSocketClient.md#function-disconnect)**(self self)<br>Function to disconnect from a MQTT Broker.  |
| | **[ping](Classes/classmqtt_1_1MQTTSocketClient.md#function-ping)**(self self) |
| | **[publish](Classes/classmqtt_1_1MQTTSocketClient.md#function-publish)**(self self, str topicLevel, topicData topicData, [MQTTFlags](Classes/classmqtt_1_1MQTTFlags.md) qosLevel)<br>Function to publish data to a MQTT topic.  |
| | **[run](Classes/classmqtt_1_1MQTTSocketClient.md#function-run)**(self self)<br>Function to run code.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| | **[clientID](Classes/classmqtt_1_1MQTTSocketClient.md#variable-clientid)**  |
| | **[username](Classes/classmqtt_1_1MQTTSocketClient.md#variable-username)**  |
| | **[password](Classes/classmqtt_1_1MQTTSocketClient.md#variable-password)**  |
| | **[host](Classes/classmqtt_1_1MQTTSocketClient.md#variable-host)**  |
| | **[port](Classes/classmqtt_1_1MQTTSocketClient.md#variable-port)**  |
| | **[tls](Classes/classmqtt_1_1MQTTSocketClient.md#variable-tls)**  |
| | **[keepalive](Classes/classmqtt_1_1MQTTSocketClient.md#variable-keepalive)**  |
| | **[timeout](Classes/classmqtt_1_1MQTTSocketClient.md#variable-timeout)**  |
| socket.socket | **[sock](Classes/classmqtt_1_1MQTTSocketClient.md#variable-sock)**  |
| | **[last_receive](Classes/classmqtt_1_1MQTTSocketClient.md#variable-last-receive)**  |
| | **[last_send](Classes/classmqtt_1_1MQTTSocketClient.md#variable-last-send)**  |
| | **[connectionTime](Classes/classmqtt_1_1MQTTSocketClient.md#variable-connectiontime)**  |
| int | **[packet_id](Classes/classmqtt_1_1MQTTSocketClient.md#variable-packet-id)**  |

## Detailed Description

```python
class mqtt::MQTTSocketClient;
```

MQTT Client Class. 

This class contains the code responsible for creating a connection to an MQTT broker, along with publishing data to the broker. 

## Public Functions Documentation

### function init

```python
init(
    self self,
    str clientID,
    str username =None,
    str password =None,
    str host ="homeassistant",
    int port =1883,
    tls tls =False,
    keepalive keepalive =60,
    timeout timeout =10
)
```

[MQTTSocketClient](Classes/classmqtt_1_1MQTTSocketClient.md) Constructor. 

### function handle_tls

```python
handle_tls(
    self self
)
```

Function to handle TLS wrapping. 

Not yet implemented. 


### function receiveAmountOfBytes

```python
bytes receiveAmountOfBytes(
    self self,
    int n
)
```

Function to receive a packet byte by byte. 

Function will receive n amount of bytes and return a full byte array of length n bytes. n * 8bits 


### function receive_packet

```python
tuple[int, bytes] receive_packet(
    self self
)
```

Function to receive an entire packet. 

This function extracts the packet type, remaining length of the packet, and its payload. The function returns the packet type and payload. 


# 
## MQTT Packet Structure:


# 
## | Fixed Header | Remaining Length | Payload |


### function constructConnectPacket

```python
bytes constructConnectPacket(
    self self,
    str client_id,
    int keepalive,
    str username,
    str password,
    bytes will_topic,
    bytes will_payload,
    bool will_retain =True,
    bool clean_start =True,
    MQTTWillQoS will_qos =MQTTWillQoS.QOS1
)
```

Function to create a MQTT CONNECT Packet. 


# 
## MQTT CONNECT Packet Structure:


# 
## | Fixed Header | Variable Header | Payload |

Fixed Header: Packet Type and Flags - 1 Byte. Remaining Length 1-4 Bytes. Variable Header: Flags - 1 Byte. Keep Alive - 2 Bytes. Payload: Length Client ID - 2 Bytes. Client ID. Length Username - 2 Bytes. Username. Length Password - 2 Bytes. Password. Returns the final CONNECT Packet 


### function constructDisconnectPacket

```python
bytes constructDisconnectPacket(
    self self
)
```

Function to create a MQTT DISCONNECT Packet. 

### function constructPingReqPacket

```python
bytes constructPingReqPacket(
    self self
)
```

Function to create a MQTT PINGREQ Packet. 

### function constructPublishPacket

```python
bytes constructPublishPacket(
    self self,
    str topic,
    str payloadIn,
    MQTTFlags qosLevel,
    int qosPacketIdentifier,
    bool duplicate =False
)
```

Function to construct a PUBLISH Packet. 



```
Fixed Header                    Variable Header                 Payload
PacketType - 4 Bits             Topic Name Length - 2 Bytes     Payload Length - 2 Bytes
[]                              Topic Name                      Data
Flags - 4 Bits                  Packet Identifier(Qos > 0)
[Duplicate, Qos, Retain]
Remaining Length - 1-4 Bytes
Retain Always True
Duplicate - Input
Qos - Input
```


### function constructPubRelPacket

```python
bytes constructPubRelPacket(
    self self
)
```

Function to create a MQTT PUBREL Packet. 

### function connect

```python
connect(
    self self
)
```

Function to create a connection to a MQTT Broker. 

Creates a connection to a MQTT Broker and varifies the connection. 


### function disconnect

```python
disconnect(
    self self
)
```

Function to disconnect from a MQTT Broker. 

Contains logic to disconnect from a MQTT Broker and free the socket. Will be refined in future versions. 


### function ping

```python
ping(
    self self
)
```


### function publish

```python
publish(
    self self,
    str topicLevel,
    topicData topicData,
    MQTTFlags qosLevel
)
```

Function to publish data to a MQTT topic. 

Takes a MQTT topic, a topic data - str, int, float, bool, dict, and a QoS level. As of now only QoS level 1 is supported and functional. A PUBLISH packet is constructed using the constructor function.

QoS 1 Structure: PUBLISH Packet, Client -> Broker. PUBACK Packet, Broker -> Client. Duplicate PUBLISH packets will be sent until the PUBACK is received from the Broker. 


### function run

```python
run(
    self self
)
```

Function to run code. 

Temporary function to create a connection, verify connection, obtain sensor data, create a payload, publish data, then disconnect. This function will be removed in further versions in favor of a proper API. 


## Public Attributes Documentation

### variable clientID

```python
clientID =  clientID;
```


### variable username

```python
username =  username;
```


### variable password

```python
password =  password;
```


### variable host

```python
host =  host;
```


### variable port

```python
port =  port;
```


### variable tls

```python
tls =  tls;
```


### variable keepalive

```python
keepalive =  keepalive;
```


### variable timeout

```python
timeout =  timeout;
```


### variable sock

```python
socket.socket sock =  None;
```


### variable last_receive

```python
last_receive =  time.time();
```


### variable last_send

```python
last_send =  time.time();
```


### variable connectionTime

```python
connectionTime =  None;
```


### variable packet_id

```python
int packet_id =  1;
```


-------------------------------

Updated on 2025-11-12 at 19:14:36 -0500