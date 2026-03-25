#!/usr/bin/env python3
"""
UserPromptSubmit hook — CARL domain injection + prompt logging.
Reads prompt JSON from stdin, injects domain context if keywords matched,
logs to ~/.claude/history-local.jsonl.
"""

import sys
import json
import os
from datetime import datetime

CLAUDE_DIR = os.path.expanduser("~/.claude")
LOG_FILE = os.path.join(CLAUDE_DIR, "history-local.jsonl")

CARL_DOMAINS = {
    "SHOPIFY": ["shopify", "liquid", "storefront", "polaris", "myshopify"],
    "GAMING": ["unity", "godot", "phaser", "three.js", "minecraft mod", "webgl", "game dev"],
    "NOTES": ["obsidian", "notion", "zoom notes", "meeting notes", "transcript", "vault"],
    "CLOTHING-BRAND": ["clothing brand", "merch", "printify", "hoodie", "apparel", "brand identity"],
    "BOTS": ["discord bot", "slack bot", "discord.js", "bolt sdk", "slash command"],
    "DOCUMENTS": ["pdf", "word doc", "docx", "excel", "xlsx", "powerpoint", "google docs", "google sheets", "google slides"],
}

CARL_RULES = {
    "SHOPIFY": "Use shopify MCP + shopify-dev MCP for all Shopify work. Liquid templates follow Shopify's theme architecture. Use Polaris components for admin UI.",
    "GAMING": "Follow game engine conventions. For web games prefer Phaser or Three.js. Always profile before optimizing render loops.",
    "NOTES": "Use obsidian MCP for vault ops (requires Local REST API plugin). Use notion MCP for Notion. Never edit raw vault files directly when MCP is available.",
    "CLOTHING-BRAND": "Use printify MCP for product creation. Brand consistency: use brand-guidelines skill. Apparel copy should match brand voice.",
    "BOTS": "Discord bots: use discord.js v14 + slash commands. Slack bots: use Bolt SDK. Register slash commands in guild scope for dev, global for prod.",
    "DOCUMENTS": "PDF: use pdf-reader MCP. Word: use office-word MCP. Google Docs/Sheets/Slides: use google-workspace MCP. Never parse binary formats manually.",
}

def detect_domains(prompt_text: str) -> list[str]:
    text = prompt_text.lower()
    matched = []
    for domain, keywords in CARL_DOMAINS.items():
        if any(kw in text for kw in keywords):
            matched.append(domain)
    return matched

def log_prompt(data: dict, domains: list[str]) -> None:
    os.makedirs(CLAUDE_DIR, exist_ok=True)
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "session_id": data.get("session_id", ""),
        "prompt_snippet": data.get("prompt", "")[:200],
        "carl_domains": domains,
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

def main() -> None:
    try:
        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
    except (json.JSONDecodeError, Exception):
        data = {}

    prompt_text = data.get("prompt", "")
    domains = detect_domains(prompt_text)

    log_prompt(data, domains)

    if domains:
        rules = "\n".join(f"- **{d}**: {CARL_RULES[d]}" for d in domains)
        injection = f"<carl-rules>\n{rules}\n</carl-rules>"
        print(json.dumps({"system": injection}))

if __name__ == "__main__":
    main()
