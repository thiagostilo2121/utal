# Messages Class

The `messages` class in `utal` is a `by structure` class that handles everything related to the message bar in the bot's DM. An example is the `send_message_to_user_by_nickname` function, which sends a text message to a specific user by locating them through their nickname.

## Methods
- Parameters enclosed in `[brackets]` are optional.
- Parameters enclosed in `(parentheses)` are required.

| Method                              | Parameters               | Function                                                                                   |
|-------------------------------------|-------------------------|-------------------------------------------------------------------------------------------|
| `get_count`                         | *No params*             | Retrieves the number of users in the message inbox                                        |
| `set_title`                         | `(title)`               | Edits the HTML title of the message inbox                                                 |
| `send_message_to_user_by_nickname`  | `(nickname)` `(*args)`  | Sends a text message to a specific user by locating them through their nickname          |
| `find_user_by_nickname`             | `(nickname)`            | Returns a boolean indicating whether the chat of a user was found by locating them through their nickname |
| `enter_user_chat_by_nickname`       | `(nickname)`            | Enters a user's chat by locating them through their nickname                             |

## Parameters
- `set_title -> (title)` Title to set. Example: `set_title(title="My Title")`.

- `send_message_to_user_by_nickname -> (nickname)` Nickname of the user to send the text message. Example: `send_message_to_user_by_nickname(nickname="user nickname")`.

- `send_message_to_user_by_nickname -> (*args*)` Text message to send. Example: `send_message_to_user_by_nickname(args="Hello world!")`.

- `find_user_by_nickname -> (nickname)` Nickname of the user to locate. Example: `find_user_by_nickname(nickname="user nickname")`.

- `enter_user_chat_by_nickname -> (nickname)` Nickname of the user to locate and enter their chat. Example: `enter_user_chat_by_nickname(nickname="user nickname")`.