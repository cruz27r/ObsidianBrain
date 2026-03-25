---
tags: [project, active]
status: active
created: 2026-03-21
priority: high
tech: [next.js, tailwind-css-v4, typescript, vercel, stripe]
linked: [EuroSide - Brand Guidelines]
---

> [!status-active] Status — Active · Pending Real Photos + Go-Live Credentials

# EuroSide Automotive — Project Reference

## Goal
Build a premium, dark-themed website for EuroSide Automotive (Norwood, MA) — a European car specialist that does repair, diagnostics, performance tuning, and custom work. No online booking or pricing. Service requests go to shop email for manual response.

## Business Info
- **Name:** EuroSide Automotive
- **Location:** Norwood, Massachusetts (Greater Boston area)
- **Specialty:** European vehicles (VW, Audi, BMW, Mercedes, Porsche) + all makes
- **Instagram:** https://www.instagram.com/eurosideauto/
- **Services:** Repair & Maintenance, Diagnostics, Performance & Tuning, Custom Work

## Tech Stack
- **Framework:** Next.js 16.2 (App Router, Turbopack)
- **Styling:** Tailwind CSS v4
- **Language:** TypeScript
- **Deployment:** Vercel (auto-deploy from git)
- **Payments:** Stripe (hosted checkout links — merch only)
- **Email:** Nodemailer (Gmail App Password) — service request form
- **Dev port:** localhost:3000

## Repo Location
`/Users/itocruz/Desktop/EuroSide/euroside/`

---

## Brand Guidelines

> [!color-token] Color Tokens — source of truth: `globals.css @theme`
> **orange** `#E8511A` — CTAs, accents, "Euro" in logo
> **blue** `#4DB6E8` — Nav active/hover, labels, "side" in logo
> **bg** `#141414` — Page background
> **surface** `#1c1c1c` — Cards, inputs
> **border** `#2e2e2e` — Borders, dividers
> **body-bg** `#181510` — Warm charcoal on `<body>`
> **surface-warm** `#1e1a12` — Cards/inputs (warm variant)
> **text** `#e2d5c3` — Main readable text
> **text-secondary** `#d8c8b0` — Supporting text
> **text-hint** `#c8b89a` — Captions, hints
>
> **Rule:** Never hardcode hex values. Always reference `@theme` tokens.

### Fonts
- `--font-display` — headings / brand name
- `--font-body` — body copy
Both defined in `globals.css @theme`.

### Logo
- File: `brand_assets/logo.png` (also at `public/images/logo.png`)
- Logo text: **"Euro"** in orange (`#E8511A`) + **"side"** in blue (`#4DB6E8`)
- Source of truth: `brand_assets/` — always check here before any brand task

### Logo in context
- `src/components/Navbar.tsx` — logo-only navbar, height `h-24`
- `src/components/Footer.tsx` — Euro/side color split, Instagram link

### Design Direction
- Dark theme — premium, automotive, industrial
- Clean and modern — not generic template style
- High-quality imagery as anchor for each section
- Diagonal SVG cuts between sections (homepage)
- Asymmetric grid layouts

---

## Image Asset Map

> [!brand-blue] Asset Map
> | Location | Contents |
|---|---|
| `brand_assets/` | logo.png, shop-exterior.jpg, diagnostics-equipment.jpg, hoodies.jpg, airfreshner.jpg |
| `public/images/hero/` | shop-exterior.jpg |
| `public/images/projects/` | audi-rs3-stage2.jpg, bmw-x3-hood-open.jpg, euroside-vw-lot.jpg, honda-civic-diagnostics.jpg, mercedes-r-lot.jpg, porsche-cayman-coilovers.jpg, vw-gti-exhaust.jpg |
| `public/images/services/` | repair.jpg, diagnostics.jpg, performance.jpg, custom.jpg |
| `public/images/merch/` | air-freshener.jpg, floor-mats.jpg, hoodie.jpg, tshirt.jpg |

**⚠ Placeholder images still needing real EuroSide photos:**
- `porsche-cayman-coilovers.jpg` — Unsplash placeholder
- `honda-civic-diagnostics.jpg` — Unsplash placeholder
- `performance.jpg` (services) — Unsplash placeholder
- `tshirt.jpg` (merch) — Unsplash placeholder
- `floor-mats.jpg` (merch) — Unsplash placeholder

