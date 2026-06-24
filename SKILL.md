---
name: phd-cv-generator
description: >
  Generate PhD-application CVs (.tex) from LaTeX templates (blue/dark-blue/black-simple),
  with content rewritten to align with a target advisor research direction.
  Output is a complete, compilable LaTeX project (.tex + .cls + fonts).
---

# PhD CV Generator

Generate a tailored PhD CV as a complete LaTeX project. The AI reads the selected template, understands its structure, and generates a complete .tex file with content aligned to the target advisor direction.

---

## 工作流

1. **收集信息** — 用户档案 + 目标导师信息
2. **选模板** — 与用户确认配色和语言
3. **读模板 + 生成 .tex** — 读取模板 .tex 和 .cls，生成完整 .tex 内容
4. **运行脚本** — `python scripts/generate_latex.py --template <name> --output <dir> --content <data.json>`
5. **交付** — 告知编译命令

---

## 1. 收集用户输入

[同之前版本，包括用户档案和导师信息]

## 2. 选取模板

| 模板名 | 配色 | 语言 |
|--------|------|------|
| `blue` | 蓝色 | 中文 (moderncv) |
| `dark-blue-zh` | 深蓝色 | 中文 |
| `dark-blue-en` | 深蓝色 | 英文 |
| `black-simple` | 黑白简约 | 中文 |

默认推荐 `dark-blue-zh`。

---

## 3. 生成完整 .tex — 核心步骤

这是最关键的一步。AI 直接生成完整的、可编译的 .tex 文件内容。

### 3.1 前置操作

在生成 .tex 之前，AI 必须先读取：

1. **模板的 .tex 文件** — 了解其结构、章节命令、环境
2. **模板的 .cls 文件** — 了解可用的 LaTeX 命令和环境
3. **模板的 header/sections 文件**（如 black-simple 的 texs/）

### 3.2 生成规则

**必须保留的（从原模板）：**
- 文档类声明 (`\documentclass[...]{resume}`)
- 所有 `\usepackage` 语句
- 字体设置（`\setmainfont`, `\setCJKmainfont` 等）
- 所有 `\definecolor` 颜色定义
- 所有格式设置（`\geometry`, `\titleformat` 等）
- `.cls` 文件中的所有自定义命令和环境
- 模板的原始注释和版权信息

**必须替换的（用用户数据）：**
- 个人信息（姓名、联系方式、照片等）
- 各章节内容（教育、论文、项目、技能等）
- 个人陈述/摘要

**生成内容必须使用模板 .cls 中定义的命令和环境。** 例如：

| 模板 | 教育章节 | 技能章节 | 成果章节 |
|------|---------|---------|---------|
| blue (moderncv) | `\cventry`, `\cvlistitem` | `\cvline` | `\cvlistitem` |
| dark-blue | `\education` + `educations` 环境 | `\comptence` + `competences` 环境 | `\item` + `itemize` |
| black-simple | `\datedsubsection`, `\normalline` | `\normalline` | `\normalline` / `itemize` |

### 3.3 各模板结构参考

**blue (moderncv) — template_cn_blue.tex:**
```
\documentclass[11pt,a4paper]{moderncv}
\usepackage{fontspec,xeCJK,xcolor}
\moderncvtheme[blue]{classic}
\firstname{...} \familyname{...} \title{...}
\mobile{...} \email{...} \social[github]{...}
\photo[64pt]{...}
\begin{document}
\maketitle
\section{教育经历}
  \cventry{start-end}{degree}{school}{dept}{}{desc}
  \cvlistitem{honor}
\section{论文发表}
  \cvline{status}{authors. title. venue.}
\section{项目}
  \subsection{科研项目}
  \cvline{name}{desc}
\section{专业技能}
  \cvline{\textbf{category}}{items}
\end{document}
```

**dark-blue (zh/en) — resume-zh.tex / resume-en.tex:**
```
\documentclass[zh]{resume}   % or \documentclass{resume} for English
\name{family}{given}
\profile{ \mobile{...} \email{...} \github{...} \degree{...} \university{...} }
\keywords{kw1, kw2}
\begin{document}
\makeheader
\begin{abstract} ... \end{abstract}
\sectionTitle{Skills}{\faWrench}
  \begin{competences}
    \comptence{category}{items}
  \end{competences}
\sectionTitle{Education}{\faGraduationCap}
  \begin{educations}
    \education{start}[end]{school}{dept}{major}{degree}
    \separator{0.5ex}
  \end{educations}
\sectionTitle{Achievements}{\faAtom} (or 科研成果)
  \begin{itemize}
    \item achievement
  \end{itemize}
\sectionTitle{Publications}{\faFile*}
  \begin{itemize}
    \item authors. title. venue.
  \end{itemize}
\sectionTitle{Projects}{\faCode} (or 项目经历)
  \begin{projects}
    \project{start}[end]{dept}{role}{name}{desc}[tags]
  \end{projects}
\sectionTitle{Experience}{\faBriefcase} (or 实习经历)
  \begin{experiences}
    \experience[start]{end}{summary}[description]
    \separator{0.5ex}
  \end{experiences}
\end{document}
```

