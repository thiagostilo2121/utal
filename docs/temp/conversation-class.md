# Conversation Class

The `conversation` class in `utal` is a `by structure` class that handles everything related to the currently active or open conversation in the bot's DM. An example is the `send` function, which sends a text message to the current conversation.

## Methods
- Parameters enclosed in `[brackets]` are optional.
- Parameters enclosed in `(parentheses)` are required.

| Method                | Parameters   | Function                                                         |
|-----------------------|--------------|-----------------------------------------------------------------|
| `send`                | `(*args)`    | Sends a message to the current conversation                     |
| `get_user_username`   | *No params*  | Retrieves the username of the user in the current conversation  |
| `get_user_nickname`   | *No params*  | Retrieves the nickname of the user in the current conversation  |
| `get_user_avatar_URL` | *No params*  | Retrieves the avatar URL of the user in the current conversation |
| `send_image`          | `(img_path)` | Sends an image to the current conversation                      |

## Parameters
- `send -> (*args)` Arguments to send in the text message. Example: `send(args="Hello world!")`.

- `send_image -> (img_path)` Path of the image to send. Example: `send_image(img_path="path/to/image")`.