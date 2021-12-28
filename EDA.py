import matplotlib.pylab as plt
import pandas as pd
import numpy as np
import os
import matplotlib as mpl
import matplotlib.pyplot as plt
import math
import seaborn as sns
from collections import Counter
from sklearn.decomposition import PCA
from scipy import stats

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(ROOT_PATH, "csvData.csv")


def load_csv():
    df = pd.read_csv(CSV_PATH)
    # print(df.head())
    return df

# Most frequent elements - One dimensional visualization
# In this section we perform a visualization of the most frequent values, for given columns.
# our steps:
# 1. Acquire most frequent elements
# 2. Plot one dimensional plots
# 3. Combine these two parts to plot one dimensional visualization of most frequent elements


def get_frequent_elements(df, col_name, num_top_elements):
    return df[col_name].astype('str').value_counts().sort_values(ascending=False).head(num_top_elements).iloc[::-1]


def one_dim_plot(sr, plot_type, axis):
    return sr.plot(kind=plot_type, ax=axis)


def plot_frequent_elements(df, df_in_params):
    fix, axes = plt.subplots(1, 3, figsize=(20, 5))
    index = 0
    for plot_type, col_name, num_top_elements in df_in_params.values:
        sr = get_frequent_elements(df, col_name, num_top_elements)
        one_dim_plot(sr, plot_type, axes[index])
        index += 1


df = load_csv()


# SPLIT TO CAR COMPANY AND CAR NAME
# car_company = df["carName"].str.split(" ", n=1, expand=True)
# df['carCompany'] = car_company[0]
# # Dropping 'CarName' column
# df.drop('carName', axis=1, inplace=True)
# cars = []
# for v in df['carCompany']:
#     if (v[::-1]) not in cars:
#         cars.append(v[::-1])
# print(cars)
# print(len(cars))


# Finding outliers in all the numerical columns with 1.5 IQR rule and removing the outlier records
col_numeric = ['price',
               'tire_width',
               'height_ratio',
               'wheel_diameter',
               'new_car_price',
               'number_of_doors',
               'number_of_seats',
               'avrage_fuel_consumption',
               'avrage_fuel_consumption_city',
               'horsepower',
               'max_speed',
               'max_torque',
               'number_of_cylinders',
               'number_of_gears',
               'rounds_per_minute_for_max_power',
               'rounds_per_minute_for_max_torque',
               'avrage_fuel_consumption_highway',
               'zero_to_100_km_in_seconds',
               'number_of_airbags',
               'trunk_volume_in_liters',
               'trunk_volume_in_seat_folding',
               'front_seat_headroom_in_cm',
               'rear_seat_headroom_in_cm',
               'height_in_cm',
               'front_seat_waist_in_cm',
               'rear_seat_waist_in_cm',
               'front_legroom_in_cm',
               'rear_legroom_in_cm',
               'length_in_cm',
               'front_seat_shoulder_in_cm',
               'rear_seat_shoulder_in_cm',
               'width_in_cm',
               'full_tank_volume_in_liters',
               'minimal_weight_in_kg',
               'maximal_weight_in_kg',
               'wheelbase_in_cm',
               'number_of_air_conditioning_locations',
               'hoops',
               'year',
               'engine',
               'current_km',
               'hand',
               'original_ownership',
               'next_test',
               'annual_licensing_fee']

# OUTLIER DETECTION USING IQR


def outlier_detection_iqr(df):
    df_copy = df.copy()
    for col in col_numeric:
        Q1 = np.percentile(df_copy[col], 25)
        Q3 = np.percentile(df_copy[col], 75)
        IQR = Q3-Q1
        df_copy.loc[(df_copy[col] < Q1 - 1.5 * IQR) |
                    (df_copy[col] > Q3 + 1.5 * IQR), col] = np.nan
    return df_copy


df_outlier_rem = outlier_detection_iqr(df)
# print(df_outlier_rem.shape)
# We can see that there are (1639-1639)=0 records, which are outliers in the dataset.


# Listing categorical columns for checking data imbalance and plotting them
# k = 0
# plt.figure(figsize=(20, 25))
# for col in col_numeric:
#     k = k+1
#     plt.subplot(1, 2, k)
#     df[col].value_counts().plot(kind='bar')
#     plt.title(col)


# # Listing categorical columns for checking data imbalance and plotting them
# col_category = ['city', 'tire_type', 'finish_level',
#                 'fuel_type', 'head_light', 'carName', 'color']
# k = 0
# plt.figure(figsize=(50, 30))
# for col in col_category:
#     k = k+1
#     plt.subplot(4, 3, k)
#     df[col].value_counts().plot(kind='bar')
#     plt.title(col)


sr = get_frequent_elements(df, "next_test", 5)
fig, axes = plt.subplots(1, 2, figsize=(15, 10))
one_dim_plot(sr, 'pie', axes[1])
one_dim_plot(sr, 'bar', axes[0])


# %%
# %%
plt.figure()
plt.plot(np.sin(np.linspace(-np.pi, np.pi, 1001)))
plt.show()
# df.carName.unique()
# print(len(df.carName.unique()))
