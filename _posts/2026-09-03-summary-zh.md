---
layout: default
title: "Horizon Summary: 2026-09-03 (ZH)"
date: 2026-09-03
lang: zh
---

> 从 15 条内容中筛选出 7 条重要资讯。

---

1. [谷歌 DeepMind 推出 Gemini 3.8 Flash 与 Flash Cyber 模型](#item-1) ⭐️ 9.0/10
2. [Meta 发布 Muse Spark 1.3：以极低成本提供接近 SOTA 的性能](#item-2) ⭐️ 8.0/10
3. [谷歌避免其广告技术业务被拆分](#item-3) ⭐️ 8.0/10
4. [Paint.NET 作者借助 AI 为 WINE 重写 Direct2D](#item-4) ⭐️ 8.0/10
5. [谷歌 DeepMind 倡导 AI 主动网络防御](#item-5) ⭐️ 7.0/10
6. [IBM 展示如何在 Confluent 上利用时间序列模型实现实时智能](#item-6) ⭐️ 7.0/10
7. [Claude 的新系统提示真的不想复制歌曲歌词](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [谷歌 DeepMind 推出 Gemini 3.8 Flash 与 Flash Cyber 模型](https://deepmind.google/blog/introducing-gemini-3-8-flash-and-38-flash-cyber/) ⭐️ 9.0/10

谷歌 DeepMind 推出了 Gemini 3.8 Flash 和 Gemini 3.8 Flash Cyber，为 Flash 系列新增最新模型。官方称 Cyber 版本是其最强的网络安全模型，具备前沿水平的漏洞检测和自动修复能力。 Gemini Flash 系列以速度、低成本和多模态输入能力著称，广受开发者工作流和媒体分析场景欢迎。如果 3.8 的基准测试结果稳定——早期报告显示其排名接近 Opus 5 等更大的模型——这次发布有望以 Flash 级价格提供接近前沿的质量。 据报道，Gemini 3.8 Flash 支持文本、图像、语音和视频输入，输出文本，并拥有 100 万 token 的上下文窗口。专门的 3.8 Flash Cyber 模型基于 3.8 Flash 构建，经过微调，可以比大型模型更低的价格发现、验证和修复漏洞。

rss · Google DeepMind · 9月2日 16:18

**背景**: Gemini 是 Google DeepMind 的多模态大语言模型家族，包含 Pro、Flash、Flash Lite 等定位；Flash 模型被定位为高速、低成本的“主力”模型。Flash Cyber 产品线把这一设计延伸至网络安全领域，早前的 3.5 Flash Cyber 和 3.6 Flash Cyber 等版本已专注于自动化漏洞发现与修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/models/gemini-3-8-flash">Gemini 3.8 Flash (high) - Intelligence, Performance... | Artificial Analysis</a></li>
<li><a href="https://deepmind.google/models/gemini/cyber/">Gemini 3.8 Flash Cyber — Google DeepMind</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gemini_%28language_model%29">Gemini (language model ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体很热烈：开发者称赞模型的速度和低成本（有演示仅花 1.8 美分、13 秒完成），擅长 HTML/JavaScript 生成，并且基准成绩可与 Opus 5 等更大的模型抗衡。也有人指出 Gemini 支持音视频输入，比 OpenAI 和 Anthropic 旗舰模型更具多模态优势；不过有用户怀疑 3.8 在低思考等级下相比 3.7 出现回退。

**标签**: `#AI`, `#Google DeepMind`, `#Gemini`, `#language models`, `#model release`

---

<a id="item-2"></a>
## [Meta 发布 Muse Spark 1.3：以极低成本提供接近 SOTA 的性能](https://developer.meta.com/ai/models/muse-spark/) ⭐️ 8.0/10

Meta 发布了其最新的 AI 模型 Muse Spark 1.3，该模型针对智能体工作流、竞赛编程和复杂推理任务进行了优化。该模型在 DeepSWE 基准测试中取得了 75.4 的领先成绩，并在 Artificial Analysis 智能指数中名列前茅，提供了接近前沿模型的性能。 这一发布加剧了主流 AI 厂商之间的性价比竞争，以传统前沿模型极小部分的成本为开发者提供了接近 SOTA 的能力。此外，Meta 明确的定价模式（如果用户允许其数据用于训练则提供折扣）为数据隐私和价值评估树立了新的行业标准。 Muse Spark 1.3 具备用于挑战性智能体任务的“最大推理”（max reasoning）模式，并提供更高的首次尝试准确率和可靠的工具调用。在基准测试中，Muse Spark 1.3 \(max\) 在 Artificial Analysis 智能指数中得分 62，仅次于 Claude Fable 5.1 和 Claude Opus 5。

hackernews · bvaldivielso · 9月2日 19:35 · [社区讨论](https://news.ycombinator.com/item?id=49541256)

**背景**: DeepSWE 是一个旨在评估语言模型在解决真实世界问题时软件工程能力的基准测试。SOTA（State-of-the-Art，最先进水平）指特定领域达到的最高技术水平，在 AI 领域通常代表最强大且最昂贵的前沿模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.meta.com/ai/models/muse-spark/">Muse Spark 1.3 | Meta</a></li>
<li><a href="https://research.meta.ai/blog/introducing-muse-spark-1-3">Introducing Muse Spark 1.3 | Meta AI Research</a></li>
<li><a href="https://artificialanalysis.ai/articles/muse-spark-1-3">Muse Spark 1.3: Meta reaches the frontier | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 用户赞扬了该模型卓越的性价比和提升的能力，例如与 1.2 版本相比具有更好的 SVG 生成效果。社区还高度赞赏 Meta 透明的定价策略（即允许数据训练以换取更低的价格），认为这是一种公平且诚实的方法。

**标签**: `#AI`, `#Meta`, `#machine learning`, `#model release`, `#cost-performance`

---

<a id="item-3"></a>
## [谷歌避免其广告技术业务被拆分](https://www.nytimes.com/2026/09/02/technology/google-ad-tech-remedies.html) ⭐️ 8.0/10

法院裁定谷歌不必出售其广告技术业务，这对该公司来说是一次重大的反垄断胜利。

hackernews · donohoe · 9月2日 14:46 · [社区讨论](https://news.ycombinator.com/item?id=49537131)

**标签**: `#antitrust`, `#google`, `#adtech`, `#regulation`, `#tech policy`

---

<a id="item-4"></a>
## [Paint.NET 作者借助 AI 为 WINE 重写 Direct2D](https://simonwillison.net/2026/Sep/2/rick-brewster/) ⭐️ 8.0/10

Rick Brewster 宣布 Paint.NET 现已内置 PaintDotNet.Windows.Direct2D1.Managed.dll，这是微软 Direct2D API 的内部净室（clean-room）重写版本，在使用 /wine 参数启动时于 WINE 上启用。这约 18 万行代码主要由 Anthropic 的 Claude 生成，Brewster 称其大部分未经人工审查，属于“vibe coding”（氛围编程）。 这表明大语言模型如今能够完成对复杂专有 API 的大规模、可运行的系统级重写，大大降低了 WINE 兼容性等项目的门槛。同时，当 AI 生成了 18 万行且没有任何人完整审阅过的代码时，也引发了关于代码审查、正确性、可维护性和安全性的严重担忧。 此次重写的起因是，上游 WINE 中的 Direct2D“永远无法完善到”满足 Paint.NET 需求的程度。Brewster 不得不干预资源管理——Claude 最初未能对引用计数对象执行相当于 COM AddRef\(\) 的操作——还纠正了一些“非常糟糕的设计”决策；Paint.NET 其余部分约有 70 万行代码，是他 20 多年积累下来的。

rss · Simon Willison · 9月2日 05:50

**背景**: Direct2D 是微软的硬件加速 2D 矢量图形 API，Paint.NET 大量使用它进行渲染。WINE 是一个免费开源兼容层，通过黑盒逆向工程重新实现 Windows API（以避免版权问题），从而让 Windows 应用能在 Linux、macOS 及其他类 Unix 系统上运行。净室逆向工程意味着仅根据观察到的行为和公开规范编写独立实现。“Vibe coding”（氛围编程）是一种 AI 辅助开发方式，由 Andrej Karpathy 推广，开发者不深入审查 AI 生成的代码，而是依靠迭代提示来修正结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Direct2D">Direct2D</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wine_compatibility_layer">Wine compatibility layer</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>

</ul>
</details>

**标签**: `#AI-assisted development`, `#Direct2D`, `#WINE`, `#Reverse engineering`, `#Software engineering`

---

<a id="item-5"></a>
## [谷歌 DeepMind 倡导 AI 主动网络防御](https://deepmind.google/blog/proactive-cyber-defense-for-governments-and-enterprises/) ⭐️ 7.0/10

谷歌 DeepMind 发表文章，介绍了 AI 如何为政府和企业提供主动式网络防御支持。文章重点强调在攻击发生前预测并化解新兴威胁，而不是事后被动应对。 这一动向意义重大，因为它标志着网络安全正从“事后响应、事件驱动”的模式转向以机器学习为核心的预测性防御。如果被采纳，可能重新定义公共部门和大型机构在安全资源上的配置方式。 该消息以保护政府和企业网络免受新兴威胁为切入点，但并未公开具体技术细节或模型名称。重点在于强调 AI 在形成主动安全防御态势中的战略作用。

rss · Google DeepMind · 9月2日 16:24

**背景**: 传统的网络防御通常是反应式的：企业在攻击发生后才发现入侵并修复漏洞。主动式网络防御则力求在攻击链条的早期进行监测、预测并化解威胁。机器学习可以通过处理海量安全数据来识别异常模式，从而帮助发现可能即将发生的入侵。

**标签**: `#AI`, `#Cybersecurity`, `#DeepMind`, `#Defense`, `#Machine Learning`

---

<a id="item-6"></a>
## [IBM 展示如何在 Confluent 上利用时间序列模型实现实时智能](https://huggingface.co/blog/ibm-research/real-time-intelligence) ⭐️ 7.0/10

IBM Research 在 Hugging Face 上发布了一篇博客文章，介绍如何在 Confluent 上部署时间序列模型以实现实时智能应用。文章展示了将 TinyTimeMixer 等轻量级预训练模型与流式数据基础设施集成的方法。 这很重要，因为它将先进的时间序列基础模型与实时流式平台连接起来，使企业能够对实时数据进行低延迟预测。这可能帮助企业在无需构建脆弱、定制化管道的情况下，打造响应更快的 AI 应用。 该方法基于 IBM 的 TinyTimeMixer（TTM），这是一个紧凑的多元时间序列预测模型，参数规模从约 100 万起步，并在公共数据集上进行了预训练。Confluent 作为事件流层，将实时数据输入模型，以支持近实时决策。

rss · Hugging Face Blog · 9月2日 13:49

**背景**: 时间序列预测利用历史观测值来预测未来数值，可支持需求规划、库存管理和异常检测等应用场景。传统预测通常需要为每个数据集单独训练模型，速度慢且需要大量数据；TinyTimeMixer 则提供了一种预训练的基础模型，可以进行零样本或少样本预测。Confluent 是构建在 Apache Kafka 之上的数据流平台，可让组织实时处理事件并采取行动。这篇博客文章属于在流式平台上运行机器学习模型以实现实时智能这一更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.ibm.com/publications/tiny-time-mixers-ttms-fast-pre-trained-models-for-enhanced-zerofew-shot-forecasting-of-multivariate-time-series--1">Tiny Time Mixers (TTMs): Fast Pre-trained Models for Enhanced Zero/Few-Shot Forecasting of Multivariate Time Series for NeurIPS 2024 - IBM Research</a></li>
<li><a href="https://www.ibm.com/products/confluent">IBM Confluent</a></li>
<li><a href="https://huggingface.co/ibm-granite/granite-timeseries-ttm-r1">ibm-granite/granite-timeseries-ttm-r1 · Hugging Face</a></li>

</ul>
</details>

**标签**: `#time series`, `#real-time streaming`, `#IBM`, `#Confluent`, `#AI models`

---

<a id="item-7"></a>
## [Claude 的新系统提示真的不想复制歌曲歌词](https://simonwillison.net/2026/Sep/2/claudes-new-system-prompt/) ⭐️ 7.0/10

Anthropic 发布的 Claude 消费类应用系统提示现在明确指示模型不要复制歌曲歌词，这反映了持续的版权约束。

rss · Simon Willison · 9月2日 14:16

**标签**: `#AI`, `#Anthropic`, `#System Prompt`, `#Copyright`, `#Claude`

---