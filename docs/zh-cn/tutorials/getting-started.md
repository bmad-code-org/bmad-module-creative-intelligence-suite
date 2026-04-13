---
title: "CIS 快速入门"
description: 学习使用 Creative Intelligence Suite 进行头脑风暴、创新和问题解决
---

使用 AI 驱动的工作流释放创意突破，专业智能体将引导你完成构思、设计思维、创新策略和系统性问题解决。

## 你将学到

- 安装并初始化 Creative Intelligence Suite
- 和 Carson 一起运行你的第一次头脑风暴会议
- 使用设计思维打造以人为本的解决方案
- 运用创新策略发现市场机会
- 通过系统性分析解决复杂问题
- 和 Sophia 一起打造引人入胜的叙事

:::note[前置条件]
- **已安装 BMad Method** — CIS 是 BMad Method 的扩展模块
- **AI 驱动的 IDE** — Claude Code、Cursor、Windsurf 或类似工具
- **一个挑战或想法** — 需要头脑风暴、解决或改进的东西
:::

:::tip[快速路径]
**安装 CIS** — 在 BMad 安装时选择，或运行 `npx bmad-method install`
**试试头脑风暴** — 使用 `/cis-brainstorm` 和 Carson 互动
**探索工作流** — 每个智能体专精不同的创意方法
**每个工作流使用新对话**，避免上下文问题。
:::

## 了解 CIS

Creative Intelligence Suite（CIS）为 BMad Method 扩展了"模糊早期"阶段的工具——在这个阶段，创意萌生、问题被重新定义、解决方案通过结构化创造力涌现。

### CIS 智能体与工作流

| 智能体 | 工作流 | 用途 |
| ----- | ------ | ---- |
| **Carson** | `brainstorming` | 使用 7 个类别 36 种技术生成创意 |
| **Maya** | `design-thinking` | 通过 5 个阶段进行以人为本的设计 |
| **Victor** | `innovation-strategy` | 发现颠覆性机会和商业模式创新 |
| **Dr. Quinn** | `problem-solving` | 系统性问题诊断与根因分析 |
| **Sophia** | `storytelling` | 使用 25 种叙事框架打造引人入胜的故事 |
| **Caravaggio** | *（即将推出）* | 构建有说服力的演示 |

### 什么时候使用 CIS

| 场景 | 使用这个 |
| ---- | -------- |
| 被某个问题困住了 | `/cis-problem-solving` |
| 需要新想法 | `/cis-brainstorm` |
| 为用户做设计 | `/cis-design-thinking` |
| 寻找市场空白 | `/cis-innovation-strategy` |
| 讲述你的故事 | `/cis-storytelling` |

## 安装

CIS 作为模块在 BMad Method 安装过程中集成。如果你还没有安装 BMad Method：

```bash
npx bmad-method install
```

当提示选择模块时，选择 **Creative Intelligence Suite**。

安装程序会将 CIS 的智能体和工作流添加到你的 `_bmad/` 文件夹。

:::note[已经安装了 BMad Method？]
再次运行安装程序并选择 Creative Intelligence Suite，即可将其添加到现有配置中。
:::

## 步骤 1：你的第一次头脑风暴会议

让我们从最受欢迎的工作流开始——和 Carson 一起头脑风暴。

### 加载 Brainstorming Coach

在新对话中加载 Carson：

```
/cis-brainstorm
```

### 运行会议

Carson 会问你想头脑风暴什么。提供一个主题——从"改善用户引导流程"到"宠物主人的新产品创意"都可以。

Carson 会引导你完成：

1. **主题探索** — 理解你在头脑风暴什么
2. **技术选择** — 从 36 种技术中选择，或让 Carson 推荐
3. **构思** — Carson 使用"Yes, and..."方法论引导
4. **创意捕获** — 结果保存到 `_bmad-output/brainstorming-{date}.md`

### 示例会话

```
你：/cis-brainstorm
Carson：你想头脑风暴什么？
你：减少用户流失的方法
Carson：让我们探索一下！我推荐 SCAMPER 技术...
    [引导你从 7 个创意角度思考]
    [生成多样化、可执行的想法]
```

## 步骤 2：和 Maya 一起做以人为本的设计

当你需要为真实用户设计解决方案时，Maya 的设计思维工作流帮助你完成共情、定义、构思、原型和测试。

### 加载 Design Thinking Coach

```
/cis-design-thinking
```

### 五个阶段

| 阶段 | 发生什么 |
| ---- | -------- |
| **共情** | 理解用户需求和痛点 |
| **定义** | 从用户视角定义问题 |
| **构思** | 生成多样化的解决方案 |
| **原型** | 创建可快速测试的原型 |
| **测试** | 用真实用户验证 |

### 你将获得

输出保存到 `_bmad-output/design-thinking-{date}.md`：

- 设计挑战描述和观点陈述
- 用户洞察和共情地图
- "How Might We"问题
- 解决方案概念和原型
- 测试计划和迭代路线图

## 步骤 3：和 Victor 一起做战略创新

Victor 帮助你发现颠覆性机会和商业模式创新。

### 加载 Innovation Strategist

