from Helper import makearrays as ma

def blow_num_candles(arr):
    res = 0
    maxNum = arr[0]

    for num in arr:
        if maxNum < num:
            maxNum = num
            res = 0

        if maxNum == num:
            res = res + 1

    return res

if __name__ == "__main__":
    arr = ma.array_1d()
    arr = [18, 90, 90, 13, 90, 75, 90, 8, 90, 43]

    print("Result:", blow_num_candles(arr))
