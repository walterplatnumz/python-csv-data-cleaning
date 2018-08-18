import csv
import pandas
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

    headerConfigurations = {"resmap-id": "walter", "lat": "Melanie"}

    def __init__(self, filename_path):
        self.fileToRead = filename_path
        self.totalrec = self.getTotalRecords()
        self.mHeaders = self.getHeaderFromFile()
        self.mNewHeaders = self.cleaningHeaderName()
        # self.writeIntoNewFile()
        self.getAllRecords()

    def getHeaderFromFile(self):
        localheaders = []
        if os.path.exists(self.fileToWrite):
            with open('./' + self.fileToWrite, 'r') as fileheaderstoread:
                headers = csv.DictReader(fileheaderstoread)
                headerJSON = headers.fieldnames
                if not headerJSON:
                    if os.path.exists(self.fileToRead):
                        with open('./' + self.fileToRead, 'r') as fileheaderstoread:
                            headers = csv.DictReader(fileheaderstoread)
                            headerJSON = headers.fieldnames
                            localheaders = headerJSON
                            return localheaders
                else:
                    localheaders = headerJSON
                    return localheaders
        else:
            if os.path.exists(self.fileToRead):
                with open('./' + self.fileToRead, 'r') as fileheaderstoread:
                    headers = csv.DictReader(fileheaderstoread)
                    headerJSON = headers.fieldnames
                    if not headerJSON:
                        print "File has no headers/titles"
                    else:
                        if os.path.exists(self.fileToRead):
                            with open('./' + self.fileToRead, 'r') as fileheaderstoread:
                                headers = csv.DictReader(fileheaderstoread)
                                headerJSON = headers.fieldnames
                                localheaders = headerJSON
                                return localheaders
    def deleteDataInList(self, index):
        for i in range(len(self.mNewHeaders)):
            del self.mNewHeaders[i]


    def cleaningHeaderName(self):
        localnewheaders = []

        for key, value in self.headerConfigurations.iteritems():
            for i in range(len(self.mHeaders)):
                if(key == self.mHeaders[i]):
                    localnewheaders.append(value)
                else:
                    localnewheaders.append(self.mHeaders[i])


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
                self.allDATA.append(localrecord)
        self.writeIntoNewFile()

    def getTotalRecords(self):
        with open('./' + self.fileToRead, 'r') as filedatatoread:
            records = csv.DictReader(filedatatoread)
            counter = 1
            for rowData in records:
                counter = counter + 1
            return counter




objInstance = CleanHFRFacilities('cainam.csv')
print objInstance.printJSON(objInstance.mNewHeaders)
print len(objInstance.mNewHeaders)

# print objInstance.printJSON(objInstance.mHeaders)
# print objInstance.printJSON(objInstance.getHeaderFromFile())
# print objInstance.printJSON(objInstance.cleaningHeaderName())




