import unittest
import DIARashDriving
import pandas as pd
import matplotlib.pyplot as plt
import os

Threshold = 30
class Test_RashDriving(unittest.TestCase):
	def testRashDriving(self):
		try:
			df_File = pd.read_csv("List_of_Data_Set.csv")
			if not(os.path.isdir("Result")):
				os.mkdir("Result")
			for i in df_File.index:
				df = pd.read_csv(str(df_File["Input_File_Name"][i]))
				TempFile1=df_File["Input_File_Name"][i].split('/')
				TempFile3=TempFile1[-1].split('.')
				TempFile4=str(TempFile3[0])
				path=os.path.join("Result/" , TempFile4)
				Location = DIARashDriving.detect_rash_driving(df[' Latitude'], df[' Longitude'], df['Accelerator PedalPosition D(%)'].replace(to_replace='-',value=0), df['Accelerator PedalPosition E(%)'].replace(to_replace='-',value=0), Threshold)

				plt.figure()
				plt.plot(Location['Latitude'],Location['Longitude'],'r.',label='RashDriving_Locations')
				plt.title("Rash Driving")
				plt.ylabel('Longitude')
				plt.xlabel('Latitude')
				plt.legend(loc='lower right')
				plt.savefig(path+'.png')
				plt.close()

		except AssertionError as e:
			f = open("Error_RashDriving", "a")
			f.write("TestCase_no_0:\n\t"+str(e)+" \n")

if __name__ == '__main__':
	unittest.main()
