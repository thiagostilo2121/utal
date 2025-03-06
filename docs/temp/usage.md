# Usage

Here's a quick start of the usage of PyUTAL:

1. First import the `utal` library or PyUTAL app from `utal.core`
```python
from utal.core import PyUTAL
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

3. Create a `main` function with the driver and an PyUTAL app arguments
```python
def main(driver, app: PyUTAL):
    driver.get("https://tiktok.com/messages")
    
    while True:  # Important to use loops
        message = app.client.listen()  # Retrieves all messages
        if message: 
            print(message)

        if message and message == "hello":  
            user_nickname = app.conversation.get_user_nickname()
            app.conversation.send(f"Hi, {user_nickname} 🌟")
```

4. Call the both functions and start the PyUTAL app
```python
if __name__ == "__main__":
    driver = startup_selenium()
    app = PyUTAL(driver)
    main(driver, app)
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
from utal.core import PyUTAL
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

def main(driver, app: PyUTAL):
    driver.get("https://tiktok.com/messages")
    
    while True:  # Important to use loops
        message = app.client.listen()  # Retrieves all messages
        if message:
            print(message)

        if message and message == "hello":  
            user_nickname = app.conversation.get_user_nickname()
            app.conversation.send(f"Hi, {user_nickname} 🌟")

if __name__ == "__main__":
    driver = startup_selenium()
    app = PyUTAL(driver)
    main(driver, app)
```

## Important Notes
- **Headless mode must be disabled the first time** to allow manual login and save session data.
- **A loop is required** for the bot to continuously listen for incoming messages.
- **The bot does NOT have a prefix configured and does not filter its own messages** in this example. See the [full documentation](index.md) to learn how to implement that.

## Next Steps
These are just recommendations.

- Implement a system of custom prefixes for each user.
- Develop a `command handler` to structure the bot’s commands better.
- Use a database to store bot or user information.
- Take inspiration from Discord bot development structures.
- Experiment and test the different functions of the library.
- See the [Selenium documentation](https://www.selenium.dev/documentation/) to scale the project.