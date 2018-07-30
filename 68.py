class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if not words:
            return []
        retStr = []
        curLength = 0
        tempWords = []
        for word in words:
            wlen = len(word)
            if curLength + wlen <= maxWidth:
                tempWords.append(word)
                curLength += wlen + 1
            else:
                temp = ""
                spaceTotal = maxWidth - curLength + len(tempWords)
                if len(tempWords) == 1:
                    temp += " " * spaceTotal + tempWords[0][::-1]
                else:
                    count = len(tempWords) - 1
                    for w in tempWords[::-1]:
                        if count:
                            spaceMean = spaceTotal // count
                            temp += w[::-1] + " " * spaceMean
                            spaceTotal -= spaceMean
                            count -= 1
                        else:
                            temp += w[::-1]
                retStr.append(temp[::-1])
                tempWords = [word]
                curLength = wlen+1
        
        if tempWords:
            temp = ""
            spaceTotal = maxWidth - curLength + len(tempWords)
            spaceCount = 0
            for w in tempWords:
                temp += w + " "
                spaceCount + =1
            if spaceCount > spaceTotal:
                temp = temp[:maxWidth]
            else:
                temp += " " * (spaceTotal - spaceCount)
            temp=temp[:maxWidth]
            retStr.append(temp)
        return retStr
