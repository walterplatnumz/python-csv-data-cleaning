# import csv
# import os.path
# import itertools
# import json
# from os import path
#
#
# class CleanHFRFacilities:
#     mheaders = []
#     mNewHeaders = []
#     filetoread = ""
#     filetowrite = "output.csv"
#     recordrows = 0
#
#     headerCOnfigurations = {"name": "jumbo"}
#
#     def __init__(self, filename):
#         self.filetoread = filename
#
#     def getHeaders(self):
#         localheaders = []
#         with open('./' + self.filetoread, 'r') as fileheadertoread:
#             headers = csv.DictReader(fileheadertoread)
#             headersJSONData = next(headers)
#
#             for key in headersJSONData.keys():
#                 localheaders.append(key)
#         return localheaders
#
#     def getJSONData(self, listofitems):
#         return json.dumps(listofitems, indent=4, sort_keys=True)
#
#     def getLengthOfItems(self, listofitems):
#         return len(listofitems)
#
#     def setHeaders(self, localheaders):
#         for i in range(len(localheaders)):
#             self.mheaders[i] = localheaders[i]
#         return true
#
#     def getAllRecordsAllRowsDataOnce(self):
#         with open('./' + self.filetoread, 'r') as fileAllrecordstoread:
#             records = csv.DictReader(fileAllrecordstoread)
#
#             for rowData in records:
#                 print (rowData)
#                 self.cleanHeaderNames(rowData)
#
#     def writeIntoNewFile(self, recordDatas):
#         with open('./' + self.filetowrite, 'w') as fileAllrecordstowrite:
#             writerOBJ = csv.DictWriter(fileAllrecordstowrite, fieldnames=self.mheaders)
#             writerOBJ = csv.writer(fileAllrecordstowrite)
#             writerOBJ.writerow(self.mheaders)
#             keyvalueArray = []
#             for rowData in recordDatas:
#                 pass
#             # for i in range(len(self.mheaders)):
#             # keyvalueArray.append(rowData[i])
#             # writerOBJ.writerow(keyvalueArray)
#             # print(rowData['name'])
#
#     def replaceHeaderNames(self, oldValue, newValue, recordData):
#
#         self.writeIntoNewFile(recordData)
#
#     def cleanHeaderNames(self, headerData):
#         for oldkey, oldvalue in headerData.iteritems():
#             for newkey, newvalue in self.headerCOnfigurations.iteritems():
#                 print(oldkey, oldvalue)
#                 if oldkey == newkey:
#                     self.replaceHeaderNames(oldvalue, newvalue, headerData)
#
#
# HFRInstance = CleanHFRFacilities('cainam.csv')
# HFRInstance.mheaders = HFRInstance.getHeaders()
# HFRInstance.getAllRecordsAllRowsDataOnce()
#
# # print(HFRInstance.filetoread)
# # print(HFRInstance.getRecordsSingleRowData())
# # print(HFRInstance.getRecordsSingleRowData())
# # print(HFRInstance.filetoread)
# # print("key: {} | value: {}".format(key, value))


# if os.path.exists(self.fileToWrite):
#     with open('./' + self.fileToWrite, 'r') as fileheaderstoread:
#         headers = csv.DictReader(fileheaderstoread)
#         headerJSON = headers.fieldnames
#         if not headerJSON:
#             if os.path.exists(self.fileToRead):
#                 with open('./' + self.fileToRead, 'r') as fileheaderstoread:
#                     headers = csv.DictReader(fileheaderstoread)
#                     headerJSON = headers.fieldnames
#                     localheaders = headerJSON
#         else:
#             localheaders = headerJSON
# else:
#     if os.path.exists(self.fileToRead):
#         with open('./' + self.fileToRead, 'r') as fileheaderstoread:
#             headers = csv.DictReader(fileheaderstoread)
#             headerJSON = headers.fieldnames
#             if not headerJSON:
#                 print "File has no headers/titles"
#             else:
#                 if os.path.exists(self.fileToRead):
#                     with open('./' + self.fileToRead, 'r') as fileheaderstoread:
#                         headers = csv.DictReader(fileheaderstoread)
#                         headerJSON = headers.fieldnames
#                         localheaders = headerJSON
