from selenium import webdriver
import time
from selenium.webdriver.common.by import By


# Path to chromedriver
PATH = "C:\Windows\chromedriver.exe"

# Which browser to use (Edge, Chrome, Firefox,etc...)
driver = webdriver.Chrome(PATH)

itemsScraped = {}

# our website - carweiz
# driver.get("https://carwiz.co.il/used-cars")
driver.get("https://carwiz.co.il/used-cars/698c48b5-8c5d-42a8-ab01-9abb07ec757e/2015-%D7%9E%D7%90%D7%96%D7%93%D7%94-6")


def getLinks():

    # This will get us to the elemnt that contain the link of the cars
    cars = driver.find_elements(
        By.XPATH, "// a[contains(@class, 'MuiButtonBase-root') and contains(@class, 'MuiButton-root') and contains(@class, 'car-details-button')]")

    listOfLinks = []

    # Here we get the actual links
    for index, car in enumerate(cars):
        link = car.get_attribute("href")
        listOfLinks.append(link)
        print("Link {}: {}".format(index, link))

    return listOfLinks


# Here we get the details - car name, city, price,km, color, etc...
def getCarDetails(objectToFill):

    detailsContainer = driver.find_element(
        By.CSS_SELECTOR, "tbody[class='MuiTableBody-root']")

    details = detailsContainer.find_elements(
        By.CSS_SELECTOR, "tr[class='MuiTableRow-root']")

    arrayOfKeys = [
        "carName",
        "year",
        "engine",
        "current_km",
        "hand",
        "gearbox",
        "color",
        "original_ownership",
        "next_test",
        "annual_licensing_fee"
    ]

    for index, detail in enumerate(details):
        # Bring us all of his "children" in array
        items = detail.find_elements(
            By.CSS_SELECTOR, "*")

        value = items[1].text
        key = arrayOfKeys[index]
        print("{}: {}".format(key, value))
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
                By.CSS_SELECTOR, "*")[2].text
    except:
        print("No new car price FOUND")

    # TODO: Check about reverse the texts
    objectToFill["city"] = city.text
    objectToFill["price"] = price.text
    objectToFill["new_car_price"] = newCarPrice


def getSpecifications():
    specificationsContainer = driver.find_element(
        By.XPATH, "// h2[contains(text(), 'מפרט טכני')]").find_element(By.XPATH, "..")

    specifications = specificationsContainer.find_elements(
        By.XPATH, "// div[contains(@class, 'MuiPaper-root') and contains(@class, 'MuiAccordion-root') and contains(@class, 'MuiPaper-elevation0')]")

    print(len(specifications))


def main():
    data = []

    linksOfCars = getLinks()
    # for every link  call this call functions
    for link in linksOfCars:
        objectToFill = {}
        driver.get(link)
        getCarDetails(objectToFill)
        getHeaders(objectToFill)
        data.append(objectToFill)
        print(objectToFill)


# main()
getSpecifications()
# driver.get("https://carwiz.co.il/used-cars/115c8036-85ef-4871-bf2e-6ccf771e0a57/2019-%D7%A7%D7%99%D7%94-%D7%A4%D7%99%D7%A7%D7%A0%D7%98%D7%95")
# getHeaders({})

time.sleep(20)
