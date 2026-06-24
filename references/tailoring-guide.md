# Tailoring Guide: Advisor-Aligned CV Content

This reference provides concrete strategies for rewriting CV content to align with different advisor research directions, plus general guidance on what makes a PhD CV stand out.

---

## Part 1: 申博简历核心原则

> 申博简历的本质是一份学术价值提案，终极目标是向导师证明：你就是课题组最需要的那个人。

### 一、研究经历 — 量化成果 > 过程描述

研究经历是整份简历的重中之重。重点不是描述参与了什么项目，而是要清晰展示具体贡献和取得的量化成果。

| 要 | 不要 |
|----|------|
| 突出量化成果：开发XX模型，性能提升X% | 只写"参与了XX项目" |
| 独立完成数据分析模型构建并取得可验证提升 | 模糊描述"负责数据分析" |
| 论文发表分层展示，高水平论文置于显著位置 | 简单按时间倒序罗列 |

【研究经历】模板：
```
项目名称 | 起止时间
负责内容：独立设计并实现了XX算法/模型/框架
量化成果：开发XX模型，性能提升X%；完成XX分析，发表于XX期刊
```

### 二、论文发表 — 突出贡献而非罗列

- 按重要性/影响力排序，**不是**时间顺序
- 每篇论文都需要：作者顺序、年份、完整标题、期刊名称、影响因子、DOI
- 高水平论文可补充关键创新点或被引情况
- 在审/待投论文标注状态：under review / accepted
- 会议口头报告或海报展示也应纳入，展现学术交流能力

【论文发表】模板：
```
已发表论文：
作者顺序. (年份). 论文标题. 期刊名称 (IF: X). DOI
创新点/被引情况（可选）：

在审/接收中：
作者顺序. (under review). 论文标题. 目标期刊

会议报告：
作者顺序. (年份). 标题. 会议名称（口头/海报展示）
```

### 三、实践经历 — 学术化重构工作内容

即使是企业实习，也要通过"学术化视角"重构，突出可迁移科研能力：

- 数据分析岗位 → 强调统计建模和实验设计能力
- 项目管理经历 → 体现科研组织协调和执行能力
- 工程开发经历 → 展现算法实现和系统设计能力

### 四、荣誉奖项 — 突显学术含金量

- 优先展示与申请方向直接相关的学术类奖项
- 高含金量奖项标注获奖比例（前5%）或竞争规模（全国300所高校参赛）
- 校级奖项若与研究方向相关，也可说明具体评选标准

### 五、技能栏 — 精准匹配课题组需求

分层次列出：
1. 核心技能：课题组明确要求的技能
2. 辅助技能：编程语言、统计工具等
3. 软技能：跨学科协作能力，附实证（如发表SCI论文1篇）

### 六、5秒匹配原则 — 拒绝无效信息

- 简历顶部添加研究方向标签和核心能力摘要（3-4个bullet point）
- 坚决删除无关信息：高中经历、无关证书等
- 确保每项内容都能为申请加分

### 七、动态适配 + 可信度

- 建立个人经历数据库，根据目标导师近年的研究方向灵活调整内容重点
- 所有成果附加可验证标识（论文DOI号、专利公开号等）
- 精准比全面更重要，与其堆砌无关经历，不如深度打磨几个核心项目

---

## Part 2: Section-by-Section Tailoring Strategies

### Personal Statement (personal_statement)

Structure into a single coherent paragraph of 4-8 sentences:

1. Research Interest -- Why this field? Use advisor-specific terminology.
2. Relevant Experience -- Connect past work to advisor research.
3. Motivation -- Why this PhD? Why this lab?

**Example** (advisor: reinforcement learning for robotics):

> My research interests lie at the intersection of reinforcement learning and robotic control, particularly in developing sample-efficient algorithms for real-world deployment. I am drawn to your work on sim-to-real transfer, which aligns with my experience in sequential decision-making under uncertainty. During my master's research, I applied evolutionary optimization methods to wind farm layout design, developing formulations for multi-objective optimization under stochastic conditions. I am strongly motivated to pursue a PhD in your lab to bridge the gap between simulation-based RL and real-world robotic systems.

### Project Overview (projects[].overview)

Structure: Problem (advisor-domain framing) -> Method (technical vocabulary) -> Outcome (relevant metrics)

**Example** (TSP -> optimization advisor):
> This project addressed the Traveling Salesman Problem, an NP-hard benchmark with relevance to logistics and scheduling. I designed an evolutionary algorithm incorporating adaptive mutation operators and population diversity maintenance, achieving competitive results against established benchmarks.

### Publication Overview (publications[].overview)

Structure: Innovation -> Context -> Contribution

**Example** (wind farm paper -> renewable energy + ML advisor):
> This work introduced a novel deep surrogate modeling framework for wind farm layout optimization, reducing computational costs by orders of magnitude compared to traditional CFD-based approaches. I designed the neural architecture and the iterative optimization loop that coupled the surrogate with a genetic algorithm.

### Skills Section (skills[])

Include context tying skills to advisor's field:
> Good: Python, C++, MATLAB -- used for implementing deep RL algorithms and robotic control pipelines
> Bad: Python, C++, MATLAB -- jmo熟练

### Research Achievements (research_achievements[])

Write as complete academic sentences:
> Good: Developed a novel deep learning framework for predicting wind farm wake dynamics, achieving 95% accuracy while reducing computation time by 100x.
> Bad: jmshen学习 + jmfeng电场 + jmja速

