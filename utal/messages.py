import utal
from selenium.webdriver.common.by import By
from utal.exceptions import DriverNotProvidedError, ElementNotFoundError, ActionFailedError


class Messages:
    def __init__(self):
        pass

    @staticmethod
    def get_count(self, driver=None):
        if driver is None:
            raise DriverNotProvidedError("get_count")

        try:
            count = driver.find_elements(By.XPATH, "//div[contains(@class, 'DivItemWrapper')]")
            return len(count)
        except Exception as e:
            raise ActionFailedError("get_count", e)

    @staticmethod
    def set_title(self, driver, title: str):
        try:
            if driver is None:
                raise DriverNotProvidedError("set_title")

            try:
                current_title = driver.find_element(By.XPATH, "//h1[contains(@data-e2e, 'message-title')]")
                driver.execute_script("arguments[0].textContent = arguments[1];", current_title, title)
            except Exception as e:
                raise ElementNotFoundError("title")
        except Exception as e:
            raise ActionFailedError("set_title", str(e))

    @staticmethod
    def send_message_to_user_by_nickname(self, driver, nickname: str, *args: str):
        if driver is None:
            raise DriverNotProvidedError("send_message_to_user_by_nickname")

        try:
            divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'DivItemWrapper')]")
            user_div = None  

            for div in divs:
                try:
                    user_div_text = div.find_element(By.XPATH, ".//p[contains(@class, 'PInfoNickname')]")
                    if user_div_text.text == nickname:  
                        user_div = div
                        break
                except Exception:
                    pass  # Ignorar si no encuentra el nickname

            if user_div:
                user_div.click()
                utal.Conversation.send(driver, *args)
                return True
            return False
        except Exception as e:
            raise ActionFailedError("send_message_to_user_by_nickname", str(e))

    @staticmethod
    def find_user_by_nickname(self, driver, nickname: str):
        if driver is None:
            raise DriverNotProvidedError("find_user_by_nickname")

        try:
            divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'DivItemWrapper')]")

            for div in divs:
                try:
                    user_div_text = div.find_element(By.XPATH, ".//p[contains(@class, 'PInfoNickname')]")
                    if user_div_text.text == nickname:  
                        return True
                except Exception:
                    pass  # Ignorar si no encuentra el nickname

            return False
        except Exception as e:
            raise ActionFailedError("find_user_by_nickname", str(e))

    @staticmethod
    def enter_user_chat_by_nickname(self, driver, nickname: str):
        if driver is None:
            raise DriverNotProvidedError("enter_user_chat_by_nickname")

        try:
            divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'DivItemWrapper')]")

            for div in divs:
                try:
                    user_div_text = div.find_element(By.XPATH, ".//p[contains(@class, 'PInfoNickname')]")
                    if user_div_text.text == nickname:  
                        div.click()
                        return True
                except Exception:
                    pass  # Ignorar si no encuentra el nickname

            return False
        except Exception as e:
            raise ActionFailedError("enter_user_chat_by_nickname", str(e))
