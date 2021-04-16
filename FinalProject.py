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

#create DataFrame
def createDataFrame(file):
    
    data = pd.read_csv(file,delimiter=";")
    
    return data

def createXData(data):

    return data[TARGET]

def createYData(data):

    return data[:INPUT_DATA]

# retrieve the x and y data
def create_x_y(data):
    
    y = data["G3"]
    
    x = []
    for i in range(data.shape[0]):
        column_data =[]
        for column in data.columns:
            column_data.append(data[str(column)][i])

        x.append(column_data)
        
    return x, y

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

# create the training and testing data for x and y
def create_train_test_data(x, y):
    
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=3)
    
    return X_train, X_test, y_train, y_test

def main():

    data = loadText("student\student-mat.csv")

    Y = createYData(data)
    X = createYData(data)
    
    
    X_train, X_test, y_train, y_test = Training_Data(X, Y)
   
    list_csv = CSV_to_list("student\student-mat.csv")
    
    # create dataframe
    file_data = createDataFrame("student\student-mat.csv")
    
    # retrieve the x and y data
    x, y = create_x_y(file_data)
    
    # create the training and testing data for x and y
    X_train, X_test, y_train, y_test = create_train_test_data(x, y)
    print(X_train, X_test, y_train, y_test)


main()
