# Review criteria

## Necessity comes first

For each clause ask: Does it change a relevant agent decision? Is it durable across tasks? Is it already enforced or documented at the right layer? Is the target and trigger explicit? Is the apparent exception still current? What useful requirement would be lost if it were removed?

Classify the disposition as retain, rewrite, merge, relocate, remove, or user decision, with a short evidence-based reason. Preserve explicit user intent. A long rule is not inherently wrong; a short vague rule is not inherently good. Do not infer the optimal length from another project's measurements.

Keep conditional procedures in authoritative task documents and reference them only when needed. Store environment facts with their owner and applicability rather than presenting them as universal policy. Remove expired historical instructions instead of perpetually archiving them as new mandates.

## Official recommendation topics

This project groups the recommendations into eleven review questions; this is a derived checklist, not an official fixed enumeration. The topics follow OpenAI's [model prompting guidance](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices). Check the relevant version before model-specific advice; the guidance describes starting points to evaluate, not universal certification.

| Topic | Review question |
|---|---|
| 1. Initiative | Can the agent infer context and advance appropriately? |
| 2. Action intent | Does an action request lead to execution? |
| 3. Approval timing | Is authorized preparation completed before a concrete approval request? |
| 4. Skill priority | Are user requirements and Skill guidance distinguished correctly? |
| 5. Pause traceability | Can a Skill-induced pause be traced to its passage and interpretation? |
| 6. Concision | Is the result stated clearly and early? |
| 7. Technical language | Does terminology suit the audience? |
| 8. Repeated phrasing | Are stock expressions and unnecessary contrasts avoided? |
| 9. Delegation | Is delegation chosen for time or quality benefits? |
| 10. Agent messages | Are handoffs legible? |
| 11. Verification | Are checks proportional, expanding for meaningful reasons? |

A topic need not become a new global clause if effective guidance already covers it. Map requirements to actual rules rather than demanding a fixed eleven-rule template. [Codex best practices](https://learn.chatgpt.com/docs/learn/best-practices) also recommends practical, concise instructions with references for specialized detail.

## Precision and compatibility

- Separate a true conflict from compatible defaults, exceptions, phases, and different scopes.
- Missing information requiring a user choice is different from a failed tool operation that can be diagnosed.
- Completion means requested outcomes checked against evidence; it is not merely a final-channel response.
- Avoid instructions that force every user correction into new research or every small edit into a large test suite.
- A file link, a loaded message, a model's action, and task success are distinct observations.

## Evidence boundaries

[IFEval](https://arxiv.org/abs/2311.07911) illustrates observable instruction checks; [Lost in the Middle](https://arxiv.org/abs/2307.03172) concerns information use in long contexts. Neither gives this Skill a guaranteed compliance rate. The rule organization, disposition map, and independent review protocol are engineering choices to evaluate on the actual workload.