**Instagram source:** https://www.instagram.com/eurosideauto/ — primary source for real work photos. Instagram blocks automated access — download manually.

---

## Pages & Routes

| Route | Purpose |
|---|---|
| `/` | Homepage — Hero, brands, services overview, featured projects, CTA |
| `/services` | Full services detail — Maintenance, Diagnostics, Performance, Custom |
| `/gallery` | Projects gallery with optional brand filter (BMW, Audi, VW, Mercedes, Other) |
| `/request` | Service request form — sends to shop email |
| `/merch` | Product listing with Stripe checkout links |
| `/podcast` | Future expansion (scaffolded, not active) |
| `/api/request-service` | API route — handles form submission, sends email |

---

## Key Components

| File | What it does |
|---|---|
| `src/app/layout.tsx` | Root layout, sets body bg `#181510` |
| `src/app/globals.css` | All `@theme` color + font tokens |
| `src/components/Navbar.tsx` | Logo-only navbar, scrolled state |
| `src/components/Footer.tsx` | Euro/side color branding, Instagram link |
| `src/components/ServiceCard.tsx` | Reusable card for services |
| `src/components/ProjectCard.tsx` | Gallery item card |
| `src/components/BrandFilter.tsx` | Filter bar for gallery |
| `src/components/Lightbox.tsx` | Image lightbox for gallery |
| `src/components/FormField.tsx` | Reusable form input |
| `src/components/PhotoUpload.tsx` | 1–5 image upload for request form |

---

## Data Structures

### Services (`src/data/services.ts`)
```ts
interface Service {
  id: string           // 'repair' | 'diagnostics' | 'performance' | 'custom'
  title: string
  description: string
  imageSrc: string     // /images/services/filename.jpg
  ctaLabel: string
  ctaHref: string      // /request?service={id}
}
```

### Projects/Gallery (`src/data/projects.ts`)
Each entry: image path + vehicle name + short description. Designed to be easily swappable.

### Merch (`src/data/merch.ts`)
```ts
interface MerchItem {
  id: string
  name: string
  description: string
  price: number        // USD cents (e.g. 3500 = $35.00)
  displayPrice: string // pre-formatted '$35.00'
  currency: 'USD'
  imageSrc: string
  stripeLink: string   // Stripe Checkout hosted URL
}
```
**Current merch:** Air Freshener ($8), Hoodie ($55), T-Shirt ($35), Floor Mats ($45)

---

## Service Request System

**What it is:** Contact form that emails the shop — NOT a booking or pricing system.

**Form fields:**
- Customer: name, email, phone, preferred contact method
- Vehicle: year, make, model, mileage (optional)
- Request: service type dropdown + description
- Images: 1–5 photo uploads
- Scheduling: preferred date (optional)

**Flow:** Form → `/api/request-service` → Nodemailer → shop Gmail → manual response

**Owner workflow:** Receives email → contacts customer → confirms date/time → optionally gives time estimate (never price)

---

## Business Rules (Hard Constraints)
- No instant booking — all scheduling is manual
- No price quotes on website
- All service type CTAs link to `/request?service={type}` — never hardcode different paths
- No admin dashboard for v1

---

## Pending Before Go-Live

> [!warning] Blockers — not live yet
> - [ ] Add real Gmail App Password to `.env.local` (currently placeholder)
> - [ ] Replace Stripe placeholder links in `src/data/merch.ts`
> - [ ] Replace Unsplash placeholder images with real EuroSide photos (see list above)
> - [ ] Get real customer Instagram photos for gallery (download manually from @eurosideauto)

---

## Image Swap Protocol
When replacing any image:
1. Rename the new file to change its URL
2. Delete `.next/` entirely
3. Restart dev server (`npm run dev`)
4. Hard-refresh browser (Cmd+Shift+R)
Never claim image is updated until all 4 steps are confirmed.

---

## Plans & Docs
- Full implementation plan: `/Users/itocruz/Desktop/EuroSide/docs/superpowers/plans/2026-03-20-euroside-website.md`
- Project CLAUDE.md: `/Users/itocruz/Desktop/EuroSide/CLAUDE.md`

## Notes
- 2026-03-21: Website built. Pending real photos and go-live credentials. CodeMSC copy of euroside folder removed — canonical repo is at `/Users/itocruz/Desktop/EuroSide/`.
