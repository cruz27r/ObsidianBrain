---
tags: [index, design-patterns]
created: 2026-03-21
---

# Design Patterns — Index

Reusable solutions to common software design problems. Grouped into three categories.

## Creational (how objects are created)
- [ ] [[Singleton]] — one instance globally
- [ ] [[Factory]] — create objects without specifying exact class
- [ ] [[Builder]] — construct complex objects step by step

## Structural (how objects are composed)
- [ ] [[Adapter]] — bridge between incompatible interfaces
- [ ] [[Decorator]] — add behavior without changing original
- [ ] [[Proxy]] — control access to another object (also: Next.js middleware)

## Behavioral (how objects communicate)
- [ ] [[Observer]] — subscribe to events (EventEmitter, React state)
- [ ] [[Strategy]] — swap algorithms at runtime
- [ ] [[Command]] — encapsulate actions as objects

## Patterns we use in our stack
| Pattern | Where we use it |
|---|---|
| Observer | React state, EventEmitter in discord.js |
| Factory | discord.js command loader |
| Decorator | Next.js middleware, API route wrappers |
| Strategy | switching AI providers (Claude vs GPT-4o) |
| Singleton | Anthropic/OpenAI client instances in bot utils |
