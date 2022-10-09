from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from sys import platform
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


from scraper import Scraper

# basic setup: https://nander.cc/using-selenium-within-a-docker-container
def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

if __name__ == "__main__":
    chrome_options = set_chrome_options()

    driver = None

    #determine if linux or windows. Add for Mac or other if necessary
    # if platform == "linux" or platform == "linux2":
    #     # linux
    #     driver = webdriver.Chrome(options=chrome_options)
    # else:
    #     driver = webdriver.Chrome(executable_path="assets/chromedriver.exe",options=chrome_options)
    
    driver = webdriver.Chrome(options=chrome_options,service=Service(ChromeDriverManager().install()))
    # Do stuff with your driver
    scraper = Scraper(driver)
    scraper.crawlAll()

    
    driver.close()