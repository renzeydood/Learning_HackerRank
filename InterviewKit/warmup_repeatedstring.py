'''
Or use //, it is division with floor of result (int)
'''

import math as m

def repeat_string(s, n):
    srmv = (m.ceil(n / len(s)) * len(s)) - n    #Gets the number of extra strings
    res = (s.count("a") * int(n / len(s))) + s[:-srmv].count("a")
    return res

if __name__ == "__main__":
    #s = input("String: ")
    #n = int(input("Length: "))
    s = "aba"
    n = 10

    print("Result:", repeat_string(s, n))