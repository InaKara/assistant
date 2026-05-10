#!/usr/bin/env python3
"""ntfy.sh push notification client for the life-assistant ecosystem.

Sends notifications to ntfy.sh. Reads NTFY_TOPIC and optionally NTFY_SERVER
from environment variables or a sibling .env file.

CLI usage:
    python notify.py <title> <message> [priority]

Priority values: min | low | default | high | max  (default: default)

Example:
    python notify.py "Maintenance due" "Review your backlog" high
"""

import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


_VALID_PRIORITIES = frozenset({"min", "low", "default", "high", "max"})
_DEFAULT_SERVER = "https://ntfy.sh"
_ENV_FILE = Path(__file__).parent / ".env"


def _load_env_file(path: Path) -> None:
    """Load KEY=VALUE pairs from a .env file into os.environ.

    Args:
        path: Path to the .env file. No-op if the file does not exist.
    """
    if not path.is_file():
        return
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            # Strip surrounding quotes that some .env editors add
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _get_config() -> tuple[str, str]:
    """Read the ntfy server URL and topic from the environment.

    Returns:
        Tuple of (server_url, topic_name).

    Raises:
        SystemExit: If NTFY_TOPIC is not set.
    """
    topic = os.environ.get("NTFY_TOPIC", "").strip()
    if not topic:
        print("ERROR: NTFY_TOPIC is not set. Add it to .env or export it.", file=sys.stderr)
        sys.exit(1)
    server = os.environ.get("NTFY_SERVER", _DEFAULT_SERVER).rstrip("/")
    return server, topic


def _validate_priority(priority: str) -> str:
    """Validate and normalise a priority label.

    Args:
        priority: Priority label to validate.

    Returns:
        Normalised priority label in lowercase.

    Raises:
        ValueError: If the label is not a recognised ntfy priority.
    """
    normalised = priority.lower().strip()
    if normalised not in _VALID_PRIORITIES:
        raise ValueError(
            f"Invalid priority '{priority}'. Valid values: {', '.join(sorted(_VALID_PRIORITIES))}"
        )
    return normalised


def send_notification(title: str, message: str, priority: str = "default") -> None:
    """Send a push notification to the configured ntfy topic.

    Reads NTFY_TOPIC and NTFY_SERVER from the environment or sibling .env file.
    Exits with code 1 on HTTP or connection errors.

    Args:
        title: Notification title shown in bold on the receiving device.
        message: Notification body text.
        priority: Delivery priority — min | low | default | high | max.

    Raises:
        ValueError: If priority is not a recognised label.
    """
    _load_env_file(_ENV_FILE)
    server, topic = _get_config()
    priority = _validate_priority(priority)

    req = urllib.request.Request(
        url=f"{server}/{topic}",
        data=message.encode(),
        headers={
            "Title": title,
            "Priority": priority,
            "Content-Type": "text/plain; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=10):
            pass  # Any 2xx response indicates success
    except urllib.error.HTTPError as e:
        error_body = e.read().decode(errors="replace")
        print(f"ERROR: HTTP {e.code} from ntfy — {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Could not reach ntfy server — {e.reason}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    """Entry point for CLI invocation.

    Parses positional arguments and delegates to send_notification.

    Usage: python notify.py <title> <message> [priority]
    """
    if len(sys.argv) < 3:
        script = Path(__file__).name
        print(f"Usage: python {script} <title> <message> [priority]", file=sys.stderr)
        print(f"Priority: {' | '.join(sorted(_VALID_PRIORITIES))} (default: default)", file=sys.stderr)
        sys.exit(1)

    title = sys.argv[1]
    message = sys.argv[2]
    priority = sys.argv[3] if len(sys.argv) > 3 else "default"

    send_notification(title, message, priority)
    print(f"Sent [{priority}] {title!r}")


if __name__ == "__main__":
    main()
