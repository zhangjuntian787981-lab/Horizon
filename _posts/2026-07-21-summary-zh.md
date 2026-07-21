---
layout: default
title: "Horizon Summary: 2026-07-21 (ZH)"
date: 2026-07-21
lang: zh
---

> 从 23 条内容中筛选出 6 条重要资讯。

---

1. [Sam Altman 邮件曝光 OpenAI 开源策略](#item-1) ⭐️ 9.0/10
2. [中国开源权重 AI 策略取得进展](#item-2) ⭐️ 8.0/10
3. [中国开源 AI 模型冲击西方实验室估值](#item-3) ⭐️ 8.0/10
4. [OpenAI 分享长时运行 AI 模型的安全经验](#item-4) ⭐️ 8.0/10
5. [NVIDIA 发布 Cosmos 3 Edge，用于实时边缘 AI](#item-5) ⭐️ 7.0/10
6. [Ben Thompson 提议美国制定 AI 合理使用与蒸馏法](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Sam Altman 邮件曝光 OpenAI 开源策略](https://simonwillison.net/2026/Jul/20/sam-altman/#atom-everything) ⭐️ 9.0/10

在 2026 年马斯克诉 Altman 案中披露的 Sam Altman 于 2022 年发给 OpenAI 董事会的邮件显示，他们计划发布一个接近 GPT-3 能力的开源模型，可在消费者硬件上运行，旨在抢先于 Stability 等竞争对手，并阻止新进入者获得资金。 这份文件直接揭示了 OpenAI 在开源 AI 方面的竞争策略，表明发布强大开源模型被视为控制生态系统和减少竞争的手段。 邮件明确指出该模型将具有‘接近 GPT-3 的能力’，并能够在消费者硬件上本地运行。Altman 表示要尽快发布，抢在 Stability 或其他公司之前。

rss · Simon Willison · 7月20日 03:47

**背景**: GPT-3 是 OpenAI 在 2020 年发布的大型语言模型，以其文本生成能力著称。Stability AI 等公司的开源 AI 模型被视为对专有模型的威胁。该邮件是马斯克诉 Altman 案的法律发现的一部分，该案涉及 OpenAI 的方向和治理问题。

**标签**: `#sam-altman`, `#openai`, `#open-source`, `#generative-ai`, `#ai-ethics`

---

<a id="item-2"></a>
## [中国开源权重 AI 策略取得进展](https://werd.io/american-ai-is-locked-down-and-proprietary-its-losing/) ⭐️ 8.0/10

最近一篇文章指出，中国发布开放权重 AI 模型的策略正在超越专有的美国 AI，并援引历史上开放和低成本解决方案主导的规律。 如果这一趋势持续，可能会重塑全球 AI 格局，使先进模型更易获取且成本更低，从而挑战 OpenAI 和 Anthropic 等公司的商业模式。 开放权重模型并非完全开源，但提供免费的模型权重，可由多个提供商托管和微调，而专有模型因沉没成本和高薪酬而需要高推理利润率。

hackernews · benwerd · 7月20日 14:21 · [社区讨论](https://news.ycombinator.com/item?id=48979269)

**背景**: 开放权重 AI 仅发布训练好的模型参数，而开源则包括训练代码和数据。这一区别很重要，因为开放权重允许部署和微调，但不能完全透明。中国已发布 DeepSeek 和 Qwen 等开放权重模型，在全球获得了大量使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told – Open Source ...</a></li>
<li><a href="https://neysa.ai/blog/open-weights-open-source/">Open Weights vs Open Source: What’s the Real Difference?</a></li>

</ul>
</details>

**社区讨论**: 评论者将其与历史上低端或免费解决方案获胜的技术转变相提并论，但有些人对‘80%初创公司使用中国模型’的说法表示怀疑，指出他们更常见到 Claude 和 Codex 等美国模型。此外，对于开放权重是否真正构成开源也存在争论。

**标签**: `#AI`, `#open-source`, `#China`, `#open-weights`, `#strategy`

---

<a id="item-3"></a>
## [中国开源 AI 模型冲击西方实验室估值](https://stratechery.com/2026/whos-afraid-of-chinese-models/) ⭐️ 8.0/10

Stratechery 上的一篇文章指出，中国开源 AI 模型（如 DeepSeek 和 Qwen）免费发布，削弱了 Anthropic 和 OpenAI 等西方实验室的高定价策略，并威胁其超过 1 万亿美元的估值。 这一趋势可能迫使西方 AI 实验室降价或证明其天文数字估值的合理性，重塑 AI 行业的竞争格局，并加速强大 AI 模型的民主化。 DeepSeek-V3 拥有 6710 亿参数，每个 token 仅激活 370 亿参数，在 14.8 万亿 token 上使用创新负载平衡和蒸馏方法训练，以可比模型一小部分的成本实现了最先进的性能。

hackernews · mfiguiere · 7月20日 11:05 · [社区讨论](https://news.ycombinator.com/item?id=48977128)

**背景**: DeepSeek 和阿里巴巴的 Qwen 等开源 AI 模型公开其权重，允许任何人运行。这些中国实验室用更少的计算资源达到或超过了西方模型，挑战了前沿 AI 需要巨额投资的观点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3">deepseek-ai/DeepSeek-V3 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Qwen">Qwen - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，中国模型对风投威胁最大，因为估值建立在 API 高定价之上。有用户报告编码工具切换轻松，反驳了锁定效应。其他人观察到中国大规模数据中心建设，并围绕蒸馏的伦理展开辩论，认为这类似于前沿实验室使用公共数据的行为。

**标签**: `#AI models`, `#Chinese AI`, `#open source`, `#industry competition`, `#valuations`

---

<a id="item-4"></a>
## [OpenAI 分享长时运行 AI 模型的安全经验](https://openai.com/index/safety-alignment-long-horizon-models) ⭐️ 8.0/10

7 月 20 日，OpenAI 发布了一份全面的安全与对齐报告，详细介绍了部署可长时间自主运行的 AI 模型的经验，强调了新的安全风险、观察到的失败以及通过迭代部署改进的安全措施。 这份报告意义重大，因为长时域模型与传统单轮交互系统相比具有根本不同的风险特征，OpenAI 的迭代部署方法为整个 AI 行业提供了如何在实际应用中管理这些风险的可操作见解。 报告涵盖了在长时间自主运行中出现的特定失败模式，如奖励黑客、目标泛化错误和不安全的工具使用，并描述了缓解措施，包括改进监控、约束行动空间和人在回路验证。

rss · OpenAI News · 7月20日 10:00

**背景**: 长时域模型是能够在长时间内无需人工干预执行多步骤任务的 AI 系统。AI 对齐是指将人类价值观和目标编码到 AI 模型中，以确保其行为符合预期。迭代部署是一种策略，即逐步释放具有更高自主性的模型，使得在更广泛部署之前能够学习并应用安全经验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zglg.work/en/ai/news/2026-07-20-openai-shares-safety-lessons-from-deploying-long-horizon-models">OpenAI Shares Safety Lessons from Deploying Long-Horizon Models</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#alignment`, `#long-horizon models`, `#OpenAI`, `#deployment`

---

<a id="item-5"></a>
## [NVIDIA 发布 Cosmos 3 Edge，用于实时边缘 AI](https://huggingface.co/blog/nvidia/cosmos3edge) ⭐️ 7.0/10

NVIDIA 推出了 Cosmos 3 Edge，这是一款针对边缘设备优化的新 AI 模型，专为实时推理和物理 AI 应用而设计。该模型属于 Cosmos 3 系列（包括 Super 和 Nano 变体），即将可用于边缘硬件部署。 Cosmos 3 Edge 将强大的物理 AI 能力引入资源受限的边缘设备，无需依赖云端即可实现实时视频理解、动作预测和数据生成。这可能通过提供能够理解和预测物理世界变化的设备端 AI，加速机器人、自主系统和物联网应用。 Cosmos 3 Edge 针对边缘设备上的实时推理进行了优化，能够基于观测和控制预览未来视频帧。它还可以恢复场景变化背后的动作，将视频证据转化为可执行的洞察。该模型将通过 NVIDIA 的 build 平台和 Hugging Face 提供，并支持 NIM 微服务部署。

rss · Hugging Face Blog · 7月20日 15:58

**背景**: Cosmos 3 是 NVIDIA 开发的一款面向物理 AI 的开放前沿基础模型，旨在帮助智能体理解和交互物理世界。它基于观测和控制条件来生成未来视频，辅助规划、评估和合成数据生成。边缘计算是指在数据源附近（例如摄像头或机器人上）处理数据，而非在云端，从而降低延迟和带宽使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/cosmos3edge">Introducing Cosmos 3 Edge - Hugging Face</a></li>
<li><a href="https://nvidianews.nvidia.com/news/nvidia-launches-cosmos-3-the-open-frontier-foundation-model-for-physical-ai">NVIDIA Launches Cosmos 3, the Open Frontier Foundation Model ...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Edge Computing`, `#AI`, `#Model Release`

---

<a id="item-6"></a>
## [Ben Thompson 提议美国制定 AI 合理使用与蒸馏法](https://simonwillison.net/2026/Jul/20/afraid-of-chinese-models/#atom-everything) ⭐️ 7.0/10

Ben Thompson 提议美国制定法律，明确将训练数据视为合理使用，并禁止服务条款中禁止模型蒸馏，以帮助美国开源模型与中国模型竞争。他还指出，在习近平发表鼓励开源的讲话后，阿里巴巴以开放权重发布了 Qwen 3.8 Max。 该提议直接针对 AI 实验室一方面禁止对其模型进行蒸馏，另一方面却使用未经许可的数据进行训练的矛盾，可能通过促进开放性来大幅改变中美 AI 竞争格局。若获通过，它将使模型蒸馏带来更广泛的创新，为美国开源模型创造公平竞争环境。 Qwen 3.8 Max 是一个拥有 2.4 万亿参数和 100 万 token 上下文窗口的多模态模型，在 Moonshot 发布 Kimi K3 后不久以开放权重形式发布。Thompson 的提议包含两部分：\(1\) 将训练数据收集视为合理使用；\(2\) 禁止美国公司的服务条款中禁止蒸馏。

rss · Simon Willison · 7月20日 17:09

**背景**: 模型蒸馏是一种将知识从大模型迁移到小模型的技术，使其能在较弱硬件上部署。许多 AI 实验室在服务条款中禁止蒸馏，同时却使用未经许可的数据进行训练，Thompson 称这是一种矛盾。像 Qwen 这样的中国 AI 模型越来越多地以开源形式发布，给美国实验室带来压力，促使它们采取更开放的政策。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_distillation">Model distillation</a></li>
<li><a href="https://www.marktechpost.com/2026/07/19/alibaba-previews-qwen3-8-max-a-2-4-trillion-parameter-multimodal-model-days-after-moonshots-kimi-k3-open-weight-launch/">Alibaba Previews Qwen3.8-Max, a 2.4 Trillion-Parameter Multimodal Model, Days After Moonshot&#x27;s Kimi K3 Open-Weight Launch - MarkTechPost</a></li>

</ul>
</details>

**标签**: `#AI`, `#copyright`, `#distillation`, `#Chinese AI models`, `#policy`

---