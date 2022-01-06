import numpy as np
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from constants import RELEVANT_PROPERTIES_FOR_MODEL
from sklearn.ensemble import RandomForestRegressor
import csv
import pickle

# In this section we were helped by the following link:
# https://www.analyticsvidhya.com/blog/2021/05/build-and-deploy-a-car-price-prediction-system/
# https://www.youtube.com/watch?v=45ryDIPHdGg&ab_channel=TechWithTim


# Function that creates a dictionary with car model as key and number as value (for example: 'קאדילאק XT5 LUXURY': 365) - this is used for the model
def create_car_model_to_number_dict():
    CAR_MODEL_COLUMN_INDEX = 70
    CAR_MODEL_TO_NUMBER = {}
    current_index = 0
    with open("./csvData.csv", newline="", encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if spamreader.line_num == 1:
                continue
            car_model = row[CAR_MODEL_COLUMN_INDEX]
            if car_model not in CAR_MODEL_TO_NUMBER:
                CAR_MODEL_TO_NUMBER[car_model] = current_index
                current_index += 1
    return CAR_MODEL_TO_NUMBER

# Function that creates a dictionary with color as key and number as value (for example: 'ירוק': 22) - this is used for the model


def create_color_to_number_dict():
    CAR_COLOR_COLUMN_INDEX = 75
    CAR_COLOR_TO_NUMBER = {}
    current_index = 0
    with open('./csvData.csv', newline="", encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if spamreader.line_num == 1:
                continue
            color = row[CAR_COLOR_COLUMN_INDEX]
            if color not in CAR_COLOR_TO_NUMBER:
                CAR_COLOR_TO_NUMBER[color] = current_index
                current_index += 1
    return CAR_COLOR_TO_NUMBER

 # Function that creates a dictionary with city as key and number as value (for example: 'קרית שמונה': 0) - this is used for the model


def create_city_to_number_dict():
    CITY_COLUMN_INDEX = 1
    CITY_TO_NUMBER = {}
    current_index = 0
    with open('./csvData.csv', newline="", encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if spamreader.line_num == 1:
                continue
            city = row[CITY_COLUMN_INDEX]
            if city not in CITY_TO_NUMBER:
                CITY_TO_NUMBER[city] = current_index
                current_index += 1
    return CITY_TO_NUMBER

# Function that returns a list of car models that are relevant for the model (dont foreget we have 130,000 datapoints so its not a big deal)


def get_valid_car_models(min_num_of_car_company):
    car_models_count = {}
    CAR_MODEL_COULMN_INDEX_IN_CSV = 70
    with open('./csvData.csv', 'r', encoding="utf8") as infile:
        reader = csv.reader(infile)
        first_row = True
        for row in reader:
            if first_row:
                first_row = False
                continue
            car_model = row[CAR_MODEL_COULMN_INDEX_IN_CSV]
            if car_model not in car_models_count:
                car_models_count[car_model] = 1
            else:
                car_models_count[car_model] += 1
    valid_car_models = []
    # Checking the total count to extract only those which above the treshold
    for car_model, car_model_count in car_models_count.items():
        if car_model_count >= min_num_of_car_company:
            valid_car_models.append(car_model)
    return valid_car_models

# Function that updates the dataframe with the relevant properties (rewrite)


def fix_csv_hebrew_data(min_num_of_car_company=2):
    import csv
    car_model_to_number = create_car_model_to_number_dict()
    car_color_to_number = create_color_to_number_dict()
    car_city_to_number = create_city_to_number_dict()
    CAR_MODEL_COLUMN_INDEX = 70
    CAR_COLOR_COLUMN_INDEX = 75
    CITY_COLUMN_INDEX = 1
    first_row = True
    valid_company_car_models = get_valid_car_models(
        min_num_of_car_company=min_num_of_car_company)
    with open('./csvData.csv', 'r', encoding="utf8") as infile, open('./fixedDataTest.csv', 'w', encoding="utf8") as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            if first_row:
                first_row = False
                writer.writerow(row)
                continue
            if row[CAR_MODEL_COLUMN_INDEX] not in valid_company_car_models:
                continue
            # Replace car model value
            row[CAR_MODEL_COLUMN_INDEX] = str(
                car_model_to_number[row[CAR_MODEL_COLUMN_INDEX]])
            # Replace car city value
            row[CITY_COLUMN_INDEX] = str(
                car_city_to_number[row[CITY_COLUMN_INDEX]])
            # Replace car color value
            row[CAR_COLOR_COLUMN_INDEX] = str(
                car_color_to_number[row[CAR_COLOR_COLUMN_INDEX]])
            writer.writerow(row)

# This function is for the UI section (babyDriverUi.py) - return dict of cars by company - {company: [car_model1, car_model2, ...]}


def create_car_types_by_company():
    CAR_MODEL_COLUMN_INDEX = 70
    CAR_COMPANY_TO_TYPES = {}
    valid_company_cars = get_valid_car_models(min_num_of_car_company=2)
    with open('./csvData.csv', newline="", encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if spamreader.line_num == 1:
                continue
            car_model = row[CAR_MODEL_COLUMN_INDEX]
            if car_model not in valid_company_cars:
                continue
            car_company_name = car_model.split()[0]
            if car_company_name not in CAR_COMPANY_TO_TYPES:
                CAR_COMPANY_TO_TYPES[car_company_name] = [car_model]
            elif car_model not in CAR_COMPANY_TO_TYPES[car_company_name]:
                CAR_COMPANY_TO_TYPES[car_company_name].append(car_model)
    print(CAR_COMPANY_TO_TYPES)
    return CAR_COMPANY_TO_TYPES


# The main function that creates the model - train and test (according - 80% train, 20% test).
# In this section we used a lot of the Internet (links mentioned above)

def train_model():
    cars_data = pd.read_csv('./fixedDataTest.csv')
    for col in cars_data.columns:
        if col not in RELEVANT_PROPERTIES_FOR_MODEL:
            cars_data = cars_data.drop([col], axis=1)

    cars_data = pd.get_dummies(cars_data, drop_first=True)
    cars_data = cars_data[['price', 'city', 'gearbox', 'carName', 'year', 'engine', 'current_km', 'hand', 'color',
                           'original_ownership', 'next_test', 'annual_licensing_fee']]
    print("Columns")
    print(cars_data.columns)

    print(cars_data.corr())

    x = cars_data.iloc[:, 1:]
    y = cars_data.iloc[:, 0]

    # Finding out feature importance to eliminate unwanted features
    from sklearn.ensemble import ExtraTreesRegressor
    model = ExtraTreesRegressor()
    model.fit(x, y)

    print("Features Importances")
    print(model.feature_importances_)

    print("Hyperparameter Optimization")
    n_estimators = [int(x) for x in np.linspace(start=100, stop=1200, num=12)]
    max_features = ['auto', 'sqrt']
    max_depth = [int(x) for x in np.linspace(5, 30, num=6)]
    min_samples_split = [2, 5, 10, 15, 100]
    min_samples_leaf = [1, 2, 5, 10]
    grid = {'n_estimators': n_estimators,
            'max_features': max_features,
            'max_depth': max_depth,
            'min_samples_split': min_samples_split,
            'min_samples_leaf': min_samples_leaf}
    print(grid)

    print("Train Test Split")
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, random_state=0, test_size=0.2)

    print("Training the Model")
    from sklearn.ensemble import RandomForestRegressor
    model = RandomForestRegressor()
    hyp = RandomizedSearchCV(estimator=model,
                             param_distributions=grid,
                             n_iter=10,
                             scoring='neg_mean_squared_error',
                             cv=5, verbose=2,
                             random_state=42, n_jobs=1)
    print("Training...")
    hyp.fit(x_train, y_train)

    print("Predicting test data on model")
    y_pred = hyp.predict(x_test)
    print(y_pred)
    r2_result = r2_score(y_test, y_pred)
    print(f"Model R2 score: {r2_result}")
    # We can also use this MSE (Mean Squared Error), RMSE (Root Mean Squared Error) to check the trained model
    print("Saving the model into file")
    # opening a new file in write mode
    file = open("fileNew.pkl", "wb")
    pickle.dump(hyp, file)  # dumping created model into a pickle file


# Let's use the model we trained!
def predict_with_model(car_name, year, engine, current_km, hand, gearbox, color, original_ownership,
                       next_test, annual_licensing_fee, city):
    car_model_to_number = create_car_model_to_number_dict()
    car_color_to_number = create_color_to_number_dict()
    car_city_to_number = create_city_to_number_dict()
    fixed_car_name = car_model_to_number[car_name]
    fixed_color_name = car_color_to_number[color]
    fixed_city_name = car_city_to_number[city]
    model = pickle.load(open("./fileNew.pkl", "rb"))
    prediction = model.predict([[fixed_city_name, gearbox, fixed_car_name, year, engine, current_km,
                               hand, fixed_color_name,
                               original_ownership, next_test, annual_licensing_fee]])
    prediction_result = round(prediction[0], 2)
    print(f"The prediction is: {prediction_result}")


if __name__ == '__main__':
    # fix_csv_hebrew_data()
    train_model()  # Run this function only when you want to retrain the model
    # create_car_types_by_company()  # This is a function for the UI (as explained above)
    result = predict_with_model(city='קרית שמונה', gearbox=1, car_name='טויוטה קורולה SUN', year=2002, engine=1598,
                                current_km=140000, hand=3, color='שחור מטלי', original_ownership=2, next_test=1, annual_licensing_fee=1424)
