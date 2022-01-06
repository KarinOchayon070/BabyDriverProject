import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import pickle

data = pd.read_csv("csvData.csv")


def getCompanyNames():
    car_company = data["carName"].str.split(" ", n=1, expand=True)
    data['carCompany'] = car_company[0]

    # Dropping 'CarName' column
    data.drop('carName', axis=1, inplace=True)
    cars = []
    for v in data['carCompany']:
        if (v[::-1]) not in cars:
            cars.append(v[::-1])


def factorize_columns():
    convert_to_numeric_columns = [
        "city",
        "fuel_type",
        "color",
        "carCompany"
    ]

    for column in convert_to_numeric_columns:
        factorize = pd.factorize(data[column])
        data[column] = factorize[0] + 1

        print(f"COLUMNS FOR ---------------- {column}")
        print("{")
        for index, item in enumerate(factorize[1]):
            print(f"'{item}':{index+1},")
        print("}")


getCompanyNames()
factorize_columns()
data = data[["carCompany", "year", "price",
             "city", "current_km", "hand", "next_test", "new_car_price", "color"]]

X = np.array(data.drop(['price'], 1))
y = np.array(data['price'])

best = 0

for _ in range(1):
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, y, test_size=0.2)

    linear = linear_model.LinearRegression()

    linear.fit(x_train, y_train)
    acc = linear.score(x_test, y_test)

    predictions = linear.predict(x_test)

    avragePredictionPrecentage = []

    for x in range(len(predictions)):
        prediction = ((predictions[x]) * 100) / y_test[x]
        if(prediction > 100):
            prediction = 200 - prediction

        avragePredictionPrecentage.append(prediction)
        round_to_tenths = [round(num) for num in x_test[x]]

        # print(f"Prediction: {np.absolute(round(predictions[x]))} items: {round_to_tenths}   True value: {y_test[x]}   Prediction accuracy: {prediction} "   )

    avrage = np.average(avragePredictionPrecentage)
    # print(f"Average prediction accuracy: {avrage}")

    if(avrage > best):
        best = avrage
        with open('bestModel.pickle', 'wb') as f:
            pickle.dump(linear, f)

print(f"Best model: {best}")
