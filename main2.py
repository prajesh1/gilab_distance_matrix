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
		 allDays = mappingFile[:,5]
		 allDays = np.unique(allDays)
		 
		 mappingFirstCol = mappingFile[:0]
		 #samples.remove("Dog")
		 samples = np.unique(samples)
		 printRow = ['Sample Name']
		 for allDay in allDays:
		 	if(allDay!="Day"):
		 		printRow.append(allDay)
		 writer(printRow)
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
						printRow = []
						printRow.append(sample)
						print "baseLine " +baseLine
						
						for allDay in allDays:
		 					if(allDay!="Day"):
			 					if(allDay in days):
			 						loc= np.nonzero(value[:,5]==allDay)
									#print loc[0]
									controlLine= value[loc[0]][0][0]
									print "controlLine " + controlLine
									#distance = []
			 						#distance = obtainDistance(baseLine,controlLine)
			 						#print "The vakl is "
			 						#print distance
			 						printRow.append(obtainDistance(baseLine,controlLine))
			 					else:
			 						printRow.append(" ")
			 			writer(printRow)

						#for day in days:
						#	if(day!= "0" and day!="Day"):
							#	print "Day is "+day
								#value = value[[value[:,5] == day]]

							#	loc= np.nonzero(value[:,5]==day)
								#print loc[0]
							#	controlLine= value[loc[0]][0][0]
								#print "controlLine " + controlLine

							#	obtainDistance(baseLine,controlLine)

								
							

def writer(output):
	with open("output4.txt","a") as outFile:
		writer = csv.writer(outFile, delimiter='\t')
		#for line in output:
		writer.writerow(output)

def obtainDistance(baseLine,controlLine):
	with open("unweighted_unifrac_dm.txt", "r") as dm:
		 dm = np.array(list(csv.reader(dm, delimiter = '\t')))

		 index = [0]
		 firstCol = dm[:,index]
		 firstRow = dm[index,:]

		 loc2 = np.nonzero(firstCol==baseLine)
		 loc1 = np.nonzero(firstRow==controlLine)
		 
		 test = dm[loc2[0],loc1[1]][0]
		 print "Distance is "+test
		 return test


if __name__ == "__main__":
	distanceMatrixFile = "unweighted_unifrac_dm.txt"
	reader(distanceMatrixFile)