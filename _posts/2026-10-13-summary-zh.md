---
layout: default
title: "Horizon Summary: 2026-10-13 (ZH)"
date: 2026-10-13
lang: zh
---

> 从 13 条内容中筛选出 3 条重要资讯。

---

1. [用 C 语言构建现代 Web 应用，引发 Hacker News 热烈讨论](#item-1) ⭐️ 8.0/10
2. [网络攻击迫使欧洲超市冷柜进入除霜模式](#item-2) ⭐️ 8.0/10
3. [Python 3.15 发布，带来 PEP 810 显式惰性导入](#item-3) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [用 C 语言构建现代 Web 应用，引发 Hacker News 热烈讨论](https://prophitt.me/writing/a-modern-web-app-in-c) ⭐️ 8.0/10

prophitt.me 上的一篇文章完整演示了如何只用 C 语言构建一个现代 Web 应用，该文登上 Hacker News 首页，获得 431 分和 176 条评论。文章主张，一个运行在 Web 服务器背后的小型 C 程序，配合 pledge、chroot 等降权措施，完全足以支撑一个现代网站的部署。 这篇文章对“现代 Web 开发必须依赖重量级语言运行时、包管理器和层层框架”的主流假设提出了反例，说明基于 C 的极简技术栈依然切实可用。对于系统程序员、独立开发者，以及关心依赖膨胀、部署复杂度和攻击面的从业者来说，这一点都具有参考价值。 该方案沿用经典的 CGI 模型，即 Web 服务器为每个请求启动一个外部程序，并借助操作系统级的降权手段（OpenBSD 的 pledge、chroot、类 setuid 限制）来限制进程被攻破后的影响范围。评论者指出的一个重要权衡是：这种“每请求一进程”的方式以牺牲常驻应用服务器的效率为代价，换取简洁性和极小的攻击面；同时 busybox 本身就内置了 cgi-bin 支持，正好适配这种部署方式。

hackernews · prophittcorey · 10月12日 16:13 · [社区讨论](https://news.ycombinator.com/item?id=50058528)

**背景**: 通用网关接口（CGI）是 20 世纪 90 年代初制定的一套接口规范，允许 Web 服务器调用外部程序来处理 HTTP 或 HTTPS 请求：服务器把请求数据传给该程序，再把程序输出的 HTML 转发回浏览器。它是最早被广泛使用的网页交互方案，但由于每来一个请求就要新建一个进程，后来才出现了 FastCGI 和常驻式应用服务器等替代方案来规避这一开销。用 C 写 Web 应用意味着要直接面对这种底层模型，因为 C 语言本身并不提供任何内置的 HTTP 或 Web 框架支持。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Common_Gateway_Interface_%28CGI%29">Common Gateway Interface (CGI)</a></li>

</ul>
</details>

**社区讨论**: 整体氛围积极且带有怀旧色彩：有评论者称这种方案“出乎意料地令人满足”，并认为文中关于降权的建议非常严谨。一位开发者分享了自己 22 年来用 C + FastCGI 为餐饮场所搭建网站的经历，表示系统运行得极好，以至于有连锁品牌直接买下了软件；也有人补充了替代方案，例如 busybox 内置的 cgi-bin 支持，或用 CGO\_ENABLED=0 编译的单个 Go 二进制文件；还有评论者坦言自己喜爱 C，但不喜欢用 C 进行并发编程。

**标签**: `#C`, `#web development`, `#CGI`, `#systems programming`, `#Hacker News`

---

<a id="item-2"></a>
## [网络攻击迫使欧洲超市冷柜进入除霜模式](https://www.tomshardware.com/tech-industry/cyber-security/unprecedented-cyberattack-cripples-supermarket-fridges-across-europe-as-hackers-activate-automatic-defrosting-delivery-and-store-prices-also-impacted-by-incident) ⭐️ 8.0/10

一场网络攻击利用联网的老旧制冷控制器，迫使欧洲各地超市冷柜进入自动除霜模式；据路透社和《世界报》2026 年 10 月 12 日的报道，法国连锁超市 Intermarché表示旗下约 150 家门店受到影响。该事件不仅让冷藏柜温度升高（有报道称温度达到 50°C），还扰乱了门店的配送排期与定价系统。 这是一起现实世界中针对普通零售基础设施的 OT/IoT 安全事件，而非实验室演示，说明那些毫无安全余量的几十年前嵌入式控制器可以被武器化，从而造成大规模物理层面的 disruption。它暴露出一个系统性盲点：节能与远程诊断功能把冷柜这类普通家电推上互联网，从而扩大了食品供应这一关键业务环节的攻击面。 被劫持的设备大多是已有 15 至 20 年历史的 Danfoss 控制器，例如 SM800（2021 年停止支持）和 SC355（2016 年停止支持），它们运行的是过时固件；Claroty 的 Team82 团队于 2026 年 8 月发布研究后，Danfoss 发布了修复这些漏洞的固件版本 R4.3.1。即便补丁已经存在，现场庞大的老旧控制器存量也意味着修复进程缓慢且不均衡，而且攻击的归因至今仍有争议。

hackernews · Zeekaas · 10月12日 12:16 · [社区讨论](https://news.ycombinator.com/item?id=50055304)

**背景**: OT（运营技术）与 IoT 设备是监控和控制工厂、楼宇和门店中物理设备的嵌入式计算机，它们往往运行 15 至 20 年，几乎不经过安全审查，也缺乏更换预算。超市越来越多地把制冷控制器接入互联网，以便技术人员远程诊断故障、启动除霜循环，并让连锁总部比较数百家门店的能效——但这种便利也让它们暴露在攻击者可触及的网络中。与被窃取的数据库不同，被黑的冷柜会造成实实在在的食物损耗、配送中断和门店定价失真。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claroty.com/team82/research/freeze-the-controller-defrost-the-food-uncovering-vulnerabilities-in-danfoss-refrigeration-controllers">Freeze the Controller, Defrost the Food: Uncovering ...</a></li>
<li><a href="https://www.msn.com/en-us/technology/cybersecurity/danfoss-says-hacked-controllers-behind-50c-french-supermarket-fridges-ran-old-firmware/ar-AA2e6nkW">Danfoss says hacked controllers behind 50C French ... - MSN</a></li>
<li><a href="https://www.thestack.technology/french-supermarkets-hacked-danfoss-vulnerabilities-blamed/">French supermarkets hacked: Danfoss vulnerabilities blamed</a></li>

</ul>
</details>

**社区讨论**: 这场约 690 条评论的讨论较少聚焦硬件漏洞本身，更多指向系统性问题：有评论者指出 Danfoss SM800/SC355 等已停止支持的老旧控制器，认为倒班一线的员工根本“没有余量”去做安全审查或按期更换硬件；也有人提到厂商日益强制要求联网和付费订阅（一位评论者举例说医院的部分检验设备没有订阅就无法使用）。还有几位评论者争论此次攻击是否与 2026 年 8 月美国军队小卖部冷柜据称被黑的事件有关，追问是同一团伙还是模仿者所为。

**标签**: `#cybersecurity`, `#IoT`, `#OT-security`, `#critical-infrastructure`, `#Danfoss`

---

<a id="item-3"></a>
## [Python 3.15 发布，带来 PEP 810 显式惰性导入](https://simonwillison.net/2026/Oct/12/python-3-15/) ⭐️ 8.0/10

Python 3.15 已正式发布，官方“What&\#x27;s New”指南由 3.14/3.15 发布经理 Hugo van Kemenade 编纂；Simon Willison 最看重的是 PEP 810 显式惰性导入（写法为 \`lazy import json\` 或 \`lazy from pathlib import Path\`）。他还提到 PEP 798 推导式中的解包语法，例如 \`\[\*sublist for sublist in lists\]\`，并说明自己的开源项目现在可以告别 Python 3.10、开始使用 Python 3.11 的特性。 惰性导入直击命令行工具和插件生态长期存在的痛点：仅仅安装一个依赖 sentence\_transformers 这类重库的插件，就可能让每次运行命令多出数秒启动时间。由于 PEP 810 采用显式、可选启用的语法且不会级联影响依赖模块，它规避了此前隐式方案 PEP 690 被 Python 指导委员会否决时所指出的不可预测性，因此更有可能被广泛采纳。 在 PEP 810 中，只有被标记为 \`lazy\` 的那条导入语句会被推迟——该模块会在相关符号第一次被使用时才真正导入，而且这种惰性不会传播到该模块自身的导入语句上。由 Adam Hartz 和 Erik Demaine 提出的 PEP 798 推导式解包，是对 Python 3.5 中落地、源自 PEP 448 的解包泛化能力的扩展，使 \`\[\*sublist for sublist in lists\]\`、\`\{\*s for s in sets\}\` 和 \`\{\*\*d for d in dicts\}\` 可以替代等价的嵌套推导式写法。

rss · Simon Willison · 10月12日 18:15

**背景**: Python 每年 10 月发布一个新的小版本，而每个发布周期也会同时淘汰最旧的支持分支——因此 Python 3.10 生命周期结束，意味着那些需要兼容“所有受支持 Python 版本”的维护者终于可以放弃它，转而使用 3.11 引入的语法。在 Python 中，\`import\` 语句会立即执行被导入模块的顶层代码，因此提前导入重型库是导致应用和命令行工具启动缓慢的常见原因。惰性导入此前曾在 2022 年以 PEP 690 的形式提出，但那一版让惰性变为隐式且全局生效，最终被指导委员会以复杂和不可预测为由否决；PEP 810 则让每一条惰性导入都显式书写、作用域局部化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://peps.python.org/pep-0810/">PEP 810 – Explicit lazy imports | peps. python .org</a></li>
<li><a href="https://socket.dev/blog/pep-810-proposes-explicit-lazy-imports-for-python-3-15">PEP 810 Proposes Explicit Lazy Imports for Python 3.15 - Soc...</a></li>
<li><a href="https://blog.jetbrains.com/pycharm/2026/06/explicit-lazy-imports-are-coming-to-python-3-15/">Explicit Lazy Imports Are Coming to Python 3.15 - The JetBrains Blog</a></li>

</ul>
</details>

**标签**: `#Python`, `#Python 3.15`, `#PEP 810`, `#lazy imports`, `#programming languages`

---