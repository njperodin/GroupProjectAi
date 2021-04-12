##  Dylan Feuerman, JackToohey and Naylah Perodin
## Group Project
## 4/12/2021
## CS-484-01
## Simari

import numpy as np

def loadText(file):

    data = np.loadtxt(file, dtype=str, delimiter=";", skiprows=1, unpack=True)
    print(data[32])
    return data


def printShape(data):

    print(data.shape)


def main():

    data = loadText(r"C:\Users\dylan\PycharmProjects\GroupProjectAi\student\student-mat.csv")
    printShape(data)


main()
