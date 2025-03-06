from utal import *

class PyUTAL:
    def __init__(self, driver):
        self.__processedmsj__ = set()
        self.driver = driver
        self.client = Client(self.driver, self.__processedmsj__)
        self.conversation = Conversation(self.driver)
        self.messages = Messages(self.driver)