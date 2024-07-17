from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
import time
import threading

# Function to generate random names
def generate_random_name():
    first_names = ["Alice", "Bob", "Charlie", "Daisy", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
    last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor"]
    return f"{random.choice(first_names)} {random.choice(last_names)}"

# Function to generate random comments
def generate_random_comment(length=100):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

# Function to automate form submission
def automate_form_submission(url, num_entries):
    driver = webdriver.Chrome()  # Make sure chromedriver is installed and in PATH

    try:
        # Open the URL
        driver.get(url)

        for _ in range(num_entries):
            name = generate_random_name()
            comment = generate_random_comment()

            # Find the input fields
            name_input = driver.find_element(By.ID, "name")
            comment_input = driver.find_element(By.ID, "comment")

            # Clear the fields
            name_input.clear()
            comment_input.clear()

            # Enter the random name and comment
            name_input.send_keys(name)
            comment_input.send_keys(comment)

            # Find the submit button and click it
            submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit')]")
            submit_button.click()

            # Wait for a short period to mimic user interaction and to ensure the form is submitted
            time.sleep(2)

            print(f"Sent: {{'name': '{name}', 'comment': '{comment}'}}")

    finally:
        # Close the browser
        driver.quit()

# URL of the form page
url = "https://example.com/form"

# Number of entries to be sent by each browser
entries_per_browser = 50

# List to hold threads
threads = []

# Start three threads for three browser instances
for _ in range(3):
    thread = threading.Thread(target=automate_form_submission, args=(url, entries_per_browser))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()
