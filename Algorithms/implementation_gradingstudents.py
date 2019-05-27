from Helper import makearrays as ma

'''
<40 always fail, no need to round
>40, round up if multiple of 5 is more than 3
n = number of students
rounded grades printed on new line

'''

def round_grades(grades):
    res = []

    for i, g in enumerate(grades):
        if (g > 35):
            diff = g%5
            
            if (diff > 2):
                g = g + (5-diff)
                res.append(g)
        
            else:
                res.append(g)

        else:
            res.append(g)

    return res



if __name__ == "__main__":
    #arr = ma.array_1d()
    arr = [73, 67, 38, 33]

    print(round_grades(arr))