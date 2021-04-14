##  Dylan Feuerman, JackToohey and Naylah Perodin
## Group Project
## 4/12/2021
## CS-484-01
## Simari

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

TARGET = 32
INPUT_DATA = 29
HEADER = 1
TEST_SIZE = 0.25


def loadText(file):

    data = np.loadtxt(file, dtype=str, delimiter=";", skiprows=1, unpack=True)

    return data


def createXData(data):

    return data[TARGET]


def createYData(data):

    return data[:INPUT_DATA]


def printShape(data):

    print(data.shape)


def CSV_to_list(file):

    data_frame = pd.read_csv(file, sep=';', )
    data_list = data_frame.values.tolist()
    data_list = data_list[HEADER:]

    return data_list


def Training_Data(X, Y):

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=TEST_SIZE, random_state=42)

    return X_train, X_test, y_train, y_test


def main():

    data = loadText("student\student-mat.csv")

    Y = createYData(data)
    X = createYData(data)

    X_train, X_test, y_train, y_test = Training_Data(X, Y)

    list_csv = CSV_to_list("student\student-mat.csv")


main()
