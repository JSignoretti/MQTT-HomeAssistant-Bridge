---
title: mqtt::ControlHeaderType
summary: Control Header Type Enum. 

---

# mqtt::ControlHeaderType



Control Header Type Enum.  [More...](#detailed-description)

Inherits from IntEnum

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[CONNECT](Classes/classmqtt_1_1ControlHeaderType.md#variable-connect)**  |
| int | **[CONNACK](Classes/classmqtt_1_1ControlHeaderType.md#variable-connack)**  |
| int | **[PUBLISH](Classes/classmqtt_1_1ControlHeaderType.md#variable-publish)**  |
| int | **[PUBACK](Classes/classmqtt_1_1ControlHeaderType.md#variable-puback)**  |
| int | **[PUBREC](Classes/classmqtt_1_1ControlHeaderType.md#variable-pubrec)**  |
| int | **[PUBREL](Classes/classmqtt_1_1ControlHeaderType.md#variable-pubrel)**  |
| int | **[PUBCOMP](Classes/classmqtt_1_1ControlHeaderType.md#variable-pubcomp)**  |
| int | **[SUBSCRIBE](Classes/classmqtt_1_1ControlHeaderType.md#variable-subscribe)**  |
| int | **[SUBACK](Classes/classmqtt_1_1ControlHeaderType.md#variable-suback)**  |
| int | **[UNSUBSCRIBE](Classes/classmqtt_1_1ControlHeaderType.md#variable-unsubscribe)**  |
| int | **[UNSUBACK](Classes/classmqtt_1_1ControlHeaderType.md#variable-unsuback)**  |
| int | **[PINGREQ](Classes/classmqtt_1_1ControlHeaderType.md#variable-pingreq)**  |
| int | **[PINGRESP](Classes/classmqtt_1_1ControlHeaderType.md#variable-pingresp)**  |
| int | **[DISCONNECT](Classes/classmqtt_1_1ControlHeaderType.md#variable-disconnect)**  |

## Detailed Description

```python
class mqtt::ControlHeaderType;
```

Control Header Type Enum. 

This enum contains the different packet identification flags for the MQTT Protocol. 

## Public Attributes Documentation

### variable CONNECT

```python
static int CONNECT =  0x10;
```


### variable CONNACK

```python
static int CONNACK =  0x20;
```


### variable PUBLISH

```python
static int PUBLISH =  0x30;
```


### variable PUBACK

```python
static int PUBACK =  0x40;
```


### variable PUBREC

```python
static int PUBREC =  0x50;
```


### variable PUBREL

```python
static int PUBREL =  0x60;
```


### variable PUBCOMP

```python
static int PUBCOMP =  0x70;
```


### variable SUBSCRIBE

```python
static int SUBSCRIBE =  0x80;
```


### variable SUBACK

```python
static int SUBACK =  0x90;
```


### variable UNSUBSCRIBE

```python
static int UNSUBSCRIBE =  0xA0;
```


### variable UNSUBACK

```python
static int UNSUBACK =  0xB0;
```


### variable PINGREQ

```python
static int PINGREQ =  0xC0;
```


### variable PINGRESP

```python
static int PINGRESP =  0xD0;
```


### variable DISCONNECT

```python
static int DISCONNECT =  0xE0;
```


-------------------------------

Updated on 2025-11-12 at 19:14:36 -0500