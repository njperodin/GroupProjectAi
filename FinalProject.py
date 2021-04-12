##

import numpy as np

def loadText(file):

    data = np.loadtxt(file, dtype=str, delimiter=";", skiprows=1)
    return data


def printShape(data):

    print(data.shape)


def main():

    data = loadText(r"C:\Users\dylan\PycharmProjects\GroupProjectAi\student\student-mat.csv")
    printShape(data)


main()
