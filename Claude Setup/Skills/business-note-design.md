---
name: business-note-design
description: "Design and structure Business vault notes — client projects, agency work, brand guidelines. Applies EuroSide brand callouts, color token blocks, and correct structure for the Business domain."
---

# Business Note Design

Use this skill when creating or editing any note in `Business/`.

## CSS Dependencies
- `business-styles.css` — always enabled (brand callouts, color token block)
- `business-tables.css` — **disabled by default**, toggle ON only when editing EuroSide notes, OFF when done

## Required Structure

Every client project note follows this layout:

```markdown
---
tags: [project, active]
status: active | planning | complete
created: YYYY-MM-DD
priority: high | medium | low
tech: [stack]
linked: []
---

> [!status-<status>] Status — <Status> · <one-line context>

# Client Name — Project Reference

## Goal
One sentence.

## Business Info
Key client details (name, location, specialty, contact).

> [!color-token] Color Tokens
> **primary** `#hex` — use case
> **secondary** `#hex` — use case
> **bg** `#hex` — background
> **text** `#hex` — body text

> [!brand-orange] Brand Guidelines
> Fonts, logo usage, design direction, rules.

## Tech Stack
Framework, hosting, integrations.

> [!brand-blue] Image Asset Map
> | Location | Contents |
> |---|---|
> | path/ | files |

## Pages & Routes
| Route | Purpose |

## Key Components
| File | What it does |

## Business Rules
Hard constraints — what this project NEVER does.

> [!warning] Pending / Blockers
> - [ ] blocker 1
> - [ ] blocker 2

## Related
- [[relevant notes]]
```

## Callout Reference

| Callout | Purpose | Color |
|---------|---------|-------|
| `[!status-active]` | Status banner | Green (from dev-styles) |
| `[!color-token]` | Brand color palette display — monospace, dark bg | Orange border |
| `[!brand-orange]` | Brand voice sections, guidelines | EuroSide orange `#E8511A` |
| `[!brand-blue]` | Tech/UI decision sections, asset maps | EuroSide blue `#4DB6E8` |
| `[!warning]` | Blockers and pending items | Orange (from clean-polish) |

## EuroSide Brand Colors (pre-loaded)
- **orange** `#E8511A` — CTAs, accents, "Euro" in logo
- **blue** `#4DB6E8` — Nav active/hover, "side" in logo
- **bg** `#141414` — Page background
- **surface** `#1c1c1c` — Cards, inputs
- **border** `#2e2e2e` — Dividers
- **body-bg** `#181510` — Warm charcoal on `<body>`
- **text** `#e2d5c3` — Main readable text

**Rule:** Never hardcode hex values in components. Always use `@theme` tokens.

## business-tables.css Toggle Rule
When editing EuroSide notes: enable `business-tables.css` in Settings > Appearance > CSS Snippets.
When done: disable it. It makes all vault tables use orange headers if left on.

## Routing
- Client projects → `Business/Web Design Agency/Clients/<client>/`
- Agency-level docs → `Business/Web Design Agency/`
- Other ventures → `Business/<venture-name>/`

## Linking Rules
- Every client project links to relevant `Knowledge/Tech Concepts/` notes
- EuroSide links to `Knowledge/Design Patterns/` for patterns used in Next.js components

## After Creating/Editing
Commit with: `update: EuroSide <what changed>` or `add: <client> project note`
Push to main.
