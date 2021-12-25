import re
import time


def clean_number(number):
    return number.replace(",", "").replace("₪", "")


def take_digits_only(text):
    return ''.join(filter(str.isdigit, text))


def take_letters_only(text):
    return ''.join(filter(str.isalpha, text))


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


# print(take_letters_only(test))
# print(take_digits_only(test))
