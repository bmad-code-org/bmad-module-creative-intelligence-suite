---
title: "CIS 工作流"
description: Creative Intelligence Suite 全部工作流参考
---

CIS 全部工作流的技术参考，包含输入、输出和调用方式。

## 工作流概览

| 工作流 | 智能体 | 用途 | 输出文件 |
| ------ | ------ | ---- | -------- |
| **brainstorming** | Carson | 生成多样化创意 | `brainstorming-{date}.md` |
| **design-thinking** | Maya | 以人为本设计 | `design-thinking-{date}.md` |
| **innovation-strategy** | Victor | 战略创新 | `innovation-strategy-{date}.md` |
| **problem-solving** | Dr. Quinn | 根因分析 | `problem-solution-{date}.md` |
| **storytelling** | Sophia | 叙事打造 | `story-{date}.md` |

## 头脑风暴工作流

**用途：** 使用结构化构思技术生成多样化、有创意的想法。

### 如何调用

```bash
# 直接命令
/cis-brainstorm

# 附带上下文数据
workflow brainstorming --data /path/to/context.md

# 通过智能体
/bmad-cis-agent-brainstorming-coach
> brainstorm
```

### 输入

| 输入 | 说明 | 必需 |
| ---- | ---- | ---- |
| **topic** | 头脑风暴的主题 | 是 |
| **technique** | 使用哪种构思方法 | 否（Carson 推荐） |
| **mode** | user-selected、AI-recommended、random、progressive | 否 |

### 输出

| 部分 | 内容 |
| ---- | ---- |
| **主题** | 你的头脑风暴挑战 |
| **技术** | 应用的方法及理由 |
| **创意** | 所有生成想法的完整列表 |
| **精选** | 推荐追求的想法 |
| **下一步** | 如何推进 |

### 技术库

Carson 可以访问存储在 `brainstorming-techniques.csv` 中的 7 个类别 36 种技术：

| 类别 | 技术数量 |
| ---- | -------- |
| 协作类 | 4 |
| 结构类 | 4 |
| 创意类 | 4 |
| 深度类 | 4 |
| 戏剧类 | 4 |
| 疯狂类 | 4 |
| 内省类 | 4 |

---

## 设计思维工作流

**用途：** 通过五阶段设计思维创建以人为本的解决方案。

### 如何调用

```bash
# 直接命令
/cis-design-thinking

# 附带用户研究上下文
workflow design-thinking --data /path/to/user-research.md

# 通过智能体
/bmad-cis-agent-design-thinking-coach
> design-thinking
```

### 输入

| 输入 | 说明 | 必需 |
| ---- | ---- | ---- |
| **design_challenge** | 正在探索的问题或机会 | 是 |
| **users_stakeholders** | 主要用户和受影响的各方 | 否 |
| **constraints** | 时间、预算、技术限制 | 否 |

### 输出

| 部分 | 内容 |
| ---- | ---- |
| **设计挑战** | 界定的机会 |
| **观点陈述** | 以用户为中心的问题陈述 |
| **用户洞察** | 共情发现和人物画像 |
| **How Might We 问题** | 重新定义为机会 |
| **解决方案概念** | 生成的想法 |
| **原型** | 可测试的产出 |
| **测试计划** | 验证方案 |

### 设计方法库

Maya 可以访问存储在 `design-methods.csv` 中的阶段特定设计方法。

---

## 创新策略工作流

**用途：** 发现颠覆性机会和商业模式创新。

### 如何调用

```bash
# 直接命令
/cis-innovation-strategy

# 附带市场上下文
workflow innovation-strategy --data /path/to/market-analysis.md

# 通过智能体
/bmad-cis-agent-innovation-strategist
> innovation-strategy
```

### 输入

| 输入 | 说明 | 必需 |
| ---- | ---- | ---- |
| **market_context** | 行业格局和竞争情报 | 否 |
| **innovation_challenge** | 战略机会或威胁 | 是 |
| **constraints** | 资源限制和战略边界 | 否 |

### 输出

