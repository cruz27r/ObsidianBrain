---
name: client-update
description: "Generate a clean, non-technical client-facing update from dev work — git diff, task list, or verbal summary. Tailored for agency/freelance delivery."
---

# Client Update Generator

Turn technical dev work into a clear, professional update ready to send to a client. No jargon, no implementation details — just what changed, what it means for them, and what's next.

## When to Use
- After completing a feature or milestone
- Before a client check-in call
- When sending a weekly progress update
- When a client asks "what's been done?"

## Process

1. **Get the work summary** — ask the user for one of:
   - A git log / diff (`git log --oneline` or `git diff`)
   - A list of completed tasks
   - A verbal description of what was done
2. **Identify the client** — ask which client/project if not obvious. Load their context if available (e.g. EuroSide = automotive website, non-technical owner).
3. **Draft the update** in the format below.
4. **Show the draft** for approval before finalizing.

## Output Format

```
Hi [Client Name],

Here's a quick update on [Project Name]:

**What's done:**
- [Plain English description of change — focus on what they can see or experience]
- [Another change]

**What it means:**
[1-2 sentences on the real-world impact — faster load, new page live, form working, etc.]

**What's next:**
- [Next milestone or pending item]
- [Any blocker that needs their input — e.g. real photos, credentials]

Let me know if you have any questions or want to hop on a call.

[Your name]
```

## Tone Rules
- No technical terms (no "API", "component", "TypeScript", "deploy" unless explained)
- Confident and professional — not overly casual
- Short — a client update should take 30 seconds to read
- If something is blocked on the client (missing photos, missing credentials), say it clearly but without blame

## EuroSide Context (pre-loaded)
- Client: EuroSide Automotive, Norwood MA
- Owner is non-technical — translate everything
- Project: premium dark-themed automotive website
- Stack: Next.js, Tailwind, Vercel, Stripe, Nodemailer
- Current blockers: Gmail App Password, real shop photos, Stripe links
- Pending items: Unsplash placeholder images need replacing with real EuroSide photos

## After Generating
Optionally save the update to the vault:
`Business/Web Design Agency/Clients/<ClientName>/Updates/<YYYY-MM-DD>-update.md`
