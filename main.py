from picoscenes import PicoFrames, Picoscenes
import numpy as np
import matplotlib.pyplot as plt

i = 60

frames = Picoscenes("rx_1_210914_144909.csi")
# print(frames.raw[0].get("CSI"))
numTones = frames.raw[i].get("CSI").get("numTones")
SubcarrierIndex = np.array(frames.raw[i].get("CSI").get("SubcarrierIndex"))
Phase = np.array(frames.raw[i].get("CSI").get("Phase"))[:numTones]
Mag = np.array(frames.raw[i].get("CSI").get("Mag"))[:numTones]

plt.title("Phase Demo")
plt.xlabel("x axis subcarryindex ")
plt.ylabel("y axis Phase && Magnitude")
plt.plot(SubcarrierIndex, Phase)
plt.plot(SubcarrierIndex, Mag)
plt.show()