**black-simple — sections.tex:**
```
\settitlelinestyle{default}
\name{...}
\basicInfo{ \phone{...}\dotSep \email{...}\dotSep \github{...} }
\begin{document}
\sectionTitle{教育背景}{\faiconsixbf{graduation-cap}}
  \datedsubsection{\texthl{school} / \textit{major} / \textit{degree}}{period}
  \normalline{desc}
\sectionTitle{项目经历}{\faiconsixbf{users}}
  \datedsubsection{\textbf{name}}{period}
  \role{role}{\href{link}{link}}
  desc
  \begin{itemize} \item detail \end{itemize}
\sectionTitle{竞赛获奖}{\faiconsixbf{award}}
  \begin{onehalfspacing}
    \datedline{name / level / detail}{date}
  \end{onehalfspacing}
\sectionTitle{专业技能}{\faiconsixbf{gears}}
  \begin{onehalfspacing}
    \normalline{\textbf{category}：items}
  \end{onehalfspacing}
\end{document}
```

### 3.4 内容定向调整策略

详细的 keyword→学术化描述 映射请看 [references/tailoring-guide.md](references/tailoring-guide.md)。

**核心原则：**
- 不要编造技能、经历、论文
- 使用导师领域术语重新表述已有经历
- 突出可迁移技能和研究关联性
- 学术语气，正式精确

**各章节调整重点：**
- 个人陈述：导师领域兴趣 → 相关经历 → 具体申请动机
- 论文概述：创新点 → 方法（用导师词汇）→ 贡献
- 项目概述：问题（导师领域框架）→ 方法 → 成果
- 技能：每类加上下文说明相关性

---

## 4. 运行脚本

```bash
python scripts/generate_latex.py --template <name> --output <dir> --content <data.json>
```

脚本行为：
1. 复制模板目录（.cls、.sty、字体、图片）到输出目录
2. 读取 JSON 中的 `tex_content` 字段
3. 写入主 .tex 文件

### JSON 格式

```json
{
  "name": "张三",
  "template": "dark-blue-en",
  "tex_content": "\\documentclass{resume}\n...完整的 .tex 内容..."
}
```

### 输出示例

```bash
python scripts/generate_latex.py --template dark-blue-en --output D:\学术简历模板\output\phd-cv --content D:\学术简历模板\output\content.json
```

---

## 5. 交付

告知用户输出路径和编译命令：
```bash
cd <output> && xelatex <main.tex>
```

各模板主文件名：`template_cn_blue.tex`(blue)、`resume-zh.tex`(dark-blue-zh)、`resume-en.tex`(dark-blue-en)、`resume-zh_CN.tex`(black-simple)

### 3.5 论文格式要求

生成简历时，论文列表必须严格按照以下格式编排（适用于所有模板）：

**已发表论文格式：**
> [序号] {AUTHOR_LIST}. {TITLE}. {JOURNAL}, {YEAR}.（{SCHOOL_RANK}，IF={IMPACT_FACTOR}，{STATUS}）

**在审/待投论文格式：**
> [序号] {TITLE}. {JOURNAL}.（Under Review / Submitted）

| 字段 | 说明 | 示例 |
|---|---|---|
| [序号] | 数字编号，按重要性排序 | [1] |
| AUTHOR_LIST | 完整作者列表，本人加粗 | Liu Y. (加粗) |
| TITLE | 论文完整标题 | Robust urban air... |
| JOURNAL | 期刊/会议名称，斜体 | Urban Climate (斜体) |
| YEAR | 发表年份 | 2025 |
| SCHOOL_RANK | 中科院分区 / CCF等级 | 中科院二区 / CCF-A |
| IF | 影响因子（可选） | 7.3 |
| STATUS | 标注一作/共一/通讯等 | 第一作者 |

**示例（已发表）：**
> [1] \\textbf{Liu Y.}, Miao F., et al. Robust urban air quality index prediction for pollution management via entropy-guided multiscale denoising and optimization-driven neuro-fuzzy modeling. \\textit{Urban Climate}, 2025.（中科院二区，IF=5.1，第一作者）

**示例（在审）：**
> [4] A Bidirectional Multiscale Temporal Adaptive Network for Multimodal Physiological Signal Fusion in Emotion Recognition. \\textit{Applied Soft Computing Journal}.（Under Review）

**注意：**
- 论文按重要性/影响力排序，不是按时间顺序
- 本人姓名在 LaTeX 中用 \\\\textbf{} 加粗
- 期刊名称在 LaTeX 中用 \\\\textit{} 斜体
- 层级分区和IF放在中文全角括号（）中
- 在审论文不列作者列表，只写标题和期刊
- 同一论文在英文版中用英文括号()，中文版中用中文括号（）

### 输出文件命名

脚本自动生成的文件名格式：


**注意：** JSON 中必须提供 
ame 字段，否则回退到模板默认文件名。

### 输出文件命名

脚本自动生成的文件名格式：

    [姓名]-定向[导师姓名]简历.tex

示例：姓名=刘英杰, 导师=崔爽 -> 刘英杰-定向崔爽简历.tex

注意：JSON中必须提供name字段，否则回退到模板默认文件名。
