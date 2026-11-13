# Periodic maintenance and public release

## Recurring review

Only create or change a schedule when requested. Prefer the platform's official scheduling tool over ad hoc background loops. A weekly review is a reasonable configurable starting point; day, time, timezone and destination must be explicit. Keep the reminder prompt short and invoke this Skill instead of duplicating its entire workflow. Review cadence does not belong in every task's global instructions.

On each run, reread the authoritative file, last accepted baseline and current changes. Inspect the complete file as well as additions. Remove justified bloat, review remaining clauses, and use focused validation for material changes. Halt edits for an unresolved real conflict and show the needed decision. Never automatically revoke an active user requirement merely because it is recent or specific.

Maintain one current local report with the reviewed hash, metrics, dispositions, evidence and unresolved decisions. Use version control for history when available, staging only scoped files. A maintenance request does not automatically authorize remote push, publication, client-setting changes, or new recurring jobs.

## Release a reusable Skill

Public release requires explicit authorization. Publish a new, isolated package containing reusable instructions, generic references, helper scripts, and synthetic fixtures. Exclude personal rule files, account details, host addresses, credentials, conversation exports, original test logs and unrelated repository history. Do not convert a private memory repository to public.

Before release:

1. Validate Skill frontmatter, names, links, and any UI metadata.
2. Run added scripts and focused tests; forward-test a realistic maintenance request and a conflict case in isolated fixtures when warranted.
3. Review every tracked file and the staged diff; exclude generated caches and private paths. A keyword scan supplements file review; it does not establish secrecy by itself.
4. Use a fresh repository and an explicit file list. Verify actual visibility, remote commit and file contents after publication; check anonymous public access separately where possible.
5. Provide a working installation path and verify local discovery. Installation is separate from proof that every existing chat loaded the Skill.

Separate attribution: official recommendations are linked and summarized; workflow mechanics and model/effort defaults are project choices. Publish original explanations rather than copying official prompts or private histories. A license covers the package's original contributions, not linked third-party documents.
