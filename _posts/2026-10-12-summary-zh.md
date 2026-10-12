---
layout: default
title: "Horizon Summary: 2026-10-12 (ZH)"
date: 2026-10-12
lang: zh
---

> 从 10 条内容中筛选出 2 条重要资讯。

---

1. [陶哲轩《数学 2.0》幻灯片：AI 正在重塑数学](#item-1) ⭐️ 8.0/10
2. [批评文章称 Passkey 是陷阱，引发热议](#item-2) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [陶哲轩《数学 2.0》幻灯片：AI 正在重塑数学](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf) ⭐️ 8.0/10

陶哲轩（Terence Tao）公开了他在加州理工学院演讲《数学 2.0》的幻灯片，其中梳理了数学的“数学 1.0”历史状态，以及当下向 AI 驱动时代过渡的现状。这份幻灯片出现在 2026 年 10 月一波由 AI 大规模产出的数学成果之后，并在 Hacker News 上引发了长达 375 条评论的实质性讨论（324 分）。 陶哲轩是当今最具影响力的数学家之一，因此他把 AI 视为数学研究方式发生结构性变革的判断，对学界、期刊与资助机构的应对方向具有非同寻常的分量。这场讨论还延伸到更广泛的问题——从科研经费与成果署名，到在数学乃至医学中，AI 产生的结果是否必须先被理解其机制才能被信任。 这份材料是会议幻灯片，而非经过同行评审的突破性论文，不少读者也把这一点视为其局限。陶哲轩使用了“未解难题是灯塔，而不是终点”这类形象说法，并认为当前的数学 AI 还不是一个“好公民”，因为它并不追求为既有理论体系做出最优雅、最融贯的补充。

hackernews · Anon84 · 10月11日 13:16 · [社区讨论](https://news.ycombinator.com/item?id=50043026)

**背景**: 陶哲轩是菲尔兹奖得主、加州大学洛杉矶分校数学家，研究横跨数论、分析与组合数学，近年来也成为观察 AI 如何进入科研实践的重要评论者。“数学 1.0”指的是延续数百年的模式：由人类数学家提出问题、构建理论并主要靠人工完成证明；“数学 2.0”则描述一种新情境——AI 系统能够大规模生成猜想、证明与解答，迫使学界在验证、署名和人才培养等方面调整规范。该演讲还根据近期事件（包括 2026 年 10 月一批大规模 AI 生成的数学成果）作了修订。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://terrytao.wordpress.com/2026/10/10/math-2-0/">Math 2 . 0 | What&#x27;s new</a></li>
<li><a href="https://en.wikipedia.org/wiki/Terence_Tao">Terence Tao - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 讨论情绪投入但意见分裂：从事药物发现 AI 研究的 dekhn 认为，陶哲轩关于癌症医学的那张幻灯片了解不足，并指出医学界本就常用机制尚未被完全弄清的药物；另一位评论者以麻醉作类比——其作用机制至今未完全明确，但手术中依然照用。也有人更认同陶哲轩的框架：thomasahle 用软件术语重新表述了他的观点，称数学是一套由理论与证明组成的“代码库”，而当前 AI 并不擅长优雅地维护它；samuelknight 则描述了那些多年难题被 AI 解出的研究者，他们不得不重写经费申请，并像失去一位老朋友一样哀悼整个领域。

**标签**: `#AI`, `#mathematics`, `#research`, `#machine-learning`, `#academia`

---

<a id="item-2"></a>
## [批评文章称 Passkey 是陷阱，引发热议](https://nonfunctional.substack.com/p/passkeys-are-a-trap-do-not-use-them) ⭐️ 8.0/10

一篇题为《Passkeys are a trap》的 Substack 文章提出，尽管 Passkey 被宣传为更安全，但它实际上带来了实用性缺陷和厂商锁定问题；该文在 Hacker News 上获得约 296 个赞成票和 168 条评论，讨论热烈。文章最后的补记也承认，Passkey 具有域名绑定特性，因此能够抵御中间人攻击，而评论者指出这一点恰恰削弱了文章自身的论点。 Apple、Google、微软以及各大平台正把 Passkey 作为密码的替代方案大力推广，因此一篇论据充分的反对文章对所有正在考虑如何在线认证的人都很有参考价值。这场争论凸显了内嵌于设备生态的安全机制与用户对可移植性、备份和凭据强度的控制权之间的张力。 评论者指出，远程证明（attestation）只能在凭据注册时请求，登录时无法追溯要求，而且网站在请求 attestation 时浏览器会弹出权限提示，因此关于“基于 attestation 的锁定”的说法可能被夸大了。另一些人则强调，Passkey 通常通过平台的云端钥匙串同步，这正是它方便的原因，但也使其绑定在单一厂商的生态之中。

hackernews · laurex · 10月11日 21:59 · [社区讨论](https://news.ycombinator.com/item?id=50048312)

**背景**: Passkey 是 FIDO2/WebAuthn 凭据的一种面向消费者的实现，它使用公钥—私钥对取代共享密码：私钥保存在你的设备或同步的钥匙串中，服务器只能看到公钥。它的设计目标是抗钓鱼攻击，并在浏览器和平台之间实现标准化，其中 WebAuthn 规定网站与认证器如何通信，CTAP 则负责与认证器本身通信。远程证明（remote attestation）是一项可选功能，让服务器能够验证所用认证器的品牌和型号，这有助于防范伪造或诈骗者提供的认证器，但也可以被用来限制允许使用的设备。域名绑定凭据与特定网站的源绑定，这正是它能够阻止中间人钓鱼页面复用凭据的原因。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.passkeys.com/what-are-passkeys">What Are Passkeys ? What Is a Passkey ? Passkey Authentication...</a></li>
<li><a href="https://developers.google.com/identity/passkeys">Passkeys | Google for Developers</a></li>

</ul>
</details>

**社区讨论**: 讨论整体对文章结论持怀疑态度：有评论者指出，attestation 只能在注册阶段获取且需要浏览器权限提示，因此所谓 Netflix 或 Twitter 强制使用 attestation 的说法并不可信。也有人为 Passkey 的实用价值辩护，一位评论者指出域名绑定使其能抵御中间人攻击，另一位则批评作者在长篇批判之后才在最后的脚注中承认这一点。还有一部分用户表示自己不主动启用 Passkey，因为他们看重可移植性、能够安全备份和存放凭据的能力，以及自行控制凭据强度，而不是依赖手机指纹。

**标签**: `#passkeys`, `#authentication`, `#security`, `#web standards`, `#privacy`

---