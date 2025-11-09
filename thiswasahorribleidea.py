import math
from pprint import pprint

rawFile = open("hatemylife.txt", "r")

lines = rawFile.readlines()

rawFile.close()

#outputFile = open("dictionary.py", "w")
#tempFile = open("temp.txt", "w")

TOP_LEVEL_PATH = "/sys/bus/iio/devices/iio:device"

def createPath(self, tlp: str, deviceID: int, attribute: str, type: str == None):
    return f"{tlp}{deviceID}/{type if type else ''}{attribute}"
#         Unit ID: (Unit, ScaleFactor)
#         Unit -> Home Assistant Unit -> https://github.com/home-assistant/core/blob/e326dd2847a18913ec10050e5a0ac01dbd4209fc/homeassistant/const.py
#         ScaleFactor -> How much the iio device output needs to be scaled to match the Unit -> https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-iio

units = {"temperatureHeat": ("°C", 0.001),
         "temperatureLight": ("K", 1),
         "emissivity": ("%", 1),
         "thermocoupleType": (str, 1),
         "humidity": ("%", 1),
         "pressure": ("kPa", 1),
         "concentration": ("%", 1),
         "massConcentration": ("µg/m³", 1),
         "voltage": ("mV", 1),
         "power": ("W", 0.001),
         "intensity": (float, 1),
         "intensityHysteresis": ("%", 1),
         "intensityWatts": ("W/m²",0.000000001),
         "illuminance": ("lx", 1),
         "illuminanceHysteresis": ("%", 1),
         "uvIndex": ("UV index", 1),
         "gravityDir": ("m/s", 1),                  # m/s because Home Assistant doesnt have a m/s^2
         "acceleration": ("m/s", 1),                # m/s because Home Assistant doesnt have a m/s^2
         "capacitance": ("", 1),
         "velocity": ("m/s", 1),
         "angularVelocity": ("m/s", 180/math.pi),   # m/s because Home Assistant doesnt have radians/s, converted to degrees/s
         "angle": (float, 180/math.pi),             # Float shows angle since Home Assistant doesnt have radians
         "activity": ("%", 1),
         "position": ("", 1),
         "ph": (float, 1),
         "resistance": ("ohms", 1),
         "boolean": (bool, 1),
         "steps": (int, 1),
         "incline": (float, 1),
         "magnetic": (float, 1),                    # Float since Home Assistant doesnt have Gauss
         "rotation": (float, 1),                    # Measurement in Float
         "proximity": ("m", 1),
         "distance": ("m", 1),
         "current": ("mA", 1),
         "mean": ("float", 1)
         }

iioData = {}


count = 0
rawAttributeData = []
attributeData = []
for line in lines:
    if(line[:5] == "What:"):
        rawAttributeData.append(line.lstrip("What:		").rstrip('\n').split('/')[-2:])

for attributeData in rawAttributeData:
    if attributeData[0] == "iio:deviceX":
        # tempFile.write(attributeData[1] + '\n')
        if "out" not in attributeData[1] and "scale" not in attributeData[1] and "calib" not in attributeData[1] and "available" not in attributeData[1] and "offset" not in attributeData[1] and "gain" not in attributeData[1]:
            if "temp" in attributeData[1]:
                if "emissivity" in attributeData[1]:
                    iioData[attributeData[1]] = units["emissivity"]

                elif "color" in attributeData[1]:
                    iioData[attributeData[1]] = units["temperatureLight"]

                elif "type" in attributeData[1]:
                    iioData[attributeData[1]] = units["thermocoupleType"]

                else:
                    iioData[attributeData[1]] = units["temperatureHeat"]

            elif "humidity" in attributeData[1]:
                iioData[attributeData[1]] = units["humidity"]

            elif "concentration" in attributeData[1]:
                if "mass" in attributeData[1]:
                    iioData[attributeData[1]] = units["massConcentration"]
                else:
                    iioData[attributeData[1]] = units["concentration"]

            elif "voltage" in attributeData[1]:
                if "label" not in attributeData[1] and "convdelay" not in attributeData[1] and "filter" not in attributeData[1] and "samp" not in attributeData[1] and "phase" not in attributeData[1]:
                    iioData[attributeData[1]] = units["voltage"]

            elif "power" in attributeData[1]:
                if "shunt" not in attributeData[1] and "accel" not in attributeData[1]:
                    iioData[attributeData[1]] = units["power"]

            elif "intensity" in attributeData[1]:
                if "integration" not in attributeData[1]:
                    if "hysteresis" in attributeData[1]:
                        iioData[attributeData[1]] = units["intensityHysteresis"]

                    elif "_x" in attributeData[1] or "_y" in attributeData[1] or "_z" in attributeData[1]:
                        iioData[attributeData[1]] = units["intensityWatts"]

                    else:
                        iioData[attributeData[1]] = units["intensity"]

            elif "illuminance" in attributeData[1]:
                if "integration" not in attributeData[1]:
                    if "hysteresis" in attributeData[1]:
                        iioData[attributeData[1]] = units["illuminanceHysteresis"]

                    else:
                        iioData[attributeData[1]] = units["illuminance"]

            elif "uvindex" in attributeData[1]:
                iioData[attributeData[1]] = units["uvIndex"]

            elif "gravity" in attributeData[1]:
                iioData[attributeData[1]] = units["gravityDir"]

            elif "accel" in attributeData[1]:
                if "mode" not in attributeData[1] and "mount" not in attributeData[1]:
                    iioData[attributeData[1]] = units["acceleration"]

            elif "vel" in attributeData[1]:
                if "mount" not in attributeData[1] and "quad" not in attributeData[1] and "integration" not in attributeData[1] and "_en" not in attributeData[1]:
                    if "angl" in attributeData[1]:
                        iioData[attributeData[1]] = units["angularVelocity"]

                    else:
                        iioData[attributeData[1]] = units["velocity"]

            elif "angl" in attributeData[1]:
                iioData[attributeData[1]] = units["angle"]

            elif "activity" in attributeData[1]:
                iioData[attributeData[1]] = units["activity"]

            elif "in_ph_raw" in attributeData[1]:
                iioData[attributeData[1]] = units["ph"]

            elif "resistance" in attributeData[1]:
                iioData[attributeData[1]] = units["resistance"]

            elif "heater_enable" in attributeData[1]:
                iioData[attributeData[1]] = units["boolean"]

            elif "steps" in attributeData[1]:
                if "_en" in attributeData[1] and "debounce" not in attributeData[1]:
                    iioData[attributeData[1]] = units["steps"]

            elif "incli" in attributeData[1]:
                iioData[attributeData[1]] = units["incline"]

            elif "magn_" in attributeData[1]:
                iioData[attributeData[1]] = units["magnetic"]

            elif "rot" in attributeData[1]:
                iioData[attributeData[1]] = units["rotation"]

            elif "proximity" in attributeData[1]:
                iioData[attributeData[1]] = units["proximity"]

            elif "distance" in attributeData[1]:
                if "_en" not in attributeData[1]:
                    iioData[attributeData[1]] = units["distance"]

            elif "current" in attributeData[1]:
                if "shunt" not in attributeData[1]:
                    iioData[attributeData[1]] = units["current"]

            elif "in_Y_mean_raw" in attributeData[1]:
                iioData[attributeData[1]] = units["mean"]


    count += 1

print(iioData)
print(f"Attribute Count: {count}")

#jsonData = json.dump(iioData)

#outputFile.write(str(iioData))