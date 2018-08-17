import csv
import os.path
import itertools
from os import path

class CleanHFRFacilities:
	
	mheaders = []
	filetoread = ""
	filetowrite = "output.csv"
	recordrows = 0
	
	headerCOnfigurations  = { "name": "jumbo" }
	
	def __init__(self, filename):
		self.filetoread = filename
				
	def getHeaders(self):
		localheaders = []
		with open('./' + self.filetoread, 'r') as fileheadertoread:
			headers = csv.DictReader(fileheadertoread)
			headersJSONData = next(headers)
			
			for key in headersJSONData.keys():
				localheaders.append(key)
		return localheaders
		
	def setHeaders(self, localheaders):
		for i in len(localheaders):
			self.mheaders[i] = localheaders[i]
		return true
	
	def getAllRecordsAllRowsDataOnce(self):
		with open('./' + self.filetoread, 'r') as fileAllrecordstoread:
			records = csv.DictReader(fileAllrecordstoread)
			
			for rowData in records:
				self.cleanHeaderNames(rowData)
				
	def writeIntoNewFile(self, recordDatas):
		with open('./' + self.filetowrite, 'w') as fileAllrecordstowrite:			
			writerOBJ = csv.DictWriter(fileAllrecordstowrite, fieldnames=self.mheaders)
			writerOBJ = csv.writer(fileAllrecordstowrite)
			writerOBJ.writerow(self.mheaders)
			keyvalueArray = []
			for rowData in recordDatas:
				for i in range(len(self.mheaders)):
					#keyvalueArray.append(rowData[i])
					print(i)
					
				writerOBJ.writerow(keyvalueArray)	
	
	def replaceHeaderNames(self, oldValue, newValue, recordData):
		self.writeIntoNewFile(recordData)
		
		
	def cleanHeaderNames(self, headerData):
		for oldkey, oldvalue in headerData.iteritems():
			for newkey, newvalue in self.headerCOnfigurations.iteritems():
				if oldkey == newkey:
					self.replaceHeaderNames(oldvalue, newvalue, headerData)
	
					
	
		
	


			
HFRInstance = CleanHFRFacilities('cainam.csv')
HFRInstance.mheaders = HFRInstance.getHeaders()
HFRInstance.getAllRecordsAllRowsDataOnce()

#print(HFRInstance.filetoread)
#print(HFRInstance.getRecordsSingleRowData())
#print(HFRInstance.getRecordsSingleRowData())
#print(HFRInstance.filetoread)
#print("key: {} | value: {}".format(key, value))


