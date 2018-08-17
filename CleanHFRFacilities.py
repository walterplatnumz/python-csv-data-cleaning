import csv
import os.path
from os import path

class CleanHFRFacilities:
	
	mheaders = []
	
	def __init__(self):
		pass
		
	def openFile(self, filename_path):
		return filename_path;
		
	def getHeaders(self, filename_path):
		localheaders = []
		filename = self.openFile(filename_path)
		with open('./' + filename_path, 'r') as filetoread:
			headers = csv.DictReader(filetoread)
			headersJSONData = next(headers)
			
			for key in headersJSONData.keys():
				localheaders.append(key)
		return localheaders
		
	def setHeaders(self, localheaders):
		for i in len(localheaders):
			self.mheaders[i] = localheaders[i]
		return true


HFRInstance = CleanHFRFacilities()
HFRInstance.mheaders = HFRInstance.getHeaders('cainam.csv')
print(HFRInstance.mheaders)

