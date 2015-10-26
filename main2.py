import csv
import numpy as np

def reader(distanceMatrixFile):
	with open(distanceMatrixFile, "r") as dm:
		 dm = np.array(list(csv.reader(dm, delimiter = '\t')))
		 
		 baseLine =["Fec.G3.D00.Bailey"]
		 controlLine = ["Fec.G3.D14.Bailey","Fec.G3.D07.Bailey","Fec.G3.D28.Bailey"]
		 index = [0]
		 firstCol = dm[:,index]
		 firstRow = dm[index,:]
		 with open("120914JS1-mapping2.txt", "r") as mappingFile:
		 	mappingFile = np.array(list(csv.reader(mappingFile, delimiter = '\t')))
		 #print fm
		 samples = mappingFile[:,6]
		 
		 mappingFirstCol = mappingFile[:0]
		 #samples.remove("Dog")
		 samples = np.unique(samples)
		 print samples
		 for sample in samples:
		 			if(sample !='Dog'):
						#print sample
						value = mappingFile[np.logical_or.reduce([mappingFile[:,6] == sample])]
						days = value[:,5]
		 				days = np.unique(days)
						#print mappingFile
						print "value"
						#print value[0][0]
						#print value[:,5]
						loc= np.nonzero(value[:,5]=="0")
						baseLine = value[loc[0]][0][0]
						print "baseLine " +baseLine
						for day in days:
							if(day!= "0" and day!="Day"):
								print "Day is "+day
								#value = value[[value[:,5] == day]]

								loc= np.nonzero(value[:,5]==day)
								#print loc[0]
								controlLine= value[loc[0]][0][0]
								print "controlLine " + controlLine

								
							

def writer(output):
	with open("output4.txt","a") as outFile:
		writer = csv.writer(outFile, delimiter=',')
		#for line in output:
		writer.writerow(output)


if __name__ == "__main__":
	distanceMatrixFile = "unweighted_unifrac_dm.txt"
	reader(distanceMatrixFile)