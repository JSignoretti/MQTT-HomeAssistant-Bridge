---
title: temp

---

# temp



## Functions

|                | Name           |
| -------------- | -------------- |
| | **[c_to_f](Namespaces/namespacetemp.md#function-c-to-f)**(int c)<br>Helper Function Converts from Celsius to Fahrenheit.  |
| | **[find_iio_device](Namespaces/namespacetemp.md#function-find-iio-device)**()<br>Function to find a specific IIO Device Function currently only tests for a specific device and returns it Function will be replaced with proper parsing code in later versions.  |
| | **[read_channel](Namespaces/namespacetemp.md#function-read-channel)**(device_path device_path, channel_name channel_name)<br>Function to read various channels from an IIO Device Function will be replaced with proper parsing code in later versions.  |
| | **[parse_Data](Namespaces/namespacetemp.md#function-parse-data)**()<br>Function to parse data from the BME680 sensor Function will be replaced with proper parsing code in later versions.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| str | **[IIO_BASE](Namespaces/namespacetemp.md#variable-iio-base)** <br>Constant Specifies the IIO Base folder in Linux.  |


## Functions Documentation

### function c_to_f

```python
c_to_f(
    int c
)
```

Helper Function Converts from Celsius to Fahrenheit. 

### function find_iio_device

```python
find_iio_device()
```

Function to find a specific IIO Device Function currently only tests for a specific device and returns it Function will be replaced with proper parsing code in later versions. 

### function read_channel

```python
read_channel(
    device_path device_path,
    channel_name channel_name
)
```

Function to read various channels from an IIO Device Function will be replaced with proper parsing code in later versions. 

### function parse_Data

```python
parse_Data()
```

Function to parse data from the BME680 sensor Function will be replaced with proper parsing code in later versions. 


## Attributes Documentation

### variable IIO_BASE

```python
str IIO_BASE =  "/sys/bus/iio/devices/";
```

Constant Specifies the IIO Base folder in Linux. 




-------------------------------

Updated on 2025-11-12 at 19:14:36 -0500