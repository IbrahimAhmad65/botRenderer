import os


# parse a file located in /home/ibrahim/arm.txt into a 2D array where each line is a new subarray, and all the elements in the sub array are comma seperated

def parseArmCoors(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    output = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(",")
        if len(lines[i]) > 2:
            output.append([float(lines[i][0]), float(lines[i][1])])

    return output


def parseWristAngles(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    output = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(",")
        if len(lines[i]) > 3:
            output.append(float(lines[i][2]))

    return output

def parseClawState(fileName):
    file = open(fileName, "r")
    lines = file.readlines()
    file.close()
    output = []
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
        lines[i] = lines[i].split(",")
        if len(lines[i]) > 4:
            output.append((lines[i][3]))

    return output