---
layout: default
title: "Horizon Summary: 2026-08-21 (ZH)"
date: 2026-08-21
lang: zh
---

> 从 23 条内容中筛选出 4 条重要资讯。

---

1. [恶意 Rust crate Arrayref 运行构建时载荷](#item-1) ⭐️ 10.0/10
2. [Linux 7.2 发布：改进 HDMI 2.1 并引发社区讨论](#item-2) ⭐️ 9.0/10
3. [LiquidAI 推出 LFM2.5-DSpark，推理速度最高提升 3.2 倍](#item-3) ⭐️ 8.0/10
4. [Bun 1.4 的 Bun.WebView 驱动一个 shot-scraper 风格的 JSON API](#item-4) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [恶意 Rust crate Arrayref 运行构建时载荷](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 10.0/10

Rust crate arrayref 被发现包含恶意构建时载荷，标志着一次严重的供应链攻击，影响广泛。

hackernews · abhisek · 8月20日 13:23 · [社区讨论](https://news.ycombinator.com/item?id=49374269)

**标签**: `#security`, `#supply-chain`, `#rust`, `#malware`, `#open-source`

---

<a id="item-2"></a>
## [Linux 7.2 发布：改进 HDMI 2.1 并引发社区讨论](https://www.igalia.com/2026/08/19/Linux-72-Released.html) ⭐️ 9.0/10

根据 Igalia 的公告，Linux 7.2 已于 2026 年 8 月 19 日发布。这个新内核版本以包括 HDMI 2.1 支持在内的改进为亮点，并在社区中引发了热烈讨论。 Linux 7.2 是 Linux 内核的主要版本，而 Linux 内核支撑着服务器、桌面、嵌入式系统以及树莓派等设备，因此其改进会影响整个开源生态。HDMI 2.1 支持对现代显示器、游戏和高刷新率显示尤为重要，可能会推动 Linux 桌面与游戏体验的发展。 这篇文章本身只提供了一句话的发布公告；按网址所示日期为 2026 年 8 月 19 日，来源是 Igalia。此次发布以 HDMI 2.1 相关改进为亮点，但摘要中没有给出具体的补丁级细节，部分社区评论也只是猜测或提出基础性问题。

hackernews · mariuz · 8月20日 15:46 · [社区讨论](https://news.ycombinator.com/item?id=49376265)

**背景**: HDMI 2.1 是一种显示接口规范，引入了 Fixed Rate Link（FRL）——一种替代传统 TMDS 通道的信令技术，通过链路训练让每个通道保持固定数据速率，从而提供更高带宽，并支持可变刷新率（VRR）和动态 HDR 等功能。VRR 让显示器根据输入源的帧率调整刷新时间，减少画面撕裂和卡顿；Display Stream Compression（DSC）则是在传输前压缩视频信号，使高分辨率和高刷新率能够适配链路带宽。在 Linux 中启用 HDMI 2.1 通常需要内核与用户态图形驱动（如 AMD、Intel、NVIDIA）共同提供支持。社区讨论中提到 HDMI Forum 过去对 AMD 开源驱动的限制，这使得内核侧的 HDMI 2.1 支持成为热议话题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tftcentral.co.uk/articles/when-hdmi-2-1-isnt-hdmi-2-1">When HDMI 2.1 Isn&#x27;t HDMI 2.1 - The Confusing World of the Standard, &quot;Fake HDMI 2.1&quot; and Likely Future Abuse - TFTCentral</a></li>
<li><a href="https://www.hdmi.org/announce/detail/172">HDMI FORUM RELEASES VERSION 2.1 OF THE HDMI SPECIFICATION</a></li>
<li><a href="https://en.wikipedia.org/wiki/Display_Stream_Compression">Display Stream Compression - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有用户表示很想更新自己的树莓派 4 内核，也有不少人提出技术问题——例如，如果 HDMI Forum 曾阻止 AMD 的开源驱动，那么 HDMI 2.1 支持如何实现；以及桌面用户为什么应该选择 HDMI 而不是 DisplayPort。还有一些评论质疑这篇文章相比 LWN 报道的价值，或好奇目标读者是谁。

**标签**: `#linux`, `#kernel`, `#release`, `#hdmi`, `#open-source`

---

<a id="item-3"></a>
## [LiquidAI 推出 LFM2.5-DSpark，推理速度最高提升 3.2 倍](https://huggingface.co/blog/LiquidAI/lfm25-dspark) ⭐️ 8.0/10

LiquidAI 推出了 LFM2.5-DSpark，这是一种面向 LFM2.5 系列大语言模型的投机解码草稿模型，推理速度最高可提升 3.2 倍，具体解码速度提升达 3.18 倍，且不改变模型输出。该模型还使 LFM2.5-2.6B 的函数调用延迟平均降低 57%，并首发支持 llama.cpp 和 SGLang。 这很重要，因为它直接针对 LLM 推理中受内存限制的解码阶段，这是实时和端侧应用的主要瓶颈。通过在不改变输出的前提下实现更快推理，并开源相关集成，LiquidAI 使投机解码在边缘部署和智能体工作负载中变得切实可行。 每个 LFM2.5-DSpark 草稿模型都为现有目标模型添加了一条投机解码路径：一个约 300M 参数的草稿模型会提出包含九个候选 token 的块，目标模型在单次前向传播中完成验证。对于 1.2B 变体，草稿模型采用 5 层 Qwen3 风格的分组查询注意力架构，并配备低秩马尔可夫转移头（秩为 256）和置信度头。

rss · Hugging Face Blog · 8月20日 16:52

**背景**: 在大语言模型推理中，解码阶段传统上受内存限制——大部分延迟来自将权重从 DRAM 流式传输到 SRAM，而非计算本身。投机解码通过使用轻量级草稿模型生成候选 token，然后让目标模型在单次前向传播中验证全部候选 token，从而分摊加载权重的成本，解决了这一问题。这种方法对于延迟至关重要的端侧推理或智能体推理尤其有用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/LiquidAI/lfm25-dspark">Up to 3.2x Faster Inference with LFM2.5-DSpark</a></li>
<li><a href="https://www.marktechpost.com/2026/08/20/liquid-ai-releases-lfm2-5-dspark-draft-models-that-deliver-up-to-3-18x-faster-decoding/">Liquid AI Releases LFM2.5-DSpark Draft Models That Deliver Up to 3.18x Faster Decoding Without Changing Model Outputs - MarkTechPost</a></li>
<li><a href="https://huggingface.co/tugot17/LFM2.5-1.2B-Instruct-DSpark-5L">tugot17/LFM2.5-1.2B-Instruct-DSpark-5L · Hugging Face</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference optimization`, `#sparse attention`, `#performance`, `#Hugging Face`

---

<a id="item-4"></a>
## [Bun 1.4 的 Bun.WebView 驱动一个 shot-scraper 风格的 JSON API](https://simonwillison.net/2026/Aug/20/bun-webview-json-api/) ⭐️ 8.0/10

Bun 1.4 正式发布，使用了 Rust 重写，并新增了用于浏览器自动化的 Bun.WebView API。Simon Willison 利用 Bun.WebView 构建了一个原型 JSON API，可以加载网页并对其执行 JavaScript，类似于他的 shot-scraper CLI 工具。 这展示了 Bun 内置浏览器自动化的实际用途，开发者或许无需 Playwright 等外部依赖即可构建爬虫和自动化工具。Bun 1.4 还带来了显著的性能提升和更强的 Node.js 兼容性，使其成为更吸引人的 Web 工具运行时。 该原型 TypeScript 服务器在运行完整 Chrome 处理复杂网页时需要 192MB-256MB 的容器，并使用 cgroups 进行了测试。Bun.WebView 使用 macOS WebKit，或通过 Chrome DevTools 协议（CDP）控制本地 Chromium 进程。

rss · Simon Willison · 8月20日 15:37

**背景**: shot-scraper 是 Simon Willison 开发的一个 Python CLI 工具，基于 Playwright，用于自动截图和在浏览器中执行 JavaScript。Bun 是一个快速的全能 JavaScript 运行时，而 Bun.WebView 是直接内置在运行时中的无头浏览器，简化了浏览器自动化任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bun.com/docs/runtime/webview">WebView | Bun Docs</a></li>
<li><a href="https://github.com/simonw/shot-scraper">GitHub - simonw/ shot - scraper : A CLI utility for taking screenshots of...</a></li>

</ul>
</details>

**标签**: `#Bun`, `#WebView`, `#JSON API`, `#JavaScript`, `#Web Development`

---