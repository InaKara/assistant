# Services Registry

<!-- Catalog of all reusable microservices. Maintained by service-architect. -->

| Service | Type | Status | Interface | How to Invoke |
|---|---|---|---|---|
| `notifier` | Local script | Active | CLI + importable Python function | `python services/notifier/notify.py <title> <message> [priority]` |
| `poll_inbox` | Local script | Active | CLI | `python services/notifier/poll_inbox.py` |
