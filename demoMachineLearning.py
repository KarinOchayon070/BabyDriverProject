import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model

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
        data[column] = pd.factorize(data[column])[0] + 1


getCompanyNames()
factorize_columns()
data = data[["carCompany", "year", "price",
             "color", "city", "current_km", "hand", "next_test", "horsepower", "new_car_price"]]

X = np.array(data.drop(['price'], 1))
y = np.array(data['price'])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
    X, y, test_size=0.2)

linear = linear_model.LinearRegression()

linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)


predictions = linear.predict(x_test)
for x in range(50):
    print(f"trueValue: {round(predictions[x])}   predicted: {y_test[x]}")
