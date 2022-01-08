import matplotlib
import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import seaborn as sns
from collections import Counter
from sklearn.decomposition import PCA
from scipy import stats
from edaConstants import col_numeric, col_strings
from scipy.stats import pearsonr
from matplotlib import pyplot as plt
import matplotlib as mpl


# ------------------------------------------------------------------------------------------------------------------- #

# paths
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(ROOT_PATH, "csvData.csv")
df = pd.read_csv(CSV_PATH)

# ------------------------------------------------------------------------------------------------------------------- #

# Function that split between the car company and the car model


def spilt_to_car_company_and_car_model():
    car_company = df["carName"].str.split(" ", n=1, expand=True)
    df['car_company'] = car_company[0]
    df.drop('carName', axis=1, inplace=True)
    cars = []
    for v in df['car_company']:
        if (v[::-1]) not in cars:
            cars.append(v[::-1])

# -------------------------------------------------------------------------------------------------------------------#

# Function that reverse string (because hebrew is right to left)


def reverse_strings_inside_eda():

    for col in col_strings:
        df[col] = df[col].map(lambda x: x[::-1])


# -------------------------------------------------------------------------------------------------------------------#

# Function that find outliers - using the IQR method

def find_outliers():

    df_copy = df.copy()
    for col in col_numeric:
        Q1 = np.percentile(df_copy[col], 25)
        Q3 = np.percentile(df_copy[col], 75)
        IQR = Q3-Q1
        df_copy.loc[(df_copy[col] < Q1 - 1.5 * IQR) |
                    (df_copy[col] > Q3 + 1.5 * IQR), col] = np.nan
    # We can see that there are (1639-1639)=0 records, which are outliers in the dataset.
    print(df_copy.shape)

# -------------------------------------------------------------------------------------------------------------------#
# EDA


# Listing categorical columns for checking data imbalance and plotting them

def list_categorical_cols():
    col_category = [
        'color',
        'head_light',
        'car_company',
    ]

    col_category1 = [
        'fuel_type',
        'city',
    ]

    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    for index, col in enumerate(col_category):
        plt.subplot(3, 1, index+1)
        df[col].value_counts().plot(kind='bar', color='pink',
                                    width=1, alpha=1)
        plt.subplots_adjust(hspace=1,)
        plt.title(col)

    for index, col in enumerate(col_category1):
        plt.subplot(2, 1, index+1)
        df[col].value_counts().plot(kind='bar', color='pink',
                                    width=1, alpha=1)
        plt.subplots_adjust(hspace=1,)
        plt.title(col)

# -------------------------------------------------------------------------------------------------------------------#
# Visualising the data to check the possiblity of linear regression model
# Visualising the numerical variables


def list_numerical_cols_for_linear_regression_model():

    linear_regression_model = ['price',
                               'new_car_price',
                               'avrage_fuel_consumption',
                               'horsepower',
                               'year',
                               'engine',
                               'current_km',
                               'original_ownership',
                               'hand',
                               'full_tank_volume_in_liters',
                               'next_test'
                               ]

    sns.set(font_scale=0.5)
    sns.pairplot(df[linear_regression_model], height=0.8, aspect=1.5)
# -------------------------------------------------------------------------------------------------------------------#


# -------------------------------------------------------------------------------------------------------------------#
# Visualising the categorical variables
# Boxplot for all categorical variables except car_company
# As X labels are not clearly visible for car_company. It is plotted in the next cell with bigger figure size.


def box_plot():
    col_category = [
        'head_light',
        'color',
    ]

    col_category1 = [
        'fuel_type',
        'city',
    ]

    mng = plt.get_current_fig_manager()
    # mng.window.style('zoomed')

    for index, col in enumerate(col_category):
        plt.subplot(2, 1, index+1)
        sns.boxplot(x=col, y='price', data=df)
        plt.subplots_adjust(bottom=.200)
    plt.xticks(rotation=90)

    for index, col in enumerate(col_category1):
        plt.subplot(2, 1, index+1)
        sns.boxplot(x=col, y='price', data=df)
        plt.subplots_adjust(bottom=.200)
    plt.xticks(rotation=90)

    plt.subplot(1, 1, 1)
    sns.boxplot(x="car_company", y='price', data=df)
    plt.subplots_adjust(bottom=.200)

    plt.xticks(rotation=90)
# -------------------------------------------------------------------------------------------------------------------#


# -------------------------------------------------------------------------------------------------------------------#


def create_crosstab():
    ct2 = pd.crosstab(df["year"], df["hand"], normalize="index")
    ct2.plot(kind="bar", figsize=(5, 2))
    plt.title("Year VS Hand")
    plt.xlabel("Year")
    plt.ylabel("Hand")


# -------------------------------------------------------------------------------------------------------------------#
# In this section we used - https://www.geeksforgeeks.org/python-pearson-correlation-test-between-two-variables/


#  Pearson Correlation Test Between Two Variables - year and hand
# Convert dataframe into series
list1 = df['year']
list2 = df['hand']
# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation (year and hand): %.3f' % corr)
# This code is contributed by Amiya Rout

plt.scatter(df['year'], df['hand'])
# -------------------------------------------------------------------------------------------------------------------#


def create_figure_pie():
    df["car_company"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", figsize=(7, 7), fontsize=7)
    plt.title("All Categories")

# -------------------------------------------------------------------------------------------------------------------#


def create_figure_pie_2():
    df["next_test"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", figsize=(10, 10), fontsize=5)
    plt.title("Next Test")

# -------------------------------------------------------------------------------------------------------------------#

# Listing categorical columns for checking data imbalance and plotting them


def one_dim_plot():
    col_category = ['fuel_type', 'car_company', 'color', 'city']
    k = 0
    plt.figure(figsize=(50, 30))
    for col in col_category:
        k = k+1
        plt.subplot(4, 3, k)
        df[col].value_counts().plot(
            kind='bar', color='#ff0066', width=1, alpha=1)
        plt.title(col)
# -------------------------------------------------------------------------------------------------------------------#


def main():

    spilt_to_car_company_and_car_model()
    reverse_strings_inside_eda()
    # create_figure_pie_2()
    # one_dim_plot()
    # find_outliers()
    # list_categorical_cols()
    # list_numerical_cols_for_linear_regression_model()
    # box_plot()
    # create_figure_pie()
    # create_crosstab()


main()
plt.show()
