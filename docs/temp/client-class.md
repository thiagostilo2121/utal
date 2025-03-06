# Client Class

The `client` class in `utal` is a `for server` class that handles everything related to the bot or application (soon to include username and nickname). For example, the `listen` function detects new messages, reads them, and identifies message requests.

## Methods
- Parameters enclosed in `[brackets]` are optional.
- Parameters enclosed in `(parentheses)` are required.

| Method   | Parameters             | Function                                                                                      |
|----------|------------------------|----------------------------------------------------------------------------------------------|
| `listen` | `[prefix]` `[my_self]` | Detects new messages, reads them, returns them, and also identifies new message requests.   |
| `test`   | `(*args)`              | Simply prints `*args`.                                                                       |

## Parameters
- `listen -> [prefix]` Returns only messages that start with the specified prefix. If no value is provided, it returns all messages (useful for a user-customizable prefix system). Example: `listen(prefix="/")`.

- `listen -> [my_self]` It is recommended to use this parameter to *exclude* messages sent by the bot itself. Example: `listen(my_self="@botusername")`.

- `test -> (*args)` Arguments to print. Example: `test(args="Hello world!")`.