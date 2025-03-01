from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search box and enter a query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")
search_box.submit()

# Wait for results to load
time.sleep(3)

# Capture screenshot
driver.save_screenshot("google_search.png")

# Close the browser
driver.quit()
