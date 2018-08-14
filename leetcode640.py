class Solution:
    def compute(self, left):
        left_x = 0
        left_number = 0
        start = 0
        left_length = len(left)
        temp_value = ""
        #print(left, right)
        while start < left_length:
            if left[start].isnumeric():
                while start < left_length and left[start].isnumeric():
                    temp_value += left[start]
                    start += 1
                if start >= left_length:
                    left_number += int(temp_value)
                    temp_value = ""
                elif left[start] == "x":
                    left_x += int(temp_value)
                    temp_value = ""
                    start += 1
                else:
                    left_number += int(temp_value)
                    temp_value = ""
            elif left[start] == "x":
                if start >= 1 and temp_value == "-":
                    left_x -= 1
                    temp_value = ""
                else:
                    left_x += 1
                start += 1
            elif left[start] == "-":
                temp_value = "-"
                start += 1
            elif left[start] == "+":
                start += 1
        return left_x, left_number
    
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        if not equation:
            return ""
        equation2 = equation.split("=")
        if len(equation2) != 2:
            return "Infinite solutions"
        left = equation2[0]
        right = equation2[1]
        left_x, left_number = self.compute(left)
        right_x, right_number = self.compute(right)
        
       
        #print(left_x, right_x, left_number, right_number)
        if left_x == right_x and left_number == right_number:
            return "Infinite solutions"
        elif left_x == right_x and left_number != right_number:
            return "No solution"
        else:
            value = (right_number - left_number) // (left_x - right_x)
            return "x={}".format(value)
        
