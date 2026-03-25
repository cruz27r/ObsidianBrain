## Multi-Agent Coordination

### Isolation Principle
Each subagent receives precisely crafted context — never the orchestrator's session history.
Subagents must not inherit conversation context; construct exactly what they need.

### Worktree Strategy
- Parallel agents on different tasks: each gets its own worktree branch.
- Worktree naming: `feature/<task-slug>` or `.worktrees/<agent-id>-<task>`.
- Worktrees live in `.worktrees/` (project-local, gitignored) or outside the repo entirely.
- Use `using-git-worktrees` skill to set up each agent's workspace.

### Subagent Prompt Template
Each agent dispatch must include:
1. Specific scope (one file, one subsystem, one test suite)
2. Clear goal (what done looks like)
3. Constraints (what NOT to change)
4. Expected output format (summary of root cause + changes made)

### Orchestrator Responsibilities
- Dispatch: one agent per independent domain
- Review: read each summary, check for conflicts before integrating
- Verify: run full test suite after all agent results are integrated
- Escalate: if agents conflict on shared code, merge manually, then re-verify

### When NOT to Parallelize
- Agents would edit the same files (shared state conflict)
- Fix A is prerequisite for understanding Fix B
- Exploratory phase (don't know what's broken yet)
- Fewer than 2 truly independent tasks

### Session-Scoped Tracking
- Use built-in TaskCreate/TaskUpdate/TaskList tools for within-session task state.
- These are ephemeral — they do not persist across sessions.

### Cross-Session Tracking
- Persistent tasks live in `~/.claude/tasks/active/<YYYY-MM-DD-slug>.md`
- Format: title, status, plan file reference, branch, last-checkpoint, next-action
- Archive to `~/.claude/tasks/done/` when complete
