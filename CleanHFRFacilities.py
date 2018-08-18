import csv
import os.path
import itertools
import json
from os import path


class CleanHFRFacilities:
    mHeaders = []
    mNewHeaders = []
    fileToRead = ""
    fileToWrite = "output.csv"
    totalrec = 0;
    allDATA = []

    headerConfigurations = {"name": "walter"}

    def __init__(self, filename_path):
        self.fileToRead = filename_path
        self.totalrec = self.getTotalRecords()
        self.mHeaders = self.getHeaderFromFile()
        self.mHeaders = self.cleaningHeaderName()
        self.writeIntoNewFile()
        # self.allDATA = self.getAllRecords()

    def getHeaderFromFile(self):
        localheaders = []

        if os.path.exists(self.fileToRead):
            with open('./' + self.fileToRead, 'r') as fileheaderstoread:
                headers = csv.DictReader(fileheaderstoread)
                headerJSON = headers.fieldnames
                localheaders = headerJSON
        return localheaders

    def cleaningHeaderName(self):
        localnewheaders = []
        localnewheaders = self.mHeaders

        if not self.headerConfigurations:
            print "Header Configuration is Empty"
            return localnewheaders
        else:
            for key, value in self.headerConfigurations.iteritems():
                for i in range(len(self.mHeaders)):
                    if(key == self.mHeaders[i]):
                        localnewheaders[i] = value
                        self.mHeaders[i] = value
                    else:
                        localnewheaders[i] = self.mHeaders[i]
                        self.mHeaders[i] = self.mHeaders[i]

        self.mHeaders = localnewheaders
        return localnewheaders


    def writeIntoNewFile(self):
        with open('./' + self.fileToWrite, 'w') as filetowrite:
            writerOBJ = csv.writer(filetowrite)
            writerOBJ.writerow(self.mHeaders)
            writerOBJ.writerows(self.allDATA)


    def printJSON(self, listofitems):
        return json.dumps(listofitems, indent=4, sort_keys=True)


    def getAllRecords(self):
        with open('./' + self.fileToRead, 'r') as filedatatoread:
            records = csv.DictReader(filedatatoread)

            for rowData in records:
                localrecord = []
                for i in range(len(self.mHeaders)):
                    localrecord.append(rowData[self.mHeaders[i]])
                    # self.writeIntoNewFile(localrecord)
                # self.allDATA.append(localrecord)
                # self.allDATA = localrecord
                return localrecord

    def getTotalRecords(self):
        with open('./' + self.fileToRead, 'r') as filedatatoread:
            records = csv.DictReader(filedatatoread)
            counter = 1
            for rowData in records:
                counter = counter + 1
            return counter




objInstance = CleanHFRFacilities('cainam.csv')
# print objInstance.printJSON(objInstance.getHeaderFromFile())
# print len(objInstance.mHeaders)
# print objInstance.allDATA
print objInstance.mHeaders
# print objInstance.getAllRecords()



# print objInstance.printJSON(objInstance.cleaningHeaderName())
# print objInstance.printJSON(objInstance.getHeaderFromFile())
# print objInstance.printJSON(objInstance.allDATA)





