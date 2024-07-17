# Form Automation Script | Contactme-BOT

This script automates form submissions on a specified website using Selenium and Python. It generates random names and comments, fills in the form, and submits it multiple times.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/form-automation.git
    cd form-automation
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and make sure it is in your PATH.

## Usage

1. Update the `url` variable in `form_automation.py` with the URL of the form you want to automate.
2. Update the IDs of the name input field, comment input field, and submit button if they differ from `name`, `comment`, and `Submit` respectively.
3. Run the script:
    ```bash
    python form_automation.py
    ```

This script will open three browser instances, each submitting the form 50 times with randomly generated data.

## Note

- Ensure the ChromeDriver version matches your installed Chrome browser version.
- The script includes a brief delay (`time.sleep(2)`) to mimic user interaction and prevent being flagged as a bot.
