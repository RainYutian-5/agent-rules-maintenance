---
name: agent-rules-maintenance
description: Audit, prune, revise, and validate AGENTS.md or equivalent shared agent instructions when asked to maintain rules, reduce context bloat, resolve instruction conflicts, or conduct a periodic rules review. Not for ordinary tasks that merely read project instructions.
---

# Agent Rules Maintenance

Maintain a small, useful instruction entrypoint. First decide what belongs there; then improve wording and validate behavior. Preserve the user's intent, not every accumulated sentence.

## Inputs and scope

Identify the target rule file, applicable instruction hierarchy, requested changes, and authoritative task-specific references. Use an explicit path when supplied; otherwise inspect the active client's configuration and ask only if the target remains ambiguous. Do not assume one universal path or loading mechanism across clients.

Read the current authoritative files and relevant changes since the last accepted review. Record a content hash before editing. A review-only request permits analysis, not mutation; a maintenance request permits the scoped edits. Publication and scheduling require their own user request.

## Workflow

1. **Inspect the structure.** Measure the current file with [rule_metrics.py](scripts/rule_metrics.py). Classify its actual clauses: general behavior, preferences, constraints, procedures, configuration/state, and historical task context. List markers are structural units, not necessarily atomic instructions.
2. **Prune before rewriting.** Assess necessity clause by clause. Delete redundant guidance, obsolete one-off context, and detail already owned by tools, hosts, projects, or task-specific procedures when justified by current evidence. Preserve active explicit requirements; do not treat a preference as a defect merely because it is not universal. Move useful specialized guidance only into an appropriate authoritative location, with a conditional entrypoint containing the trigger and reference, not a copied procedure. Do not turn deletion into a new dump of copied rules.
3. **Resolve conflicts before mutation.** Check intent, scope, conditions, recency, and authority. A Skill's emphatic wording does not elevate its instruction priority. Distinguish tool-enforced requirements from the agent's interpretation of prose. If a genuine incompatibility still needs a user decision, stop editing and identify both clauses, locations, consequences, and the exact decision needed. Do not silently choose or disguise a conflict as missing information.
4. **Revise what remains.** Give each rule a clear scope, trigger, action, and observable completion condition where appropriate. Merge semantic duplication; remove dangling references and historical pronouns. Avoid fixed line/word/token targets or imposed output formats. Consult [review criteria](references/review-criteria.md) for eleven review topics mapped from official recommendations and their limits.
5. **Apply a narrow patch.** Check the authoritative file still matches the recorded version; on change, reread and recompute. Maintain a disposition map with source locations so every original requirement is accounted for as removed, merged, retained, or relocated. Separate pruning from substantive behavioral edits in the review record or commits so their effects can be assessed independently. Preserve unrelated edits.
6. **Review and test independently.** Follow [validation](references/validation.md). Have a fresh reviewer inspect fidelity, necessity, scope, conflicts, and reference resolution. Give a separate evaluator a realistic request and minimum raw artifacts, without the intended answer or diagnosis. Parent acceptance requires reading real outputs. Preserve failures and corrections; do not accept a subagent's completion claim as evidence by itself.
7. **Deliver and maintain.** Report before/after metrics, material edits, rule dispositions, unresolved decisions, and evidence types. Verify owned-resource cleanup and retained deliverables. Check actual loading only for the clients/chats in scope; links and installations alone prove neither loading nor compliance. For recurring maintenance or publication, read [maintenance and release](references/maintenance.md).

## Review parameters

Keep the main agent on the current chat model. Reviewer/evaluator model and reasoning effort are configurable; a supported economical reviewer with `high` effort is a starting point, with `xhigh` for complex interpretation. `gpt-6-luna` is one implementation option, not an official requirement. Preserve explicit user choices; disclose unsupported settings and actual fallbacks.

Use the smallest test set that covers changed behavior and meaningful regressions. Select test count and sampling before evaluation; avoid repeated tests solely to obtain a pass. Defaults such as a weekly review cadence are adjustable. Neither this Skill nor a passing review is a runtime enforcement mechanism.
