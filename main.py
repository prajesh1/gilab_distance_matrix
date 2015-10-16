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
		 fm  = np.array(['Dog','baseLine','controlLine','distance'])
		 writer(fm)
		 loc2 = np.nonzero(firstCol==baseLine)
		 for control in controlLine:
			loc1 = np.nonzero(firstRow==control)		 	
			# print type(loc1)
			# print loc1
			#print "loc1"
			##print loc1[0]
			#print loc2
			#print "   loc2"
			#print loc2[1]
			#print control
			#print dm[loc2[0],loc1[1]]
			test = dm[loc2[0],loc1[1]][0]
			print "hi"
			tt = np.array(['Bailey',baseLine[0],control,test],dtype=object)
			writer(tt.transpose())
			#fm = np.concatenate(fm,tt)
			#print fm
		 
		 
		# dm = dm[:,'Fec.G2.D42.Chase']
		# print fm.transpose()
		# writer(fm)

def writer(output):
	with open("output.txt","a") as outFile:
		writer = csv.writer(outFile, delimiter=',')
		#for line in output:
		writer.writerow(output)


if __name__ == "__main__":
	distanceMatrixFile = "unweighted_unifrac_dm.txt"
	reader(distanceMatrixFile)