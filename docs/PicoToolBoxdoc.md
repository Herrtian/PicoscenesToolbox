# PicoToolBox

This docs shows you how the datastructure displays in PicoToolBox.

You will not know how the python parse CSI data,but you would better know the structure if you want to create your own data analysis.

## Picoscenes

Picoscenes is the well packed frames ,you can use **.raw**[]  to get a specific frame.

Example:

 ```python
 i = 0
 frames = Picoscenes("rx_by_usrpN210.csi") # return a Picoscenes Object
 First_Frame = frames.raw[i] # get the first frame ,you can set i to get different frame
 ```



Now i will show you the more details in Picoscenes raw.

For all the attributes i will give you a small example. 

### Frame

frame is a structure which inlcudes all information and structure .

you can also use **print(frames.raw[0])** to get the newst infomation if i have not updated the docs.

frame has the method frame_value_xxx_has_value it means some attributes are **optional**

For example, if **frame_value.mvmExtraSegment.has_value** == 1 ,then **frame.raw[0].MVMExtra** is a concrete value, or it is **None** 

| Name             | Type                       | Illustration |
| ---------------- | -------------------------- | ------------ |
| StandardHeader   | ieee80211_mac_frame_header |              |
| RxSBasic         | RxSBasicSegment            |              |
| RxExtraInfo      | ExtraInfoSegment           |              |
| CSI              | CSISegment                 |              |
| MVMExtra         | MVMExtraSegment            | optional     |
| PicoScenesHeader | PicoScenesFrameHeader      | optional     |
| TxExtraInfo      | ExtraInfoSegment           | optional     |
| PilotCSI         | CSISegment                 | optional     |
| LegacyCSI        | CSISegment                 | optional     |
| BasebandSignals  | BasebandSignalSegment      | optional     |
| PreEQSymbols     | PreEQSymbolsSegment        | optional     |
| MPDU             | vector[uint8_t]            |              |



**note**: **StandardHeader** & **CSI** & **RxSBasic** & **RxExtraInfo** are all the strcutures contained.



### CSI

CSI is the most important structure in Picoscenes.

| Name                | Type                           | Illustration   |
| ------------------- | ------------------------------ | -------------- |
| DeviceType          | PicoScenesDeviceType           | uint16_t       |
| PacketFormat        | PacketFormatEnum               | int8_t         |
| CBW                 | ChannelBandwidthEnum           | uint16_t       |
| CarrierFreq         | uint64_t                       |                |
| SamplingRate        | uint64_t                       |                |
| SubcarrierBandwidth | uint32_t                       |                |
| numTones            | CSIDimension                   | uint16_t       |
| numTx               | CSIDimension                   | uint8_t        |
| numRx               | CSIDimension                   | uint8_t        |
| numESS              | CSIDimension                   | uint8_t        |
| numCSI              | CSIDimension                   | uint16_t       |
| ant_sel             | uint8_t                        |                |
| CSI                 | SignalMatrix[ccomplex[double]] | Cplx structure |
| Mag                 | SignalMatrix[double]           | Cplx structure |
| Phase               | SignalMatrix[double]           | Cplx structure |
| SubcarrierIndex     | vector[int16_t]                | Cplx structure |

**uint** means **unsigned int**

#### Example 

```python
i = 0
frames = Picoscenes("rx_by_usrpN210.csi")
numTones = frames.raw[i].get("CSI").get("numTones") # get the first frame numtones
```



#### PicoScenesDeviceType (uint16_t)

        # all attributes are uint16_t
        QCA9300
        IWL5300
        IWLMVM
        MAC80211Compatible
        USRP
        VirtualSDR
        Unknown



#### PacketFormatEnum(int8_t)

        PacketFormat_NonHT
        PacketFormat_HT
        PacketFormat_VHT
        PacketFormat_HESU
        PacketFormat_HEMU
        PacketFormat_Unknown



#### ChannelBandwidthEnum(uint16_t)

        CBW_5
        CBW_10
        CBW_20
        CBW_40
        CBW_80
        CBW_160

#### SignalMatrix

| Name       | Type            | Illustratio |
| ---------- | --------------- | ----------- |
| array      | vector[T]       |             |
| dimensions | vector[int64_t] |             |



#### CSIDimension

        uint16_t numTones
        uint8_t numTx
        uint8_t numRx
        uint8_t numESS
        uint16_t numCSI

### StandardHeader

| Name         | Type                       | Illustration   |
| ------------ | -------------------------- | -------------- |
| ControlField | ieee80211_mac_frame_header | Cplx Structure |
| Addr1        | uint8_t [6]                |                |
| Addr2        | uint8_t [6]                |                |
| Addr3        | uint8_t [6]                |                |
| Fragment     | uint16_t                   |                |
| Sequence     | uint16_t                   |                |

#### Example 

