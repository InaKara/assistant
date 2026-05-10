# Function Registry

> Auto-maintained by Copilot. Do not remove entries manually — update them through code changes.

## `services/notifier/notify.py`

ntfy.sh push notification client for the life-assistant ecosystem. Sends notifications to ntfy.sh using environment-configured credentials. Usable as a CLI command or imported as a module.

| Function | Description |
|---|---|
| `send_notification(title, message, priority)` | Send a push notification to the configured ntfy topic. |
| `main()` | Parse CLI arguments and invoke send_notification. |
| `_load_env_file(path)` | Load KEY=VALUE pairs from a .env file into os.environ. |
| `_get_config()` | Read the ntfy server URL and topic from the environment. |
| `_validate_priority(priority)` | Validate and normalise an ntfy priority label. |

## `services/notifier/poll_inbox.py`

Polls the ntfy inbox topic for messages sent from the phone and appends them to knowledge/inbox.md as an unchecked checklist. Called at agent session startup to surface queued phone messages.

| Function | Description |
|---|---|
| `fetch_messages(server, topic, since)` | Fetch ntfy messages posted after a given Unix timestamp. |
| `append_to_inbox(messages)` | Append new messages to knowledge/inbox.md as checklist items. |
| `main()` | Poll ntfy inbox and append new messages to inbox.md. |
| `_load_env_file(path)` | Load KEY=VALUE pairs from a .env file into os.environ. |
| `_get_config()` | Read ntfy server URL and inbox topic from the environment. |
| `_read_last_poll_time()` | Return the Unix timestamp of the last successful poll. |
| `_save_poll_time(timestamp)` | Persist the poll timestamp for the next run. |
