# Usage

Here's a quick start of the usage of PyUTAL:

1. First import `utal`
```python
import utal
```

2. Create a Selenium instance. Here's a basic recommended example
```python
from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service

def startup_selenium():
    USERDATADIR = os.path.abspath("path/to/user/data/directory")
    DRIVERPATH = "path/to/webdriver"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")  # Run without headless mode the first time
    options.add_argument(rf"user-data-dir={USERDATADIR}")
    
    driver = webdriver.Chrome(service=Service(DRIVERPATH), options=options)
    return driver  # Important to return the driver
```

3. Create a `main` function with the driver by argument
```python
def main(driver):
    driver.get("https://tiktok.com/messages")
    
    while True:  # Important to use loops
        message = ut.Client.listen(driver=driver)  # Retrieves all messages
        print(message)

        if message and message == "hello":  
            user_nickname = ut.Conversation.get_user_nickname(driver)
            ut.Conversation.send(driver, f"Hi, {user_nickname} 🌟")
```

4. Call the both functions
```python
if __name__ == "__main__":
    driver = startup_selenium()
    main(driver)
```

5. If the user sends `hello` to the bot DM, the console output wil be:
```sh
hello
```

6. And, if the user nickname is "thiago" the response will be:
```sh
Hi, thiago 🌟
```

7. Here's the full code:
```python
import os
import utal as ut
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def startup_selenium():
    USERDATADIR = os.path.abspath("path/to/user/data/directory")
    DRIVERPATH = "path/to/webdriver"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless")  # Run without headless mode the first time
    options.add_argument(rf"user-data-dir={USERDATADIR}")
    
    driver = webdriver.Chrome(service=Service(DRIVERPATH), options=options)
    return driver  # Important to return the driver

def main(driver):
    driver.get("https://tiktok.com/messages")
    
    while True:  # Important to use loops
        message = ut.Client.listen(driver=driver)  # Retrieves all messages
        print(message)

        if message and message == "hello":  
            user_nickname = ut.Conversation.get_user_nickname(driver)
            ut.Conversation.send(driver, f"Hi, {user_nickname} 🌟")

if __name__ == "__main__":
    driver = startup_selenium()
    main(driver)
```

## Important Notes
- **Headless mode must be disabled the first time** to allow manual login and save session data.
- **A loop is required** for the bot to continuously listen for incoming messages.
- **The bot does NOT have a prefix configured and does not filter its own messages** in this example. See the [full documentation](#index) to learn how to implement that.

## Next Steps
These are just recommendations.

- Implement a system of custom prefixes for each user.
- Develop a `command handler` to structure the bot’s commands better.
- Use a database to store bot or user information.
- Take inspiration from Discord bot development structures.
- Experiment and test the different functions of the library.
- See the [Selenium documentation](https://www.selenium.dev/documentation/) to scale the project.