import time
from selenium.webdriver.common.by import By
from utal.exceptions import DriverNotProvidedError, ElementNotFoundError, ActionFailedError

class Client():

    def __init__(self, driver, __processedmsj__):
        self.driver = driver
        self.__processedmsj__ = __processedmsj__

    def listen(self, prefix: str = "", my_self: str = "") -> str:
        driver = self.driver
        if driver is None:
            raise DriverNotProvidedError(function_name="listen")

        bot_username = my_self

        try:
            # Detectar nuevos mensajes
            try:
                element = driver.find_element(By.XPATH, "//div[contains(@class, 'SpanNewMessage')]")
                div = driver.find_element(By.XPATH, "//div[contains(@class, 'SpanNewMessage')]/..")

                if element.is_displayed():
                    div.click()
            except:
                response = ""
                pass  # Ignorar si no hay notificaciones nuevas

            messages = driver.find_elements(By.XPATH, "//p[contains(@class, 'css-1rdxtjl-PText')]")

            # Verificar solicitudes de mensajes
            try:
                request = driver.find_element(By.XPATH, "//div[contains(@class, 'DivRequestGroup')]")
            except:
                request = None

            if request:
                request.click()
                try:
                    divs = driver.find_elements(By.XPATH, "//div[contains(@class, 'DivItemWrapper')]")
                    for user in divs:
                        user.click()
                        ok_btns = driver.find_elements(By.XPATH, "//div[contains(@class, 'DivItem')]")
                        for btn in ok_btns:
                            if btn.text in ("Aceptar", "Accept", "Ok", "Send"):
                                btn.click()
                                break
                except Exception:
                    response = ""
                    pass
                driver.get("https://tiktok.com/messages")

            # Procesar último mensaje
            if messages:
                last_message_element = messages[-1]
                last_message = last_message_element.text

                if last_message.startswith(prefix):
                    last_message_id = last_message_element.get_attribute("data-message-id")  
                    if last_message_id in self.__processedmsj__:
                        return ""
                    self.__processedmsj__.add(last_message_id)

                    # Verificar si el link pertenece al bot
                    links = driver.find_elements(By.XPATH, "//a[contains(@class, 'css-1qxabns-StyledLink')]")
                    if links:
                        last_link = links[-1]
                        if last_link.get_attribute("href") == f"https://www.tiktok.com/@{bot_username}":
                            return ""

                    # Medir tiempo de respuesta
                    start_time = time.time()
                    response = last_message
                    elapsed_time = time.time() - start_time

                    if elapsed_time > 3:
                        return None

                    # Seleccionar chat para responder
                    try:
                        title = driver.find_element(By.XPATH, "//h1[contains(@data-e2e, 'message-title')]")
                        title.click()
                    except:
                        raise ElementNotFoundError("title")

                    return response
        except Exception as e:
            raise ActionFailedError("listen", e)

        time.sleep(0.5)

    @staticmethod
    def test(*args) -> None:
        print(*args)
