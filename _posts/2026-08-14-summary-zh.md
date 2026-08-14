---
layout: default
title: "Horizon Summary: 2026-08-14 (ZH)"
date: 2026-08-14
lang: zh
---

> 从 25 条内容中筛选出 7 条重要资讯。

---

1. [Cerebras 与 OpenAI 发布 GPT-5.6 Sol Ultrafast，速度提升近 7 倍](#item-1) ⭐️ 9.0/10
2. [逆向工程 DRAM 地址映射揭示重大硬件攻击面](#item-2) ⭐️ 9.0/10
3. [OpenAI 发布 GPT-5.6，旨在打造更快、更省成本的 AI 智能体](#item-3) ⭐️ 9.0/10
4. [谷歌 DeepMind 发布 Gemini 3.7 Flash 模型](#item-4) ⭐️ 9.0/10
5. [复现 ICML 2200 篇论文：Hugging Face 的经验教训](#item-5) ⭐️ 8.0/10
6. [DeepSeek V4 Pro 0813 发布：开放权重并可通过 API 使用](#item-6) ⭐️ 8.0/10
7. [Hugging Face 将 Strands Agents、LeRobot 与存储桶整合到机器人工作流中](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Cerebras 与 OpenAI 发布 GPT-5.6 Sol Ultrafast，速度提升近 7 倍](https://www.cerebras.ai/blog/accelerating-gpt-5-6-sol-ultrafast-with-openai) ⭐️ 9.0/10

这篇博客宣布了 OpenAI 全新 API 服务 Ultrafast，该服务在 Cerebras 硬件上运行 GPT-5.6 Sol。评测中，它在 11 小时 11 分钟内回答了“人类最后的考试”全部 2500 道题，而 Claude Fable 5 需要 78 小时 27 分钟——在准确率相当的情况下快了近 7 倍。 这很重要，因为推理速度常常是 AI 应用的瓶颈，而在前沿基准上实现近 7 倍加速，可能让迭代式推理工作流变得更实用。这也可能加剧推理服务商之间的竞争，推动其他厂商在优化准确率的同时也优化延迟。 这里提到的基准是“人类最后的考试”（HLE），一个涵盖多学科专家级问题的前沿学术测试。评论中引用的 OpenAI 官方帖指出尚未公布定价，而且该博文没有明确说明快速模式与普通 Sol 的输出完全一致，这一点已引起关注。

hackernews · pr337h4m · 8月13日 18:10 · [社区讨论](https://news.ycombinator.com/item?id=49289844)

**背景**: Cerebras 以“晶圆级引擎”（wafer-scale engine）闻名，这种芯片由整片硅晶圆制成，包含数十万个核心，能够加速深度学习任务。HLE 是一个用经专家审核的高难度问题测试 AI 模型的基准，是衡量前沿推理能力的强力工具。此次发布将 OpenAI 的前沿模型与 Cerebras 的专用硬件结合，以提升推理吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cerebras_Systems">Cerebras Systems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Humanity&#x27;s_Last_Exam">Humanity&#x27;s Last Exam - Wikipedia</a></li>
<li><a href="https://artificialanalysis.ai/evaluations/humanitys-last-exam">Humanity&#x27;s Last Exam Benchmark Leaderboard | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 评论区总体很兴奋，有用户表示如果该服务正式可用，愿付双倍于当前 Claude 订阅的费用。但也存在一些质疑：有评论指出博文没有明确声称快速模式与普通 Sol 准确率完全一致，而且价格未公布，可能意味着高端定价或仍在试探市场需求。

**标签**: `#AI`, `#LLM`, `#Inference`, `#OpenAI`, `#Cerebras`

---

<a id="item-2"></a>
## [逆向工程 DRAM 地址映射揭示重大硬件攻击面](https://github.com/xoreaxeaxeax/skitter-creek-bath-salts) ⭐️ 9.0/10

安全研究员 Christopher Domas 发布了一个 GitHub 仓库（skitter-creek-bath-salts），并将在 Black Hat 上展示对 DRAM 地址映射的逆向工程，从而揭示一个重大的硬件安全攻击面。该工具目前演示支持 AMD 的 Jaguar 架构（AMD16h），并指出 Zen 3 的内存控制器寄存器基地址不同。 这项研究扩大了已知的 DRAM 攻击面：在受影响系统上，ring-0 根权限可以访问此前隐藏在负环（negative ring）领域中的大量内容。这对操作系统和硬件安全具有重要意义，也可能让游戏主机安全团队感到担忧，因为在主机上获得 ring-0 后，系统其余部分将完全敞开。 根据 README，该攻击适用于 AMD Jaguar（一种 2013 年的低功耗架构），并注明 Zen 3 的内存控制器寄存器基地址不同。仓库页面没有说明其他哪些处理器系列可能同样受影响。

hackernews · matt\_d · 8月13日 14:17 · [社区讨论](https://news.ycombinator.com/item?id=49286341)

**背景**: DRAM 地址映射是将物理地址转换为 DRAM 通道、rank、bank 以及行/列位置的非公开函数。现代 SoC 通过线性地址加扰来混淆这一映射，这使性能优化变得复杂，并阻碍了主动安全分析，尤其是针对 Rowhammer 攻击的分析。此前的工作如 DRAMA 和 Knock-Knock 已尝试在 Intel 等平台上逆向这些映射。Domas 的项目延续了这一研究方向，将映射本身视为一个安全关键的攻击面。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2509.19568">Knock-Knock: Black-Box, Platform-Agnostic DRAM Address-Mapping Reverse ...</a></li>
<li><a href="https://github.com/isec-tugraz/drama">DRAMA Reverse-Engineering Tool and Side-Channel Tools</a></li>
<li><a href="https://arxiv.org/abs/2506.15918">Sudoku: Decomposing DRAM Address Mapping into Component Functions - arXiv</a></li>

</ul>
</details>

**社区讨论**: 评论者对即将举行的 Black Hat 演讲表示兴奋，称赞 Christopher Domas 解释复杂研究的能力。一些人指出，现代 DRAM 的复杂性已大大增加，因此如此大的攻击面并不令人意外；另一些人则质疑除 AMD Jaguar 外还有哪些较新的 CPU 受影响，并指出页面对此并未说明。有评论者推测，Xbox 和 PlayStation 的安全团队可能会感到紧张，因为在这些主机上获得 ring-0 后，其他一切都会暴露。

**标签**: `#DRAM`, `#security`, `#reverse-engineering`, `#hardware`, `#BlackHat`

---

<a id="item-3"></a>
## [OpenAI 发布 GPT-5.6，旨在打造更快、更省成本的 AI 智能体](https://openai.com/index/builders-guide-to-gpt-5-6) ⭐️ 9.0/10

OpenAI 发布了新模型 GPT-5.6，重点帮助初创公司更快、更省成本地构建 AI 智能体，并突出更智能的模型选择以及新的 Responses API 功能。 这是 OpenAI 的一次重大模型发布，对 AI 开发具有重要影响，因为它通过成本效率的改进增强了智能体应用的构建。这将影响依赖 OpenAI API 构建 AI 智能体的开发者和初创公司。 公告强调了新的 Responses API 功能，该功能通过将 Chat Completions API 与高级工具调用能力相结合，简化了智能体应用的创建。它还提倡更智能的模型选择，以优化每次请求的成本、速度和质量。

rss · OpenAI News · 8月13日 11:00

**背景**: OpenAI 于 2025 年 3 月 11 日发布了 Responses API，这是一个旨在简化智能体应用创建的开发者工具。它支持有状态交互、文本和图像输入、文本输出，以及文件搜索、网页搜索和计算机使用等内置工具。模型选择对 AI 智能体至关重要，因为不同模型可分配到不同的智能体或端点，或由路由器根据可配置标准动态选择每次请求的最佳模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/api/reference/responses/overview">Responses Overview | OpenAI API Reference</a></li>
<li><a href="https://grokipedia.com/page/OpenAI_Responses_API">OpenAI Responses API</a></li>
<li><a href="https://clawpane.co/blog/model-selection">Model Selection for AI Agents: Manual vs. Automated Approaches | ClawPane</a></li>

</ul>
</details>

**标签**: `#GPT-5.6`, `#OpenAI`, `#AI agents`, `#API`, `#model release`

---

<a id="item-4"></a>
## [谷歌 DeepMind 发布 Gemini 3.7 Flash 模型](https://deepmind.google/blog/introducing-gemini-3-7-flash/) ⭐️ 9.0/10

谷歌 DeepMind 正式推出了其 Gemini 模型家族的新成员 Gemini 3.7 Flash。该模型采用限时优惠定价，计划于 2026 年 12 月 31 日翻倍，距离 3.6 Flash 发布仅三周时间。 此次发布意义重大，因为 Gemini Flash 系列模型面向低成本、高吞吐量的文本处理场景，为开发者和企业提供了经济实惠的选择。同时，这也凸显了谷歌在竞争激烈的 AI 模型市场中的快速迭代节奏，而像 GPT-5.6 Luna 这样的竞品也在不断获得关注。 根据 Hacker News 上的讨论，Gemini 3.7 Flash 的限时优惠价格将在 2026 年 12 月 31 日后翻倍，从 2027 年 1 月 1 日起，输入 token 价格为每百万个 1.50 美元，输出 token 价格为每百万个 7.50 美元。早期测试表明，该模型在图像转 HTML 任务和 DeepSWE 1.1 基准上表现良好，但部分用户认为在特定视觉任务上竞品仍然更胜一筹。

rss · Google DeepMind · 8月13日 17:04

**背景**: Gemini 3.7 Flash 是谷歌 Gemini 大语言模型家族的一员，可通过 Gemini API 访问。&\#x27;Flash&\#x27;系列旨在为总结、解析、格式化等大吞吐量、以文本为主的应用场景提供成本与性能的平衡。3.6 Flash 刚于三周前发布，如此快速的迭代反映了 AI 领域的激烈竞争压力。用户还可以在默认、高、中、低四种&\#x27;思考级别&\#x27;中调整，以控制推理 token 的使用量。

**社区讨论**: Hacker News 上的评论者反应不一。一些人称赞 Gemini 3.7 Flash 的视觉能力，指出它在图像转 HTML 方面表现不错，但 Opus 5 仍是该类任务的最佳选择。另一些人则批评其限时定价结构不切实际，因为模型更新换代太快；还有人认为 GPT-5.6 Luna 等竞品性能更好、价格更低，可能降低了对 Flash 模型的需求。

**标签**: `#AI`, `#Gemini`, `#Google DeepMind`, `#LLM`, `#Model Release`

---

<a id="item-5"></a>
## [复现 ICML 2200 篇论文：Hugging Face 的经验教训](https://huggingface.co/blog/icml-2026-open-reproductions) ⭐️ 8.0/10

Hugging Face 发布了一篇博客文章，分享了他们尝试复现 ICML 收录的 2200 篇论文时学到的经验，指出了常见的可复现性挑战和最佳实践。 这是机器学习领域规模最大的可复现性研究之一，涵盖了 2200 篇 ICML 论文。研究结果可以帮助研究人员采用更好的实践，并促使会议和期刊推行可复现性标准。 该研究聚焦于 ICML 论文，找出了复现失败的常见原因，例如代码缺失、超参数不明确以及实验细节不完整。博客文章还为作者提供了提高可复现性的实用最佳实践。

rss · Hugging Face Blog · 8月13日 00:00

**背景**: ICML（国际机器学习大会）是机器学习领域的顶级学术会议之一。可复现性指的是独立研究人员使用原始数据和代码能够获得相同结果的能力。许多机器学习论文因不公开代码或详细的实验设置而受到批评，导致研究结果难以验证。Hugging Face 是一个知名的人工智能社区平台，托管模型、数据集和研究内容。

**标签**: `#reproducibility`, `#machine learning`, `#ICML`, `#research practices`, `#open science`

---

<a id="item-6"></a>
## [DeepSeek V4 Pro 0813 发布：开放权重并可通过 API 使用](https://simonwillison.net/2026/Aug/12/deepseek-v4-pro-0813/) ⭐️ 8.0/10

DeepSeek 发布了其最新旗舰模型 V4 Pro 0813，现可通过 API 并在 OpenRouter 上使用。随后，开放权重已在 Hugging Face 上发布，总计 1.7T 参数，检查点大小为 893 GB。 此次发布巩固了 DeepSeek 在开放权重大语言模型领域的地位，提供了一个拥有 1.7T 参数的大型模型，开发者既可以自行运行，也可以通过 API 访问。不同推理级别下的明显行为差异，也凸显了中国顶级 AI 模型日益成熟与差异化的发展趋势。 Hugging Face 上的仓库显示模型参数为 1.7T，大小为 893 GB，之前已有 4 月的 DeepSeek-V4-Pro 和 7 月的 DeepSeek-V4-Flash-0731。Simon Willison 注意到低、中、高推理级别生成的鹈鹕图片差异明显，他表示其他模型没有出现过这种效果；基准测试表据称先是在微信流传，后经 Reddit 删除，又在 Hacker News 上被转发。

rss · Simon Willison · 8月12日 23:59

**背景**: OpenRouter 是一个统一网关，让开发者通过单一界面和 API 访问来自多个提供商的数百种 AI 模型。开放权重模型会发布预训练参数（即权重），使其他人能够运行推理和微调，但这与完全开源不同，后者还会包括训练代码和数据。DeepSeek 是一家以发布大型开放权重模型著称的中国 AI 实验室，此次 0813 更新是其一系列增量发布中的最新版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">OpenRouter</a></li>
<li><a href="https://promptengineering.org/llm-open-source-vs-open-weights-vs-restricted-weights/">Openness in Language Models: Open Source vs Open Weights vs Restricted ...</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-an-open-weight-model">What is an Open-Weight Model? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#open weights`, `#model release`

---

<a id="item-7"></a>
## [Hugging Face 将 Strands Agents、LeRobot 与存储桶整合到机器人工作流中](https://huggingface.co/blog/amazon/strands-lerobot-streaming-data-loop) ⭐️ 7.0/10

Hugging Face 宣布推出一个统一平台，将 Strands Agents、LeRobot 和存储桶整合在一起，使机器人工作流中的数据记录、训练和部署能够在一个地方无缝完成。这一整合承诺为从数据采集到机器人部署提供了一条简化的路径。 这一整合简化了机器人与机器学习的工作流程，减少了数据采集、模型训练和实际部署之间的摩擦。它有望提高机器人学习项目的可复现性和可扩展性，使从事具身人工智能的研究人员、爱好者和企业受益。 该平台利用 Strands Agents 进行物理人工智能推理，利用 LeRobot 提供与硬件无关的机器人学习与控制能力，并通过 Hugging Face 存储桶为大型数据集提供可扩展的 S3 兼容对象存储。该工作流支持以相同的磁盘格式存储仿真到现实数据集，并支持通过字符串切换策略。

rss · Hugging Face Blog · 8月13日 17:16

**背景**: LeRobot 是 Hugging Face 的开源项目，为现实世界的机器人提供模型、数据集和工具，旨在让机器人人工智能更容易上手。Strands Agents 是 AWS 开发的框架，用于构建智能物理人工智能，使智能体能够在真实环境中感知、推理和行动。Hugging Face 存储桶于 2026 年 3 月推出，为 Hugging Face 生态系统增加了原生 S3 兼容对象存储，用于存储不符合标准仓库模式的大型文件和工作流资产。这些工具共同满足了具身人工智能和机器人学习对端到端基础设施日益增长的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/blogs/opensource/building-intelligent-physical-ai-from-edge-to-cloud-with-strands-agents-bedrock-agentcore-claude-4-5-nvidia-gr00t-and-hugging-face-lerobot/">Building intelligent physical AI: From edge to cloud with Strands Agents, Bedrock AgentCore, Claude 4.5, NVIDIA GR00T, and Hugging Face LeRobot | AWS Open Source Blog</a></li>
<li><a href="https://huggingface.co/blog/amazon/strands-lerobot-hub-to-hardware">From the Hugging Face Hub to robot hardware with Strands Agents and LeRobot</a></li>
<li><a href="https://github.com/huggingface/lerobot">GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning</a></li>

</ul>
</details>

**标签**: `#robotics`, `#machine learning`, `#data streaming`, `#Hugging Face`, `#deployment`

---