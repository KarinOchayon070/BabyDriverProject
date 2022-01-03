from io import DEFAULT_BUFFER_SIZE
import random
from tkinter import *
import tkinter as tk
from tkinter import ttk
import pickle
import numpy as np


cities = {
    "קרית שמונה": 1,
    "אשקלון": 2,
    "ראשון לציון": 3,
    "בית שמש": 4,
    "בת ים": 5,
    "טבריה": 6,
    "אבן יהודה": 7,
    "ירכא": 8,
    "תל אביב יפו": 9,
    "פתח תקווה": 10,
    "עפולה": 11,
    "חיפה": 12,
    "נתניה": 13,
    "באר שבע": 14,
    "חצור הגלילית": 15,
    "כפר יונה": 16,
    "חולון": 17,
    "פרדס חנה כרכור": 18,
    "עיספיא": 19,
    "אזור": 20,
    "רמת גן": 21,
    "טמרה": 22,
    "קדימה צורן": 23,
    "חדרה": 24,
    "אשדוד": 25,
    "מחניים": 26,
    "רחובות": 27,
    "באקה אל-ע'רביה": 28,
    "טירת כרמל": 29,
    "כרמיאל": 30,
    "רמת השרון": 31,
    "מודיעין מכבים רעות": 32,
    "כפר סבא": 33,
    "אעבלין": 34,
    "באר טוביה": 35,
    "צפת": 36,
    "משהד": 37,
    "שדרות": 38,
    "ירושלים": 39,
    "סח'נין": 40,
    "רמלה": 41,
    "לוד": 42,
    "מעיליא": 43,
    "תל אביב-יפו": 44,
    "עראבה": 45,
    "בוקעאתא": 46,
    "אור יהודה": 47,
    "דאלית אל-כרמל": 48,
    "קרית אתא": 49,
    "גן יבנה": 50,
    "הרצליה": 51,
    "הוד השרון": 52,
    "נתיבות": 53,
    "אור עקיבא": 54,
    "נצרת": 55,
    "טירה": 56,
    "טורעאן": 57,
}

carCompanies = {
    "טויוטה": 1,
    "רנו": 2,
    "מאזדה": 3,
    "קיה": 4,
    "יונדאי": 5,
    "ניסאן": 6,
    "הונדה": 7,
    "מרצדס": 8,
    "סיאט": 9,
    "ב.מ.וו": 10,
    "סובארו": 11,
    "סקודה": 12,
    "אאודי": 13,
    "מיצובישי": 14,
    "פיג'ו": 15,
    "פולקסווגן": 16,
    "שברולט": 17,
    "ג'יפ": 18,
    "פורד": 19,
    "סוזוקי": 20,
    "פיאט": 21,
    "אופל": 22,
    "איסוזו": 23,
    "דאצ'יה": 24,
    "סיטרואן": 25,
    "ביואיק": 26,
    "אינפיניטי": 27,
    "לנד": 28,
    "קאדילאק": 29,
    "אלפא": 30,
    "מיני": 31,
}

color = {
    "שחור מטלי": 1,
    "לבן": 2,
    "כסוף בהיר": 3,
    "כסוף כהה": 4,
    "כסוף כהה מטלי": 5,
    "שחור פנינה": 6,
    "שחור": 7,
    "אפור": 8,
    "אפור כהה מטלי": 9,
    "אפור מטל": 10,
    "בורדו מטל": 11,
    "אפור כחול מטלי": 12,
    "כסף תכלת מטלי": 13,
    "אפור מטאלי": 14,
    "אפור כהה": 15,
    "אדום מטל": 16,
    "כחול מטל": 17,
    "כסף": 18,
    "שחור חציל": 19,
    "כסף מטלי": 20,
    "בז מטאלי": 21,
    "כחול": 22,
    "ירוק": 23,
    "טורקיז": 24,
    "אפור בהיר מטלי": 25,
    "חום": 26,
    "אדום": 27,
    "אפור ברונזה": 28,
    "אדמדם מטאלי": 29,
    "תכלת": 30,
    "כחול כהה": 31,
    "אפור עכבר": 32,
    "כחול בהיר": 33,
    "אפור פלדה": 34,
    "אדום בהיר": 35,
    "כסוף מטאלי": 36,
    "ירקרק מטלי": 37,
    "תכלת מטאלי": 38,
    "כחול קריסטל": 39,
    "כחול פנינה": 40,
    "אדום כהה יין": 41,
    "צהוב": 42,
    "כסף כחלחל מטלי": 43,
    "ורוד": 44,
    "בז": 45,
    "חום מטאלי": 46,
    "אדום מטאלי": 47,
    "לבן שנהב": 48,
    "כחול מטאלי": 49,
    "כחול פחם מטלי": 50,
    "זהב מטאלי": 51,
    "בורדו": 52,
    "ברונזה": 53,
    "ברונזה מטאלי": 54,
    "לבן פנינה": 55,
    "סגול": 56,
    "חציל": 57,
    "צהוב מטאלי": 58,
    "קרם": 59,
    "זהב": 60,
    "כסף ירקרק": 61,
    "לבן מטאלי": 62,
    "אפור בהיר": 63,
    "כתום": 64,
    "חום כהה": 65,
    "ירקרק בהיר": 66,
    "שן פיל": 67,
    "קפה מטאלי": 68,
    "כסף מטאלי": 69,
    "אדום זוהר": 70,
    "שחור מטאלי": 71,
    "פלטינה": 72,
    "כסף ים": 73,
    "כסוף": 74,
    "אחר": 75,
    "אדום שחור": 76,
    "ירוק בהיר": 77,
    "ירוק אקווה": 78,
    "אפור מטאלי ": 79,
}


class CarBabyUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Dor & Karin amazing project :)")
        self.window.geometry("500x700")
        self.layout()
        self.load_model()

    def load_model(self):
        self.linear = pickle.load(open("bestModel87.pickle", "rb"))

    def layout(self):
        self.carCompany = self.create_combobox(
            "Car Company", list(carCompanies.keys()))
        self.city = self.create_combobox("City", list(cities.keys()))
        self.color = self.create_combobox("color", list(color.keys()))
        self.year = self.create_input("year")
        self.current_km = self.create_input("current km")
        self.hand = self.create_input("hand")
        self.next_test = self.create_input("next test")
        self.new_car_price = self.create_input("Tariff")
        self.create_button("Predict price", self.predict_price)
        self.create_button("Auto Fill", self.auto_fill_form)
        self.clear_button = self.create_button(
            "Clear", self.clear_text)
        self.predicted_price_label = self.create_label()

    def create_label(self, text=""):
        label = tk.Label(self.window, text=text, font=("Arial", 18))
        label.pack()
        return label

    def create_input(self, text):
        self.create_label(text)

        input = tk.Entry(self.window, bg="pink", font=("Arial", 18))
        input.pack()
        return input

    def create_combobox(self, text, options):
        self.create_label(text)

        variable = tk.StringVar()
        selector = ttk.Combobox(self.window, textvariable=variable, values=options, font=(
            "Arial", 18), background="pink")
        selector.configure(background="pink")
        selector.pack()
        return selector

    def create_button(self, text, command):
        button = tk.Button(self.window, text=text, command=command,
                           font=("Arial", 14), width=12, bg="pink")
        button.pack(pady=5)
        return button

    def auto_fill_form(self):
        self.carCompany.set(random.choice(list(carCompanies.keys())))
        self.year.delete(0, tk.END)
        self.year.insert(0, random.randint(2010, 2021))
        self.city.set(random.choice(list(cities.keys())))
        self.current_km.delete(0, tk.END)
        self.current_km.insert(0, random.randint(0, 20000))
        self.hand.delete(0, tk.END)
        self.hand.insert(0, random.randint(0, 8))
        self.next_test.delete(0, tk.END)
        self.next_test.insert(0, random.randint(0, 12))
        self.new_car_price.delete(0, tk.END)
        self.new_car_price.insert(0, random.randint(90000, 300000))
        self.color.set(random.choice(list(color.keys())))

    def predict_price(self):
        predicted_data = np.array([[
            int(carCompanies[self.carCompany.get()]),
            int(self.year.get()),
            int(cities[self.city.get()]),
            int(self.current_km.get()),
            int(self.hand.get()),
            int(self.next_test.get()),
            int(self.new_car_price.get()),
            int(color[self.color.get()])
        ]])

        prediction = self.linear.predict(predicted_data)
        self.predicted_price_label.config(
            text=f"Predicted price: {prediction[0]}")

    # Define a function to clear the Entry Widget Content
    def clear_text(self):
        self.carCompany.delete(0, tk.END)
        self.city.delete(0, tk.END)
        self.color.delete(0, tk.END)
        self.year.delete(0, tk.END)
        self.current_km.delete(0, tk.END)
        self.hand.delete(0, tk.END)
        self.next_test.delete(0, tk.END)
        self.new_car_price.delete(0, tk.END)


window = tk.Tk()
carBabyUI = CarBabyUI(window)
window.mainloop()
