---
layout: default
title: "Horizon Summary: 2026-08-30 (ZH)"
date: 2026-08-30
lang: zh
---

> 从 12 条内容中筛选出 2 条重要资讯。

---

1. [腾讯开源 Hy4 预览版，具备自我改进能力](#item-1) ⭐️ 8.0/10
2. [罗曼空间望远镜发射：宽视场与开放数据将重塑天文学](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [腾讯开源 Hy4 预览版，具备自我改进能力](https://www.tencent.com/tencent-releases-and-open-sources-tencent-hy4-preview/) ⭐️ 8.0/10

腾讯发布并开源了 Hy4 预览版，这是一个 7700 亿参数的混合专家模型，通过递归式自我改进循环参与了自己的开发。该模型已上线 Hugging Face 和 OpenRouter，上线数日内即处理了数万亿 token。 此次发布标志着大型科技公司在开源 AI 领域迈出重要一步，其新颖的自我改进机制可能重塑模型训练与优化的方式。该模型在 OpenRouter 上迅速被采用，速度超过 GLM 5.3，显示出市场对高效高质量开源模型的强烈需求。 Hy4 预览版总参数为 7700 亿，活跃参数为 490 亿，上下文窗口为 1,048,576 个 token，最大输出为 64,000 个 token。在 OpenRouter 上，输入价格约为每百万 token 0.834 美元，输出约为每百万 token 2.501 美元，缓存成本仅 5%，低于通常的 10%–20%。

hackernews · shenli3514 · 8月29日 19:33 · [社区讨论](https://news.ycombinator.com/item?id=49492632)

**背景**: Hy4 预览版是混合专家（MoE）模型，这种架构每次只激活部分参数以降低计算成本。它是腾讯 Hy3（2950 亿参数）的继任者，延续了该公司在开源权重 AI 领域的布局，并与腾讯 CodeBuddy 和 WorkBuddy 等产品协同设计。自我改进循环使模型能够提出方案、运行实验，并将结果反馈到后续训练迭代中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/tencent/Hy4-preview">tencent/Hy4-preview · Hugging Face</a></li>
<li><a href="https://openrouter.ai/tencent/hy4-preview">Hy4 preview - API Pricing &amp; Providers | OpenRouter</a></li>
<li><a href="https://cryptobriefing.com/tencent-hy4-preview-770b-ai-model/">Tencent spotted testing Hy4 model in Yuanbao app as expert-level model</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极：minimaxir 强调 Hy4 在 OpenRouter 上的“惊人热度”，数日内处理了数万亿 token 且缓存价格更低。jorl17 称赞 Hy3 的质量，称其几乎与 deepseek4-flash 相当，还有用户猜测它与 DeepSeek 存在关联。一些用户（如 fastball）批评发布中的基准图表具有误导性。

**标签**: `#AI`, `#Open Source`, `#Tencent`, `#LLM`

---

<a id="item-2"></a>
## [罗曼空间望远镜发射：宽视场与开放数据将重塑天文学](https://science.nasa.gov/mission/roman-space-telescope/) ⭐️ 8.0/10

NASA 的南希·格蕾丝·罗曼空间望远镜定于 2026 年 8 月 30 日搭乘 SpaceX 猎鹰重型火箭发射，此前已于 2025 年 11 月完成组装。它将提供覆盖 0.28 平方度的宽视场红外成像，并完全开放、无禁运期的数据供所有人使用。 罗曼的视场比哈勃大 100 倍，将使天文学家能够以前所未有的规模测绘暗能量、暗物质和系外行星。其开放数据政策意味着任何人都能——从专业研究人员到业余爱好者——立即下载并浏览每天多达 1.4TB 的原始压缩数据，无需等待任务团队分析，就有机会做出新发现。 罗曼搭载两台仪器：300.8 百万像素的宽视场仪器（WFI）以及用于高对比度系外行星成像的日冕仪（CGI）。其 2.4 米主镜由美国国家侦察局捐赠，这也是该任务得以在预算内并提前完成的原因之一。

hackernews · JumpCrisscross · 8月29日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49490870)

**背景**: 罗曼空间望远镜以 NASA 首任天文学主任南希·格蕾丝·罗曼的名字命名，是一台红外天文台，计划发射至日地 L2 拉格朗日点。它在 2010 年被列为天文学十年规划的最高优先级任务，并于 2016 年获批开发。该任务依托捐赠的间谍卫星主镜，将哈勃级别的清晰度与超大视场相结合，其数据将与鲁宾天文台等地面设施的巡天观测互补。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nancy_Grace_Roman_Space_Telescope">Nancy Grace Roman Space Telescope</a></li>
<li><a href="https://science.nasa.gov/mission/roman-space-telescope/">Nancy Grace Roman Space Telescope - NASA Science</a></li>
<li><a href="https://science.nasa.gov/mission/roman-space-telescope/wide-field-instrument/">Wide Field Instrument - NASA Science</a></li>

</ul>
</details>

**社区讨论**: 评论者们对任务的完全开放数据政策尤其兴奋，有人指出任何人都可能成为在每天 1.4TB 数据中第一个发现新天体（如奇异星际天体或星系）的人。还有人强调，罗曼在巡天方面的视场远优于哈勃；也有人认为，复用报废的间谍卫星使任务得以低于预算并提前完成。多位评论者期待未来十年罗曼与鲁宾天文台、哈勃和詹姆斯·韦伯望远镜协同工作。

**标签**: `#space`, `#astronomy`, `#NASA`, `#telescope`, `#open-data`

---