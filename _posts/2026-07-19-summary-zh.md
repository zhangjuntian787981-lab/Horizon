---
layout: default
title: "Horizon Summary: 2026-07-19 (ZH)"
date: 2026-07-19
lang: zh
---

> 从 18 条内容中筛选出 3 条重要资讯。

---

1. [GPT-5.6 通过提示解决凸优化 30 年难题](#item-1) ⭐️ 9.0/10
2. [LG 显示器通过 Windows Update 静默安装软件](#item-2) ⭐️ 9.0/10
3. [Claude Fable 5 永久纳入订阅套餐](#item-3) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GPT-5.6 通过提示解决凸优化 30 年难题](https://old.reddit.com/r/math/comments/1uxj3cy/after_openais_cdc_proof_announcement_gpt56_used_a/) ⭐️ 9.0/10

GPT-5.6（一种大型语言模型）通过一个提示证明了一个关于凸 Lipschitz 函数优化复杂度的猜想，弥补了凸优化领域 30 年的空白。 这表明大语言模型能够为长期未解的数学问题做出贡献，可能加速研究进展，并将焦点转移到更具创新性的方法上。 该猜想涉及在球形域上凸优化时间复杂度的上界，由于变量替换，球形域并不是真正的限制。该证明尚未经过同行评审。

hackernews · mbustamanter · 7月18日 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48957779)

**背景**: 凸优化是数学优化的一个子领域，旨在在凸集上最小化凸函数，通常可在多项式时间内求解。所解决的问题是凸 Lipschitz 函数最优复杂度方面的空白，已有 30 年未解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Convex_optimization">Convex optimization</a></li>
<li><a href="https://grokipedia.com/page/Convex_optimization">Convex optimization</a></li>

</ul>
</details>

**社区讨论**: 社区评论者指出该问题虽然小众但确实是贡献，有人质疑同行评审状态，也有人建议 LLM 可以针对其他难解证明如 abc 猜想。情绪谨慎乐观。

**标签**: `#AI`, `#convex optimization`, `#mathematical proof`, `#LLM`, `#theory`

---

<a id="item-2"></a>
## [LG 显示器通过 Windows Update 静默安装软件](https://videocardz.com/newz/lg-monitors-silently-install-software-through-windows-update-without-user-consent) ⭐️ 9.0/10

LG 显示器通过 HDMI 连接时，利用 Windows Update 在未经用户同意的情况下静默安装软件（例如 LG OnScreen Control），一旦插入显示器或甚至已连接时就会触发。 这构成了安全与隐私风险，因为它允许第三方软件在无沙盒、全系统及网络访问权限下安装，并持续到每次启动，可能演变为类似恶意软件的行为。 软件通过与显示器关联的设备元数据安装，绕过了微软的驱动程序包隔离策略（仅适用于已签名的驱动程序，而非捆绑的软件）。解决方法是通过组策略或设备安装设置禁用自动下载制造商应用。

hackernews · baranul · 7月18日 10:21 · [社区讨论](https://news.ycombinator.com/item?id=48956688)

**背景**: Windows Update 可自动安装推荐的驱动程序更新及与设备关联的软件。设备元数据允许硬件制造商捆绑软件，在设备（如显示器）连接时安装。微软在 Windows 10 版本 2004 中引入的驱动程序包隔离策略旨在防止此类行为，但仅涵盖已签名的驱动程序，而非捆绑的可执行文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://support.microsoft.com/en-US/Windows/Hardware/Drivers/automatically-get-recommended-and-updated-hardware-drivers">Automatically get recommended and updated hardware drivers</a></li>
<li><a href="https://asibiont.com/en/blog/monitory-lg-tayno-ustanavlivayut-po-cherez-windows-update-bez-vashego-soglasiya-chto-proiskhodit-i-kak-zashchititsya">LG Monitors Silently Install Software Through... — ASI Biont Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了警惕，指出该安装程序在启动时以完全权限运行，且问题适用于已有的 LG 显示器。一名用户提供了通过 gpedit.msc 或 sysdm.cpl 的有效解决方法。另一人批评 Windows 损坏的驱动同意模型，并提到联想触摸屏驱动存在类似问题。

**标签**: `#security`, `#windows`, `#privacy`, `#driver`, `#lg`

---

<a id="item-3"></a>
## [Claude Fable 5 永久纳入订阅套餐](https://simonwillison.net/2026/Jul/18/claude-make-fable-5-permanent/#atom-everything) ⭐️ 7.0/10

Anthropic 宣布自 2026 年 7 月 20 日起，Claude Fable 5 将永久纳入 Max 和 Team Premium 订阅套餐，并享有 50% 的使用额度。 这一逆转源于 GPT-5.6 Sol 和 Kimi 3 的竞争压力，确保订阅用户无需额外支付 API 费用即可继续使用 Anthropic 最强大的模型。 只有 Max（每月 100/200 美元）和 Team Premium 套餐包含 Fable 5；Pro 和 Team Standard 用户将获得一次性 100 美元额度并可通过积分使用该模型，而每月 20 美元的套餐仍无法访问。

rss · Simon Willison · 7月18日 06:00

**背景**: Claude Fable 5 是 Anthropic 于 2026 年 6 月 9 日推出的“Mythos 级”大型语言模型，旨在安全用于一般用途。Anthropic 最初因计算能力问题计划将 Fable 5 从订阅套餐中移除，仅通过 API 提供，但由于 OpenAI 的 GPT-5.6 Sol 和 Moonshot AI 的 Kimi 3 的竞争而改变了策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Fable_5">Claude Fable 5</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Claude`, `#Fable`, `#Anthropic`, `#GPT-5.6`

---