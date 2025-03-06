# PyUTAL Method

The `PyUTAL` method (actually a class) is essential in any `utal` application or bot, as it defines the `driver` to be used by all the library's methods.

If this method and/or class is not called in the code or is not correctly implemented, the program may encounter errors or fail to start due to the `driver` and other automatically defined variables not being properly set by `utal`.

## Usage:

```python
app = PyUTAL(driver)
app.client.listen()
```

To implement any `utal` method or class, use the defined variable (`app` in the previous example), for instance:

```python
app = PyUTAL(driver)

# Client methods
app.client.listen()

# Conversation methods
app.conversation.get_user_username()

# Messages methods
app.messages.get_count()
```