import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# User info - fill these in manually
FIRST_NAME = "YourFirstName"
LAST_NAME = "YourLastName"
EMAIL = "your.email@example.com"
PHONE = "1234567890"
ADDRESS = "Your Street Address"
CITY = "Your City"
ZIP_CODE = "Your Zip Code"
COUNTRY = "Poland"  # Or your country
STATE = ""  # If applicable
CARD_NUMBER = "4111111111111111"  # Test card or your info - BE CAREFUL WITH REAL INFO
EXP_MONTH = "12"
EXP_YEAR = "2025"
CVV = "123"

# Website URL (cleaned without tracking params)
URL = "https://shop.travisscott.com/"

# Set up Selenium WebDriver (assuming Chrome - download chromedriver and set path if needed)
driver = webdriver.Chrome()  # Or webdriver.Chrome(executable_path='/path/to/chromedriver')


# Function to check if timer is over
def is_timer_over():
    try:
        # Adjust these selectors based on actual website inspection (use DevTools to find)
        timer_elements = driver.find_elements(By.CSS_SELECTOR,
                                              ".countdown span")  # Assuming spans for hours, mins, secs
        if len(timer_elements) >= 3:
            hours = timer_elements[0].text.strip()
            minutes = timer_elements[1].text.strip()
            seconds = timer_elements[2].text.strip()
            return hours == "00" and minutes == "00" and seconds == "00"  # Or check if all zero
        return False
    except NoSuchElementException:
        return True  # If timer not found, assume it's over


# Load the page
driver.get(URL)

# Wait until 9 PM local time or monitor timer
target_time = datetime.now().replace(hour=21, minute=0, second=0, microsecond=0)  # 9 PM
if datetime.now() > target_time:
    print("It's already past 9 PM. Proceeding immediately.")
else:
    wait_seconds = (target_time - datetime.now()).total_seconds()
    print(f"Waiting {wait_seconds} seconds until 9 PM.")
    time.sleep(wait_seconds)

# Now poll until timer is over (in case of slight delay)
while not is_timer_over():
    time.sleep(1)  # Check every second
    driver.refresh()  # Refresh to update timer

print("Timer is over! Attempting to purchase.")

# Find and click the purchase button
# Adjust selector - e.g., button with text 'Buy Now' or class 'add-to-cart'
try:
    purchase_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[name='add']"))  # Common for Shopify 'Add to Cart'
    )
    purchase_button.click()
    print("Clicked purchase button.")
except Exception as e:
    print(f"Error clicking purchase button: {e}")
    driver.quit()
    exit()

# Wait for checkout page or cart
time.sleep(2)  # Adjust as needed

# If it goes to cart, click checkout
try:
    checkout_button = driver.find_element(By.CSS_SELECTOR, "button[name='checkout']")
    checkout_button.click()
except NoSuchElementException:
    pass  # Maybe directly to checkout

# Now on checkout page - fill info
try:
    # Shipping info - adjust IDs based on inspection (Shopify often uses #checkout_email, etc.)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "checkout_email")))

    driver.find_element(By.ID, "checkout_email").send_keys(EMAIL)
    driver.find_element(By.ID, "checkout_shipping_address_first_name").send_keys(FIRST_NAME)
    driver.find_element(By.ID, "checkout_shipping_address_last_name").send_keys(LAST_NAME)
    driver.find_element(By.ID, "checkout_shipping_address_address1").send_keys(ADDRESS)
    driver.find_element(By.ID, "checkout_shipping_address_city").send_keys(CITY)
    driver.find_element(By.ID, "checkout_shipping_address_zip").send_keys(ZIP_CODE)
    driver.find_element(By.ID, "checkout_shipping_address_country").send_keys(COUNTRY)  # Or select from dropdown
    if STATE:
        driver.find_element(By.ID, "checkout_shipping_address_province").send_keys(STATE)
    driver.find_element(By.ID, "checkout_shipping_address_phone").send_keys(PHONE)

    # Continue to payment
    continue_button = driver.find_element(By.ID, "continue_button")
    continue_button.click()

    # Payment info - CAREFUL, this is sensitive
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[name^='card-fields']")))  # Shopify uses iframes for cards
    driver.find_element(By.ID, "number").send_keys(CARD_NUMBER)
    driver.find_element(By.ID, "expiry").send_keys(EXP_MONTH + EXP_YEAR[-2:])
    driver.find_element(By.ID, "verification_value").send_keys(CVV)
    driver.switch_to.default_content()

    # Complete purchase
    complete_button = driver.find_element(By.ID, "continue_button")  # Or 'Pay Now'
    complete_button.click()

    print("Purchase attempted. Check the browser for confirmation.")
except Exception as e:
    print(f"Error filling form: {e}")

# Keep browser open for user to see
input("Press Enter to close browser...")
driver.quit()