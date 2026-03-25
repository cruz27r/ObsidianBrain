#!/usr/bin/env python3
"""
Stop hook — session boundary logging.
Fires when Claude finishes a response turn.
Appends a timestamp entry to ~/.claude/sessions/summary.log.
"""

import sys
import json
import os
from datetime import datetime

CLAUDE_DIR = os.path.expanduser("~/.claude")
SESSIONS_DIR = os.path.join(CLAUDE_DIR, "sessions")
LOG_FILE = os.path.join(SESSIONS_DIR, "summary.log")

def main() -> None:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except (json.JSONDecodeError, Exception):
        data = {}

    os.makedirs(SESSIONS_DIR, exist_ok=True)

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "session_id": data.get("session_id", ""),
        "stop_reason": data.get("stop_reason", ""),
    }

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

if __name__ == "__main__":
    main()
