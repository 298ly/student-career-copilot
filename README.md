# Student Career Copilot

面向大学生与应届生的求职决策 Agent Skill。把每一份 JD、每一次投递、每一场面试、每一个学习结果，都变成对求职策略的一次**可追溯更新**——而不是一次性的聊天建议。

核心立场：**把职业方向当作待检验的假设，而不是性格测试给出的结论。**

> 以 [Claude Agent Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 规范实现，`agents/openai.yaml` 提供跨平台适配。

## 为什么不是又一个「简历 GPT」

通用助手在求职场景有三个固定失效模式，本 skill 逐个用机制约束，而不是靠提示词劝阻：

| 失效模式 | 本项目的机制 |
|---|---|
| 把课程项目说成生产经验、把参与说成主导 | **证据四级分类** `confirmed / self_reported / inferred / unknown`，每条声明绑定来源、日期、置信度；推断**不得**被静默提升为已确认 |
| 简历越改越漂亮，事实越飘越远 | 改写只允许取用证据库中已有事实；每处改动强制留存 `原文 / 改后 / 所服务的 JD 要求 / 支撑证据 / 面试风险` |
| 被拒就归因到"能力不够"，然后推翻整个方向 | **证据层级**排序（明确反馈 > 跨投递重复模式 > 测评表现 > 自我解读 > 无理由沉默）；原因未知时**禁止**归因为技能缺口，须并列列出时机、HC、竞争、定位等替代解释；**不得**因单次结果改变方向 |

## 设计要点

**受限输出空间.** JD 分析只能返回五个动作之一：`apply_now` / `tailor_then_apply` / `apply_while_learning` / `learn_first` / `skip`，并须给出要求级别的证据。显式**禁止**输出"匹配度 78%"这类伪精确总分——一条硬性门槛可以压过十条加分项。

**渐进式披露.** `SKILL.md` 只承载路由与不变约束；`references/` 下的 5 篇细则按任务按需加载，不把全部知识灌进上下文。

**追加式状态.** 投递与事件只追加不改写；简历只派生新版本，不覆盖旧版；原始输入与派生结论分目录存放。后续反馈必须对照**雇主当时实际看到**的材料来判断，而不是对照最新版简历。

**校准而非编造.** 时间、岗位供给、招聘窗口未知时，拒绝给出"每周投 N 家"的配额，只给可测量的流程或小批量试投。

**拒绝泛化.** "我不知道该学什么"不会换来一份课程清单——每个学习任务必须绑定 JD 需求、面试证据或明确的职业假设，并带截止时间和可观测的完成标准。

## 结构

```
SKILL.md                     路由与不变约束
references/
  jd-decision-rubric.md      JD 拆解与五动作判定
  workspace-schema.md        状态模型与证据分级
  application-operations.md  排序、投递、归档、结果解读
  interview-research.md      面试题溯源与训练
  roadmap-policy.md          成长路线更新策略
scripts/
  init_workspace.py          初始化工作区
  validate_workspace.py      结构校验
assets/workspace-template/   工作区模板
agents/openai.yaml           跨平台适配
```

## 使用

```bash
python scripts/init_workspace.py ~/career-workspace
```

随后在支持 Agent Skills 的客户端中加载本目录，把 JD 粘贴进去即可。修改结构化记录后运行：

```bash
python scripts/validate_workspace.py ~/career-workspace
```

## 数据与边界

- 个人数据默认留在本地；`career-workspace/` 已在 `.gitignore` 中排除，不会入库。
- 发布任何示例前须脱敏姓名、电话、邮箱、学号、私有链接与雇主保密信息。
- **不会**代为投递、联系 HR 或发布仓库，除非获得明确授权。
- 面试题研究只走公开可访问来源，不绕过登录、验证码、付费墙或 robots 限制；只保留链接、元数据与简短转述，不复制题库。
- 网络传闻按噪声证据处理，不当作确定的招聘事实。

## 状态

v0.1，作者本人求职中实际使用。评测协议（JD 判定金标集与一致性度量）建设中。

## License

MIT
