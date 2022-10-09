from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from models.descriptionMapper import DescriptionMapper

from models.descriptionModel import DescriptionModel


class Scraper():

    webdriver.Chrome
    driver = None

    stocklist = [
        "ADBE",
        "ADP",
        "AMD",
        "ADI",
        "ANSS",
        "AAPL",
        "AMAT",
        "ASML",
        "TEAM",
        "ADSK",
        "AVGO",
        "CDNS",
        "CSCO",
        "CTSH",
        "CRWD",
        "DDOG",
        "DOCU",
        "FISV",
        "FTNT",
        "INTC",
        "INTU",
        "KLAC",
        "LRCX",
        "MRVL",
        "MCHP",
        "MU",
        "MSFT",
        "NVDA",
        "NXPI",
        "OKTA",
        "PANW",
        "PAYX",
        "PYPL",
        "QCOM",
        "SWKS",
        "SPLK",
        "SNPS",
        "TXN",
        "VRSN",
        "WDAY",
        "ZM",
        "ZS"
    ]

    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver

    def crawlAll(self):
        self.driver.set_window_size(1920, 8080)

        #accept cookies
        self.driver.get("https://finance.yahoo.com")
        self.driver.find_element(By.CSS_SELECTOR, "button[name='agree']").click()

        for company in self.stocklist:
            print("Crawling " + company)

            self.driver.get("https://finance.yahoo.com/quote/"+ company)

            delay = 300 # seconds
            try:
                WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, 'app')))
                print ("    Page is ready!")
            except TimeoutException:
                print ("    Loading took too much time!")

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            elem = None
            try:
                elem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.businessSummary ')))
                print ("    Information is ready!")
            except TimeoutException:
                print ("    Information loading took too much time!")
            print(elem.text)
            print("------------------------------------------")
            self.sendDescription(company, elem.text)

    def sendDescription(self, company, description):
        descriptionModel = DescriptionModel()
        descriptionModel.company = company
        descriptionModel.description = description

        descriptionMapper = DescriptionMapper()
        descriptionMapper.save(descriptionModel)

    def crawl(self):
        self.driver.set_window_size(1920, 8080)
        self.driver.get("https://finance.yahoo.com/quote/ADP")
        #elem = self.driver.find_elements(By.CSS_SELECTOR, ".asset-profile-container")
        # self.driver.implicitly_wait(5)
       
        self.driver.find_element(By.CSS_SELECTOR, "button[name='agree']").click()

        delay = 300 # seconds
        try:
            WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, 'app')))
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        elem = None
        try:
            elem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.businessSummary ')))
            print ("Page is ready!")
        except TimeoutException:
            print ("Loading took too much time!")
        print(elem.text)


        # # Get scroll height after first time page load
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     # Wait to load page / use a better technique like `waitforpageload` etc., if possible
        #     time.sleep(2)
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     print(new_height,last_height)
        #     if new_height == last_height:
        #         break
        #     last_height = new_height
                    
        # html = self.driver.execute_script("return document.documentElement.outerHTML")
        # print(html)
        #elem = self.driver.find_element(By.ID, "Col2-11-QuoteModule-Proxy")
        # elem = self.driver.find_element(By.CSS_SELECTOR, ".asset-profile-container")

        #print(myElem.text)