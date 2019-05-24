'''
Without using Python's min(), max() functions, the created function is of O(n), since the loop only runs n times
'''

from Helper import makearrays as ma

def minimaxsum(arr):
    res = 0
    maxNum, minNum = arr[0], arr[0]
    
    for num in arr:
        res = res + num
        
        if maxNum < num:
            maxNum = num

        if minNum > num:
            minNum = num

    return (str((res-maxNum)) + " " + str((res-minNum)))

if __name__ == "__main__":
    arr = ma.array_1d()
    #arr = [5, 2, 4, 8, 10]

    print("Result: ", minimaxsum(arr))