---

## Part 3: Keyword-to-Description Mapping

### Machine Learning / Deep Learning

| Original | Reframed |
|----------|----------|
| Used Python to train models | Designed and implemented deep neural network architectures for [domain] tasks |
| Built a classifier for images | Developed convolutional neural network models for visual recognition tasks |
| Used scikit-learn for data analysis | Applied statistical learning methods to high-dimensional data analysis |
| Trained models on GPU | Optimized training pipelines for large-scale deep learning on parallel computing architectures |
| Used transfer learning | Leveraged pretrained representations and domain adaptation techniques |

### Reinforcement Learning

| Original | Reframed |
|----------|----------|
| Trained an agent to play a game | Designed reward functions and policy optimization algorithms for sequential decision-making |
| Used Q-learning | Implemented value-based reinforcement learning methods for Markov decision processes |
| Tuned hyperparameters | Conducted systematic exploration of learning rate schedules and exploration-exploitation tradeoffs |
| Built a simulation environment | Developed custom environments for evaluating RL algorithms under controlled conditions |

### Optimization / Operations Research

| Original | Reframed |
|----------|----------|
| Solved TSP with genetic algorithms | Designed evolutionary optimization approaches for NP-hard combinatorial problems |
| Used gradient descent | Implemented first-order optimization methods with convergence analysis |
| Wind farm layout optimization | Applied constrained optimization techniques to renewable energy infrastructure design |

### Robotics / Control

| Original | Reframed |
|----------|----------|
| Built a robot that follows lines | Developed sensor-based control policies for autonomous navigation |
| Used PID control | Designed feedback control systems with stability guarantees |
| Simulated robot movements | Built physics-based simulation pipelines for testing control algorithms |
| Sensor data processing | Implemented sensor fusion and state estimation for perception under uncertainty |

### NLP / Language Models

| Original | Reframed |
|----------|----------|
| Built a chatbot | Developed transformer-based conversational agents for [domain] applications |
| Used BERT for text classification | Fine-tuned pretrained language models for specialized text understanding tasks |
| Processed text data | Engineered text preprocessing pipelines for large-scale natural language corpora |

### Computer Vision

| Original | Reframed |
|----------|----------|
| Used OpenCV for image processing | Implemented classical and learning-based computer vision pipelines |
| Detected objects in images | Developed object detection and localization models for [domain] |
| Segmented images | Designed semantic and instance segmentation architectures for visual scene understanding |
| Used GANs for image generation | Applied generative adversarial frameworks for visual content synthesis |

### Scientific Computing / PDE / Physics

| Original | Reframed |
|----------|----------|
| Used finite difference methods | Developed numerical solvers for partial differential equations with accuracy analysis |
| Solved linear systems | Implemented scalable linear algebra routines for physics-based simulations |
| Used MATLAB for simulations | Built computational models for simulating physical systems |
| Parallel computing | Designed distributed computing strategies for large-scale numerical simulations |

### Uncertainty / Stochastic Systems

| Original | Reframed |
|----------|----------|
| Used random sampling | Designed Monte Carlo methods for uncertainty quantification in complex systems |
| Did sensitivity analysis | Conducted systematic perturbation analysis to identify key drivers of system behavior |
| Modeled random processes | Developed stochastic models for systems with inherent randomness |
| Used Bayesian methods | Applied Bayesian inference frameworks for probabilistic reasoning and parameter estimation |

### Multi-Agent Systems

| Original | Reframed |
|----------|----------|
| Built multiple agents | Designed decentralized coordination protocols for multi-agent systems |
| Agents communicate | Developed communication-efficient protocols for distributed agent collaboration |
| Simulated group behavior | Modeled emergent collective behaviors in multi-agent environments |

### Embodied AI / Manipulation (NEW)

| Original | Reframed |
|----------|----------|
| Made a robot arm grab things | Developed visuomotor policies for dexterous manipulation in unstructured environments |
| Used inverse kinematics | Implemented motion planning and trajectory optimization for robotic manipulators |
| Calibrated robot sensors | Designed perception pipelines for real-time object detection and pose estimation |

### AI for Science (NEW)

| Original | Reframed |
|----------|----------|
| Used ML to predict chemical properties | Developed physics-informed neural network surrogates for molecular property prediction |
| Simulated physical system with AI | Built data-driven reduced-order models to accelerate physics-based simulations |
| Used neural networks for PDE solving | Implemented neural operators for learning solution mappings of parametric PDEs |

---

## Part 4: Common Mistakes to Avoid

1. Over-promising: "I have extensive experience in deep RL" when you trained one simple agent.
2. Non-sequitur alignment: Forcing a connection that does not exist.
3. Too verbose: Overviews should be 2-4 sentences. Personal statement: 4-8 sentences.
4. Forgetting the "why this lab": Generic statements are weaker than specific references to advisor work.
5. Ignoring template language: Chinese template = Chinese content, English = English.
6. jmkua页面chuai分: Ensure sections are not split across pages.
7. jmguo度ge式: Use bold/italic moderately.
8. yi遗lou漏在tou投lun文: Include under-review/submitted papers, note their status.

---

## Reference: Academic Phrases for PhD CVs

- "This work addresses the challenge of..."
- "I developed a novel framework for..."
- "The proposed approach leverages..."
- "Experimental results demonstrate that..."
- "This project involved designing and implementing..."
- "I contributed to the development of..."
- "The research focuses on [problem], which is fundamental to [broader field]..."
