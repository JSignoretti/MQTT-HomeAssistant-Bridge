---
title: helper

---

# helper

 [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| str | **[getFileContent](Namespaces/namespacehelper.md#function-getfilecontent)**(filename filename)<br>Function to return the first line in a file.  |
| bytes | **[bitwiseOrForBytes](Namespaces/namespacehelper.md#function-bitwiseorforbytes)**(bytes byte1, bytes byte2) |
| bytes | **[bitwiseAndForBytes](Namespaces/namespacehelper.md#function-bitwiseandforbytes)**(bytes byte1, bytes byte2) |
| bytes | **[enc_utf8](Namespaces/namespacehelper.md#function-enc-utf8)**(str s)<br>Function to encode a string in network byte order.  |
| bytes | **[encodeVarint](Namespaces/namespacehelper.md#function-encodevarint)**(int n)<br>Function to encode an integer in network byte order.  |
| int | **[decodeVarint](Namespaces/namespacehelper.md#function-decodevarint)**(receive_function receive_function)<br>Function to decode an integer from a byte stream.  |

## Detailed Description




```
10/8/2025
Kristijan Stojanovski

Various helper functions
```


## Functions Documentation

### function getFileContent

```python
str getFileContent(
    filename filename
)
```

Function to return the first line in a file. 



```
Displays the content of a given file to the console.
```


### function bitwiseOrForBytes

```python
bytes bitwiseOrForBytes(
    bytes byte1,
    bytes byte2
)
```


### function bitwiseAndForBytes

```python
bytes bitwiseAndForBytes(
    bytes byte1,
    bytes byte2
)
```


### function enc_utf8

```python
bytes enc_utf8(
    str s
)
```

Function to encode a string in network byte order. 

### function encodeVarint

```python
bytes encodeVarint(
    int n
)
```

Function to encode an integer in network byte order. 

### function decodeVarint

```python
int decodeVarint(
    receive_function receive_function
)
```

Function to decode an integer from a byte stream. 





-------------------------------

Updated on 2025-11-12 at 19:14:36 -0500