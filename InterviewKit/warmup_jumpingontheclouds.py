from Helper import makearrays as ma

def cloud_jumps(c):
    res = 0
    jumpcount = 0;

    for i, x in enumerate(c):
        if(jumpcount == 0):
            if((i+2)<len(c) and c[i+2]!=1): #can jump more than once!
                jumpcount = 1
            
            res = res + 1
        
        else:
            jumpcount = jumpcount - 1
        
    return res-1

if __name__ == "__main__":
    #arr = ma.array_1d()
    arr = [0, 0, 1, 0, 0, 1, 0]
    
    print("Result:", cloud_jumps(arr))