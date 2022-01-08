# This is the relevent UI for our project

from io import DEFAULT_BUFFER_SIZE
from math import log
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pickle
import numpy as np
from PIL import ImageTk, Image
from machineLearningFinal import create_car_model_to_number_dict, create_city_to_number_dict, create_color_to_number_dict, get_valid_car_models, create_car_types_by_company
import csv


# Manual settigns of some of the parameters
gearbox = {
    'ידני': 0,
    'אוטומטי': 1
}

original_ownership = {
    'ליסינג': 0,
    'פרטי': 1,
    'השכרה': 2,
    'חברה': 3,
    'מונית': 4,
    'ייבוא אישי': 5
}


# Function that split between cars company and cars model
def split_cars_by_company(cars_to_split):
    CAR_COMPANY_TO_TYPES = create_car_types_by_company()
    cars_by_company = {}
    for car_company in CAR_COMPANY_TO_TYPES:
        cars_by_company[car_company] = []
        for car_model in CAR_COMPANY_TO_TYPES[car_company]:
            if car_model in cars_to_split:
                cars_by_company[car_company].append(car_model)
    return cars_by_company


# Define a class for the main window
class CarBabyUI:

    # Initialize the main window (size, title, etc.)
    def __init__(self, window):
        self.window = window
        self.window.title(
            "WOW --- Karin & Dor amazing project --- WOW")
        self.window.geometry("450x700")
        self.cars = create_car_model_to_number_dict()
        self.colors = create_color_to_number_dict()
        self.cities = create_city_to_number_dict()
        self.carsByCompany = split_cars_by_company(self.cars)
        self.load_model()
        self.layout()

    # Load the model from the pickle file
    def load_model(self):
        self.linear = pickle.load(open("fileNew.pkl", "rb"))

    # All the layout of the main window (car company, car model, etc.)
    def layout(self):
        self.carCompany = self.create_combobox(
            "Car Company", list(self.carsByCompany.keys()))

        self.carModel = self.create_combobox(
            "Car Model", list(self.cars.keys()))
        # Brings the list of models of a specific company
        self.carCompany.bind("<<ComboboxSelected>>",
                             self.on_car_comapny_change)

        self.city = self.create_combobox("City", list(self.cities.keys()))
        self.color = self.create_combobox("Color", list(self.colors.keys()))
        self.gearbox = self.create_combobox("Gearbox", list(gearbox.keys()))
        self.original_ownership = self.create_combobox(
            "Original Ownership", list(original_ownership.keys()))
        self.year = self.create_input("Year")
        self.current_km = self.create_input("Current Km")
        self.hand = self.create_input("Hand")
        self.next_test = self.create_input("Next Test")
        self.engine = self.create_input("Engine")
        self.annual_licensing_fee = self.create_input("Annual Licensing Fee")
        self.create_button("Predict price", self.predict_price)
        self.create_button("Auto Fill", self.auto_fill_form)
        self.clear_button = self.create_button(
            "Clear", self.clear_text)
        self.predicted_price_label = self.create_label()

    # Create a label
    def create_label(self, text=""):
        label = tk.Label(self.window, text=text, font=("Arial", 10))
        label.pack()
        return label

    # Create input - notice that "create_label" is called before "create_input" (for input we need to know the label)
    def create_input(self, text):
        self.create_label(text)
        input = tk.Entry(self.window, bg="white", font=("Arial", 10))
        input.pack()
        return input

    # Create combobox - notice that "create_label" is called before "create_combobox" (for combobox we need to know the label)
    def create_combobox(self, text, options):
        self.create_label(text)
        variable = tk.StringVar()
        selector = ttk.Combobox(self.window, textvariable=variable, values=options, font=(
            "Arial", 10), background="white")
        selector.configure(background="white")
        selector.pack()
        return selector

    # Create button
    def create_button(self, text, command):
        button = tk.Button(self.window, text=text, command=command,
                           font=("Arial", 10), width=12, bg="#ff0066")
        button.pack(pady=10)
        return button

    # Auto fill option - to save us some time (random) :)
    def auto_fill_form(self):

        self.carCompany.set(random.choice(
            list(self.carsByCompany.keys())))
        self.carModel.set(random.choice(
            list(self.carsByCompany[self.carCompany.get()])))
        self.carCompany.bind("<<ComboboxSelected>>",
                             self.on_car_comapny_change)
        self.city.set(random.choice(list(self.cities.keys())))
        self.color.set(random.choice(list(self.colors.keys())))
        self.gearbox.set(random.choice(list(gearbox.keys())))
        self.original_ownership.set(
            random.choice(list(original_ownership.keys())))
        self.year.delete(0, tk.END)
        self.year.insert(0, random.randint(2010, 2021))
        self.current_km.delete(0, tk.END)
        self.current_km.insert(0, random.randint(0, 200000))
        self.hand.delete(0, tk.END)
        self.hand.insert(0, random.randint(0, 7))
        self.next_test.delete(0, tk.END)
        self.next_test.insert(0, random.randint(0, 36))
        self.engine.delete(0, tk.END)
        self.engine.insert(0, random.randint(900, 3000))
        self.annual_licensing_fee.delete(0, tk.END)
        self.annual_licensing_fee.insert(0, random.randint(700, 4000))

    # Conditioning the cars models acording to the car company
    def on_car_comapny_change(self, _event):
        cars_models = self.carsByCompany[self.carCompany.get()]
        self.carModel.configure(values=cars_models)

    # Predict price - the magic happens here

    def predict_price(self):
        predicted_data = np.array([[
            int(self.cities[self.city.get()]),
            int(gearbox[self.gearbox.get()]),
            int(self.cars[self.carModel.get()]),
            int(self.year.get()),
            int(self.engine.get()),
            int(self.current_km.get()),
            int(self.hand.get()),
            int(self.colors[self.color.get()]),
            int(original_ownership[self.original_ownership.get()]),
            int(self.next_test.get()),
            int(self.annual_licensing_fee.get())
        ]])
        prediction = self.linear.predict(predicted_data)
        self.predicted_price_label.config(
            text=f"Predicted price: {prediction[0]}")

    # Clear the form - for the "clear" button
    def clear_text(self):
        self.carCompany.delete(0, tk.END)
        self.carModel.delete(0, tk.END)
        self.city.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.gearbox.delete(0, tk.END)
        self.original_ownership.delete(0, tk.END)
        self.year.delete(0, tk.END)
        self.current_km.delete(0, tk.END)
        self.hand.delete(0, tk.END)
        self.next_test.delete(0, tk.END)
        # self.new_car_price.delete(0, tk.END)
        self.engine.delete(0, tk.END)
        self.annual_licensing_fee.delete(0, tk.END)


# Call this baby!
window = tk.Tk()
carBabyUI = CarBabyUI(window)
window.mainloop()
