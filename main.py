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

		 #print fm
		 fm  = ['Bailey']
		
		 loc2 = np.nonzero(firstCol==baseLine)
		 for control in controlLine:
			loc1 = np.nonzero(firstRow==control)		 	
			test = dm[loc2[0],loc1[1]][0]
			fm.append(control)
			print fm
		 
		 writer(fm) 
		 fm  = ['Distance']
		 for control in controlLine:
			loc1 = np.nonzero(firstRow==control)		 	
			test = dm[loc2[0],loc1[1]][0]
			fm.append(test)
			print fm
		 
		 writer(fm)
		# dm = dm[:,'Fec.G2.D42.Chase']
		# print fm.transpose()
		# writer(fm)

def writer(output):
	with open("output4.txt","a") as outFile:
		writer = csv.writer(outFile, delimiter=',')
		#for line in output:
		writer.writerow(output)


if __name__ == "__main__":
	distanceMatrixFile = "unweighted_unifrac_dm.txt"
	reader(distanceMatrixFile)