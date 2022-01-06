# Here we stored a few utils functions (we did not want to soil the code and are therefore in a separate space)
import re
import time

# Function to clean special characters from a string


def clean_number(number):
    return number.replace(",", "").replace("₪", "")

# Function to get only the digits from a string


def take_digits_only(text):
    return ''.join(filter(str.isdigit, text))

# Function to get only the letters from a string


def take_letters_only(text):
    return ''.join(filter(str.isalpha, text))

# Function to scroll to the bottom of the page (in our case - 2000 cars)


def scrollToBottom(driver, numberOfLinks):
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(4)
        print("SCROLLING TO BOTTOM")

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
