---
title: mqtt::MQTTConnectFlags
summary: MQTT Connect Packet Flags Enum. 

---

# mqtt::MQTTConnectFlags



MQTT Connect Packet Flags Enum.  [More...](#detailed-description)

Inherits from IntEnum

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[RESERVED](Classes/classmqtt_1_1MQTTConnectFlags.md#variable-reserved)**  |
| int | **[CLEAN_SESSION](Classes/classmqtt_1_1MQTTConnectFlags.md#variable-clean-session)**  |
| int | **[WILL_FLAG](Classes/classmqtt_1_1MQTTConnectFlags.md#variable-will-flag)**  |
| int | **[WILL_RETAIN](Classes/classmqtt_1_1MQTTConnectFlags.md#variable-will-retain)**  |
| int | **[PASSWORD](Classes/classmqtt_1_1MQTTConnectFlags.md#variable-password)**  |
| int | **[USERNAME](Classes/classmqtt_1_1MQTTConnectFlags.md#variable-username)**  |

## Detailed Description

```python
class mqtt::MQTTConnectFlags;
```

MQTT Connect Packet Flags Enum. 

CONNECT flags bitfield (MQTT v3.1.1) This enum contains the varius flags a MQTT CONNECT packet can contain. 

## Public Attributes Documentation

### variable RESERVED

```python
static int RESERVED =  0x01;
```


### variable CLEAN_SESSION

```python
static int CLEAN_SESSION =  0x02;
```


### variable WILL_FLAG

```python
static int WILL_FLAG =  0x04;
```


### variable WILL_RETAIN

```python
static int WILL_RETAIN =  0x20;
```


### variable PASSWORD

```python
static int PASSWORD =  0x40;
```


### variable USERNAME

```python
static int USERNAME =  0x80;
```


-------------------------------

Updated on 2025-11-12 at 19:14:36 -0500