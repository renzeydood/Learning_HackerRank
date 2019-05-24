def staircase(hght):
    for stair in range(hght):
        print(" "*(hght-stair-1) + "#"*(stair+1))


if __name__ == "__main__":
    hght = int(input("Height of staircase: "))
    staircase(hght)