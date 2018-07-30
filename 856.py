class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        leftcount = []
        total = 0
        for char in S:
            if char == "(":
                leftcount.append(1)
            elif char == ")":
                if leftcount and len(leftcount) > 1:
                    temp = leftcount.pop() * 2
                    if leftcount[-1] == 1:
                        leftcount[-1] = temp
                    else:
                        leftcount[-1] += temp
                elif leftcount and len(leftcount) == 1:
                    total += leftcount.pop()
        
        return total
