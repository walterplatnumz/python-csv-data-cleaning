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

    headerConfigurations = {"resmap-id": "jumbo", "lat": "Walter", "name": "Usenge"}

    def __init__(self, filename_path):
        self.fileToRead = filename_path
        self.totalrec = self.getTotalRecords()
        self.mHeaders = self.getHeaderFromFile()


        self.mNewHeaders = self.cleaningHeaderName()
        # self.writeIntoNewFile()
        self.getAllRecords()

    def getHeaderFromFile(self):
        localheaders = []
        if os.path.exists(self.fileToRead):
            with open('./' + self.fileToRead, 'r') as fileheaderstoread:
                headers = csv.DictReader(fileheaderstoread)
                headerJSON = headers.fieldnames
                localheaders = headerJSON
                return localheaders
        else:
            print "File doesn't exist, please check the file again"

    def cleaningHeaderName(self):
        localnewheaders = []

        for key, value in self.headerConfigurations.iteritems():
            for i in range(len(self.mHeaders)):
                if(key == self.mHeaders[i]):
                    if key in self.mNewHeaders:
                        pass
                    else:
                        localnewheaders.append(value)
                else:
                    if self.mHeaders[i] in self.mNewHeaders:
                        pass
                    else:
                        localnewheaders.append(self.mHeaders[i])
                # print key + " - " + self.mHeaders[i]
                    # localnewheaders.append(self.mHeaders[i])
        return localnewheaders

    def writeIntoNewFile(self):
        with open('./' + self.fileToWrite, 'w') as filetowrite:
            writerOBJ = csv.DictWriter(filetowrite, fieldnames=self.mNewHeaders)
            writerOBJ = csv.writer(filetowrite)
            writerOBJ.writerow(self.mNewHeaders)
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
print len(objInstance.mNewHeaders)
print len(objInstance.mHeaders)
# print objInstance.printJSON(objInstance.cleaningHeaderName())




