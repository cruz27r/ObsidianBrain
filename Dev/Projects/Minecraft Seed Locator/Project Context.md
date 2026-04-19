---
tags: [project, minecraft, seed-finder, c, python]
status: active
created: 2026-04-19
---

# Minecraft Seed Locator — Project Context

## Snapshot

- Repo: `/Users/itocruz/Desktop/Projects/MinecraftSeedLocator`
- GitHub: `https://github.com/cruz27r/MinecraftSeedLocator`
- Purpose: local Minecraft Java 1.21.1 seed scanner using Cubiomes for biome + structure filtering
- Stack: C, Python `ctypes`, native macOS `.dylib`, Cubiomes
- Current branch: `master`
- Current state: clean worktree; self-contained repo packaged and pushed

## Current Architecture

- `cubiomes_interface.c`: thin bridge over Cubiomes
- `cubiomes_py.py`: Python wrapper for the native library
- `seed_scanner.py`: user-editable conditions + scan loop
- `test_cubiomes_py.py`: smoke test for dylib loading and basic biome queries
- `cubiomes/`: vendored source dependency

## Recent Work

- Fixed scanner logic so biome conditions can target either `origin` or actual computed `spawn`
- Added repo hygiene: `README.md`, `.gitignore`, vendored `cubiomes/`, ignored runtime scan output
- Removed tracked `results.txt` so future scans stay local
- Local/GitHub commit: `e13ac86` — `feat: package self-contained minecraft seed locator`

## Verification

- `python3 test_cubiomes_py.py` passes locally
- Short scanner run succeeded with `python3 seed_scanner.py --start 0 --end 1000`

## Next Useful Actions

- If revisited, next likely step is longer scan runs or result-management workflow outside the repo
- Keep runtime outputs local/ignored rather than committing scan artifacts

## Related

- [[Desktop Projects Repo Map]]
