import math

def doStuff():
    numColors = input("Number of colors to mix: ")

    red = []
    green = []
    blue = []
    sumRed = 0
    sumGreen = 0
    sumBlue = 0

    for i in range(0, int(numColors)):
        red.append(int(input("Red" + str(i+1) + ":")))
        green.append(int(input("Green" + str(i+1) + ":")))
        blue.append(int(input("Blue" + str(i+1) + ":")))

    for i in range(0, len(numColors)):
        sumRed = red[i] + sumRed
        sumGreen = green[i] + sumGreen
        sumBlue = blue[i] + sumBlue
        
        
    outRed = math.ceil(sumRed/int(numColors))
    outGreen = math.ceil(sumGreen/int(numColors))
    outBlue = math.ceil(sumBlue/int(numColors))

    output = [outRed, outGreen, outBlue]


    print(output)


