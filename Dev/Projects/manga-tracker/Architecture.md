---
tags: [project, manga, web-app, architecture]
status: planning
created: 2026-03-24
---

# Manga/Manhwa Tracker — Architecture

A chapter-level manga and manhwa reading tracker. Track what you're on, how many chapters behind you are from the latest release, and organize titles into lists. Designed to expand into a social reading platform (sharing lists, follows, comment threads) post-MVP.

## Links
- [[Initial Data]] — starting title dataset + tier logic
- Related: [[Dev/Projects/Discord Bot/Dev Log]]

---

## Core MVP Features

1. Title search + add to tracker (via MangaDex API)
2. Chapter-level progress — log last chapter read per title
3. Live chapter sync — auto-pull latest released chapter
4. "Chapters behind" counter (`latest_chapter - last_read`)
5. Reading status — Not Started / Reading / Caught Up / On Hold / Dropped
6. Reading lists — organize titles into named, shareable lists
7. Dashboard — recently updated + biggest backlogs

---

## Tech Stack

| Layer | Choice | Why |
|-------|--------|-----|
| Frontend | Next.js 14 (App Router) + TypeScript | SSR for public profiles/SEO, RSC for feeds |
| Styling | Tailwind CSS + shadcn/ui | Fast composition, accessible primitives |
| State | Zustand (UI) + TanStack Query (server) | Optimistic chapter updates feel instant |
| Forms | React Hook Form + Zod | End-to-end type safety |
| Backend | Node.js + Fastify + TypeScript | Typed, fast, plugin ecosystem |
| ORM | Drizzle ORM | Zero-overhead SQL, schema-first, edge-compatible |
| Database | PostgreSQL via Supabase | Relational integrity + native FTS |
| Cache | Redis via Upstash | MangaDex response cache, rate limiting |
| Auth | Supabase Auth | Email + Google OAuth out of the box |
| Storage | Supabase Storage | User avatars, custom cover uploads |
| Job Queue | BullMQ (Redis-backed) | Background chapter sync cron |
| Hosting | Vercel (web) + Supabase (DB/API) | Minimal infra for MVP |

---

## Data Sources

### MangaDex API (primary — free, public)
- `GET /manga?title=` — title search
- `GET /manga/{id}` — metadata (title, author, cover, genres)
- `GET /chapter?manga={id}&order[chapter]=desc&limit=1` — latest released chapter
- Rate limit: ~5 req/s → buffer with Redis cache (1–2h TTL on latest chapter)

### MangaUpdates (fallback)
- For titles not indexed on MangaDex

### Anilist GraphQL (post-MVP enrichment)
- Popularity scores, ratings, seasonal data

---

## Data Model

```
User
  id, username, email, avatar_url, is_private, created_at

Title  (shared global catalog, cached from MangaDex)
  id, external_id (MangaDex uuid), source, slug, title, description
  cover_url, type (manga|manhwa|manhua), release_status (ongoing|completed|hiatus)
  genres: text[], latest_chapter: numeric, latest_chapter_synced_at

ReadingEntry  (user's per-title tracking row)
  id, user_id → User, title_id → Title
  status: not_started | reading | caught_up | on_hold | dropped
  last_read_chapter: numeric | null
  last_read_at: timestamp | null
  chapters_behind: COMPUTED (latest_chapter - last_read_chapter)
  visibility: public | friends | private
  notes: text | null
  UNIQUE(user_id, title_id)

ReadingList
  id, user_id, name, description, visibility, cover_url

ReadingListTitle  (M:N)
  list_id, title_id, sort_order

Comment  (Post-MVP — polymorphic)
  id, author_id, target_type (title|list|entry), target_id
  parent_id (for threading), body, created_at, deleted_at

Follow  (Post-MVP)
  follower_id, followee_id, status (pending|accepted)
```

### Critical DB Indexes
```sql
CREATE INDEX idx_entry_user    ON reading_entries(user_id, status);
CREATE INDEX idx_comment_tgt   ON comments(target_type, target_id, created_at);
CREATE INDEX idx_follow_flwr   ON follows(follower_id);
CREATE INDEX idx_follow_flwe   ON follows(followee_id);
CREATE INDEX idx_book_fts      ON titles USING GIN(to_tsvector('english', title));
```

---

## API Routes (`/api/v1/`)

```
TITLES
  GET  /titles/search?q=          search MangaDex + local catalog
  POST /titles/import             import + cache a title from MangaDex
  GET  /titles/:id                title detail + latest chapter
  POST /titles/:id/sync           force chapter refresh (rate-limited)

READING ENTRIES
  GET    /me/entries              full shelf, filterable by status, sortable
  POST   /me/entries              add title to tracker
  PATCH  /me/entries/:id          update progress, status, visibility, notes
  DELETE /me/entries/:id

LISTS
  GET/POST       /me/lists
  GET/PATCH/DEL  /lists/:id
  POST/DEL       /lists/:id/titles
  PATCH          /lists/:id/titles/reorder

SOCIAL (Post-MVP)
  POST /users/:id/follow
  GET  /me/feed
  POST /users/:id/suggest
  GET/POST/PATCH/DEL /comments
```

---

## Chapter Sync Architecture

```
User adds title
  → POST /titles/import
  → Fetch MangaDex metadata + latest chapter number
  → Store in titles table
  → Create ReadingEntry { status: 'not_started' }

Background Cron (every 2 hours via BullMQ)
  → Query: titles WHERE release_status = 'ongoing'
      AND latest_chapter_synced_at < NOW() - INTERVAL '2 hours'
  → Fetch latest chapter from MangaDex per title
  → Update titles.latest_chapter + synced_at
  → (Post-MVP) push notification to users tracking this title

On-demand sync
  → POST /titles/:id/sync
  → Rate-limited: 1 per title per 30 min per user
```

---

## Frontend Routes (Next.js App Router)

```
app/
  (public)/
    page.tsx                    landing + feature overview
    titles/[id]/page.tsx        title detail (SSR for SEO)
    [username]/page.tsx         public profile (Post-MVP)
  (auth)/
    login/, register/
  (app)/                        authenticated shell + nav sidebar
    dashboard/page.tsx          recently updated + chapters-behind summary
    tracker/page.tsx            full reading list (filter by status)
    lists/page.tsx              my lists index
    lists/[id]/page.tsx         list detail + edit
    search/page.tsx             search + add new titles
    settings/page.tsx
```

---

## Monorepo Structure (Turborepo)

```
/
  apps/
    web/          Next.js frontend
    api/          Fastify backend
  packages/
    db/           Drizzle schema + migrations
    shared/       Zod schemas, TypeScript types, constants
  turbo.json
  package.json
```

---

## MVP Scope

**Ships in v1.0:**
- Auth (email + Google)
- Title search + add via MangaDex
- Chapter progress tracking + chapters-behind counter
- Reading status management
- Background chapter sync cron
- Reading lists (create, add, reorder)
- Dashboard with recently read + biggest backlogs
- Responsive web

**Post-MVP:**
- Social follows, public profiles, sharing
- Comment threads
- Notifications on new chapter releases
- Ratings + reviews
- Goodreads/AniList import
- Mobile app (React Native)

---

## Critical Files (build order)

1. `packages/db/schema.ts` — Drizzle schema (everything depends on this)
2. `apps/api/src/services/mangadex.ts` — MangaDex API client
3. `apps/api/src/jobs/chapter-sync.ts` — background cron
4. `apps/api/src/routes/entries.ts` — core reading entry CRUD
5. `apps/web/src/app/(app)/tracker/page.tsx` — main view
