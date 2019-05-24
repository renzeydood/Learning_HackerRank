from Helper import makearrays as ma

def compare(listA, listB):
    points = [0] * 2
    
    for a, b in zip(listA, listB):
        if(a > b):
            points[0] = points[0] + 1
        if(a < b):
            points[1] = points[1] + 1

    return points

if __name__ == "__main__":
    arrA = ma.array_1d()
    arrB = ma.array_1d()
    print("Result: ", compare(arrA, arrB))
    