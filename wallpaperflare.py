from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import os
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome()


## ====================================================
## Chrome Config ## 

CHROME_LOCATION = os.getenv("CHROME_BIN")

# uBlock origin setup (Ad-Blocker) -----------------------

options = webdriver.ChromeOptions()
ublock_path = os.path.abspath("public/Ublock-Origin.crx")
options.add_extension(ublock_path)


## Download Path Setup -----------------------------------

# prefs = {'download.default_directory': "C:/test/laz/Scrapping/random/img/"}
prefs = {"download.default_directory" : r"C:\test\laz\Scrapping\random\img"}
options.add_experimental_option('prefs', prefs) 

##  --------------------------------------------------------

driver = webdriver.Chrome(options=options)

## ============================================================
## Wallpaper Flare Anime page 


def wallpaperflare(link):

    driver.get(link)
    time.sleep(3)


    try:
        driver.find_element(By.XPATH, '//*[@id="back"]').click()
    except NoSuchElementException:
        print("Ublock caution page not detected")



    item_blocks = driver.find_elements(
        By.XPATH,
        "//figure",
    )


    for item in item_blocks:
        try:
            item_link = item.find_element(By.XPATH, ".//a[@itemprop][@href]").get_attribute("href")
            try:
                # driver.get(item_link)
                # time.sleep(60)
                # download_link = driver.find_element(By.XPATH, '//*[@id="mid"]/div[1]/a[@href]').get_attribute("href")
                # driver.get(download_link)
                download_link = item_link+"/download"
                driver.get(download_link)
                print('item_link: ', item_link)
                # print('download_link: ', download_link)
                print("================================")
                # time.sleep(2)
                
                download_button = driver.find_element(By.XPATH, '//*[@id="dld_result"]')
                download_button.click()
                driver.back()
                # time.sleep(2)

            except NoSuchElementException:
                print("1 link not problem")
                driver.get(link)
                continue
        except NoSuchElementException or StaleElementReferenceException:
            print("1 image not found")
            driver.get(link)
            continue
        
    
k = 1

while(k<=20):
    wallpaperflare(f"https://www.wallpaperflare.com/search?wallpaper=ANIME&page={k}")
    k=k+1

time.sleep(30000)
driver.close()


## ==========================================
## Testing Area
## ==========================================

## To Work on (1) ---------------------------------------
# uBlock origin setup (Ad-Blocker)

# # Set up the Chrome WebDriver
# chrome_options = webdriver.ChromeOptions()
# # Set the download directory to a specific path
# chrome_options.add_experimental_option('prefs', {
#     'download.default_directory': 'C:/test/laz/Scrapping/random/img'
# })
# driver = webdriver.Chrome(chrome_options=chrome_options)

# chromeOptions = webdriver.ChromeOptions()
# prefs = {"download.default_directory" : "C:/test/laz/Scrapping/random/img"}
# chromeOptions.add_experimental_option("prefs",prefs)
# chromedriver = "chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)

# Test -------------------------------------------------
# uBlock origin setup (Ad-Blocker)

# driver.get("https://chrome.google.com/webstore/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm/related")
# time.sleep(30)
# add_to_chrome_btn = driver.find_element(By.XPATH, '(//text()[contains(., "uBlock Origin")])[1]')
# # add_to_chrome_btn = driver.find_element(By.XPATH, '(//text()[contains(., "Add to Chrome")]/parent::node())[2]')
# print(add_to_chrome_btn.get_attribute('outerHTML'))
# time.sleep(30)

# # add_to_chrome_btn.click()

# alert = driver.switch_to.alert
# alert.accept()
# time.sleep(60)

