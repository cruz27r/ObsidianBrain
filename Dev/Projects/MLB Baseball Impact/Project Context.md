---
tags: [project, mlb, php, mysql, analytics, class-project]
status: active
created: 2026-04-19
---

# MLB Baseball Impact — Project Context

## Snapshot

- Repo: `/Users/itocruz/Desktop/Projects/MLB-Baseball-Impact`
- GitHub: `https://github.com/cruz27r/MLB-Baseball-Impact`
- Purpose: CS437 MLB Global Era analytics portal examining the impact of foreign players in MLB
- Stack: PHP, MySQL, SQL, Python ETL, HTML/CSS
- Current branch: `main`
- Current state: pushed portal refresh and country-analysis work; one untracked local script remains (`country_percentage.py`)

## Project Shape

- `public/`: PHP analytics portal and public pages
- `app/`: DB and application logic
- `sql_mysql/`: staging/data warehouse build scripts
- `etl/` + scripts: data acquisition/transformation pipeline
- Includes a class-compliant analytics portal and reporting/ML components

## Recent Work

- Refreshed analytics portal styling/pages with a more polished stadium-night design direction
- Added MySQL compatibility fixes in the app DB layer and SQL scripts
- Added substantive country-analysis scripts and upload helpers
- Normalized a broken case-collision by keeping `app/db.php` and removing duplicate tracked `app/Db.php`
- Pushed commit: `86dc048` — `feat: refresh analytics portal and country analysis`

## Verification

- `php -l` passed on the changed `app/` and `public/` PHP files during publish cleanup

## Important Repo Hygiene Notes

- Raw local data trees like `mainfiles/` should stay ignored/local
- Empty placeholder scripts were removed instead of being kept as repo noise
- `country_percentage.py` is still local and intentionally untracked for now

## Related

- [[Desktop Projects Repo Map]]
