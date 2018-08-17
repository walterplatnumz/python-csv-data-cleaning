import csv
import os.path
from os import path

class CleanHFRFacilities:
	
	headers = []
	
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
	
	def ConcatenateNames(self, first, last):
		return self.first + " - " + self.last


HFRInstance = CleanHFRFacilities()
print(HFRInstance.getHeaders('cainam.csv'))
