'''
Helper functions to make arrays from user inputs
'''

def array_1d():
    arr = []
    size = int(input("Size of Array: "))
    
    for i in range(size):
        arr.append(int(input("Value at {0}: ".format(i))))
    
    print("Size: {0}, Array: {1}".format(size, arr))
    
    return arr

def array_sq():
    arr = []
    size = int(input("Size of Square Matrix: "))
    
    for outer in range(size):
        arrIn = []

        for inner in range(size):
            arrIn.append(int(input("Value at [{0}][{1}]: ".format(outer, inner))))

        arr.append(arrIn)
    
    print("Size: {0}, Array: {1}".format(size, arr))
    return arr