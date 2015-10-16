import csv
import numpy as np

def reader(distanceMatrixFile):
	with open(distanceMatrixFile, "r") as dm:
		 dm = np.array(list(csv.reader(dm, delimiter = '\t')))
		 
		 baseLine =["Fec.G3.D00.Bailey"]
		 controlLine = ["Fec.G3.D14.Bailey","Fec.G3.D07.Bailey","Fec.G3.D28.Bailey"]
		 index = [0]
		 fm = list(dm[:,index])
		 #print fm
		 loc = np.nonzero(fm=='Fec.G3.D28.Bailey')
		 print loc
		 print "hi"
		 
		# dm = dm[:,'Fec.G2.D42.Chase']
		 writer(dm)

def writer(output):
	with open("output.txt","w") as outFile:
		writer = csv.writer(outFile, delimiter=',')
		for line in output:
			writer.writerow(line)


if __name__ == "__main__":
	distanceMatrixFile = "unweighted_unifrac_dm.txt"
	reader(distanceMatrixFile)