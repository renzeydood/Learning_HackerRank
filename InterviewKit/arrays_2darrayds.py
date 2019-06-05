'''
- square array of 6 by 6
- there are 16 hourglass combinations inside
- traverse by sliding (sliding window?)
- find maximum sum of hourglass
'''

from Helper import makearrays as ma
import math as m

def max_sum_inglass(arr):
    res = -float("inf")

    for y in range(len(arr) - 2):
        for x in range(len(arr[0]) - 2):
            tempSum = sum_inglass(arr, x, y)
            print(tempSum)
            if(tempSum > res):
                res = tempSum
    
    return res

    '''
    Resulting sum:
    7, 4, 2, 0
    4, 8, 10, 8
    3, 6, 7, 6
    3, 9, 19, 16
    '''

def sum_inglass(arr, arrX, arrY):
    hgArr = [[1, 1, 1,], [0, 1, 0], [1, 1, 1]]
    tempSum = 0

    for y in range(len(hgArr)):   #Main array (y axis)
        for x in range(len(hgArr)):
            tempSum = tempSum + hgArr[y][x]*arr[y+arrY][x+arrX]

    return tempSum

if __name__ == "__main__":
    #arr = ma.array_sq(6)
    arr =  [[1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]

    print("Result:", max_sum_inglass(arr))