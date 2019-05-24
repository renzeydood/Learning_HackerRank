def input_time():
    ampm = input("Input time (Format = hh:mm:ssAM/PM): ")
    return ampm

def convert_time(ampm):
    hour = ''
    if(ampm[8:] == 'AM'):
        hour = int(ampm[:2])%12
        hour = str(hour).zfill(2)
    
    else:
        hour = (int(ampm[:2])%12) + 12

    return str(hour) + ampm[2:8]

if __name__ == "__main__":
    print("Result: ", convert_time(input_time()))
    