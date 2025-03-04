from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utal.exceptions import DriverNotProvidedError, ElementNotFoundError, ActionFailedError

class Conversation:
    def __init__(self): ...

    @staticmethod
    def send(driver=None, *args: str):
        """ Send a message to the current conversation """
        if driver is None:
            raise DriverNotProvidedError("send")
        
        try:
            message_field = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[@contenteditable='true']"))
            )
            driver.execute_script("""
                let field = arguments[0];
                field.focus();
            """, message_field)

            driver.execute_script(
                f'''
                const text = `{args}`;
                const dataTransfer = new DataTransfer();
                dataTransfer.setData('text', text);
                const event = new ClipboardEvent('paste', {{
                    clipboardData: dataTransfer,
                    bubbles: true
                }});
                arguments[0].dispatchEvent(event)
                ''', message_field)  

            message_field.send_keys(Keys.RETURN)
        except Exception as e:
            raise ActionFailedError("send", str(e))
    
    @staticmethod
    def get_user_nickname(driver=None):
        if driver is None:
            raise DriverNotProvidedError("get_user_nickname")
        
        try:
            nickname = driver.find_element(By.XPATH, "//p[contains(@class, 'PNickname')]")
            return nickname.text
        except Exception:
            raise ElementNotFoundError("nickname")
    
    @staticmethod
    def get_user_username(driver=None):
        if driver is None:
            raise DriverNotProvidedError("get_user_username")
        
        try:
            username = driver.find_element(By.XPATH, "//p[contains(@data-e2e, 'chat-uniqueid')]")
            return username.text
        except Exception:
            raise ElementNotFoundError("username")

    @staticmethod
    def get_user_avatar_URL(driver=None):
        if driver is None:
            raise DriverNotProvidedError("get_user_avatar_URL")
        
        try:
            avatar = driver.find_element(By.XPATH, "//span[contains(@data-e2e, 'top-chat-avatar')]")
            avatar = avatar.find_element(By.XPATH, "./*")
            return avatar.get_attribute("src")
        except Exception:
            raise ElementNotFoundError("avatar")

    @staticmethod   
    def send_image(driver, img_path: str):
        if driver is None:
            raise DriverNotProvidedError("send_image")
        
        try:
            btn = driver.find_element(By.XPATH, "//input[contains(@id, 'file-input-select-image')]")
            btn.send_keys(img_path)
            time.sleep(1.1)
            btns = driver.find_elements(By.XPATH, "//div[contains(@class, 'ButtonLabel')]")
            for btn in btns:
                if btn.text in ("Enviar", "Send"): 
                    btn.click()
                    return
            raise ElementNotFoundError("send button")
        except Exception as e:
            raise ActionFailedError("send_image", str(e))