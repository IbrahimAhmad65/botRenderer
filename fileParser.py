import os

# parse a file located in /home/ibrahim/arm.txt into a 2D array where each line is a new subarray, and all the elements in the sub array are comma seperated

def parseArmCoors(fileName, headers):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()

    hds = []
    output = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(",")

        if i == 0: 
            for j in range(len(headers)):
                for k in range(len(lines[0])):
                    if headers[j] == lines[0][k]:
                        hds.append(k)
        else:
            if len(lines[i]) > hds[len(hds) - 1]:
                tmp = []

                for j in range(len(headers)):
                    tmp.append(float(lines[i][hds[j]]))
                output.append(tmp)

    return output