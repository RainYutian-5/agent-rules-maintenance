# Validation and independent review

## Before tests

Record the target hash, scope, applicable model/effort, tool availability, test set, acceptance criteria, and cleanup owner. Keep tests isolated from live rules and external systems. Label sample instructions as test data so an intentional fixture conflict does not become a change to the user's active policy.

A text-only review needs no agent benchmark. Substantive behavior changes merit focused cases. Broader claims of improvement require a comparison design: fix model/version, tools, permissions, source materials, and task population; separate pruning from behavioral rewriting; repeat and use held-out tasks when warranted. Report sample sizes, regressions, time, and cost as available. Do not tune or rerun until a convenient result appears.

## Independent roles

- **Reviewer:** Inspect the current file, disposition map and relevant references. Check requirement fidelity, necessity, ambiguity, conflicts and on-demand links. Report source passages and concrete defects.
- **Evaluator:** Receive the Skill, a realistic user request, and minimal raw artifacts. Do not reveal the desired patch, suspected failure, prior answer, or acceptance oracle. Require real artifacts and cleanup where execution is requested.
- **Parent:** Inspect artifacts and actual records, request revisions or take over, and retain ownership while needed subagents run. A timeout is a checkpoint; a returned message is not acceptance.

Use separate fresh agents when available and worthwhile. If delegation is unavailable, record that fact and conduct a bounded self-review; do not claim independence. Do not change models silently. Use configured economical reviewers; higher effort is justified by interpretation complexity, not a universal rule.

## Useful cases

Choose cases relevant to the changed clauses:

| Case | Observable check |
|---|---|
| Clear, reversible action request | Actual change is made and other content preserved |
| Reversible missing detail | Reasonable progress without unnecessary questions |
| Ambiguous target or consequential decision | Specific question; independent preparation continues |
| Skill prose contradicts explicit user request | Authority is resolved from actual hierarchy, not emphatic words |
| Unresolvable same-level conflict | No conflicting edits; exact clauses and needed decision reported |
| Missing path or transient read failure | Real error is diagnosed; valid source used if available |
| Challenged factual inference | Original relevant evidence inspected |
| Subagent claims completion with missing output | Parent rejects and follows through |
| Temporary resource and deliverable | Temporary resource removed and absence checked; deliverable retained |

## Results

For each rule, identify trigger, expected action and observable acceptance. Distinguish text review, scenario judgment, actual execution, client exposure/loading, and measured effectiveness. A scenario answer is not execution evidence; a few passed executions are not a reliability estimate. Preserve initial failures, revisions and the hashes of versions exercised. Retest changed behavior and affected dependencies, not every unchanged branch.

Report remaining required work with attempted actions, observations, the concrete blocker, and the input needed. Exclude private chat histories and credentials from reusable fixtures or public reports. The original evidence can stay local.
