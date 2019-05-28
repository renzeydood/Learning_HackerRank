from Helper import makearrays as ma

def num_of_sockpairs(n, arr):
    res = 0
    arr.sort()
    currentSock = arr[0]
    numSock = 0

    for i, val in enumerate(arr):
        if (currentSock == val):
            numSock = numSock + 1
        else:
            res = res + int(numSock/2)
            numSock = 1
        if (i == n-1):
            res = res + int(numSock/2)
        currentSock = val
    return res

if __name__ == "__main__":
    #n = int(input("Number of socks (n): "))
    #arr = list(ma.num_pair("Socks list (len n): "))[:n]
    
    #n = 9
    #arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    #[10, 10, 10, 10, 20, 20, 20, 30, 50]

    #n = 10
    #arr = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]
    #[1, 1, 1, 1, 2, 3, 3, 3, 3, 3]

    n = 15
    arr = [6, 5, 2, 3, 5, 2, 2, 1, 1, 5, 1, 3, 3, 3, 5]

    print(num_of_sockpairs(n, arr))
