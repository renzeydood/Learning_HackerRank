from Helper import makearrays as ma

def plus_minus(arr):
    result = [0]*3
    sign = lambda elmt: elmt and (1, -1)[elmt < 0]

    for val in map(sign, arr):
        if val == 1:
            result[0] = result[0] + 1
        if val == -1:
            result[1] = result[1] + 1
        if val == 0:
            result[2] = result[2] + 1

    result = [round((x/len(arr)), 6) for x in result]

    print("{0:.6f}".format(result[0]))
    print("{0:.6f}".format(result[1]))
    print("{0:.6f}".format(result[2]))

    return result

if __name__ == "__main__":
    #arr = ma.array_1d()
    arr = [-4, 3, -9, 0, 4, 1]
    print("Result: ", plus_minus(arr))