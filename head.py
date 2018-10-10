# This script is the replicate of the head function in Unix

def head(file_name, num = 5):
	''' 
	file_name is the name of file to read, including extension;
	num is the lines to print. Default value is 5
	'''
	InFile = open(file_name,'r')
	LineNumber = 0
	for line in InFile:
		if LineNumber > 0 and LineNumber <= num:
			line = line.strip()
			print line
		LineNumber = LineNumber+1

	InFile.close()

head("iris.csv",5)
