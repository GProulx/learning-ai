import re

class splitter():

    basicWords = ["the", "a", "an", "for", "and", "with"]

    def extract(fullDesc):
        basicSplit = splitter.splitString(fullDesc)

        cleanedList = splitter.removeBasicWords(basicSplit)

        for x in range(0, len(cleanedList) - 1):
            cleanedList.append(cleanedList[x] + " " + cleanedList[x + 1])

        listWithOutDuplicates = splitter.removedupplicates(cleanedList)
        return listWithOutDuplicates

    def extract_basic(fullDesc):
        basicSplit = splitter.splitString(fullDesc)

        cleanedList = splitter.removeBasicWords(basicSplit)

        #for x in range(0, len(cleanedList) - 1):
        #    cleanedList.append(cleanedList[x] + " " + cleanedList[x + 1])

        listWithOutDuplicates = splitter.removedupplicates(cleanedList)
        return listWithOutDuplicates

    def splitString(receivedString):
        splitedList = re.split('\s|(?<!\d)[,.](?!\d)', receivedString)
        result = []
        for x in range(0, len(splitedList)):
            if (len(splitedList[x]) > 0):
                result.append(splitedList[x])

        return result
    
    def removeBasicWords(input):
        cleanedList = []
        for x in range(0, len(input)):
            if (len(input[x]) > 2 and not input[x].lower() in splitter.basicWords):
                cleanedList.append(input[x])

        return cleanedList

    def removedupplicates(fullList):
        cleanedList = []
        if len(fullList) > 0:
            lastValueRead = fullList[0]
            cleanedList.append(fullList[0])
            for x in range(1, len(fullList)):
                if fullList[x] != lastValueRead:
                    lastValueRead = fullList[x]
                    cleanedList.append(fullList[x])
    
        return cleanedList
