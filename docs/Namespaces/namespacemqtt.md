---
title: mqtt

---

# mqtt

 [More...](#detailed-description)

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[mqtt::ControlHeaderType](Classes/classmqtt_1_1ControlHeaderType.md)** <br>Control Header Type Enum.  |
| class | **[mqtt::HeaderType](Classes/classmqtt_1_1HeaderType.md)**  |
| class | **[mqtt::MQTTConnectFlags](Classes/classmqtt_1_1MQTTConnectFlags.md)** <br>MQTT Connect Packet Flags Enum.  |
| class | **[mqtt::MQTTFlags](Classes/classmqtt_1_1MQTTFlags.md)** <br>MQTT Packet Flags Enum.  |
| class | **[mqtt::MQTTProtocolLevel](Classes/classmqtt_1_1MQTTProtocolLevel.md)** <br>MQTT Protocol Level Enum.  |
| class | **[mqtt::MQTTSocketClient](Classes/classmqtt_1_1MQTTSocketClient.md)** <br>MQTT Client Class.  |
| class | **[mqtt::MQTTWillQoS](Classes/classmqtt_1_1MQTTWillQoS.md)** <br>MQTT QOS Flags Enum.  |

## Functions

|                | Name           |
| -------------- | -------------- |
| bytearray | **[constructControlHeader](Namespaces/namespacemqtt.md#function-constructcontrolheader)**([ControlHeaderType](Classes/classmqtt_1_1ControlHeaderType.md) packetType, int variableHeaderSize, int payloadSize, int flags =0x00)<br>Function used to create a CONTROLL packet header.  |
| bytearray | **[constructVariableHeader](Namespaces/namespacemqtt.md#function-constructvariableheader)**(bytes headerFlags)<br>Function used to create the CONNECT packet variable header.  |
| bytearray | **[constructPayload](Namespaces/namespacemqtt.md#function-constructpayload)**(self self, str payload) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| dict | **[IIO_ATTRIBUTES](Namespaces/namespacemqtt.md#variable-iio-attributes)**  |
| str | **[HOST](Namespaces/namespacemqtt.md#variable-host)** <br>Constants.  |
| int | **[PORT](Namespaces/namespacemqtt.md#variable-port)**  |
| str | **[CLIENTID](Namespaces/namespacemqtt.md#variable-clientid)**  |
| int | **[MAX_QOS_PACKET_ATTEMPTS](Namespaces/namespacemqtt.md#variable-max-qos-packet-attempts)**  |
| | **[STOP](Namespaces/namespacemqtt.md#variable-stop)**  |
| | **[client](Namespaces/namespacemqtt.md#variable-client)**  |

## Detailed Description




```
@mainpage Python MQTT–Home Assistant Bridge

This project is a Python-based MQTT bridge for Home Assistant.

It:
- Connects to an MQTT broker
- Publishes sensor data or state changes
- Follows Home Assistant’s MQTT discovery conventions
- Provides a simple, scriptable way to expose devices to Home Assistant
```


## Functions Documentation

### function constructControlHeader

```python
bytearray constructControlHeader(
    ControlHeaderType packetType,
    int variableHeaderSize,
    int payloadSize,
    int flags =0x00
)
```

Function used to create a CONTROLL packet header. 

### function constructVariableHeader

```python
bytearray constructVariableHeader(
    bytes headerFlags
)
```

Function used to create the CONNECT packet variable header. 

Will be removed in further versions.



```
Protocol Name Length 2x bytes
Protocol Name
Protocol Level i.e. version
Content Flag 1x bytes
Keep Alive
```


### function constructPayload

```python
bytearray constructPayload(
    self self,
    str payload
)
```



## Attributes Documentation

### variable IIO_ATTRIBUTES

```python
dict IIO_ATTRIBUTES =  {'current_timestamp_clock': ('mA', 1), 'in_intensity_sampling_frequency': (float, 1), 'in_voltageY_raw': ('mV', 1), 'in_voltageY_supply_raw': ('mV', 1), 'in_voltageY-voltageZ_raw': ('mV', 1), 'in_altvoltageY_rms_raw': ('mV', 1), 'in_powerY_raw': ('W', 0.001), 'in_powerY_active_raw': ('W', 0.001), 'in_powerY_reactive_raw': ('W', 0.001), 'in_powerY_apparent_raw': ('W', 0.001), 'in_powerY_powerfactor': ('W', 0.001), 'in_temp_raw': ('°C', 0.001), 'in_tempY_raw': ('°C', 0.001), 'in_temp_x_raw': ('°C', 0.001), 'in_temp_y_raw': ('°C', 0.001), 'in_temp_ambient_raw': ('°C', 0.001), 'in_temp_object_raw': ('°C', 0.001), 'in_tempY_input': ('°C', 0.001), 'in_temp_input': ('°C', 0.001), 'in_accel_x_raw': ('m/s', 1), 'in_accel_y_raw': ('m/s', 1), 'in_accel_z_raw': ('m/s', 1), 'in_accel_linear_x_raw': ('m/s', 1), 'in_accel_linear_y_raw': ('m/s', 1), 'in_accel_linear_z_raw': ('m/s', 1), 'in_gravity_x_raw': ('m/s', 1), 'in_gravity_y_raw': ('m/s', 1), 'in_gravity_z_raw': ('m/s', 1), 'in_deltaangl_x_raw': (float, 57.29577951308232), 'in_deltaangl_y_raw': (float, 57.29577951308232), 'in_deltaangl_z_raw': (float, 57.29577951308232), 'in_deltavelocity_x_raw': ('m/s', 1), 'in_deltavelocity_y_raw': ('m/s', 1), 'in_deltavelocity_z_raw': ('m/s', 1), 'in_angl_raw': (float, 57.29577951308232), 'in_anglY_raw': (float, 57.29577951308232), 'in_anglvel_x_raw': ('m/s', 57.29577951308232), 'in_anglvel_y_raw': ('m/s', 57.29577951308232), 'in_anglvel_z_raw': ('m/s', 57.29577951308232), 'in_incli_x_raw': (float, 1), 'in_incli_y_raw': (float, 1), 'in_incli_z_raw': (float, 1), 'in_magn_x_raw': (float, 1), 'in_magn_y_raw': (float, 1), 'in_magn_z_raw': (float, 1), 'in_accel_x_peak_raw': ('m/s', 1), 'in_accel_y_peak_raw': ('m/s', 1), 'in_accel_z_peak_raw': ('m/s', 1), 'in_humidityrelative_peak_raw': ('%', 1), 'in_temp_peak_raw': ('°C', 0.001), 'in_humidityrelative_trough_raw': ('%', 1), 'in_temp_trough_raw': ('°C', 0.001), 'in_accel_xyz_squared_peak_raw': ('m/s', 1), 'in_humidityrelative_raw': ('%', 1), 'in_humidityrelative_input': ('%', 1), 'in_Y_mean_raw': ('float', 1), 'in_activity_still_input': ('%', 1), 'in_activity_walking_input': ('%', 1), 'in_activity_jogging_input': ('%', 1), 'in_activity_running_input': ('%', 1), 'in_distance_input': ('m', 1), 'in_distance_raw': ('m', 1), 'in_proximity_raw': ('m', 1), 'in_proximity_input': ('m', 1), 'in_proximityY_raw': ('m', 1), 'in_illuminance_input': ('lx', 1), 'in_illuminance_raw': ('lx', 1), 'in_illuminanceY_input': ('lx', 1), 'in_illuminanceY_raw': ('lx', 1), 'in_illuminanceY_mean_raw': ('lx', 1), 'in_illuminance_ir_raw': ('lx', 1), 'in_illuminance_clear_raw': ('lx', 1), 'in_intensityY_raw': (float, 1), 'in_intensityY_ir_raw': (float, 1), 'in_intensityY_both_raw': (float, 1), 'in_intensityY_uv_raw': (float, 1), 'in_intensityY_uva_raw': (float, 1), 'in_intensityY_uvb_raw': (float, 1), 'in_intensityY_duv_raw': (float, 1), 'in_intensity_red_raw': (float, 1), 'in_intensity_green_raw': (float, 1), 'in_intensity_blue_raw': (float, 1), 'in_intensity_clear_raw': (float, 1), 'in_uvindex_input': ('UV index', 1), 'in_rot_quaternion_raw': (float, 1), 'in_rot_from_north_magnetic_tilt_comp_raw': (float, 1), 'in_rot_from_north_true_tilt_comp_raw': (float, 1), 'in_rot_from_north_magnetic_raw': (float, 1), 'in_rot_from_north_true_raw': (float, 1), 'in_currentY_raw': ('mA', 1), 'in_currentY_supply_raw': ('mA', 1), 'in_altcurrentY_rms_raw': ('mA', 1), 'in_steps_en': (int, 1), 'in_velocity_sqrt(x^2+y^2+z^2)_input': ('m/s', 1), 'in_velocity_sqrt(x^2+y^2+z^2)_raw': ('m/s', 1), 'in_magn_x_oversampling_ratio': (float, 1), 'in_magn_y_oversampling_ratio': (float, 1), 'in_magn_z_oversampling_ratio': (float, 1), 'in_concentration_raw': ('%', 1), 'in_concentrationY_raw': ('%', 1), 'in_concentration_co2_raw': ('%', 1), 'in_concentrationY_co2_raw': ('%', 1), 'in_concentration_ethanol_raw': ('%', 1), 'in_concentrationY_ethanol_raw': ('%', 1), 'in_concentration_h2_raw': ('%', 1), 'in_concentrationY_h2_raw': ('%', 1), 'in_concentration_o2_raw': ('%', 1), 'in_concentrationY_o2_raw': ('%', 1), 'in_concentration_voc_raw': ('%', 1), 'in_concentrationY_voc_raw': ('%', 1), 'in_resistance_raw': ('ohms', 1), 'in_resistanceY_raw': ('ohms', 1), 'heater_enable': (bool, 1), 'in_ph_raw': (float, 1), 'in_massconcentration_pm1_input': ('µg/m³', 1), 'in_massconcentrationY_pm1_input': ('µg/m³', 1), 'in_massconcentration_pm2p5_input': ('µg/m³', 1), 'in_massconcentrationY_pm2p5_input': ('µg/m³', 1), 'in_massconcentration_pm4_input': ('µg/m³', 1), 'in_massconcentrationY_pm4_input': ('µg/m³', 1), 'in_massconcentration_pm10_input': ('µg/m³', 1), 'in_massconcentrationY_pm10_input': ('µg/m³', 1), 'in_temp_thermocouple_type': (str, 1), 'in_intensity_x_raw': ('W/m²', 1e-09), 'in_intensity_y_raw': ('W/m²', 1e-09), 'in_intensity_z_raw': ('W/m²', 1e-09), 'in_anglY_label': (float, 57.29577951308232), 'in_illuminance_hysteresis_relative': ('%', 1), 'in_intensity_hysteresis_relative': ('%', 1), 'in_powerY_sampling_frequency': ('W', 0.001), 'in_currentY_sampling_frequency': ('mA', 1), 'in_rot_yaw_raw': (float, 1), 'in_rot_pitch_raw': (float, 1), 'in_rot_roll_raw': (float, 1), 'in_colortemp_raw': ('K', 1)};
```


### variable HOST

```python
str HOST =  "homeassistant";
```

Constants. 

### variable PORT

```python
int PORT =  1883;
```


### variable CLIENTID

```python
str CLIENTID =  "client-1";
```


### variable MAX_QOS_PACKET_ATTEMPTS

```python
int MAX_QOS_PACKET_ATTEMPTS =  10;
```


### variable STOP

```python
STOP =  Event();
```


### variable client

```python
client =  MQTTSocketClient(CLIENTID, username="oniic", password="Saltersimp5904", host=HOST, port=PORT);
```





-------------------------------

Updated on 2025-11-12 at 19:14:36 -0500