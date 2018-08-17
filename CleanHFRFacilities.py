import csv
import os.path
from os import path

class CleanHFRFacilities:
	
	mheaders = []
	filetoread = ""
	recordrows = 0
	
	def __init__(self, filename):
		self.filetoread = filename
		
	def openFile(self):
		return self.filetoread;
		
	def getHeaders(self):
		localheaders = []
		with open('./' + self.filetoread, 'r') as filetoread:
			headers = csv.DictReader(filetoread)
			headersJSONData = next(headers)
			
			for key in headersJSONData.keys():
				localheaders.append(key)
		return localheaders
		
	def setHeaders(self, localheaders):
		for i in len(localheaders):
			self.mheaders[i] = localheaders[i]
		return true
	
	def getRecordsData(self):
		pass
		
#HFRInstance = CleanHFRFacilities()
#HFRInstance.mheaders = HFRInstance.getHeaders(self.filetoread)
#print(HFRInstance.mheaders)

HFRInstance = CleanHFRFacilities('cainam.csv')
HFRInstance.mheaders = HFRInstance.getHeaders()
print(HFRInstance.filetoread)