```
/cis-innovation-strategy
```

### 战略分析

Victor 会引导你完成：

1. **市场格局** — 竞争动态和趋势
2. **Jobs-to-be-Done** — 用户实际想要完成什么
3. **蓝海战略** — 寻找未被争夺的市场空间
4. **商业模式创新** — 创造和获取价值的新方式

### 你将获得

输出保存到 `_bmad-output/innovation-strategy-{date}.md`：

- 市场颠覆分析
- 创新机会图谱
- 商业模式画布替代方案
- 战略优先级和实施路线图

## 步骤 4：和 Dr. Quinn 一起系统性解决问题

对于复杂、顽固的问题，Dr. Quinn 运用系统性方法论找到根因和有效解决方案。

### 加载 Problem Solver

```
/cis-problem-solving
```

### 分析流程

Dr. Quinn 把问题当作谜题来对待：

1. **问题诊断** — 区分表象和根因
2. **框架选择** — TRIZ、约束理论、五个为什么、系统思维
3. **方案生成** — 评估多种方法
4. **实施规划** — 附带风险缓解的可执行步骤

### 你将获得

输出保存到 `_bmad-output/problem-solution-{date}.md`：

- 根因分析
- 方案评估矩阵
- 附带指标的实施计划
- 风险缓解策略

## 步骤 5：和 Sophia 一起讲故事

当你需要说服、启发或建立联系时，Sophia 打造引人入胜的叙事。

### 加载 Storyteller

```
/cis-storytelling
```

### 叙事开发

Sophia 会引导你完成：

1. **目的定义** — 受众应该感受/思考/行动什么？
2. **框架选择** — 英雄之旅、Story Brand、三幕式等
3. **角色发展** — 可共鸣的主角和真实的声音
4. **叙事弧线** — 张力、高潮和解决
5. **平台适配** — 针对你的媒介量身定制

### 你将获得

输出保存到 `_bmad-output/story-{date}.md`：

- 完整叙事及情感节拍
- 角色发展和对话
- 感官细节和生动场景
- 平台特定格式

:::note[Sophia 的记忆]
Sophia 会在她的 sidecar 中记住你的故事偏好和过往故事。她会随着时间推移，基于对你风格的了解不断优化。
:::

## 你已完成的工作

你已经学会了使用 CIS 进行创意智能的基础：

- 安装了 CIS 并探索了六个智能体
- 和 Carson 一起运行了头脑风暴会议
- 和 Maya 一起应用了设计思维
- 和 Victor 一起分析了创新机会
- 和 Dr. Quinn 一起系统性解决了问题
- 和 Sophia 一起打造了叙事

你的 `_bmad-output/` 文件夹现在包含：

```
your-project/
├── _bmad/
│   └── cis/                          # CIS 智能体和工作流
├── _bmad-output/
│   ├── brainstorming-{date}.md       # 构思会议结果
│   ├── design-thinking-{date}.md     # 以人为本的设计产出
│   ├── innovation-strategy-{date}.md # 战略创新路线图
│   ├── problem-solution-{date}.md    # 根因与解决方案
│   └── story-{date}.md               # 你打造的叙事
└── ...
```

## 快速参考

| 工作流 | 命令 | 智能体 | 用途 |
| ------ | ---- | ------ | ---- |
| `brainstorming` | `/cis-brainstorm` | Carson | 生成多样化创意 |
| `design-thinking` | `/cis-design-thinking` | Maya | 以人为本的设计 |
| `innovation-strategy` | `/cis-innovation-strategy` | Victor | 战略创新 |
| `problem-solving` | `/cis-problem-solving` | Dr. Quinn | 根因分析 |
| `storytelling` | `/cis-storytelling` | Sophia | 打造引人入胜的叙事 |

## 常见问题

**如何为工作流提供上下文？**

使用 `--data` 标志加上文件路径：

```bash
workflow cis-design-thinking --data /path/to/user-research.md
```

**可以组合使用多个 CIS 工作流吗？**

可以。先用头脑风暴生成选项，然后用设计思维优化以用户为中心的方案，或用创新策略评估商业潜力。

**问题解决和设计思维有什么区别？**

设计思维聚焦于用户需求和快速原型。问题解决运用分析框架找到根因并系统性评估方案。

**我需要使用所有工作流吗？**

不需要。每个工作流都是独立的。使用与你当前挑战匹配的即可。

## 获取帮助

- **工作流过程中** — 智能体通过提问和技术讲解引导你
- **社区** — [Discord](https://discord.gg/gk8jAdXWmj)（#creative-intelligence-suite）
- **问题反馈** — [GitHub Issues](https://github.com/bmad-code-org/bmad-module-creative-intelligence-suite/issues)

## 关键要点

:::tip[记住这些]
- **始终使用新对话** — 为每个工作流开始新对话
- **信任引导过程** — 智能体引导你使用经过验证的技术
- **捕获一切** — 输出会自动保存
- **自由迭代** — 随着想法演进，多次运行工作流
:::

准备好换一种方式思考了吗？开始你的第一次头脑风暴会议，发现结构化创造力能把你带到哪里。
