#!/usr/bin/env python3
"""Poll the ntfy inbox topic for new messages sent from the phone.

Fetches messages posted since the last poll, appends them to
knowledge/inbox.md as a checklist, and updates the last-poll timestamp.

CLI usage:
    python poll_inbox.py
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


_DEFAULT_SERVER = "https://ntfy.sh"
_REPO_ROOT = Path(__file__).parent.parent.parent  # services/notifier/ → repo root
_INBOX_FILE = _REPO_ROOT / "knowledge" / "inbox.md"
_LAST_POLL_FILE = Path(__file__).parent / ".last-poll"
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
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def _get_config() -> tuple[str, str]:
    """Read ntfy server URL and inbox topic from the environment.

    Returns:
        Tuple of (server_url, inbox_topic_name).

    Raises:
        SystemExit: If NTFY_INBOX_TOPIC is not set.
    """
    topic = os.environ.get("NTFY_INBOX_TOPIC", "").strip()
    if not topic:
        print("ERROR: NTFY_INBOX_TOPIC is not set. Add it to .env or export it.", file=sys.stderr)
        sys.exit(1)
    server = os.environ.get("NTFY_SERVER", _DEFAULT_SERVER).rstrip("/")
    return server, topic


def _read_last_poll_time() -> int:
    """Return the Unix timestamp of the last successful poll.

    Returns:
        Unix timestamp, or 0 if the service has never been polled.
    """
    if _LAST_POLL_FILE.is_file():
        try:
            return int(_LAST_POLL_FILE.read_text().strip())
        except ValueError:
            pass
    return 0


def _save_poll_time(timestamp: int) -> None:
    """Persist the poll timestamp so the next run only fetches newer messages.

    Args:
        timestamp: Unix timestamp to save.
    """
    _LAST_POLL_FILE.write_text(str(timestamp))


def fetch_messages(server: str, topic: str, since: int) -> list[dict]:
    """Fetch messages from ntfy posted after the given Unix timestamp.

    Uses the ntfy polling API (ndjson, one message per line).

    Args:
        server: ntfy server base URL.
        topic: ntfy topic name.
        since: Return only messages newer than this Unix timestamp.

    Returns:
        List of ntfy message dicts. Empty if no new messages.

    Raises:
        SystemExit: On HTTP or connection errors.
    """
    url = f"{server}/{topic}/json?poll=1&since={since}"
    req = urllib.request.Request(url, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            body = response.read().decode()
    except urllib.error.HTTPError as e:
        error_body = e.read().decode(errors="replace")
        print(f"ERROR: HTTP {e.code} from ntfy — {error_body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"ERROR: Could not reach ntfy — {e.reason}", file=sys.stderr)
        sys.exit(1)

    messages = []
    for line in body.strip().splitlines():
        if not line:
            continue
        try:
            msg = json.loads(line)
            # Skip keepalive and open events — only real messages
            if msg.get("event") == "message":
                messages.append(msg)
        except json.JSONDecodeError:
            pass
    return messages


def append_to_inbox(messages: list[dict]) -> int:
    """Append new messages to knowledge/inbox.md as unchecked checklist items.

    Creates inbox.md with a header if it does not yet exist.

    Args:
        messages: List of ntfy message dicts to append.

    Returns:
        Number of messages appended.
    """
    if not messages:
        return 0

    _INBOX_FILE.parent.mkdir(parents=True, exist_ok=True)
    if not _INBOX_FILE.is_file():
        _INBOX_FILE.write_text(
            "# Inbox\n\n"
            "Messages sent from phone. Processed by the assistant at session startup.\n"
            "Mark items `[x]` once handled.\n\n"
            "---\n"
        )

    with open(_INBOX_FILE, "a", encoding="utf-8") as f:
        for msg in messages:
            ts = datetime.fromtimestamp(
                msg.get("time", 0), tz=timezone.utc
            ).strftime("%Y-%m-%d %H:%M UTC")
            title = msg.get("title", "").strip()
            body = msg.get("message", "").strip()
            # Format: - [ ] [timestamp] **title** — body  (or just body if no title)
            if title:
                f.write(f"\n- [ ] [{ts}] **{title}** — {body}")
            else:
                f.write(f"\n- [ ] [{ts}] {body}")

    return len(messages)


def main() -> None:
    """Poll ntfy inbox and append any new messages to knowledge/inbox.md."""
    _load_env_file(_ENV_FILE)
    server, topic = _get_config()

    since = _read_last_poll_time()
    now = int(datetime.now(tz=timezone.utc).timestamp())

    messages = fetch_messages(server, topic, since)
    count = append_to_inbox(messages)

    _save_poll_time(now)

    if count:
        print(f"{count} new message(s) added to inbox.md.")
    else:
        print("No new messages.")


if __name__ == "__main__":
    main()
