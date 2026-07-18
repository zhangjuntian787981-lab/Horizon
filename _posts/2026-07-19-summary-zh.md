---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 14 条内容中筛选出 3 条重要资讯。

---

1. [LG 显示器通过 Windows Update 自动安装软件](#item-1) ⭐️ 9.0/10
2. [LLM 填补凸优化领域 30 年空白](#item-2) ⭐️ 8.0/10
3. [Anthropic 永久保留 Claude Fable 5 于订阅计划中](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [LG 显示器通过 Windows Update 自动安装软件](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

据报道，LG 显示器会在未经用户同意的情况下，通过 Windows Update 自动安装软件。该软件以系统权限运行，并在开机时自启动，带来安全风险。 这种行为类似于恶意软件——未经同意安装软件、拥有高权限且持久化，令人担忧。它影响所有连接 LG 显示器的用户，并暴露了 Windows 驱动程序分发模型的缺陷。 该软件通过 Windows Update 的自动驱动程序更新机制安装，拥有完全的系统访问权限和互联网连接。解决方法包括在设备安装设置中禁用“自动下载制造商的应用”。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 可以自动安装硬件厂商提交并经过 WHQL 认证的驱动程序和关联软件，以确保硬件正常运行。但厂商可以在驱动之外捆绑额外软件。这次 LG 显示器的软件正是利用这一机制，在未明确获得用户同意的情况下被推送。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://asibiont.com/en/blog/monitory-lg-tayno-ustanavlivayut-po-cherez-windows-update-bez-vashego-soglasiya-chto-proiskhodit-i-kak-zashchititsya">LG Monitors Silently Install Software Through Windows Update ...</a></li>
<li><a href="https://lightmask.net/trending/lg-monitors-silently-install-software-through-windows-update-without-consent/">LG Monitors Silently Install Software Through Windows Update ...</a></li>
<li><a href="https://support.microsoft.com/en-us/windows/hardware/drivers/automatically-get-recommended-and-updated-hardware-drivers">Automatically get recommended and updated hardware drivers | Microsoft Support</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈不满，指出该软件会在静默中安装并拥有系统权限，仅需连接显示器即可触发。用户分享了通过组策略或设备安装设置进行阻止的方法，并批评 LG 和微软缺乏防护措施。

**标签**: `#security`, `#Windows`, `#privacy`, `#LG`, `#hardware`

---

<a id="item-2"></a>
## [LLM 填补凸优化领域 30 年空白](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 8.0/10

LLM GPT-5.6（可能是 GPT-4 或 GPT-5 的一个变体）通过一个提示工程，解决了凸优化领域一个长达 30 年的开放问题，具体而言，它证明了在内存限制下优化凸 Lipschitz 函数的 oracle 复杂度的上界。 这一成就表明大型语言模型能够贡献新颖的数学证明，标志着人工智能辅助研究的一个转折点，可能加速理论计算机科学和优化领域的进展。 使用的模型为 Sol Pro（而非 Ultra），问题涉及球域上凸 Lipschitz 函数的时间复杂度界限，该限制虽然非平凡但具有泛化性。社区评论确认该成果是一个真实但较为小众的贡献。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化问题涉及在凸集上最小化凸函数；对偶间隙是原始问题最优值与对偶问题最优值之差，在约束规范条件下为零。该领域的一个开放问题是在有限内存下进行一阶凸优化的 oracle 复杂度，旨在刻画在内存约束下优化凸 Lipschitz 函数所需的最少查询次数。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Duality_gap">Duality gap - Wikipedia</a></li>
<li><a href="https://proceedings.mlr.press/v99/woodworth19a.html">Open Problem: The Oracle Complexity of Convex Optimization with Limited Memory</a></li>

</ul>
</details>

**社区讨论**: 社区大致验证了这一贡献，一位专家指出这是一个真实但小众的成果。评论者讨论了这对研究者的影响，认为低垂的果实将被自动化，并质疑 LLM 是否能因 ABC 猜想的晦涩而证明它。

**标签**: `#AI`, `#convex optimization`, `#mathematical proof`, `#LLM`

---

<a id="item-3"></a>
## [Anthropic 永久保留 Claude Fable 5 于订阅计划中](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 7.0/10

Anthropic 宣布自 7 月 20 日起，Claude Fable 5 将永久包含在 Max 和 Team Premium 订阅计划中，推翻了此前将其从订阅中移除、仅通过 API 提供的计划。 这一决定反映了来自 OpenAI 的 GPT-5.6 Sol 和 Kimi 的 K3 的激烈竞争，确保订阅用户无需额外 API 成本即可继续使用 Anthropic 最强大的模型。 Max 计划（每月 100/200 美元）和 Team Premium 以 50%的使用额度包含 Fable 5；Pro 和 Team Standard 用户获得一次性 100 美元积分并通过使用额度访问，但每月 20 美元的计划仍无法使用 Fable 5。

rss · Simon Willison · 7月18日 06:00

**背景**: Claude Fable 5 是 Anthropic 的旗舰推理模型，专为复杂、长时间运行的任务设计，具有 100 万 token 的上下文窗口。Anthropic 最初因计算容量限制计划从订阅中移除 Fable 5，但来自 GPT-5.6 Sol 和 Kimi K3 的竞争压力迫使公司改变决定以留住订阅用户。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/GPT-5.6">GPT-5.6 - Wikipedia</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Fable 5`, `#pricing`, `#competition`

---