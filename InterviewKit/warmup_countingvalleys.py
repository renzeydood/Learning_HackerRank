from Helper import makearrays as ma

def count_valleys(n, s):
    res = 0
    alt = 0

    for c in s:
        if(c == "D"):
            alt = alt - 1

        elif(c == "U"):
            alt = alt + 1

        if(alt == 0 and c == "U"):
            res = res + 1

    return res

if __name__ == "__main__":
    n = 8
    s = "UDDDUDUU"

    print("Result:", count_valleys(n, s))