| 部分 | 内容 |
| ---- | ---- |
| **战略问题** | 正在解决的创新挑战 |
| **市场分析** | 力量、趋势、竞争格局 |
| **Jobs-to-be-Done** | 未被满足的客户需求 |
| **蓝海机会** | 未被争夺的市场空间 |
| **商业模式** | 价值创造和获取 |
| **竞争优势** | 可持续的护城河 |
| **战略路线图** | 执行优先级 |

### 创新框架库

Victor 可以访问存储在 `innovation-frameworks.csv` 中的战略框架：
- Jobs-to-be-Done
- 蓝海战略
- 颠覆性创新
- 商业模式画布
- 价值链分析

---

## 问题解决工作流

**用途：** 系统性问题诊断与根因分析。

### 如何调用

```bash
# 直接命令
/cis-problem-solving

# 附带问题简报
workflow problem-solving --data /path/to/problem-brief.md

# 通过智能体
/bmad-cis-agent-creative-problem-solver
> problem-solving
```

### 输入

| 输入 | 说明 | 必需 |
| ---- | ---- | ---- |
| **problem_description** | 附带症状和上下文的挑战 | 是 |
| **previous_attempts** | 之前的方案和结果 | 否 |
| **constraints** | 解决方案边界 | 否 |
| **success_criteria** | 如何衡量有效性 | 否 |

### 输出

| 部分 | 内容 |
| ---- | ---- |
| **问题陈述** | 清晰定义的挑战 |
| **诊断** | 根因分析 |
| **解决方案选项** | 多种方案及评估 |
| **推荐方案** | 最佳选项及理由 |
| **实施计划** | 可执行的步骤 |
| **风险缓解** | 潜在问题和预防措施 |
| **成功指标** | 如何衡量结果 |

### 解决方法库

Dr. Quinn 可以访问存储在 `solving-methods.csv` 中的分析框架：
- 五个为什么
- TRIZ
- 约束理论
- 系统思维
- 根因分析

---

## 叙事工作流

**用途：** 使用经过验证的叙事框架打造引人入胜的故事。

### 如何调用

```bash
# 直接命令
/cis-storytelling

# 附带品牌上下文
workflow storytelling --data /path/to/brand-info.md

# 通过智能体
/bmad-cis-agent-storyteller
> story
```

### 输入

| 输入 | 说明 | 必需 |
| ---- | ---- | ---- |
| **story_purpose** | 为什么要讲这个故事 | 是 |
| **target_audience** | 谁会体验它 | 是 |
| **story_subject** | 关于什么或谁 | 是 |
| **platform_medium** | 在哪里讲述 | 否 |
| **desired_impact** | 受众应该感受/思考/行动什么 | 否 |

### 输出

| 部分 | 内容 |
| ---- | ---- |
| **故事框架** | 使用的结构及理由 |
| **受众画像** | 故事面向谁 |
| **情感弧线** | 感受旅程 |
| **完整叙事** | 含生动细节的完整故事 |
| **角色发展** | 声音和转变 |
| **平台适配** | 针对媒介格式化 |
| **影响计划** | 效果衡量 |

### 叙事框架库

Sophia 可以访问存储在 `story-types.csv` 中的 25 种叙事框架：
- 英雄之旅
- Story Brand
- 三幕式结构
- Before-After-Bridge
- Pixar Pitch
- 以及 20 种以上

---

## 输出位置

所有工作流将输出保存到配置的输出文件夹（默认：`./creative-outputs/` 或 `_bmad-output/`，取决于配置）。

输出文件包含时间戳，格式为：`{workflow-name}-{YYYY-MM-DD}.md`

## 通用工作流特性

所有 CIS 工作流共享：

- **互动引导** — AI 通过提问引导，而非仅仅生成
- **技术库** — 经过验证的方法的 CSV 数据库
- **上下文整合** — 可选的文档输入以提高相关性
- **结构化输出** — 包含洞察和行动的综合报告
- **能量监测** — 基于参与度的自适应节奏

## 下一步

- **[快速入门](/zh-cn/tutorials/getting-started/)** — 试试你的第一个工作流
- **[智能体参考](/zh-cn/reference/agents/)** — 了解工作流引导者
- **[配置](/zh-cn/reference/configuration/)** — 自定义工作流行为
