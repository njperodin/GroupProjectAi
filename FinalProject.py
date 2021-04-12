import numpy as np


def loadText(file):

    data = np.loadtxt(file, dtype=str, delimiter=";", skiprows=1)
    print(data.shape)










def main():

    loadText(r"C:\Users\dylan\PycharmProjects\GroupProjectAi\student\student-mat.csv")


main()