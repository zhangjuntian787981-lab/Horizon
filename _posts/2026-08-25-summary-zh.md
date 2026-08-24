---
layout: default
title: "Horizon Summary: 2026-08-25 (ZH)"
date: 2026-08-25
lang: zh
---

> 从 23 条内容中筛选出 4 条重要资讯。

---

1. [微软画图和照片应用在 AI 生成图片中悄悄嵌入不可见 GUID 水印](#item-1) ⭐️ 8.0/10
2. [旧金山全城被重建成可玩的 3D 网页游戏地图](#item-2) ⭐️ 8.0/10
3. [OpenAI 将 GPT-5.6 引入 Kiro IDE，承诺更优性价比](#item-3) ⭐️ 8.0/10
4. [SQLite 数据库文件变身 Linux 可执行程序](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软画图和照片应用在 AI 生成图片中悄悄嵌入不可见 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软画图（Microsoft Paint）和微软照片（Microsoft Photos）会在本地 AI 生成或处理过的图片中不可见地嵌入一个唯一的 GUID 水印，即使 AI 模型完全在本地运行也是如此。可见水印可以关闭，但不可见水印无法关闭，并且会在用户不知情的情况下悄悄嵌入。 这引发了严重的隐私和匿名性担忧，因为 GUID 可能与微软账户绑定，从而可能识别出创建图片的用户身份。这也反映了行业趋势——在 AI 生成内容中嵌入来源元数据，这种技术既可用于真实性验证，也可能被用于监控等更有争议的目的。 根据该报告，微软画图和微软照片都会对经过 AI 处理的图片添加不可见水印，即使操作完全由本地模型执行。目前尚不清楚简单的操作（如 AI 增强背景删除）是否也会被添加水印；GUID 是一个 128 位的标识符，是微软对 UUID 的称呼。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: 不可见水印技术会将信息嵌入数字图像中，人眼无法察觉，但软件可以读取。GUID（全局唯一标识符）是微软对 UUID 的称呼，UUID 是一种 128 位的数字，用于在计算机系统中唯一标识信息。内容来源与真实性联盟（C2PA）提供了一个开放技术标准，用于认证媒体内容的来源和历史，越来越多地被用于打击虚假信息。该报告表明，微软的实现在精神上与此类似，但由于该唯一标识符未向用户披露，可能更具争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Universally_unique_identifier">Universally unique identifier - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Content_Authenticity_Initiative">Content Authenticity Initiative - Wikipedia</a></li>
<li><a href="https://c2pa.org/">C2PA | Providing Origins of Media Content</a></li>

</ul>
</details>

**社区讨论**: 评论者惊讶于画图应用变成了支持 AI 的编辑器，许多人关注到与微软账户绑定的秘密唯一标识符带来的隐私影响。有人将此事与微软过去错误地在 Azure DevOps 提交上盖章 Copilot 水印的做法联系起来，并建议不要使用画图或其他支持 LLM 的应用。也有评论认为 AI 方面是障眼法——核心问题在于所有图片都被悄悄添加了唯一标识符。

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#image-processing`

---

<a id="item-2"></a>
## [旧金山全城被重建成可玩的 3D 网页游戏地图](https://sf.thijs.gg/) ⭐️ 8.0/10

开发者创建了 sf.thijs.gg，这是一个基于 GIS 数据构建的整个旧金山市的交互式 3D 地图，并以类视频游戏的体验在线分享。该项目发布在 Twitter 上，允许用户驾车环游城市并收集硬币。 这展示了将开放城市数据用于游戏引擎的新颖且易得的方式，让真实城市能以趣味方式被探索。这可能会启发更多城市被重建为游戏地图，并推动将 GIS 数据转化为互动体验的工具发展。 该地图基于 Web，由公共 GIS 数据构建，以风格化但可辨认的方式呈现旧金山布局。它包含驾车与收集硬币的玩法，用户建议加入街道名称、地标及更高分辨率纹理。

hackernews · centrosphere · 8月24日 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**背景**: 地理信息系统（GIS）是一种捕获、存储、分析和显示与特定位置相关数据的计算机系统。3D 城市模型是城市环境的数字表示，通常使用 Esri CityEngine 等工具从 GIS 数据生成，或从 LiDAR 扫描中提取。这个项目运用这些技术构建了一个类似游戏的、可探索的真实城市版本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.usgs.gov/faqs/what-a-geographic-information-system-gis">What is a geographic information system (GIS)? | U.S. Geological Survey</a></li>
<li><a href="https://en.wikipedia.org/wiki/3D_city_model">3D city model - Wikipedia</a></li>
<li><a href="https://developers.arcgis.com/documentation/mapping-and-location-services/data-visualization/3d-visualization/cities-in-3d/">Cities in 3D | Documentation | Esri Developer - ArcGIS Online</a></li>

</ul>
</details>

**社区讨论**: 评论区反响热烈：一位旧金山前居民表示在熟悉地点漫步时感到激动，其他人建议增加街道名称、地址传送、更高分辨率的街景纹理以及 MMO 模式。还有人分享了相关项目，包括一个为费城制作的类似 GIS 游戏，另一个人描述了自己长期设想的、从城市数据自动构建 GTA 风格地图的流程。

**标签**: `#GIS`, `#3D rendering`, `#web-based game`, `#San Francisco`, `#open data`

---

<a id="item-3"></a>
## [OpenAI 将 GPT-5.6 引入 Kiro IDE，承诺更优性价比](https://openai.com/index/gpt-5-6-in-kiro) ⭐️ 8.0/10

OpenAI 宣布 GPT-5.6 现已集成到 Kiro（一款智能体驱动的 AI 集成开发环境）中。该集成帮助开发者以更优的性价比规划、构建、审查和测试软件。 此举将前沿 AI 模型能力直接带入开发者的日常工作流程，有望降低编码成本并加速软件交付。同时，它也加剧了 AI 辅助开发工具市场的竞争，该市场已有 GitHub Copilot 和 Cursor 等竞争者。 Kiro 是一款智能体 IDE，内置 Kiro Agent 以支持 AI 辅助的编程任务。GPT-5.6 模型系列包含三个变体——Luna、Terra 和 Sol，其中 Sol 能力最强；公告强调成本效率，但未给出具体定价或可用层级。

rss · OpenAI News · 8月24日 12:00

**背景**: Kiro 是一款面向智能体编程辅助的 AI 驱动集成开发环境，其配置路径如 ~/.config/Kiro/User/globalStorage/kiro.kiroagent。GPT-5.6 是 OpenAI 的大语言模型系列，于 2026 年 7 月 9 日公开发布，此前在 2026 年 6 月进行过有限预览；该系列面向企业工作、编码、科学研究和网络安全。智能体 IDE 与前沿模型的结合旨在简化整个软件开发周期。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Kiro_IDE">Kiro IDE</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT-5.6: Frontier intelligence that scales with your ambition | OpenAI</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#developer tools`, `#AI`, `#price-performance`

---

<a id="item-4"></a>
## [SQLite 数据库文件变身 Linux 可执行程序](https://simonwillison.net/2026/Aug/24/your-executable-is-a-sqlite-database/) ⭐️ 7.0/10

Farid Zakaria 展示了一种方法，可以将 SQLite 数据库文件同时作为 Linux 可执行程序使用：把 ELF 格式的各个组件存入 SQLite 数据表，并将数据库的应用 ID 设为“SELF”。该技术使用名为 self-exec 的自定义解释器，并可借助 Linux 内核的 binfmt\_misc 机制自动执行此类文件。 这一技术模糊了数据文件与可执行程序之间的界限，使同一个文件既能作为可查询的数据库，又能作为可运行的程序，为软件分发带来新的可能性。它同时也彰显了 Linux binfmt\_misc 机制在支持新型可执行格式方面的灵活性。 该技术利用了 SQLite 文件头中第 68 字节偏移处的 4 字节应用 ID 字段，将其设置为“SELF”（Structured Executable &amp; Linkable Format）。自定义解释器 self-exec 负责提取并运行 ELF 组件，同时可通过 binfmt\_misc 注册模式“:self:M:68:SELF::/usr/local/bin/self-exec:”来实现自动执行。

rss · Simon Willison · 8月24日 11:38

**背景**: SQLite 是一个嵌入式数据库引擎，数据存放在一个自带固定文件头的便携式文件中，其中包含一个 4 字节的应用 ID 字段，供应用程序识别文件类型。ELF（Executable and Linkable Format，可执行与可链接格式）是 Linux 及其他类 Unix 系统上可执行文件、目标代码和共享库的标准二进制格式。binfmt\_misc 是 Linux 内核的一项功能，允许通过魔数字节序列注册任意可执行格式，并交由用户空间的解释器处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kernel.org/doc/html/latest/admin-guide/binfmt-misc.html">Kernel Support for miscellaneous Binary Formats ( binfmt _misc)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binfmt_misc">binfmt_misc - Wikipedia</a></li>
<li><a href="https://0xax.gitbooks.io/linux-insides/content/Theory/linux-theory-2.html">Elf 64 · Linux Inside</a></li>

</ul>
</details>

**标签**: `#linux`, `#sqlite`, `#executable`, `#elf`, `#binfmt`

---