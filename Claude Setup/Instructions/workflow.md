## Core Workflow

- Session start: invoke `using-superpowers` (establishes skill routing).
- Before any feature/significant change: invoke `brainstorming` → `writing-plans`.
- Before plan execution: invoke `using-git-worktrees` (isolated branch + baseline tests).
- Plan execution: `subagent-driven-development` (preferred) OR `executing-plans` (inline).
  - Each task: `test-driven-development` → `requesting-code-review` (dispatch reviewer subagent).
  - When review arrives: `receiving-code-review` (technical eval, no performative agreement).
- Debugging/regressions: `systematic-debugging` before ANY fix attempt.
- Before claiming done: `verification-before-completion` (evidence, not assumptions).
- Branch completion: `finishing-a-development-branch` (verify → 4 options → cleanup worktree).
- Parallel independent domains: `dispatching-parallel-agents`.
- Creating reusable patterns: `writing-skills` (TDD applied to documentation).
- Plans saved to: `~/.claude/plans/` (global) or `docs/superpowers/plans/` (project).
- Cross-session tracking: `~/.claude/tasks/active/` (see tasks/README.md).
