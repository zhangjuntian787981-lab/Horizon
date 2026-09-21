---
layout: default
title: "Horizon Summary: 2026-09-21 (ZH)"
date: 2026-09-21
lang: zh
---

> 从 12 条内容中筛选出 2 条重要资讯。

---

1. [Qwen 发布 Image 2.1：7B 开放权重文生图模型](#item-1) ⭐️ 8.0/10
2. [三星拟将 HBM4 与 HBM4E DRAM 产量提升一倍以上](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Qwen 发布 Image 2.1：7B 开放权重文生图模型](https://qwen.ai/blog?id=qwen-image-2.1) ⭐️ 8.0/10

Qwen 发布了 Qwen-Image 2.1，这是一个开放权重的文生图模型，参数量从前代 Qwen-Image 1 的 20B 缩减到仅 7B，同时新增原生透明背景支持，并显著提升了文字渲染能力。该模型可在 ComfyUI 中原生运行，并在单一模型中同时支持图像生成和基于一句话的图像编辑。 文字渲染一直是开放权重图像模型的短板，因此一个仅 7B 却能在排版上媲美甚至超越其他开源模型的版本，对任何在本地硬件上构建设计、海报或 UI 生成工具的人都意义重大。这也让 Qwen 直接与 GPT-Image 2、Flux 2、Ideogram 等规模更大的闭源与开源对手竞争，不过其更严格的许可证可能会限制商业应用。 该模型以 7B 参数成为目前最小的开放权重图像模型之一，据称只有 Z-Image Turbo 以 6B 更小；它还支持原生透明背景，而 Qwen 团队似乎是开放模型阵营中唯一在攻克这一方向的。值得注意的是，与以往许多采用 Apache 许可证的 Qwen 模型不同，该版本使用了限制性更强的许可证。

hackernews · jmillikin · 9月20日 13:09 · [社区讨论](https://news.ycombinator.com/item?id=49775499)

**背景**: 开放权重模型指任何人都可以下载并在本地运行的模型，与 OpenAI 图像模型这类闭源 API 相对。原生透明意味着模型自身直接生成 alpha 通道（即定义哪些像素透明的那部分数据），而不需要在生成后再做单独的去背景处理——OpenAI 也为其 GPT-Image-2 API 加入了同样的能力，说明这正成为一项竞争性特性。Qwen 是阿里巴巴的模型系列，该领域的文生图模型通常会被拿来与 Flux、Ideogram 和 Krea 比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://comfy.org/qwen-image-2.1/">Qwen-Image 2.1 on Comfy: Open-Weight Image Generation and Editing</a></li>
<li><a href="https://www.bentoml.com/blog/a-guide-to-open-source-image-generation-models">The Best Open-Source Image Generation Models in 2026</a></li>
<li><a href="https://www.llms.blog/posts/openai-adds-native-alpha-transparency-to-gpt-image-2-api">OpenAI Adds Native Alpha Transparency to GPT-Image-2 API</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论整体偏正面，强调其更小的 7B 体积、少见的原生透明支持，以及多位评论者认为在开放权重市场上最好的文字渲染能力，还有一位开发者分享了与 GPT-Image 2 的并排对比。主要担忧在于许可证：有评论者指出许多此前的 Qwen 模型采用 Apache 许可证，而这一版限制性明显更强；也有人询问如何像使用 llama-server 那样在本地运行该模型。

**标签**: `#AI image generation`, `#open-weight models`, `#Qwen`, `#text rendering`, `#model licensing`

---

<a id="item-2"></a>
## [三星拟将 HBM4 与 HBM4E DRAM 产量提升一倍以上](https://en.sedaily.com/finance/2026/09/20/samsung-to-double-hbm4-output-next-year-sources-say) ⭐️ 7.0/10

据 Sedaily 于 2026 年 9 月 20 日援引的消息人士称，三星预计将把 HBM4 和 HBM4E DRAM 的产量提升一倍以上，扩产计划瞄准明年。报道将此举描述为三星下一代高带宽内存产品线的大规模产能爬坡，而非小幅增量。 HBM 是为 AI 加速器供给数据的关键内存，因此三星 HBM4/HBM4E 产能翻倍有望缓解 GPU 与加速器出货的内存端瓶颈，同时加剧其与 SK 海力士、美光的竞争。但与此同时，将更多晶圆产能转向高利润的 HBM，可能会进一步挤压普通 DRAM 的供给，最终推高消费级内存的价格。 三星 HBM4 采用业界首个 1c DRAM 工艺、基于 4nm 代工的逻辑基础裸片以及先进封装技术，单堆栈容量最高可达 64GB、带宽达 4TB/s；在 2026 年 5 月向客户交付 12 层产品后，HBM4E 预计将推向 16 层堆栈。需要说明的是，产量翻倍这一数字来自匿名消息源，并非三星官方确认，因此实际时间表与出货量仍属未经证实。

hackernews · giuliomagnifico · 9月20日 17:38 · [社区讨论](https://news.ycombinator.com/item?id=49778029)

**背景**: 高带宽内存（HBM）是一种将多层内存裸片垂直堆叠、并用硅通孔（TSV）互连的 DRAM，带宽远超普通 DIMM 内存，因此被用于搭配 AI GPU 与加速器。HBM4 是 JEDEC 标准化（JESD270-4A）的第四代产品，通过宽位分布式接口与主计算裸片紧密耦合，而 HBM4E 是扩展版本，增加堆叠层数与容量。三星最初与 AMD、SK 海力士共同开发了 HBM 标准，如今 HBM 供给已成为 AI 硬件生产的关键瓶颈之一。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiconductor.samsung.com/dram/hbm/hbm4/">HBM4 | DRAM | Samsung Semiconductor Global</a></li>
<li><a href="https://www.jedec.org/standards-documents/docs/jesd270-4a">High Bandwidth Memory (HBM4) DRAM | JEDEC</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者指出，中国生产 AI 加速器的真正瓶颈并非逻辑裸片或 ASML 设备，而是长鑫存储（CXMT）的 HBM 产能，这限制了华为昇腾的出货量。其他人则讨论了大规模晶圆/裸片减薄工艺的经济性，追问为何 HBM 不能作为消费设备的首选内存（主要原因是成本），并感叹此次扩产很可能让消费级 DRAM 价格进一步恶化。

**标签**: `#HBM4`, `#Samsung`, `#semiconductors`, `#AI hardware`, `#memory supply chain`

---