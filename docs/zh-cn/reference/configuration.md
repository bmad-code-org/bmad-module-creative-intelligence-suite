---
title: "CIS 配置"
description: 配置 CIS 工作流、输出位置和智能体行为
---

配置 Creative Intelligence Suite 的工作流、输出行为和智能体偏好。

## 配置文件

CIS 配置存储在：

```
_bmad/cis/config.yaml
```

如果文件不存在，CIS 使用默认值。

## 配置选项

| 设置 | 说明 | 默认值 |
| ---- | ---- | ------ |
| **output_folder** | 工作流输出保存位置 | `./_bmad-output/` |
| **user_name** | 工作流引导中使用的名字 | `User` |
| **communication_language** | 智能体响应语言 | `english` |

### output_folder

**工作流结果的保存位置。**

可以是绝对路径或相对路径。工作流输出命名为 `{workflow-name}-{date}.md`。

**示例：**

```yaml
output_folder: "./creative-outputs"
# 或
output_folder: "/Users/name/Documents/creative-work"
```

**相对路径**从项目根目录解析。

### user_name

**智能体在引导过程中如何称呼你。**

用于个性化互动。智能体会在回复中融入你的名字。

**示例：**

```yaml
user_name: "Alex"
# Carson 可能会说："Alex，让我们换个角度试试..."
```

### communication_language

**工作流引导的语言。**

智能体在保持独特个性的同时使用指定语言进行交流。

**支持的值：**

- `english`（默认）
- `spanish`
- `french`
- `german`
- `italian`
- `portuguese`

**示例：**

```yaml
communication_language: "spanish"
# Maya facilitará en español manteniendo su estilo jazzístico
```

## 默认配置

如果没有配置文件，CIS 使用：

```yaml
output_folder: "./_bmad-output/"
user_name: "User"
communication_language: "english"
```

## 创建配置

创建或编辑 `_bmad/cis/config.yaml`：

```yaml
# CIS 配置

output_folder: "./_bmad-output/"
user_name: "你的名字"
communication_language: "english"
```

## 工作流特定上下文

部分工作流通过命令行标志接受额外上下文：

### 提供上下文数据

向工作流传递上下文文档：

```bash
workflow design-thinking --data /path/to/user-research.md
workflow innovation-strategy --data /path/to/market-analysis.md
workflow problem-solving --data /path/to/problem-brief.md
workflow storytelling --data /path/to/brand-guidelines.md
```

上下文文件应为 markdown 格式。智能体会将这些信息融入引导过程。

## 智能体 Sidecar 配置

部分智能体在 sidecar 目录中维护持久数据：

### Sophia 的 Sidecar

Sophia（叙事师）记住你的偏好和故事历史：

```
_bmad/_memory/storyteller-sidecar/
├── story-preferences.md    # 你的叙事偏好
└── stories-told.md          # 已创建的故事历史
```

**关键动作**（自动调用）：

1. 叙事开始前加载偏好
2. 故事创建后更新历史

这使 Sophia 能够学习你的风格并构建一致的叙事。

## 环境变量

CIS 支持以下环境变量：

| 变量 | 用途 | 示例 |
| ---- | ---- | ---- |
| `BMAD_OUTPUT_DIR` | 覆盖输出文件夹 | `BMAD_OUTPUT_DIR=./outputs` |
| `BMAD_USER_NAME` | 覆盖用户名 | `BMAD_USER_NAME=Jordan` |
| `BMAD_LANGUAGE` | 覆盖语言 | `BMAD_LANGUAGE=spanish` |

环境变量优先于配置文件设置。

## 配置问题排查

### 输出没有出现

检查输出文件夹路径是否有效：

```bash
# 测试路径解析
ls ./_bmad-output/
```

确保文件夹存在或 CIS 可以创建它。

### 智能体没有使用你的名字

验证配置文件中的 `user_name`。对于 Sophia，确保 sidecar 文件存在且可读。

### 语言没有改变

确认 `communication_language` 使用了支持的值。自定义语言需要更新智能体提示词。

## 下一步

- **[快速入门](/zh-cn/tutorials/getting-started/)** — 使用默认配置运行工作流
- **[工作流参考](/zh-cn/reference/workflows/)** — 详细的工作流机制
