---
name: obsidian-capture
description: "Process and route raw notes, ideas, or content into the ObsidianBrain vault with correct folder placement, frontmatter, and wikilinks."
---

# Obsidian Capture & Route

Turn raw input — a thought, a paste, a URL, a meeting note, a code snippet — into a properly structured vault note and route it to the right folder.

## Vault Location
`E:/ObsidianBrain/`

## Routing Rules

| Type of content | Destination |
|-----------------|-------------|
| Raw idea / quick thought / unprocessed | `00-Inbox/` |
| Coding project or engineering work | `Dev/Projects/<project-name>/` |
| Game dev, modding, engines | `Gaming/Projects/<game>/` or `Gaming/Modding/<game>/` |
| Reference, concept, tech knowledge | `Knowledge/Tech Concepts/` or `Knowledge/Algorithms/` |
| Business venture, client, agency work | `Business/<venture>/` |
| Career, job apps, interview prep | `Career/` (create if missing) |
| School, courses, assignments | `School/` (create if missing) |
| Meeting notes, session summaries | `00-Inbox/` (process later) |
| Claude setup changes | `Claude Setup/` |

## Process

1. **Understand the input** — ask one clarifying question if the type or destination is ambiguous. Never ask multiple questions at once.
2. **Determine destination** using the routing table above.
3. **Draft the note** with:
   - Frontmatter (`tags`, `status`, `created: YYYY-MM-DD`, and any relevant fields)
   - Clear heading structure
   - At least one `[[wikilink]]` to a related note — never create an isolated note
4. **Show the draft** and proposed file path before writing.
5. **Write the file** once confirmed (or immediately if the user says "just do it").
6. **Commit and push** to git after writing:
   ```bash
   cd "E:/ObsidianBrain"
   git add .
   git commit -m "add: <short description>"
   git push origin main
   ```

## Note Conventions

- Algorithm notes: include time/space complexity, when to use, TypeScript example
- Project notes: link to relevant Knowledge notes
- All notes: use `[[double bracket]]` wikilinks — never plain text references
- Dates: always use `YYYY-MM-DD` format
- No isolated notes — every note must link to at least one other

## Quick Capture Mode

If the user says "quick capture" or "just inbox this", skip the preview and write directly to `00-Inbox/` with minimal frontmatter. Still commit and push.
