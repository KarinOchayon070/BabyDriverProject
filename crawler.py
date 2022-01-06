from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from constants import (CAR_PROPERTIES, SPECIFICATIONS_PROPERTIES_TRANSLATIONS)
from utils import (clean_number, take_digits_only, take_letters_only)

# Path to chromedriver
PATH = "C:\Windows\chromedriver.exe"

# Which browser to use (Edge, Chrome, Firefox,etc...)
driver = webdriver.Chrome(PATH)

itemsScraped = {}

# our website - carweiz
driver.get("https://carwiz.co.il/used-cars")


# Here we get the links of all the cars - stop at 2000 cars
def getLinks():
    listOfLinks = []
    while True:
        cars = driver.find_elements(
            By.XPATH, "// a[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'car-details-button')]")
        for car in cars:
            link = car.get_attribute("href")
            if(link not in listOfLinks):
                listOfLinks.append(link)
        # Scroll down to bottom
        print("SCROLLING TO BOTTOM")
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        if(len(listOfLinks) >= 2000):
            break
    return listOfLinks


# Here we get the details - car name, city, price,km, color, etc...
def getCarDetails(objectToFill):

    detailsContainer = driver.find_element(
        By.CSS_SELECTOR, "tbody[class='MuiTableBody-root']")
    details = detailsContainer.find_elements(
        By.CSS_SELECTOR, "tr[class='MuiTableRow-root']")
    for index, detail in enumerate(details):
        # Bring us all of his "children" in array
        items = detail.find_elements(
            By.CSS_SELECTOR, "*")
        value = items[1].text
        key = CAR_PROPERTIES[index]
        objectToFill[key] = value


# Here we get the city, price, new car price (mhir mhiron)
def getHeaders(objectToFill):

    newCarPrice = None
    city = driver.find_element(
        By.XPATH, "// p[contains(@class, 'MuiTypography-root') and contains(@class, 'MuiTypography-body2')]")
    price = driver.find_element(
        By.XPATH, "// div[contains(@class, 'MuiBox-root') and contains(@align, 'center')]")
    try:
        newCarPrice = driver.find_element(
            By.XPATH, "// p[contains(text(), 'היקר בהיצע')]").find_element(By.XPATH, "..").find_elements(
                By.CSS_SELECTOR, "*")[2]
        objectToFill["new_car_price"] = newCarPrice.text
    except:
        print("No new car price FOUND")
    objectToFill["city"] = city.text
    objectToFill["price"] = price.text

# Here we get specifications - engine, transmission, etc...


def getSpecifications(objectToFill):
    specificationsContainer = driver.find_element(
        By.XPATH, "// h2[contains(text(), 'מפרט טכני')]").find_element(By.XPATH, "..")
    specificationsHeaders = specificationsContainer.find_elements(
        By.XPATH, "// div[contains(@class, 'MuiPaper-root') and contains(@class, 'MuiAccordion-root') and contains(@class, 'MuiPaper-elevation0')]")

    # This opens all the tabs
    for index, header in enumerate(specificationsHeaders):
        if(index != 0):
            header.click()
            time.sleep(0.5)

    # This is all the keys
    specificationsKeys = specificationsContainer.find_elements(
        By.XPATH, "// div[contains(@class, 'MuiGrid-root') and contains(@class, 'MuiGrid-item') and contains(@class, 'MuiGrid-grid-xs-6') and contains(@class, 'MuiGrid-grid-md-8')]")

    specificationsValues = specificationsContainer.find_elements(
        By.XPATH, "// div[contains(@class, 'MuiGrid-root') and contains(@class, 'MuiGrid-item') and contains(@class, 'MuiGrid-grid-xs-5') and contains(@class, 'MuiGrid-grid-md-3')]")

    # Takes the p tags and takes the text
    for index, spec in enumerate(specificationsKeys):

        key = spec.find_element(By.TAG_NAME, "p").text
        value = specificationsValues[index].find_element(
            By.TAG_NAME, "p").text
        keyTranslated = SPECIFICATIONS_PROPERTIES_TRANSLATIONS[key]
        objectToFill[keyTranslated] = value


# Here we normalize the data - we arranged everything more neatly under "cleanMe"
def normalizeData(objectToFill):
    tempObj = {}
    for key, value in objectToFill.items():
        if(key == "rear_wheels" or key == "front_wheels"):
            splitSlash = value.split("/")  # 175/65r14 [175,65r14]
            tire_width = splitSlash[0]
            tireType = take_letters_only(splitSlash[1])  # r
            splittedValues = splitSlash[1].split(tireType)  # [65,14]
            [height_ratio, wheel_diameter] = splittedValues
            tempObj["tire_type"] = tireType
            tempObj["tire_width"] = tire_width
            tempObj["height_ratio"] = height_ratio
            tempObj["wheel_diameter"] = wheel_diameter

        elif(key == "next_test" or key == "engine"):
            tempObj[key] = take_digits_only(value)
        elif(value == "ליסינג"):
            tempObj[key] = 0
        elif(value == "פרטית"):
            tempObj[key] = 1
        elif(value == "ידנית"):
            tempObj[key] = 0
        elif(value == "אוטומטית"):
            tempObj[key] = 1
        elif(value == "ידני"):
            tempObj[key] = 0
        elif(value == "אוטומטי"):
            tempObj[key] = 1
        elif(value == "סגסוגת"):
            tempObj[key] = 1
        elif(value == "פלדה"):
            tempObj[key] = 0
        elif(value == "יש"):
            tempObj[key] = 1
        elif(value == "אין"):
            tempObj[key] = 0
        elif(value == "טורבו"):
            tempObj[key] = 1
        else:
            tempObj[key] = clean_number(value)
    return tempObj

# Run this baby!


def main():
    data = []
    linksOfCars = getLinks()
    # for every link  call this call functions
    for link in linksOfCars:
        try:
            objectToFill = {}
            driver.get(link)
            getCarDetails(objectToFill)
            getHeaders(objectToFill)
            getSpecifications(objectToFill)
            normalizedData = normalizeData(objectToFill)
            data.append(normalizedData)
        except:
            print("ERROR IN CRAWLER: " + link)
    return data


# Give him time to breathe
time.sleep(20)
