---
layout: default
title: "Horizon Summary: 2026-09-08 (ZH)"
date: 2026-09-08
lang: zh
---

> 从 8 条内容中筛选出 2 条重要资讯。

---

1. [Linux 内核 Git 托管被恶意爬虫压垮](#item-1) ⭐️ 7.0/10
2. [OpenAI 首席科学家呼吁发展防御性 AI 并警告勿鲁莽竞赛](#item-2) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Linux 内核 Git 托管被恶意爬虫压垮](https://simonwillison.net/2026/Sep/7/creepy-crawlies/) ⭐️ 7.0/10

Konstantin Ryabitsev 报告称，git.kernel.org 为恶意爬虫渲染提交页面所消耗的 CPU 周期，已超过包括 git 克隆在内的所有合法访问。在 5 个地理分布节点上，有 14 个 CPU 核心持续为爬虫将提交渲染为 HTML。 这凸显了 AI 训练爬虫和激进爬虫给开源基础设施带来的日益增长的财务与运营负担。如果不加遏制，这种“背景辐射”可能迫使维护者采取更严格的机器人防护措施，从而也影响合法用户。 受影响的基础设施是 Linux 内核官方 Git 托管站点 git.kernel.org，它使用 cgit 来渲染网页。这些 CPU 消耗纯粹用于提交记录的 HTML 渲染，而非提供 git 克隆流量；负载由爬虫反复抓取提交页面所产生。

rss · Simon Willison · 9月7日 23:08

**背景**: cgit 是一个用 C 语言编写的超快 Git 仓库 Web 前端，内置缓存以减轻服务器 I/O 压力。像 git.kernel.org 这样的网站将提交历史和源码以 HTML 形式公开，方便用户免克隆浏览；AI 公司爬虫及其他机器人频繁抓取这些页面，消耗与其价值不成比例的资源。Linux 内核项目运营着多地冗余节点，为全球开发者社区提供服务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wiki.archlinux.org/title/Cgit">cgit - ArchWiki</a></li>
<li><a href="https://github.com/kernelorg-mirror/infra_cgit">GitHub - kernelorg-mirror/infra_cgit: Kernel.org fork of cgit</a></li>

</ul>
</details>

**标签**: `#crawling`, `#linux-kernel`, `#web-operations`, `#abuse`, `#infrastructure`

---

<a id="item-2"></a>
## [OpenAI 首席科学家呼吁发展防御性 AI 并警告勿鲁莽竞赛](https://simonwillison.net/2026/Sep/7/jakub-pachocki/) ⭐️ 7.0/10

在 OpenAI 发布的《An Alien Mind》文章中，首席科学家 Jakub Pachocki 提出，需要强大且对齐的 AI 来构建防御系统，以应对其他 AI 带来的危险。他表示防御性部署将是 OpenAI 工作的重点，但同时强调这种紧迫性不应成为鲁莽竞赛的借口。 这反映了领先 AI 实验室内部的一种战略观点，即安全与能力发展相互交织，并以防御需求作为继续训练的理由。它可能影响关于前沿 AI 开发应当加速还是暂停的公共与政策讨论。 该引文出自 OpenAI 文章中的“可扩展防御”部分，提到了保护基础设施、实时防范失控智能体，以及发明全新防护措施。但这段摘录没有披露具体技术路线或新能力。

rss · Simon Willison · 9月7日 22:26

**背景**: AI 对齐旨在让 AI 系统的目标与行为符合人类的实际意愿，即我们的价值观、规则和意图，而不是因为机械遵循指令而造成伤害。“失控的 AI 代理”通常指偏离其预期角色或运行场景的智能体，随着自主智能体投入部署，这类风险越来越受关注。Pachocki 的言论处于关于如何管理前沿 AI 风险同时继续受益于技术进步的更广泛讨论之中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-alignment">What is AI alignment? - IBM</a></li>
<li><a href="https://hai.stanford.edu/ai-definitions/what-is-ai-alignment">What is AI Alignment? - Stanford HAI</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#OpenAI`, `#AI policy`, `#AI ethics`, `#defensive AI`

---