# PhD CV Generator — 申博简历生成器（LaTeX）

## 这是什么？

一个 Codex 技能，根据你的个人经历和目标导师的研究方向，自动生成学术化、定向的申博简历 LaTeX 项目。使用 latex/ 目录下的 LaTeX 模板（蓝色、深蓝色、黑白简约），保留原始排版和字体配置，输出可直接用 xelatex 编译的 .tex 文件。

---

## 用户需要提供什么信息？

### 第一步：提供你的个人档案

参考你已有的简历，提供以下信息：

| 信息类别 | 具体内容 |
|---------|---------|
| 姓名 | 全名 |
| 研究方向 | 1-3 个关键词 |
| 联系方式 | 电话、邮箱、GitHub、主页 |
| 教育经历 | 每段：学校、学位、专业、时间、导师、荣誉、GPA |
| 论文列表 | 每篇：标题、作者角色、期刊/会议、状态、概述 |
| 项目经历 | 每个：名称、角色、时间、类型、概述、技术细节 |
| 竞赛/获奖 | 每个：名称、等级、奖项、时间 |
| 技能 | 分类列出（编程语言、框架、工具等） |
| 个人陈述 | 研究兴趣、背景、申请动机 |
| 工作经验 | 如有（公司、岗位、时间、职责） |

### 第二步：提供目标导师信息

| 信息 | 说明 | 重要性 |
|------|------|--------|
| 导师姓名 | 教授全名 | 必须 |
| 所在机构 | 大学或研究所 | 必须 |
| 研究方向关键词 | 2-5 个精确关键词 | 核心 |
| 近期代表作 | 1-3 篇标题 | 高 |
| 实验室名称 | 如 "Robot Learning Lab" | 推荐 |

---

## 可选模板

| 模板名 | 配色 | 语言 | 说明 |
|--------|------|------|------|
| blue | 蓝色 | 中文 | 基于 moderncv |
| dark-blue-zh | 深蓝色 | 中文 | 自定义 resume.cls，结构丰富 |
| dark-blue-en | 深蓝色 | 英文 | 同上，英文版 |
| black-simple | 黑白简约 | 中文 | 轻量级，字体齐全 |

默认推荐：dark-blue-en（申博通常需要英文）。

---

## 工作流程

```
你提供信息 → Codex 读取 README.md →
  1. 解析你的个人档案
  2. 记录目标导师研究方向
  3. 选取模板（与你确认）
  4. 用导师领域语言重写个人陈述、论文概述、项目描述 → 输出 JSON
  5. 运行脚本：python scripts/generate_latex.py --template <name> --output <dir> --content <data.json>
  6. 交付完整可编译的 LaTeX 项目（.tex + .cls + 字体）
```

---

## 编译方法

```bash
cd <输出目录>
xelatex <主文件名>.tex
```

各模板主文件名：
- blue: template_cn_blue.tex
- dark-blue-zh: resume-zh.tex
- dark-blue-en: resume-en.tex
- black-simple: resume-zh_CN.tex

---

## 对用户的提示

- 越具体越好：导师的研究方向关键词越精确，定向效果越好
- 不要编造：不会添加你没有的技能或经历，但会换说法展示已有经验
- 可以迭代：对生成的简历不满意，告知需要调整的部分即可重新生成
- 支持中英文：选择英文模板内容用英文，中文模板用中文
- 需要 LaTeX 环境：建议安装 TeXLive 或 MiKTeX

简历模板来自 [awesome-resume-for-chinese](https://github.com/dyweb/awesome-resume-for-chinese)

# Prompt 示例

``` markdown
个人信息和导师信息，请使用phd-cv-generator skills 生成个人-导师的定向简历, 模板使用dark-blue-zh

# 个人信息：
## 个人介绍

姓名：林子丹
个人照片：D:\学术简历模板\skills\phd-cv-generator\static\avatar.png

研究方向：海上风电预测；智能优化算法；深度学习时序建模；工业系统建模

联系方式：
电话：13810294756
邮箱：[linzidan_research@outlook.com](mailto:linzidan_research@outlook.com)

籍贯：浙江宁波
出生年月：2001.11

## 教育背景

### 西文大学（硕士）

专业：控制科学与工程
专业排名：前12%
时间：2024.09 – 至今

* 获得：研究生国家奖学金（2025）
* 导师：王启明 教授

### 苏北大学（学士）

专业：自动化
专业排名：前8%
时间：2020.09 – 2024.06

* 获得：校级优秀毕业生
* 导师：陈志远 副教授

## 论文发表

[1] Lin d, Wang Q. Physics-informed hybrid neural network for offshore wind speed prediction under nonlinear turbulence conditions. Renewable Energy, 2026.（SCI二区，IF=8.1，已发表）

[2] Deep contrastive learning framework for multi-site renewable energy forecasting under distribution shift. IEEE Transactions on Sustainable Energy.（Under Review）


## 科研能力陈述

* 语言能力：通过 CET-6（548），能够熟练阅读英文科研论文并进行文献复现
* 编程能力：熟练掌握 Python、MATLAB、PyTorch，熟悉深度学习与智能优化算法
* 办公能力：熟练使用 Office 套件，具备规范学术论文排版与答辩汇报能力
* 可视化能力：能够绘制复杂系统架构图、算法流程图及科研技术路线图
* 综合能力：具备较强的独立科研能力、数学建模能力与工程问题抽象能力


# 导师信息
汪沿海副研究员，长期从事风能高效利用与智能化数值建模及工业软件研发。研究方向包括：
1）多尺度复杂场景下风电场微观选址与环境耦合效应分析；
2）风电场集群尾流效应的智能协同优化与控制策略；
3）风电超短期、短期及中长期功率预测建模方法；
4）面向工程应用的风电系统优化与智能化工业软件开发。

近年来，在 Renewable Energy, Energy, Applied Energy Systems 等能源与环境领域高水平期刊发表论文40余篇。担任多个能源与工程类国际期刊审稿人，并参与若干学术期刊青年编委工作。

在科研成果方面，申请/授权发明专利约20项，登记软件著作权10余项，参与编写风能相关技术专著1部，并为能源领域政策研究报告提供技术支持建议。学术活动方面，曾担任国际能源与可再生能源会议分会主席，并在国内外学术会议作邀请报告10余次。科研项目方面，主持国家级与省部级科研项目及产学研合作项目共计10余项，涵盖基础研究与工程应用多个方向。在人才培养方面，指导研究生及本科生团队在可再生能源与节能减排相关竞赛中多次获奖，包括国家级二等奖、三等奖及省级优秀科技作品奖等。曾获得研究生阶段学业奖学金、优秀毕业生等荣誉称号。
```





![image-20260624190233254](D:\学术简历模板\skills\phd-cv-generator\README.assets\image-20260624190233254.png)
