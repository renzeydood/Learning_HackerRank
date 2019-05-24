from Helper import makearrays as ma

def diag_diff(arr):
    sumltr = 0
    sumrtl = 0

    for i in range(len(arr)):
        sumltr = sumltr + arr[i][i]

    rightInd = len(arr)-1
    for i in range(len(arr)):
        sumrtl = sumrtl + arr[i][rightInd]
        rightInd = rightInd - 1
    
    print(sumltr)
    print(sumrtl)
    return abs(sumltr - sumrtl)

if __name__ == "__main__":
    arr = [[1,2,3], [3,2,1], [3,3,3]]
    #arr = ma.array_sq()

    print(str(arr).replace('],', '],\n'))
    print(diag_diff(arr))