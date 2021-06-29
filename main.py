import tkinter.messagebox
from time import sleep

from selenium import webdriver
from retry import retry

# REPLACE THE STRING VALUES BELOW THIS LINE

# This is your personal code that comes to your email account after initial manual registration.
DEIN_VERMITTLUNGS_CODE = "XXXX-XXXX-XXXX" 

# These numbers are identifiers for a vaccination center i.e. https://XXX-iz.impfterminservice.de/impftermine/service?plz=XXXXX)
IMPFZENTRUM_VORNUMMER= "XXX"
IMPFZENTRUM_PLZ = "XXXXX"

# REPLACE THE STRING VALUES ABOVE THIS LINE

DELAY = 5 # Abstand zwischen Versuchen [Minuten]


@retry(delay=60*DELAY)
def get_impftermin():
    browser = webdriver.Chrome()
    sleep(5)
    url = f'https://{IMPFZENTRUM_VORNUMMER}-iz.impfterminservice.de/impftermine/suche/{DEIN_VERMITTLUNGS_CODE}/{IMPFZENTRUM_PLZ}'
    print("URL: " + url)
    browser.get(url)
    sleep(3)
    cookie_button = browser.find_element_by_css_selector(
        ".pr-md-3 > a:nth-child(1)")
    cookie_button.click()
    sleep(1)
    browser.get(url)
    sleep(3)
    try:
        termin_suchen_button = browser.find_element_by_css_selector(".kv-btn-round")
        termin_suchen_button.click()
    except:
        raise ValueError("no button is found. Something wrong here.")
    sleep(5)
    try:
        print(browser.find_element_by_css_selector(
            ".its-slot-pair-search-no-results").text)
        browser.quit()
        del browser
    except:
        print("Holly cow, you can book an appointment!")
        tkinter.messagebox.showinfo(
            title="Congrats!",
            message="Now go quickly to impfterminservice.de and book your appointment ;)")

if __name__ == "__main__":
    get_impftermin()
