"""Function checks the coolant temperature and compare it with the threshold. Returns Safestate or not."""
import numpy as np
import pandas as pd

def Coolant(CoolantTemperatureC,EngineLoad,TripTime):
	State0=[]
	State1=[]
	State2=[]
	State3=[]

	IndexTripTimeThreshold=0
	Safestate = 0
	LowestTemperatureC = 0.0
	NormalTemperatureC = 190.0 #Reference form internet safe state 190F to 220F
	HighestTemperatureC = 220.0

	CoolantTemperatureC_np=np.asarray(CoolantTemperatureC)
	CoolantTemperatureC_np=CoolantTemperatureC_np.astype(float)
	CoolantTemperatureF_np=(CoolantTemperatureC_np*(9/5))+32

	EngineLoad_np=np.asarray(EngineLoad)
	EngineLoad_np=EngineLoad_np.astype(float)

	TripTime_np=np.asarray(TripTime)
	TripTime_np=TripTime_np.astype(int)

	EngineLoadThreshold=0.50*max(EngineLoad_np)
	TripTimeThreshold = 0.50*max(TripTime_np)

	for i in range(0,CoolantTemperatureF_np.size):
		if CoolantTemperatureF_np[i] > NormalTemperatureC and CoolantTemperatureF_np[i] < HighestTemperatureC:
			if (TripTime_np[i] < TripTimeThreshold):
				IndexTripTimeThreshold=i
				if (EngineLoad_np[i] < EngineLoadThreshold):
					Safestate=Safestate+1
					State1.append([Safestate,i])
		elif CoolantTemperatureF_np[i] < NormalTemperatureC and CoolantTemperatureF_np[i] > LowestTemperatureC:
			Safestate=Safestate+1
			State2.append([Safestate,i])
		elif CoolantTemperatureF_np[i] > HighestTemperatureC:
			Safestate=Safestate-1
			State3.append([Safestate,i])
		State0.append(Safestate)


	SafeState1 = pd.DataFrame(data=State1, columns=['Safestate','Index'])
	SafeState2 = pd.DataFrame(data=State2, columns=['Safestate','Index'])
	SafeState3 = pd.DataFrame(data=State3, columns=['Safestate','Index'])

	return CoolantTemperatureF_np,HighestTemperatureC,NormalTemperatureC,LowestTemperatureC,SafeState1,SafeState2,SafeState3,State0,IndexTripTimeThreshold,EngineLoadThreshold
