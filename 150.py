class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        pay attention to the int(x/y)
        Division between two integers should truncate toward zero
        """
        if not tokens:
            return None
        ret=[]
        tlen=len(tokens)
        index=0
        d={"+":lambda x,y:x+y,
          "-":lambda x,y:x-y,
          "*":lambda x,y:x*y,
          "/":lambda x,y:int(x/y)}
        while index < tlen:
            if tokens[index] in "+-*/":
                temp1=ret.pop()
                temp2=ret.pop()
                ret.append(d[tokens[index]](temp2,temp1))
            else:
                ret.append(int(tokens[index]))
            index+=1
        
        return ret[0]
