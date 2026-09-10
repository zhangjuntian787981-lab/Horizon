---
layout: default
title: "Horizon Summary: 2026-09-10 (ZH)"
date: 2026-09-10
lang: zh
---

> 从 27 条内容中筛选出 4 条重要资讯。

---

1. [苹果发布首款折叠屏手机 iPhone Duo](#item-1) ⭐️ 9.0/10
2. [Calif Research 发布 WeWorm：借助 AI 打造的微信通话零点击蠕虫](#item-2) ⭐️ 9.0/10
3. [Shopify 收购广受欢迎的实用优先 CSS 框架 Tailwind](#item-3) ⭐️ 8.0/10
4. [IBM 以商业友好许可发布 Granite 时间序列 PatchTST-FM-r2 模型](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [苹果发布首款折叠屏手机 iPhone Duo](https://www.apple.com/iphone-duo/) ⭐️ 9.0/10

苹果发布了其首款折叠屏手机 iPhone Duo，该消息在 Hacker News 上获得 847 分和 1648 条评论。看过早期上手视频的社区成员表示屏幕几乎没有可见折痕，还有不少人指出发布会的整体风格发生明显变化，并将其归因于硬件负责人 John Ternus 扮演了更重要的角色。 苹果进入折叠屏品类意义重大，因为这可能终于能推动开发者为折叠形态专门设计应用——而 Android 折叠屏用户普遍认为这个问题至今仍未真正解决。同时，这也释放出苹果产品方向与领导风格变化的信号，毕竟该公司历来在新硬件品类中都是后发但影响力巨大的玩家。 此前的报道显示，苹果一直在与超薄玻璃（UTG）供应商合作，据称其方案只对玻璃的中央区域做减薄处理，从而保留更大的整体厚度以提升耐用性。评论者特别指出，屏幕上几乎看不到折痕这一点，恰恰是发布会本身没能很好传达的细节。

hackernews · thecosmicfrog · 9月9日 18:15 · [社区讨论](https://news.ycombinator.com/item?id=49630931)

**背景**: 折叠屏手机的原理是将柔性 OLED 面板与精密铰链以及超薄玻璃盖板组合在一起，这种玻璃最薄可做到约 30 微米，三星显示是业界首家将此类 UTG 商用化的厂商。由于屏幕可以半折使用或完全展开，软件也必须相应适配，这正是应用连续性、分屏模式等功能重要的原因。此前普遍有报道称苹果正为首款折叠设备做准备，时间点大约在 2026 年，因此 iPhone Duo 可视为这一长期传闻产品线的落地。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/apple/comments/1inri8a/apple_taps_ultrathin_glass_suppliers_for_first/">r/apple on Reddit: Apple Taps Ultra-Thin Glass Suppliers for First Foldable Device</a></li>
<li><a href="https://news.samsung.com/us/samsung-utg-glass-foldable-display-easily-bendable-ultra-thin-glass">Samsung Display Introduces Foldable Display with Easily Bendable, Ultra-thin Glass</a></li>
<li><a href="https://developer.samsung.com/sdp/blog/en/2021/09/14/adapt-your-app-to-foldable-devices-for-an-optimal-user-experience">Adapt Your App to Foldable Devices for an Optimal User Experience</a></li>

</ul>
</details>

**社区讨论**: 讨论情绪褒贬不一，但对硬件整体偏正面：多位评论者称赞其设计和无折痕屏幕，一位 Android 折叠屏用户也欢迎苹果入场，认为这会促使开发者真正适配折叠形态，而不是简单拉伸应用。持怀疑态度的人认为折叠屏是“既是更差的手机，也是更差的平板”，而更谨慎的声音则表示会再观望几代，毕竟手机是日常生活中极其关键的设备。

**标签**: `#Apple`, `#iPhone Duo`, `#foldable phones`, `#mobile hardware`, `#Hacker News`

---

<a id="item-2"></a>
## [Calif Research 发布 WeWorm：借助 AI 打造的微信通话零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，称这是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫。该团队表示，借助 AI，他们在约两天内找到了漏洞并写出首个远程代码执行（RCE）利用程序，之后又用大约一周时间构建出蠕虫。 这表明 AI 已把针对一个拥有超十亿用户的即时通讯平台开发蠕虫级攻击所需的时间和人力大幅压缩，把过去需要大团队耗时数月的工作变成大约一周的产出。这对平台安全团队、漏洞披露规范以及围绕 AI 辅助攻击性安全的讨论都有直接影响。 据 Calif Research 称，受害者无需接听电话，也完全不需要操作手机；即使接听，他们也听不到任何声音，而利用仍然成功。目前这只是一个演示，团队将自己的角色定位为提供判断——决定攻击目标以及如何安全测试——而非亲自完成漏洞利用工作。

rss · Simon Willison · 9月10日 00:56

**背景**: 零点击利用是指在完全不需要用户任何交互（例如点击链接或打开文件）的情况下就攻陷设备，因此比普通的钓鱼式攻击更加隐蔽、也更难防御。远程代码执行（RCE）指攻击者能够通过网络在目标机器上运行任意代码，通常属于最严重的一类漏洞。蠕虫则是一种会自动复制并向新目标传播的恶意软件——在这里是通过微信通话传播——因此在主流即时通讯应用上实现可用的零点击 RCE 蠕虫属于最糟糕的组合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Zero-click_exploit">Zero-click exploit</a></li>
<li><a href="https://en.wikipedia.org/wiki/Remote_code_execution">Remote code execution</a></li>
<li><a href="https://www.f5.com/glossary/zero-click-attack">Zero - click attack | F5</a></li>

</ul>
</details>

**标签**: `#ai-security-research`, `#zero-click-exploit`, `#wechat`, `#rce`, `#cybersecurity`

---

<a id="item-3"></a>
## [Shopify 收购广受欢迎的实用优先 CSS 框架 Tailwind](https://tailwindcss.com/blog/tailwind-is-joining-shopify) ⭐️ 8.0/10

Shopify 已收购由 Adam Wathan 及其 Tailwind Labs 团队打造的实用优先（utility-first）CSS 框架 Tailwind CSS，这一消息发布在项目官方博客上。此次收购将这一使用最广泛的前端样式工具之一并入一家大型电商平台公司。 Tailwind CSS 被嵌入到无数 Web 项目、设计系统和组件库中，因此所有权变更会立刻引发关于治理、许可证以及路线图的疑问——而这恰恰是整个前端生态所依赖的开源项目。此事也凸显了一个更广泛的趋势：AI 编程助手正在侵蚀那些依靠开源核心之上的文档、模板和教育内容变现的开发者工具公司的商业模式。 讨论中分享的背景信息指出，Tailwind Labs 的工程团队裁减了 75% 的人员，官方文档的流量相比 2023 年初下降了约 40%，尽管框架本身的热度仍在上升——因为 AI 助手现在直接回答了开发者过去需要查文档的问题。有评论者认为，这笔交易本质上是对团队和品牌的“人才收购”（acqui-hire），而非技术收购。

hackernews · EdwinHoksberg · 9月9日 13:27 · [社区讨论](https://news.ycombinator.com/item?id=49626190)

**背景**: Tailwind CSS 让“实用优先”的方法流行起来：开发者不再编写自定义 CSS 规则或语义化类名，而是直接在 HTML 标记中组合 flex、pt-4、text-center 这类单一用途的小类来套用样式。这类框架已成为许多前端团队的默认选择，因为样式与标记保持在一起，避免了维护庞大手写样式表的痛苦。Tailwind Labs 通过 Tailwind Plus（原 Tailwind UI）组件模板等付费产品以及与文档相关的服务，为这个开源项目实现商业化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tailwindcss.com/">Tailwind CSS - Rapidly build modern websites without ever leaving...</a></li>
<li><a href="https://medevel.com/13-css-frameworks/">13 Open Source Utility - first CSS Frameworks For Serious Developers</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体是向团队道贺，但对框架的未来看法不一：simonw 提供了背景，称 AI 使 Tailwind Labs 的工程团队缩减 75%、文档流量下降 40%；jedberg 认为，当 LLM 能够“vibe code”出付费部分时，同时经营开源与商业组件的开发者工具公司越来越难持续；而 fg137 则质疑，在原生 CSS 加上 AI 生成代码已消除许多维护痛点的情况下，是否还有必要使用 Tailwind。

**标签**: `#tailwind-css`, `#shopify`, `#acquisition`, `#open-source`, `#ai-impact`

---

<a id="item-4"></a>
## [IBM 以商业友好许可发布 Granite 时间序列 PatchTST-FM-r2 模型](https://huggingface.co/blog/ibm-research/ibm-releases-sota-granite-time-series) ⭐️ 7.0/10

IBM Research 在 Hugging Face 上发布了 Granite Time Series PatchTST-FM-r2，这是一个达到当前最优水平（SOTA）的时间序列基础模型，并采用商业友好的许可协议。它是 IBM Granite 时间序列家族的最新成员，该家族此前主要以超紧凑的 TinyTimeMixer（TTM）和 TSPulse 模型为代表。 以宽松商业许可发布的最优时间序列基础模型，降低了企业将预测能力嵌入生产系统的门槛，无需承担法律或成本上的摩擦。这也加剧了该领域的竞争——Google 的 TimesFM、Amazon 的 Chronos 和 Salesforce 的 Moirai 已在此布局，而开放的许可协议正成为关键的差异化因素。 该模型基于 PatchTST 架构，将时间序列切分为若干片段（patch）作为 Transformer 的输入 token，并主打对未见序列的零样本预测能力。IBM 尚未公布独立的基准对比或详细的参数规模，因此所谓 SOTA 性能目前仍基于 IBM 自身的评测，而非第三方验证。

rss · Hugging Face Blog · 9月9日 15:36

**背景**: 时间序列基础模型沿用了大语言模型的思路：先在一个大规模、多样化的序列语料上预训练一次，随后无需针对具体任务重新训练即可对新数据进行预测，这一特性被称为零样本泛化。PatchTST 出自 ICLR 2023 论文《A Time Series is Worth 64 Words: Long-term Forecasting with Transformers》，是一种被广泛使用的长周期预测 Transformer 骨干，它将子序列视为片段（patch）而非单个时间步。IBM 的 Granite 时间序列产品线最初以 TinyTimeMixer 为代表，这类模型参数不足 100 万，追求极致的高效性，因此本次发布标志着其向更大容量基础模型的转向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/ibm-granite/granite-timeseries-ttm-r2">ibm - granite / granite - timeseries -ttm-r2 · Hugging Face</a></li>
<li><a href="https://www.ibm.com/granite/docs/models/time-series/">IBM Granite Time Series Documentation – IBM Granite</a></li>
<li><a href="https://github.com/yuqinie98/PatchTST">GitHub - yuqinie98/PatchTST: An offical implementation of PatchTST: &quot;A Time Series is Worth 64 Words: Long-term Forecasting with Transformers.&quot; (ICLR 2023) https://arxiv.org/abs/2211.14730 · GitHub</a></li>

</ul>
</details>

**标签**: `#time series`, `#foundation models`, `#IBM Granite`, `#PatchTST`, `#open source`

---