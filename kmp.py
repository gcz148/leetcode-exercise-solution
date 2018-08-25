def simplematch(str1, str2):
    s1_length = len(str1)
    s2_length = len(str2)
    ret = []
    for i in range(s1_length):
        j = i
        k = 0
        while True:
            if k < s2_length and str1[j] == str2[k]:
                j += 1
                k += 1
            else:
                break
        if k == s2_length:
            ret.append(i)
    return ret

def kmpmatch(str1, str2):
    s1_length = len(str1)
    s2_length = len(str2)
    ret = []
    def calculate(strs):
        str_length = len(strs)
        nexts = [-1] * str_length
        j = -1
        for i in range(1, str_length):
            while j >= 0 and strs[j+1] != strs[i]:
                #print(nexts)
                j = nexts[j]
            if strs[j+1] == strs[i]:
                j += 1
            nexts[i] = j
        return nexts
    nexts = calculate(str2)
    print(nexts)
    j = -1
    for i in range(s1_length):
        while j >= 0 and str2[j+1] != str1[i]:
            j = nexts[j]
        if str2[j+1] == str1[i]:
            j = j + 1
        if j == s2_length - 1:
            ret.append(i-s2_length+1)
            j = nexts[j]
    
    return ret
        

if __name__ == "__main__":
    print(simplematch("aaaaaaaaaaaabaaaaaaaaaaaabaaaaaaaaaaaaaaaab", "aaaaaaaaaab"))
    print(kmpmatch("aaaaaaaaaaaabaaaaaaaaaaaabaaaaaaaaaaaaaaaab", "aaaaaaaaaab"))
    print(simplematch("abababaababacb", "ababacb"))
    print(kmpmatch("abababaababacb", "ababacb"))
