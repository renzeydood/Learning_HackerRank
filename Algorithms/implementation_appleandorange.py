from Helper import makearrays as ma

def count_apples_and_oranges(s, t, a, b, apples, oranges):
    appleHit = 0
    orangeHit = 0
    
    for i, apl in enumerate(apples):
        if(s <= a+apl <= t):
            appleHit = appleHit + 1
    
    for i, org in enumerate(oranges):
        if(s <= b+org <= t):
            orangeHit = orangeHit + 1

    print(str(appleHit) + "\n" + str(orangeHit))

if __name__ == "__main__":
    s, t = ma.num_pair("House location (s, t):")
    a, b = ma.num_pair("Trees location (a, b):")
    m, n = ma.num_pair("Number of apples and oranges (m, n):")
    apples = list(ma.num_pair("Apples (len m): "))[:m]
    oranges = list(ma.num_pair("Oranges (len n): "))[:n]
    count_apples_and_oranges(s, t, a, b, apples, oranges)
