"""Function checks the load on the engine and returns it as overloaded or not."""

import numpy as np
import pandas as pd

def LoadAnalysis(EngineLoad, EngineRPM, VehicleSpeed, TripTime):
    GearRatio = 1.5
    AxleRatio = 4
    TyreSize = 12
    ExpectedSpeed = []
    MaxLoad = 0
    MaxRPM = 0
    TempEngineLoadLess = []
    TempEngineLoadMore = []
    TempEngineRPMLess = []
    TempEngineRPMMore = []
    TempVehicleSpeedLess = []
    TempVehicleSpeedMore = []

    CounterOverload = []
    TempCounterOverload = 0

    for i in EngineLoad.index:
        if EngineLoad[i] == '-':
            EngineLoad[i] = '0'
        if EngineRPM[i] == '-':
            EngineRPM[i] = '0'
        EngineLoad[i] = float(EngineLoad[i])
        EngineRPM[i] = float(EngineRPM[i])

        if MaxLoad < EngineLoad[i]:
            MaxLoad = EngineLoad[i]

        if MaxRPM < EngineRPM[i]:
            MaxRPM = EngineRPM[i]

    LoadThreshold = 0.5 * MaxLoad
    RPMThreshold = 0.5 * MaxRPM

    for i in EngineRPM.index:
        if VehicleSpeed[i] == '-':
            VehicleSpeed[i] = '0'
        if TripTime[i] == '-':
            TripTime[i] = '0'

        if (EngineLoad[i] < LoadThreshold):  # Checking whether vehicle speed is less than expected speed
            TempEngineLoadLess.append([EngineLoad[i], i])
        else:
            TempEngineLoadMore.append([EngineLoad[i], i])

        if (EngineRPM[i] < RPMThreshold):  # Checking whether vehicle speed is less than expected speed
            TempEngineRPMLess.append([EngineRPM[i], i])
        else:
            TempEngineRPMMore.append([EngineRPM[i], i])

        if EngineLoad[i] > LoadThreshold and EngineRPM[i] > RPMThreshold:
            TempCounterOverload = TempCounterOverload + 1  # Checking whether engine load and engine rpm are less than threshold
        CounterOverload.append(TempCounterOverload)

        VehicleSpeed[i] = float(VehicleSpeed[i])

        # ACTUAL SPEED = (ENGINE RPM * PERIMETER OF TYRE)/(AXLE RATIO * GEAR RATIO)
        ExpectedSpeed.append(
            0.4 * (EngineRPM[i] * 60 * 3.14 * 2 * TyreSize * 25.4 * 0.000001) / (GearRatio * AxleRatio))

        if (VehicleSpeed[i] < (ExpectedSpeed[i])):  # Checking whether vehicle speed is less than expected speed
            TempVehicleSpeedLess.append([VehicleSpeed[i], i])
        else:
            TempVehicleSpeedMore.append([VehicleSpeed[i], i])

    EngineLoadLess = pd.DataFrame(data=TempEngineLoadLess, columns=['EngineLoad', 'Index'])
    EngineLoadMore = pd.DataFrame(data=TempEngineLoadMore, columns=['EngineLoad', 'Index'])
    EngineRPMLess = pd.DataFrame(data=TempEngineRPMLess, columns=['EngineRPM', 'Index'])
    EngineRPMMore = pd.DataFrame(data=TempEngineRPMMore, columns=['EngineRPM', 'Index'])
    VehicleSpeedLess = pd.DataFrame(data=TempVehicleSpeedLess, columns=['VehicleSpeed', 'Index'])
    VehicleSpeedMore = pd.DataFrame(data=TempVehicleSpeedMore, columns=['VehicleSpeed', 'Index'])

    return EngineLoadLess, EngineLoadMore, EngineRPMLess, EngineRPMMore, VehicleSpeedLess, VehicleSpeedMore, ExpectedSpeed, LoadThreshold, RPMThreshold, CounterOverload
