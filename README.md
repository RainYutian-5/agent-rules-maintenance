# Agent Rules Maintenance

把不断膨胀的 AGENTS.md 维护成简洁、清楚、可验证的共享规则。支持 AGENTS.md、CLAUDE.md 等等效入口；跨客户端使用时，以实际指令层级和加载机制为准。

An independent, reusable Skill for pruning, reviewing, and validating shared agent instructions. It combines linked official guidance with an evidence-based maintenance workflow.

## 方法

**必要性判断 → 先删减 → 检查冲突 → 修改剩余条款 → 独立 review → 按需实测 → 周期维护。**

- 先问一条规则是否应该常驻；不把全部旧要求重新润色、搬家。
- 保留有效的明确要求，删除有依据的重复、过期背景和已有层级负责的样板。
- 真正无法解决的冲突先停下，给出具体条款、影响和所需决定。
- 为保留的规则明确范围、触发、动作与验收；用实际产物核验。
- 分开记录文本审查、情境判断、实际执行、加载检查和效果评估。
- 定期复查完整正文及新增内容，维护报告留在按需文档中。

这是独立项目。官方建议作为有来源的起点；流程组织、review 参数和测试方法是可配置的工程选择。

## 安装到 Codex

可直接对 Codex 说：

> 从 https://github.com/RainYutian-5/agent-rules-maintenance 安装 skills/agent-rules-maintenance 到 ~/.agents/skills。

或克隆后复制技能目录到个人技能目录：

```bash
git clone https://github.com/RainYutian-5/agent-rules-maintenance.git
mkdir -p ~/.agents/skills
cp -R agent-rules-maintenance/skills/agent-rules-maintenance ~/.agents/skills/
```

复制前检查目标是否已存在；已安装版本应按差异更新，避免直接覆盖个人修改。其他支持 Skill 的客户端使用自己的技能目录。独立入口是 [SKILL.md](skills/agent-rules-maintenance/SKILL.md)。

## 调用示例

```text
用 $agent-rules-maintenance 审查我的共享 AGENTS.md，先给删减理由，不修改。
```

```text
用 $agent-rules-maintenance 精简并修改指定规则文件；先去掉不必要常驻内容，
再独立 review 和验证；遇到无法解决的冲突先停下来告诉我。
```

用户提出相应规则维护任务时也可自动选择该 Skill；正常读取项目说明不会触发一次全局规则改造。

## 参数原则

| 参数 | 原则 |
|---|---|
| 主代理 | 保持当前对话模型 |
| Reviewer / Evaluator | 根据可用性、成本和解释复杂度选择；可用 gpt-6-luna/high 起步，复杂解释再用 xhigh |
| 独立性 | Reviewer 读规则和修改依据；Evaluator 只拿真实请求及最少原始材料，不喂预期答案 |
| 测试量 | 覆盖实际变化；预先确定样本与通过条件，保留失败，不循环刷到通过 |
| 文件长度 | 记录字节、单词和结构条目，不强设万能上限；这些不是模型 token 数 |
| 修改权限 | review-only 不写文件；维护授权仅覆盖目标文件及必要承接文档 |
| 冲突 | 先按层级、条件、范围和时效判断；仍需用户决定时停止修改 |
| 周期 | 用户可选择每周一次；通过正式调度工具设置日期、时间、时区，不擅自安装后台任务 |

## 周期维护提示词

```text
每周在约定时间使用 $agent-rules-maintenance 维护指定的共享规则文件。
比较上次验收基线和当前变化，先删减不必要内容，再 review 与按需验证。
出现未解决的真实冲突时停止修改并说明。报告长度变化、修改理由及验收证据。
```

调度只能由用户明确要求后创建。具体时间与输出位置由当前用户选择，不能从此示例推断授权。

## 辅助工具与检查

```bash
python3 skills/agent-rules-maintenance/scripts/rule_metrics.py path/to/AGENTS.md
python3 skills/agent-rules-maintenance/scripts/rule_metrics.py path/to/AGENTS.md --baseline path/to/before.md
python3 -m unittest discover -s tests -v
```

指标脚本仅使用 Python 标准库，只读输入文件；它统计结构，不做语义判断或自动删规则。

- [逐条 review 与官方建议映射](skills/agent-rules-maintenance/references/review-criteria.md)
- [独立审查、情境与实际执行验证](skills/agent-rules-maintenance/references/validation.md)
- [周期维护与公开发布](skills/agent-rules-maintenance/references/maintenance.md)

官方依据：[模型提示建议](https://developers.openai.com/api/docs/guides/latest-model#prompting-best-practices)、[Codex 最佳实践](https://learn.chatgpt.com/docs/learn/best-practices)。包中使用原创归纳，不附个人规则、聊天历史或真实执行日志。

## License

MIT；见 [LICENSE](LICENSE)。链接的第三方材料适用其各自条款。
