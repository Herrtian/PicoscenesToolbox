from picoscenes import  Picoscenes
import numpy as np
import matplotlib.pyplot as plt

i = 0  # stands for the first frame of csi frames

frames = Picoscenes("rx_by_usrpN210.csi")
numTones = frames.raw[i].get("CSI").get("numTones")
SubcarrierIndex = np.array(frames.raw[i].get("CSI").get("SubcarrierIndex"))
Phase = np.array(frames.raw[i].get("CSI").get("Phase"))[:numTones]
Mag = np.array(frames.raw[i].get("CSI").get("Mag"))[:numTones]

plt.title("Phase && Magnitude Demo")
plt.xlabel("x axis subcarryindex ")
plt.ylabel("y axis Phase && Magnitude")
plt.plot(SubcarrierIndex, Phase)
plt.plot(SubcarrierIndex, Mag)
plt.show()
