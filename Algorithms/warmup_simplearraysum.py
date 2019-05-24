'''
Notes: Python automatically promote the type of variable depending on size
'''

from Helper import makearrays as ma

def count(arr):
    sumVal = arr[0]
    
    for i, num in enumerate(arr[1:]):
        sumVal = sumVal + num

    return sumVal

if __name__ == "__main__":
    print("Result: ", count(ma.array_1d()))
