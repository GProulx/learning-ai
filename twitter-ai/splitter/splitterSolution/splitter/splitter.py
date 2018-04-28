
class splitter():
    def extract(fullDesc):
        basicSplit = fullDesc.split()
        for x in range(0, len(basicSplit) - 1):
            basicSplit.append(basicSplit[x] + " " + basicSplit[x + 1])

        cleanedList = []
        if len(basicSplit) > 0:
            lastValueRead = basicSplit[0]
            cleanedList.append(basicSplit[0])
            for x in range(1, len(basicSplit)):
                if basicSplit[x] != lastValueRead:
                    lastValueRead = basicSplit[x]
                    cleanedList.append(basicSplit[x])
    
        return cleanedList
