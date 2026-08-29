---
layout: default
title: "Horizon Summary: 2026-08-29 (ZH)"
date: 2026-08-29
lang: zh
---

> 从 17 条内容中筛选出 2 条重要资讯。

---

1. [Htmx 4.0.0 发布，带来新特性与兼容性改进](#item-1) ⭐️ 9.0/10
2. [vphone-cli：用 Apple Virtualization.framework 启动虚拟 iPhone](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Htmx 4.0.0 发布，带来新特性与兼容性改进](https://four.htmx.org/announcements/2026-08-28-htmx-4.0.0-is-released) ⭐️ 9.0/10

2026 年 8 月 28 日，Htmx 4.0.0 正式发布。新版本引入多项新功能和兼容性改进，例如通过 hx-alpine-compat 改善 htmx 与 Alpine.js 之间的兼容性。 这对超媒体驱动（hypermedia-driven）的 Web 开发社区来说是一个重要里程碑，因为 htmx 是在不编写自定义 JavaScript 的前提下构建交互式 Web 界面的最广泛使用的库之一。此次发布巩固了 htmx 作为复杂前端 JavaScript 框架替代方案的地位，也印证了业界对服务端渲染和以 HTML 为中心的架构日益增长的兴趣。 发布公告发布在 four.htmx.org 上，称新版本带来了新特性和兼容性改进。社区讨论显示此次发布获得了大量关注，评分 9.0/10，有 565 个点赞和 139 条评论；讨论中特别提到新版本加入 hx-alpine-compat 以改善 htmx 与 Alpine.js 的兼容性。

hackernews · rmsaksida · 8月28日 13:28 · [社区讨论](https://news.ycombinator.com/item?id=49478178)

**背景**: htmx 是一个 JavaScript 库，允许开发者通过 HTML 中的属性直接使用 AJAX、CSS 过渡、WebSocket 和 Server-Sent Events，而无需编写自定义 JavaScript。它属于更广泛的超媒体（hypermedia）运动的一部分，该运动将 HTML 视为应用的主要界面，并把服务器生成的片段直接换入页面。4.0 是该系列最新的主要版本，延续了库对简洁性和超媒体驱动交互的专注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Htmx">htmx - Wikipedia</a></li>
<li><a href="https://htmx.org/">htmx - high power tools for html</a></li>
<li><a href="https://htmx.org/docs/">htmx ~ Documentation</a></li>

</ul>
</details>

**社区讨论**: 开发者整体情绪非常正面，有人称赞 htmx 给开发带来乐趣和简洁，甚至 htmx 的 CEO 也表示迫不及待想试用新版本。也有少数不同观点：一位 .NET/Angular 开发者认为 htmx 迫使他重新混合表现层与业务逻辑，另一位开发者则觉得 alpine-ajax 更小且能满足自己的需求。总体而言，评论者将 htmx 视为一种给前端复杂度过重的环境带来清新空气、自然成长起来的替代方案。

**标签**: `#htmx`, `#web development`, `#hypermedia`, `#javascript`, `#release`

---

<a id="item-2"></a>
## [vphone-cli：用 Apple Virtualization.framework 启动虚拟 iPhone](https://github.com/Lakr233/vphone-cli) ⭐️ 8.0/10

vphone-cli 是一款新的开源命令行工具，利用 Apple 的 Virtualization.framework 在 Apple Silicon Mac 上启动虚拟 iPhone。它会下载并合并 IPSW 固件、修补引导链，并支持安装基于越狱的自定义固件（CFW）变体。 这一工具意义重大，因为它让开发者和安全研究人员无需实体 iPhone，即可在 Mac 上运行完整的 iOS 系统镜像（包括越狱变体），为 iOS 实验、自动化和恶意软件分析提供了新可能。不过目前需要 Apple Silicon Mac，并需要关闭或部分关闭系统完整性保护（SIP）。 该工具将所有文件存放在 ~/.vphone/ 下，并支持通过 fw prepare 指定本地 IPSW 文件来更新到更新的 iOS 版本。它提供五种安全绕过程度递增的补丁变体，用户需通过 --variant 参数选择；部分操作（如安装 CFW）需要 sudo 权限。

hackernews · hentrep · 8月28日 23:02 · [社区讨论](https://news.ycombinator.com/item?id=49485267)

**背景**: Apple 的 Virtualization.framework 是用于在 Mac 上创建和管理虚拟机的高级 API，官方支持启动 macOS 或 Linux。vphone-cli 通过合并 IPSW 固件并修补引导链，将此框架扩展到 iOS——这很不寻常，因为 iOS 通常只能在物理设备上运行。该项目是开源的，配套脚本 vphone-aio 旨在通过一条命令运行整个工具链。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Lakr233/vphone-cli">GitHub - Lakr233/vphone-cli · GitHub</a></li>
<li><a href="https://developer.apple.com/documentation/virtualization">Virtualization | Apple Developer Documentation</a></li>
<li><a href="https://github.com/34306/vphone-aio">GitHub - 34306/vphone-aio: 1 script run the vphone · GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者总体上很兴奋，但也提出了实际问题：有人想知道这与 iOS Simulator 有何不同，有人询问在选择日本或欧盟作为地区时会有哪些额外监管检查，还有人希望该工具未来能在非 Apple 电脑上运行。一个普遍的担忧是，使用该工具需要关闭或部分关闭系统完整性保护（SIP），这可能会破坏部分功能。

**标签**: `#virtualization`, `#iOS`, `#open-source`, `#Apple`, `#developer-tools`

---