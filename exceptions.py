class SeleniumError(Exception):
    """Base exception for Selenium-related errors."""
    pass

class DriverNotProvidedError(SeleniumError):
    """Raised when the 'driver' argument is missing or not initialized."""
    def __init__(self, function_name):
        super().__init__(f"The 'driver' argument is missing or not initialized in '{function_name}'. Make sure to pass a valid Selenium WebDriver instance.")

class ElementNotFoundError(SeleniumError):
    """Raised when a required element cannot be found."""
    def __init__(self, element_description):
        super().__init__(f"Element not found: '{element_description}'. Ensure the locator is correct and the element is visible.")

class ActionFailedError(SeleniumError):
    """Raised when an action fails to execute properly."""
    def __init__(self, action_description, original_exception):
        super().__init__(f"Failed to execute action: '{action_description}'. Error: '{original_exception}'")

class MessageSendError(SeleniumError):
    """Raised when a message fails to send."""
    def __init__(self, message_content):
        super().__init__(f"Failed to send message: '{message_content}'. Check if the chat input field is accessible.")

class UserNotFoundError(SeleniumError):
    """Raised when a user cannot be found in the chat list."""
    def __init__(self, username):
        super().__init__(f"User '{username}' not found in the chat list. Ensure the nickname is correct.")