```python
i = 0  # stands for the first frame of csi frames

frames = Picoscenes("rx_by_usrpN210.csi")
Fragment = frames.raw[i].get("StandardHeader").get("Fragment")
```



#### ieee80211_mac_frame_header

| Name       | Type     | Illustration |
| ---------- | -------- | ------------ |
| version    | uint16_t |              |
| type       | uint16_t |              |
| subtype    | uint16_t |              |
| toDS       | uint16_t |              |
| fromDS     | uint16_t |              |
| moreFrags  | uint16_t |              |
| retry      | uint16_t |              |
| power_mgmt | uint16_t |              |
| more       | uint16_t |              |
| protect    | uint16_t |              |
| order      | uint16_t |              |



### RxSBasic

| Name         | Type     | Illustration |
| ------------ | -------- | ------------ |
| deviceType   | uint16_t |              |
| timestamp    | uint64_t |              |
| centerFreq   | int16_t  |              |
| controlFreq  | int16_t  |              |
| CBW          | uint16_t |              |
| packetFormat | uint8_t  |              |
| packetCBW    | uint16_t |              |
| GI           | uint16_t |              |
| MCS          | uint8_t  |              |
| numSTS       | uint8_t  |              |
| numESS       | uint8_t  |              |
| numRx        | uint8_t  |              |
| noiseFloor   | int8_t   |              |
| rssi         | int8_t   |              |
| rssi1        | int8_t   |              |
| rssi2        | int8_t   |              |
| rssi3        | int8_t   |              |



#### Example 

```python	
i = 0  # stands for the first frame of csi frames

frames = Picoscenes("rx_by_usrpN210.csi")
timestamp = frames.raw[i].get("RxSBasic").get("timestamp")

```



### RxExtraInfo(Optional)

Extrainfo is also a cplx flexible structure. It contains the **has_xxx** attribute.

**has_xxx** is a **bint** type, which is 0 or 1. 

For example, if **hasLength** == 1 ,then **RxExtraInfo.Length** is a concrete value, or it is **None** 

In order to **not** trouble you ,i will just list the meaningful Information of the RXExtraInfo.



| Name             | Type                  | Illustration   |
| ---------------- | --------------------- | -------------- |
| length           | uint16_t              |                |
| version          | uint64_t              |                |
| macaddr_cur      | uint8_t [6]           |                |
| macaddr_rom      | uint8_t [6]           |                |
| chansel          | uint32_t              |                |
| bmode            | uint8_t               |                |
| evm              | int8_t [20]           |                |
| tx_chainmask     | uint8_t               |                |
| rx_chainmask     | uint8_t               |                |
| txpower          | uint8_t               |                |
| cf               | uint64_t              |                |
| txtsf            | uint32_t              |                |
| last_txtsf       | uint32_t              |                |
| channel_flags    | uint16_t              |                |
| tx_ness          | uint8_t               |                |
| tuning_policy    | AtherosCFTuningPolicy | Cplx structure |
| pll_rate         | uint16_t              |                |
| pll_clock_select | uint8_t               |                |
| pll_refdiv       | uint8_t               |                |
| agc              | uint8_t               |                |
| ant_sel          | uint8_t [3]           |                |
| cfo              | int32_t               |                |
| sfo              | int32_t               |                |



#### Example 

```python	
i = 0  # stands for the first frame of csi frames

frames = Picoscenes("rx_by_usrpN210.csi")
if frames.raw[i].get("RxExtraInfo").get("has_txpower"):
	txpower = frames.raw[i].get("RxExtraInfo").get("txpower")
    # make sure the frame has_xxx attribute then assign the variable

```



#### AtherosCFTuningPolicy

| Name                    | Type    | Illustration |
| ----------------------- | ------- | ------------ |
| CFTuningByDefault       | uint8_t |              |
| CFTuningByChansel       | uint8_t |              |
| CFTuningByFastCC        | uint8_t |              |
| CFTuningByHardwareReset | uint8_t |              |



### MVMExtra(Optional)

| Name       | Type     | Illustration |
| ---------- | -------- | ------------ |
| FMTClock   | uint32_t |              |
| usClock    | uint32_t |              |
| RateNFlags | uint32_t |              |



### PicoScenesHeader(Optional)

| Name       | Type                 | Illustration |
| ---------- | -------------------- | ------------ |
| MagicValue | uint32_t             |              |
| Version    | uint32_t             |              |
| DeviceType | PicoScenesDeviceType | uint16_t     |
| FrameType  | uint8_t              |              |
| TaskId     | uint16_t             |              |
| TxId       | uint16_t             |              |



### TxExtraInfo(Optional)

Txtrainfo is also a cplx flexible structure. It contains the **has_xxx** attribute.

**has_xxx** is a **bint** type, which is 0 or 1. 

For example, if **hasLength** == 1 ,then **Txtrainfo .Length** is a concrete value, or it is **None** 

In order to **not** trouble you ,i will just list the meaningful Information of the Txtrainfo .

