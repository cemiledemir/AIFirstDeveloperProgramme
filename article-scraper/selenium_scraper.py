from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Set up the WebDriver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # Navigate to Google Turkey
    driver.get("https://www.google.com.tr")

    # Find the search box
    search_box = driver.find_element(By.NAME, "q")

    # Type "Hello World!" in the search box
    search_box.send_keys("Hello World!")

    # Press Enter to perform the search
    search_box.send_keys(Keys.RETURN)

    # Alternatively, you can click the search button
    # search_button = driver.find_element(By.NAME, "btnK")
    # search_button.click()

finally:
    # Close the browser after a short delay to see the result
    import time
    time.sleep(5)
    driver.quit()
