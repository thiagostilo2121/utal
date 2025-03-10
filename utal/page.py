from utal.core import PyUTAL

class Page(PyUTAL):
    def __init__(self, driver): 
        self.driver = driver
    
    def wait_to_load(self):
        driver = self.driver

        while driver.execute_script("return document.readyState") != "complete":
            pass