| Name             | Type                  | Illustration   |
| ---------------- | --------------------- | -------------- |
| length           | uint16_t              |                |
| version          | uint64_t              |                |
| macaddr_cur      | uint8_t [6]           |                |
| macaddr_rom      | uint8_t [6]           |                |
| chansel          | uint32_t              |                |
| bmode            | uint8_t               |                |
| evm              | int8_t [20]           |                |
| tx_chainmask     | uint8_t               |                |
| rx_chainmask     | uint8_t               |                |
| txpower          | uint8_t               |                |
| cf               | uint64_t              |                |
| txtsf            | uint32_t              |                |
| last_txtsf       | uint32_t              |                |
| channel_flags    | uint16_t              |                |
| tx_ness          | uint8_t               |                |
| tuning_policy    | AtherosCFTuningPolicy | Cplx structure |
| pll_rate         | uint16_t              |                |
| pll_clock_select | uint8_t               |                |
| pll_refdiv       | uint8_t               |                |
| agc              | uint8_t               |                |
| ant_sel          | uint8_t [3]           |                |
| cfo              | int32_t               |                |
| sfo              | int32_t               |                |



#### Example 

```python	
i = 0  # stands for the first frame of csi frames

frames = Picoscenes("rx_by_qca9300.csi")
txpower = frames.raw[i].get("TxExtraInfo").get("txpower")
print(txpower)

```



### PilotCSI(Optional)

| Name                | Type                           | Illustration   |
| ------------------- | ------------------------------ | -------------- |
| DeviceType          | PicoScenesDeviceType           | uint16_t       |
| PacketFormat        | PacketFormatEnum               | int8_t         |
| CBW                 | ChannelBandwidthEnum           | uint16_t       |
| CarrierFreq         | uint64_t                       |                |
| SamplingRate        | uint64_t                       |                |
| SubcarrierBandwidth | uint32_t                       |                |
| numTones            | CSIDimension                   | uint16_t       |
| numTx               | CSIDimension                   | uint8_t        |
| numRx               | CSIDimension                   | uint8_t        |
| numESS              | CSIDimension                   | uint8_t        |
| numCSI              | CSIDimension                   | uint16_t       |
| ant_sel             | uint8_t                        |                |
| CSI                 | SignalMatrix[ccomplex[double]] | Cplx structure |
| Mag                 | SignalMatrix[double]           | Cplx structure |
| Phase               | SignalMatrix[double]           | Cplx structure |
| SubcarrierIndex     | vector[int16_t]                | Cplx structure |



#### Example 

```python
i = 0
frames = Picoscenes("rx_by_usrpN210.csi")
frame = frames.raw[i]  
if frame.get("PilotCSI"):
    numTones = frame.get("PilotCSI").get("numTones")
```





### LegacyCSI(Optional)

| Name                | Type                           | Illustration   |
| ------------------- | ------------------------------ | -------------- |
| DeviceType          | PicoScenesDeviceType           | uint16_t       |
| PacketFormat        | PacketFormatEnum               | int8_t         |
| CBW                 | ChannelBandwidthEnum           | uint16_t       |
| CarrierFreq         | uint64_t                       |                |
| SamplingRate        | uint64_t                       |                |
| SubcarrierBandwidth | uint32_t                       |                |
| numTones            | CSIDimension                   | uint16_t       |
| numTx               | CSIDimension                   | uint8_t        |
| numRx               | CSIDimension                   | uint8_t        |
| numESS              | CSIDimension                   | uint8_t        |
| numCSI              | CSIDimension                   | uint16_t       |
| ant_sel             | uint8_t                        |                |
| CSI                 | SignalMatrix[ccomplex[double]] | Cplx structure |
| Mag                 | SignalMatrix[double]           | Cplx structure |
| Phase               | SignalMatrix[double]           | Cplx structure |
| SubcarrierIndex     | vector[int16_t]                | Cplx structure |



#### Example 

```python
i = 0
frames = Picoscenes("rx_by_usrpN210.csi")
frame = frames.raw[i]  
if frame.get("LegacyCSI"):
    numTones = frame.get("LegacyCSI").get("numTones")
```



### BasebandSignals(Optional[np.asarray])

```python
i = 0
frames = Picoscenes("rx_by_usrpN210.csi")
frame = frames.raw[i]  
BasebandSignals = frame.get("BasebandSignals")
```



### PreEQSymbols(Optional[np.asarray])

```python
i = 0
frames = Picoscenes("rx_by_usrpN210.csi")
frame = frames.raw[i]  
BasebandSignals = frame.get("PreEQSymbols")
```



### MPDU(uint8_t)

```python
i = 0
frames = Picoscenes("rx_by_usrpN210.csi")
frame = frames.raw[i]  # get the first frame numtones
MPDU = frame.get("MPDU")
```

**If you have something dont know , you can check picoscenes.pyx or contact with me. **

















