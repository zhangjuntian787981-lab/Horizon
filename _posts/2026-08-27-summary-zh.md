---
layout: default
title: "Horizon Summary: 2026-08-27 (ZH)"
date: 2026-08-27
lang: zh
---

> 从 32 条内容中筛选出 5 条重要资讯。

---

1. [英伟达同意以 130 亿美元收购 Hugging Face](#item-1) ⭐️ 9.0/10
2. [亚马逊 Mechanical Turk 将于 9 月 30 日关闭](#item-2) ⭐️ 9.0/10
3. [Hugging Face Transformers v5.16.1 加入 GLM-5.3-Flash 原生支持](#item-3) ⭐️ 8.0/10
4. [Transformers v5.16.0 新增 Qwen4-Exp，采用 GatedResidual 与 QSA](#item-4) ⭐️ 8.0/10
5. [谷歌 DeepMind 推出 Gemini 3.5 Transcribe 智能语音转文字](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [英伟达同意以 130 亿美元收购 Hugging Face](https://www.businessinsider.com/nvidia-in-talks-to-buy-hugging-face-13-billion-dollars-2026-8) ⭐️ 9.0/10

英伟达已同意以约 130 亿美元收购人工智能社区平台 Hugging Face，这一消息由 The Information 和 TechCrunch 报道。这笔交易将使最广泛使用的开源模型仓库之一置于英伟达的控制之下。 这是 AI 行业具有里程碑意义的举措，使英伟达在占据主导地位的 GPU 硬件之外，又掌握了 AI 模型和数据的关键分发渠道。此举引发了对整个 AI 开发栈控制权、开源生态系统未来以及潜在反垄断审查的担忧。 据报道交易金额约为 130 亿美元；The Information 的付费文章引用的是 129 亿美元。Hugging Face 托管了超过 200 万个模型，是数据集和 AI 应用的重要中心，因此是 AI 基础设施的关键组成部分。

hackernews · mfiguiere · 8月27日 01:12 · [社区讨论](https://news.ycombinator.com/item?id=49458161)

**背景**: Hugging Face 是一家总部位于纽约的公司，以开源社区和用于自然语言处理的 Transformers 库而闻名，同时也是一个让机器学习从业者共享模型、数据集和应用的平台。AI 技术栈（AI stack）是指支持 AI 开发的技术、框架和基础设施的集合。作为 AI 芯片的主要供应商，英伟达一直在从硬件向软件扩展；收购 Hugging Face 将把其影响力扩展到模型发现、分发和开发者工作流程中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Hugging_Face">Hugging Face - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/hugging-face">What is Hugging Face? | IBM</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-stack">What is an AI stack? - IBM</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍持警惕态度，指出英伟达在开源方面的历史记录不佳，并希望控制在其硬件上运行的软件栈。一些人认为，获得 Hugging Face 平台数据的特权访问权可能引发反垄断问题；也有少量用户欢迎可能到来的免费 GPU 额度，并向团队表示祝贺。还有评论者指出，Hugging Face 此前曾拒绝较低估值下的较小投资，却在不到一年内同意以 130 亿美元被整体收购，这颇具讽刺意味。

**标签**: `#nvidia`, `#hugging-face`, `#acquisition`, `#ai`, `#open-source`

---

<a id="item-2"></a>
## [亚马逊 Mechanical Turk 将于 9 月 30 日关闭](https://www.mturk.com/) ⭐️ 9.0/10

亚马逊宣布其众包微任务平台 Mechanical Turk（MTurk）将于 9 月 30 日关闭。这一关闭标志着一个开创性平台的终结，该平台曾将企业与远程工作者连接起来，完成小型的、需要人工处理的任务。 此次关闭表明，AI 已经削弱了由人工完成微任务的经济合理性，也影响到依赖该平台获取收入的广大“Turker”群体。同时，随着 AI 越来越多地处理原本外包给人类的任务，这引发了关于众包劳动力未来的思考。 Mechanical Turk 由 Amazon Web Services 运营，使用“人类智能任务”（HITs）机制。据报道，该平台的高级项目经理早在几年前就已转往其他 AWS 项目，且即便在 AI 转型之前，该服务在 AWS 内部也被视为一个异类。

hackernews · tmp10423288442 · 8月26日 23:55 · [社区讨论](https://news.ycombinator.com/item?id=49457545)

**背景**: Mechanical Turk 于 2005 年上线，是一个众包市场，企业可以在上面发布小型“人类智能任务”（HITs），例如识别图片或撰写产品描述，这些任务是计算机难以轻易完成的。被称为“Turker”的工人完成这些任务以获取小额报酬。该平台成为研究人员和企业获取可扩展人力劳动的重要工具，但其模式日益受到人工智能发展的挑战。亚马逊在 8 月宣布，该服务将于 2026 年 9 月 30 日关闭。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Amazon_Mechanical_Turk">Amazon Mechanical Turk</a></li>
<li><a href="https://www.nytimes.com/interactive/2019/11/15/nyregion/amazon-mechanical-turk.html">I Found Work on an Amazon Website. I Made 97 Cents an Hour. - The New York Times</a></li>

</ul>
</details>

**社区讨论**: 评论者大多对此并不感到意外，指出 AI 和任务套利已侵蚀了该平台的独特价值。有几位提到管理层的变动——例如高级项目经理转往其他 AWS 项目——并认为关闭对 AWS 而言是迟早的事。另一些人则回顾了 MTurk 的文化意义，其中一位分享了 2005 年 MTurk“救了我一命”的个人经历，还有人认为在 AI 代理与人类工人结合潜力日增的当下，这个时机关闭并不明智。

**标签**: `#crowdsourcing`, `#amazon`, `#ai`, `#platform-shutdown`, `#mechanical-turk`

---

<a id="item-3"></a>
## [Hugging Face Transformers v5.16.1 加入 GLM-5.3-Flash 原生支持](https://github.com/huggingface/transformers/releases/tag/v5.16.1) ⭐️ 8.0/10

Hugging Face Transformers v5.16.1 正式支持 GLM-5.3-Flash，这是 GLM-5 系列中首个原生多模态模型。该版本还包含一些小修复，例如恢复 tensor-parallel API 的向后兼容性，并出于安全原因固定了 ESMFold2 的内核。 此次集成将一个拥有 320B 总参数、仅 18B 激活参数、并采用混合稀疏/线性注意力架构的 MoE 模型带入主流 Transformers 生态。这标志着业界正朝着高性价比多模态模型方向发展，这类模型在编程和智能体基准上可与更大的闭源模型竞争。 GLM-5.3-Flash 采用结合稀疏注意力与线性注意力的混合架构，以降低长上下文推理成本，并通过 Manifold-Constrained Hyper-Connections \(mHC\) 提升扩展效率。该模型在 30T token 的多模态语料上训练，据称在编程与智能体基准上接近 Claude Opus 4.8。

github · vasqu · 8月26日 14:50

**背景**: GLM-5.3-Flash 是由 Z.ai（原智谱 AI）开发的混合专家（MoE）模型，总参数 320B，每个 token 仅激活 18B 参数。稀疏注意力只关注部分 token 以提升效率，而线性注意力的计算量随序列长度线性增长；将两者结合旨在兼顾长上下文精度与更低的推理成本。mHC 是一种残差连接框架，将超连接投影到数学流形上，以保持恒等映射并提高深层网络的训练稳定性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/vlm/glm-5.3-flash">GLM - 5 . 3 - Flash - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://arxiv.org/abs/2512.24880">[2512.24880] mHC: Manifold-Constrained Hyper-Connections mHC: Manifold-Constrained Hyper-Connections - arXiv.org mHC: Manifold-Constrained Hyper-Connections ICML Poster mHC: Manifold-Constrained Hyper-Connections mHC (Manifold-Constrained Hyper-Connections) - GitHub mHC: Manifold-Constrained Hyper-Connections - GitHub DeepSeek mHC: Manifold-Constrained Hyper-Connections</a></li>
<li><a href="https://www.emergentmind.com/topics/hybrid-sparse-and-linear-attention-mechanisms">Hybrid Sparse &amp; Linear Attention</a></li>

</ul>
</details>

**标签**: `#transformers`, `#glm`, `#multimodal`, `#efficient-attention`, `#release`

---

<a id="item-4"></a>
## [Transformers v5.16.0 新增 Qwen4-Exp，采用 GatedResidual 与 QSA](https://github.com/huggingface/transformers/releases/tag/v5.16.0) ⭐️ 8.0/10

Hugging Face Transformers v5.16.0 新增了 Qwen4-Exp，它引入了 GatedResidual（GR）、Qwen Sparse Attention（QSA）和 Per-Layer Embedding（PLE）。该版本还加入了 GraniteSpeech5（约 4.7 亿参数的 CTC 语音识别模型）和 Step-3.7-Flash（1980 亿参数稀疏 MoE 视觉语言模型）。 Qwen4-Exp 是首个将线性注意力与稀疏注意力结合起来的混合架构，显著提升了长上下文场景的推理效率。由于 Transformers 是模型部署的标准库，这些新增功能使前沿架构能立即被更广泛的机器学习生态使用。 QSA 使用多个查询头对压缩后的键块打分，选择连续的 token 块，并保留不完整的尾部块不压缩，以降低索引开销。GraniteSpeech5 使用帧堆叠、带 Shaw 相对位置编码的块注意力以及自条件 CTC；Step-3.7-Flash 则采用基于 sigmoid 的路由器评分和每专家偏置，与 DeepSeek-V3 类似。

github · Cyrilvallez · 8月26日 12:35

**背景**: Transformers 是一个广泛使用的开源库，提供预训练模型架构。Qwen4-Exp 基于 Qwen3.5 的文本与多模态混合架构，采用 GatedResidual 等组件，通过细粒度门控混合多条残差流；QSA 则将 Gated DeltaNet（线性注意力）与稀疏块级选择结合，以高效处理长序列。PLE 使用哈希 n-gram 的词汇特征来丰富特定解码器层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/QwenLM/Qwen3.8-Flash-Next/">GitHub - QwenLM/Qwen3.8-Flash-Next: Qwen3.8-Flash-Next is the ...</a></li>
<li><a href="https://developer.nvidia.com/blog/experiment-with-qwen3-8-flash-next-176b-model-on-nvidia-gb300-nvl72-for-agentic-coding/">Experiment with Qwen3.8-Flash-Next 176B Model on NVIDIA GB300 ...</a></li>
<li><a href="https://sebastianraschka.com/llm-architecture-gallery/per-layer-embeddings/">Per-Layer Embeddings (PLE) | Sebastian Raschka, PhD</a></li>

</ul>
</details>

**标签**: `#transformers`, `#Qwen4`, `#model release`, `#AI/ML`, `#open source`

---

<a id="item-5"></a>
## [谷歌 DeepMind 推出 Gemini 3.5 Transcribe 智能语音转文字](https://deepmind.google/blog/intelligent-transcription-with-gemini-3-5-transcribe/) ⭐️ 7.0/10

谷歌 DeepMind 推出了 Gemini 3.5 Transcribe，这是一个基于 Gemini 音频理解能力的新型语音转文字模型。它提供低延迟、高精度的转录，并支持说话人分离、词级时间戳，以及能够清理语音不流畅现象的智能转录功能。 这一公告标志着转录技术的重大进步，利用 Gemini 先进的音频理解能力提升了准确性和实用性。它将惠及开发者、企业以及在日常应用中依赖快速可靠语音转文字功能的普通用户。 Gemini 3.5 Transcribe 可通过 Gemini API、Google AI Studio 和 Gemini Enterprise 使用，也可以在 macOS 上的 Gemini 应用或 Android 上的 Rambler 中体验。它支持基于话语的语言检测、多说话人识别和词级时间戳，并基于 Gemini 现有的音频理解能力构建。

rss · Google DeepMind · 8月26日 17:01

**背景**: 语音转文字技术将口语音频转换为文本，但传统模型在多人对话、背景噪音以及犹豫或重复等会话不流畅现象上常常表现不佳。Gemini 3.5 Transcribe 利用 Gemini 大语言模型的音频理解能力，更智能地应对这些挑战，并提供适合实时应用的低延迟结果。该模型属于谷歌更广泛的 Gemini 系列，该系列旨在统一文本、视觉和音频的多模态理解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemini-api/docs/models/gemini-3.5-transcribe">Gemini 3 . 5 Transcribe | Gemini API | Google AI for Developers</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/">Introducing Gemini 3 . 5 Transcribe</a></li>

</ul>
</details>

**标签**: `#speech-to-text`, `#transcription`, `#Gemini`, `#DeepMind`, `#AI`

---