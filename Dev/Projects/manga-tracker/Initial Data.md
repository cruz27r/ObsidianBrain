---
tags: [project, manga, data, seed]
status: active
created: 2026-03-24
---

# Manga Tracker — Initial Title Dataset

Seed data for the tracker. 130+ titles with chapter counts as of March 2026.

## Links
- [[Architecture]] — full project architecture

---

## Tier System

| Tier | Rule |
|------|------|
| **Current** | `read > 10` AND `pct >= 95%` |
| **Almost There** | `read > 10` AND `70% <= pct < 95%` |
| **In Progress** | `read > 10` AND `30% <= pct < 70%` |
| **Barely Started** | `read > 10` AND `pct < 30%` |
| **Not Started** | `read <= 10` (regardless of %) |

## Data Rules
- `read = max(0, total - unread)` — capped at 0 if `unread >= total`
- `pct = (read / total) * 100`
- LIVE badge shown on `ongoing = true` titles

---

## Dataset

| Title | Genre | Total | Unread | Ongoing |
|-------|-------|-------|--------|---------|
| Solo Leveling | System / Action | 179 | 0 | false |
| Fire Force | Shounen / Action | 304 | 0 | false |
| Jujutsu Kaisen | Shounen / Dark | 271 | 0 | false |
| The Promised Neverland | Shounen / Thriller | 181 | 181 | false |
| The God of High School | Martial / Shounen | 569 | 583 | false |
| Tomb Raider King | System / Adventure | 412 | 414 | false |
| Legend of the Northern Blade | Sword / Martial | 171 | 211 | false |
| Solo Leveling: Ragnarok | System / Action | 95 | 0 | true |
| One Piece | Shounen / Adventure | 1130 | 0 | true |
| Mercenary Enrollment | Mercenary / Modern | 195 | 0 | true |
| The Return of the 8th Class Mage | Mage / Regression | 175 | 0 | true |
| The Greatest Estate Developer | Strategy / Comedy | 223 | 0 | true |
| The Indomitable Martial King | Martial Arts / Action | 130 | 0 | true |
| The Regressed Demon Lord is Kind | Regression / Fantasy | 135 | 0 | true |
| The Regressed Mercenary's Machinations | Mercenary / Regression | 115 | 0 | true |
| The Reincarnated Assassin is a Genius Swordsman | Assassin / Sword | 180 | 2 | true |
| The Dark Mage ~ I Am the Only One | Mage / Dark | 85 | 1 | true |
| The Dark Swordsman Returns | Sword / Regression | 75 | 5 | true |
| Regressing as the Reincarnated Bastard | Regression / Noble | 90 | 1 | true |
| Regressing with the King's Power | Regression / System | 120 | 0 | true |
| The Novel's Extra (2022) | Strategy / Meta | 155 | 3 | true |
| The Reborn Young Lord is an Assassin | Assassin / Noble | 100 | 0 | true |
| The Rebirth of an 8th-Circled Mage | Mage / Regression | 215 | 0 | true |
| Plunder Countless Tales | System / Action | 100 | 0 | true |
| Relife Player | System / Action | 110 | 0 | true |
| Star-Embracing Swordmaster | Sword / Fantasy | 125 | 0 | true |
| Becoming a Cheat-Level Swordsman | Sword / System | 95 | 0 | true |
| Full-Time Awakening | System / Awakening | 115 | 0 | true |
| I Became the First Prince | Noble / Strategy | 100 | 0 | true |
| Legend of the Reincarnated Demon God | Dark / Reincarnation | 90 | 0 | true |
| Reincarnator's Stream | Modern / Stream | 95 | 0 | true |
| Swordmaster's Youngest Son | Sword / Noble | 180 | 0 | true |
| The Beginning After the End | Fantasy / Reincarnation | 220 | 0 | true |
| The Bottom-Feeder Scavenger | System / Dark | 85 | 0 | true |
| After Rebirth, I Used Mirror Revenge | Regression / Revenge | 75 | 0 | true |
| Absolute Necromancer | Necromancer / System | 130 | 0 | true |
| Return of the Apocalypse-Class Hero | Regression / Hero | 90 | 2 | true |
| Second Life Ranker | System / Action | 175 | 1 | true |
| Solo Max-Level Newbie | System / Action | 251 | 0 | true |
| SSS-Class Suicide Hunter | System / Regression | 200 | 0 | true |
| Magic Academy's Genius Blinker | Mage / Academy | 120 | 0 | true |
| Life of a Magic Academy Mage | Mage / Academy | 115 | 0 | true |
| I Regressed As the Duke | Noble / Regression | 190 | 0 | true |
| Raising Villains the Right Way | Strategy / Comedy | 100 | 100 | true |
| I Gave Up Being Stronger | System / Comedy | 85 | 0 | true |
| Regressor Instruction Manual | Regression / Strategy | 120 | 0 | true |
| The Strongest Assassin Gets Reincarnated | Assassin / Reincarnation | 100 | 0 | true |
| Reincarnated as a Genius Prodigy | Genius / Noble | 90 | 0 | true |
| Dragonslayer's Class Regression | Sword / Regression | 70 | 1 | true |
| A Hero Who Knows His Stuff | Hero / Action | 80 | 4 | true |
| Act Like a Boss, Mr. Swallow | System / Comedy | 75 | 4 | true |
| Arctic Cold War | Action / Post-Apoc | 80 | 6 | true |
| Awakening the Purple Thunder | System / Action | 80 | 5 | true |
| Han Dae Sung Returned from Hell | Modern / Action | 200 | 0 | true |
| The Extra's Academy Survival Guide | Academy / Strategy | 165 | 0 | true |
| My Daughter is the Final Boss | Strategy / Regression | 210 | 0 | true |
| Terminally-Ill Genius Dark Knight | Dark / Sword | 200 | 0 | true |
| Talent-Swallowing Magician | Mage / System | 200 | 0 | true |
| The Constellations Are My Disciples | System / Strategy | 175 | 0 | true |
| The Crown Prince That Sells Medicine | Strategy / Historical | 160 | 0 | true |
| The Martial God Who Regressed | Martial Arts / Regression | 175 | 0 | true |
| Standard of Reincarnation | Reincarnation / Sword | 170 | 0 | true |
| The Heavenly Demon Can't Live a Normal Life | Martial Arts / Dark | 192 | 0 | true |
| The Illegitimate Who Devours Everything | System / Dark | 80 | 5 | true |
| The World After the Fall | System / Dark | 110 | 0 | true |
| Reformation of the Deadbeat Noble | Sword / Growth | 220 | 0 | true |
| Player Who Returned 10,000 Years Later | System / Regression | 155 | 10 | true |
| Trash of the Count's Family | Strategy / Fantasy | 195 | 12 | true |
| Vampire's Alchemy | Dark / Fantasy | 90 | 7 | true |
| The Sword God from a Ruined World | Sword / Dark | 145 | 24 | true |
| Return of the Disaster-Class Hero | Regression / Hero | 175 | 69 | true |
| Revenge of the Iron-Blooded Sword Hound | Sword / Revenge | 155 | 6 | true |
| The Genius Healer Starts Academy | Academy / Healer | 80 | 8 | true |
| Overgeared | System / Crafting | 200 | 25 | true |
| Pick Me Up! Infinite Gacha | System / Gacha | 193 | 56 | true |
| I Am the Angel of Death | Assassin / Dark | 95 | 20 | true |
| I Am the Final Boss | System / Dark | 100 | 29 | true |
| I Contracted Myself | System / Unique | 115 | 30 | true |
| I Awoke As a God After Auto | System / Modern | 100 | 33 | true |
| I Got Lucky and Pulled a 10th | Gacha / System | 90 | 10 | true |
| I Obtained a Mythic Item | System / Action | 175 | 56 | true |
| I Used to Be a Boss | Dark / System | 90 | 14 | true |
| I Walk on a Road to Slay Enemies | Action / System | 175 | 83 | true |
| I Am the Strongest Boss | System / Action | 140 | 41 | true |
| Eternally Regressing Knight | Sword / Regression | 130 | 22 | true |
| Frozen Warrior | Dark / Action | 130 | 38 | true |
| Cleric of Decay | Dark / Fantasy | 145 | 52 | true |
| Dragon-Devouring Mage | Mage / Dragon | 110 | 19 | true |
| Dungeon Architect | System / Strategy | 175 | 65 | true |
| The Luckiest Mage | Mage / Comedy | 90 | 7 | true |
| Lord of the Mysteries (Remake) | Mystery / Dark Fantasy | 300 | 16 | true |
| The Island Where Stars and Deer Rise | Fantasy / Unique | 145 | 39 | true |
| The Eldest Son of the Marquis | Noble / Regression | 155 | 39 | true |
| The Archmage Returns After 4000 Years | Mage / Regression | 175 | 19 | true |
| The Fox-Eyed Villain of the Dark Magic Academy | Academy / Villain | 135 | 61 | true |
| Infinite Awakening | System / Awakening | 135 | 34 | true |
| Infinite Mage | Mage / Fantasy | 165 | 28 | true |
| Leveling With the Gods | System / Mythic | 155 | 26 | true |
| The Max-Level Hero Strikes Back | System / Action | 165 | 54 | true |
| The Mythical Weapon Creation | Crafting / System | 175 | 70 | true |
| Summoning Demons — I Am... | Dark / Summoner | 100 | 25 | true |
| Duke's Eldest Son is a Regressor | Noble / Regression | 155 | 73 | true |
| A Genius Wizard Who Breaks Boundaries | Mage / System | 145 | 52 | true |
| Bad Born Blood | Dark / Action | 150 | 63 | true |
| Bon Appétit | Slice of Life / Fantasy | 155 | 68 | true |
| Catastrophic Necromancer | Necromancer / Dark | 100 | 16 | true |
| City of Sin | Dark / Fantasy | 120 | 22 | true |
| The Third Prince of the Fallen Kingdom | Noble / Regression | 160 | 53 | true |
| The Regressed Extra Becomes a Genius | Strategy / Academy | 130 | 26 | true |
| The 100th Regression of the Max-Level Player | System / Regression | 150 | 0 | true |
| Regressor of the Fallen Family | Noble / Regression | 205 | 0 | true |
| Night of the Soulless Heathens | Dark / Fantasy | 130 | 53 | true |
| Omniscient Reader's Viewpoint | System / Meta | 305 | 41 | true |
| My Status Window is On... | System / Modern | 175 | 71 | true |
| Genius Archer's Streaming | Modern / Stream | 185 | 100 | true |
| Ghost King | Dark / Necromancer | 195 | 86 | true |
| The Legendary Hero is an Academy Honors Student | Academy / Hero | 195 | 77 | true |
| Regressor of the Close Combat Mage | Regression / Martial | 185 | 89 | true |
| The Dragon Slayer Academy | Academy / Dragon | 270 | 142 | true |
| +99 Reinforced Wooden Stick | System / Comedy | 185 | 79 | true |
| Apocalyptic Super Farm | Post-Apoc / Unique | 210 | 94 | true |
| Tyrant of the Tower Defense Game | Strategy / System | 168 | 161 | true |
| The Knight King Who Returned with God | Knight / Fantasy | 153 | 157 | true |
| Necromancer Academy and the Genius Summoner | Necromancer / Academy | 222 | 215 | true |
| Logging 10,000 Years Into the Future | System / Unique | 304 | 308 | true |
| Survival Story of a Sword King | Sword / Survival | 209 | 337 | true |
| A Returner's Magic Should Be Special | Mage / Regression | 270 | 279 | true |
