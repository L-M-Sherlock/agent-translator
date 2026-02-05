# 如何使用 5ch

[How to use 5ch](https://learnjapanese.moe/2ch/)

![Image](https://learnjapanese.moe/img/2ch00.png)

**2025 年更新：我建议你去看看[エッヂ](https://learnjapanese.moe/2ch/#new)**

2channel（日语：２ちゃんねる）（新名称：５ちゃんねる）是一个日本匿名的**文字**论坛。你可以把它理解为介于 Reddit 和 4chan 之间的「日本版」，用户群比 Reddit 更毒、版面管理程度也参差不齐。你可以用它来打发时间，而不是去刷英文网站。以今天的标准来看，这个网站的设计非常可疑；在本文里我会不断称它为「很糟糕」。糟糕的设计再加上极差的用户友好性，让它变得非常**难用**——尤其对仍在学习日语的人来说。本文会尝试解释如何在浏览器里使用 5ch。

## 这网站到底叫啥？

它以前广泛被称作「にちゃんねる」。后来因为[一些原因](https://www.wdic.org/w/WDIC/2%E3%81%A1%E3%82%83%E3%82%93%E3%81%AD%E3%82%8B%E4%B9%97%E3%81%A3%E5%8F%96%E3%82%8A%E4%BA%8B%E4%BB%B6)，网站改名为 5channel（ごちゃんねる）。很多用户至今仍用旧名称呼它，但为了减少混乱，我在本文里统一叫它 5ch。不过还有一个不同的网站叫 Futaba Channel，被称为 2**chan**，它和 2channel/5channel 没关系。很混乱。

## URL

<https://5ch.net/>

## 首页

![Image](https://learnjapanese.moe/img/2ch01.png)

你说「哪儿糟糕了」？首先，那张截图其实是开着广告拦截器截的；不开广告拦截器的话广告多到让人很难愉快使用。  
其次，这网站的设计其实非常**不一致**：不同页面长得不一样。只有首页看起来还行，笑。

我推荐用 uBlock Origin 作为广告拦截器（[Chrome](https://chromewebstore.google.com/detail/ublock-origin/cjpalhdlnbpafiamejdnhcphjbkeiagm) \| [Firefox](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)）。这是唯一一个真正好用的广告拦截器。

首页会展示[ニュース速報+](https://asahi.5ch.net/newsplus/index.html)（新闻板）和[野球実況板](https://tanuki.5ch.net/livebase/index.html)（一个[実況](https://learnjapanese.moe/2ch/#_7)棒球板）的热门帖子。

虽然首页内容挺无聊，但实际上 5ch 有大量不同兴趣的板块。你可以点击左上角的[掲示板](https://www2.5ch.net/5ch.html)按钮查看板块列表。

## 板块（Boards）

![Image](https://learnjapanese.moe/img/2ch02.png)

板块非常多；与其说像 4chan 的 board，更像 Reddit 的 subreddit。

5ch 对板块做了非常细的分类，这意味着你基本只会读到你感兴趣的东西；但这也会导致很多板块变成死板，因为分类有时细得过头。

你可以试着用 `Ctrl`+`F` 找找和你兴趣相关的东西。也可以在搜索栏输入关键词（当然要用日语！），肯定能搜到相关帖子；你也能通过帖子反推自己应该去哪个板块。

有一个页面会把所有板块的链接都放在同一页里：[掲示板リスト](https://menu.5ch.net/bbstable.html)。

我个人经常看的板块是[ラブライブ！](https://fate.5ch.net/lovelive/)和[声優](https://kizuna.5ch.net/voiceactor/)。

## 板块页面（Board Page）

![Image](https://learnjapanese.moe/img/2ch03.png)

板块页面的第一个框里包含规则和板块信息。

![Image](https://learnjapanese.moe/img/2ch04.png)

下一个框里是帖子列表。你会通过这里找帖子。帖子名后面括号里的数字表示这个帖子有多少条回复（responses）。

继续往下滚，你会看到最近被顶起来的帖子预览：它会显示首帖（OP）和最后 50 条回复。  
「レス」表示帖子里有多少条回复；「CP」（click point？）表示帖子当前的人气，数字越大越热门。（最近被顶帖的预览视图）你需要点「全部読む」才能看完整帖子。

![Image](https://learnjapanese.moe/img/2ch05.png)

你从帖子列表点进一个帖子时，5ch 默认只显示首帖和最新 50 条回复。你需要点击「全部」，或者从 URL 里删掉 `/l50` 才能看到完整帖子。

![Image](https://learnjapanese.moe/img/2ch06.png)

## 纯帖子列表页（Thread List Dedicated Page）

每个板块都有一个专门的页面，只显示所有帖子的列表，不带其他杂七杂八的东西。你可以点击帖子列表顶部的**スレッド全一覧はこちら**进入，或者把 URL 改成以 `subback.html` 结尾。

![Image](https://learnjapanese.moe/img/2ch07.png)

默认视图不太好用，但你可以点**表示スタイル切替**切换到你喜欢的视图。

## Imgur 链接

你可能会注意到很多人发 Imgur 链接。这是因为 5ch 是一个**文字**论坛，不支持上传图片；想分享图片只能用外部图床。

有些浏览器扩展能改善 5ch 体验，比如把图片和推文直接内嵌显示。我个人用的是 [5chutil](https://learnjapanese.moe/2ch/#improve-the-web-browser-2ch-experience-5chutil)。

2023 年 12 月更新：Imgur 开始删除包含 18+ 内容的图片以及未注册用户的图片，因此有些 5ch 用户转去用 xxup.org 和 catbox.moe 作为图床。

## 回复（Responses）

回复的运作方式和 4chan 那种回帖几乎一样：最旧的回复在最上面，最新的在最下面。

不过 4chan 的回帖编号是按整个板块的所有帖子一起累计的（所以编号会非常大）；而 5ch 的回复编号只在同一个帖子里累计。  
在 5ch 上，回复别人通常是用 `>>` 引用楼层号：例如回复 1 楼就是 `>>1`，回复 19 楼就是 `>>19`。

在 5ch 上，帖子到 1000 回复会自动 DAT落ち。你可以在過去ログ里查看这些归档帖；归档帖无法回复。

## 過去ログ

5ch 的過去ログ是 DAT落ち 的帖子去的地方。你可以点击帖子列表顶部的**過去ログ一覧はこちら**按钮进入過去ログ。

![Image](https://learnjapanese.moe/img/2ch08.png)

你也可以访问[過去ログ网页](https://kakolog.jp/)来搜索那些归档得还太新、没被 Google 收录的旧帖。

重要更新（2023 年 10 月）：在一段时间的 DDoS 攻击之后，過去ログ 的帖子因为 522 错误而无法查看。

2023 年 12 月更新：很多帖子仍然无法查看。已经 2 个月没修了，也不知道是什么原因。

## 发帖（Posting）

## 新功能：DONGURI 系统

作为防喷子与防刷屏措施，用户需要「种下一颗橡子」并等待一段时间后才能发帖。

方法是：在「名前」字段里输入 `!donguri`，然后在任意帖子里随便发点东西。你在每一台不同的设备／浏览器／App 上使用 5ch，都需要重复做一次。  
![Image](https://learnjapanese.moe/img/2ch15.png)

之后你应该会看到一条报错信息，告诉你橡子（donguri）已经种下了。过几分钟你就能发帖。

![Image](https://learnjapanese.moe/img/2ch14.png)

你可以把页面滚到帖子最底部，在文本框里输入内容来发帖。

![Image](https://learnjapanese.moe/img/2ch11.png)

发帖时要确保内容不违法，也不要给别人添麻烦。你在 5ch 上 trolling 很容易被封号；而解封或绕封会非常难看！

发帖时最好的习惯是使用 [sage](https://learnjapanese.moe/2ch/#sage)！

你也可以通过进入板块页面并滚到底部（写着「新規スレッド作成」）来发新帖。

![Image](https://learnjapanese.moe/img/2ch12.png)

## 发帖文化（Posting Culture）

因为是匿名发帖，氛围**可能**会变得有毒；有人会互相骂。我觉得这和 4chan 比不算什么。不过这也很取决于你在什么板块发帖。[アニメ](https://pug.5ch.net/anime/)这类板块管理不错，基本不怎么毒；相反，[ニュー速(嫌儲)](https://greta.5ch.net/poverty/)这种 sh\*thole 基本永远是日本互联网的阴暗面。

你发的低质量帖子和你开的低质量楼可能会招来负面回应，而且到处都会有喷子贬低你喜欢的东西。重要的是不要把这些负面回应往心里去，并学会放下。

## 如何在日本国外发帖

![Image](https://learnjapanese.moe/img/2ch10.png)

非日本 IP 不能在 5ch 发帖。

5ch 对哪些 IP 能发帖非常严格 ~~（99% 的板块不行，但大使館和 Anarchy 板可以自由发帖）。~~

2023 年 10 月更新：没有 5ch premium 的情况下，你已经不能用海外 IP 在 5ch 的任何板发帖。

你在日本国外正常浏览 5ch 没问题，但发帖只能用「被批准的」日本 ISP 和手机运营商。这意味着普通 VPN 不行，因为不仅 IP 要对，ISP 也必须被批准。

不过仍然有办法绕过发帖限制，但会比较麻烦。

### 方法 1：住宅 IP VPN（Residential IP address VPN）

这是我唯一成功在 5ch 发过帖的方法。但要搞到这种 VPN 可能很难；而且取决于你用的服务，你会不断「抽卡」，看哪些 IP 还没被别人拿去 5ch 用过、也还没被封。和 5ch 管理员基本就是猫鼠游戏。

#### Tuxler

Tuxler 是一种 VPN 服务，可以让你使用住宅 IP。搞懂怎么用之后效果挺好。  
我建议你下 Windows 客户端，不要用 Chrome 扩展。  
[Tuxler Windows App](https://www.tuxlervpn.com/download-windows/)。

我尝试在 Residential 模式下直接连日本节点时，发现不行。但后来我发现软件有 bug，可以用一个变通方法。  
你需要先连 Datacenter 节点，再连 Residential 节点。（可以叠加连接。）

步骤如下：  
1. 先连接到离你最近的 Datacenter 节点（我在英国，所以对我来说是法国）。  
2. 然后切到 Residential 标签页，选择 Japan。  
3. 当底部旗帜变成日本时，说明成功了。  
4. 访问 ipleak.net 看看你的 ISP 显示成什么，应该会像 KDDI、NTT、au、SoftBank、Docomo 之类。  
5. 达到每日限额后，先连到另一个住宅 VPN，再连回来（它会记住你的原始 IP）。

**警告：Tuxler 也会让其他人把你的 IP 当作住宅 VPN 来用。用完之后一定要把 App 完全退出（任务栏图标和任务管理器里都彻底没有）！**

#### 筑波vpn

也叫 SoftEther 或 VPN Gate。出于对贡献者的礼貌，我不展开细说，但这也是一个选项。

#### 专用住宅代理（Dedicated Residential Proxy）

这个选项很贵。有些面向爬虫的代理商会提供难以检测的住宅代理；其中不少也有日本地区的住宅代理。在日本国外发帖最安全、最可靠的方法就是这个，但成本会很高。注意别买「ISP Proxy」！那只是带了假 ISP 的机房 IP。你需要的是**住宅**或**移动**代理。

### 方法 2：购买 ＵＰＬＩＦＴ

2023 年 11 月更新：5ch ＵＰＬＩＦＴ（旧称 浪人）类似 5ch Premium：你会获得更多权益，比如更强的刷屏能力，并且可以在日本国外、甚至用 VPN 发帖。以前它只支持日本信用卡／借记卡，但他们把支付处理器换成 Stripe 之后，没有日本卡的人也能买了。最低是 1 个月 4 美元。  
不过购买前一定要关掉「自動更新」！看起来除了给他们发邮件之外，没有别的办法能让他们删除你的支付信息，所以别勾那个选项。

**这是迄今为止在日本国外发帖的最佳方式！！**

![Image](https://learnjapanese.moe/img/2ch13.png)

购买后，你会收到一封包含登录信息的邮件，大概长这样。

如果不小心打开了自動更新，可以用下面这封邮件模板请求他们删除支付信息：

Subject: 自動更新の解除とお支払い方法の削除についてのお願い

おはようございます。

この度は、購入手続き中に「自動更新」を誤って有効にしてしまったため、その解除をお願いしたくメールを差し上げました。5ch UPLIFTサービスは引き続き利用させていただく予定ですので、自動更新機能のみを停止していただけますと助かります。

また、可能であれば、私の登録されているお支払い方法も削除していただけないでしょうか。

購入確認のメールは、以下の通りです。

\[Insert purchase confirmation email you received\]

お手数をおかけして申し訳ありませんが、ご対応いただけますと幸いです。 どうぞよろしくお願いいたします。

## 专用浏览器（5ch dedicated browsers）

一般不推荐用网页浏览器访问 5ch。因为 5ch 的工作方式是：你（客户端）请求帖子的数据（.dat），服务器再为你生成 HTML 页面。这会给服务器带来额外负载。因此推荐使用 5ch 专用浏览器，因为它们能更「原生」地展示帖子 .dat。

有些板块甚至有发帖限制：你只能通过专用浏览器发帖。

对日语学习者来说，这种方式最大的缺点是：你没法在里面用 Yomichan。

推荐的 5ch 専用ブラウザ：  
Windows: [Siki](https://sikiapp.net/)  
Android: [Chmate](https://play.google.com/store/apps/details?id=jp.co.airfront.android.a2chMate&hl=ja)  
iOS: [Thread Master](https://apps.apple.com/jp/app/threadmaster/id6455370741)

## 改善网页版 5ch 体验：5chutil

你可以用 5chutil 扩展来改善网页版 5ch 体验。  
[Chrome（load unzipped）](https://drive.proton.me/urls/JJNBJQYXFG#Rxrr6Flaic6V)  
[Firefox](https://addons.mozilla.org/ja/firefox/addon/5chutil/)

它包含很多实用的体验改进，例如：  
- 改善帖子列表视图：支持按名称、回复数（レス）、CP（勢い）（click point）和日期排序。  
- 内嵌显示 Imgur 与 Twitter  
- 把同一用户的回复汇总成列表：把鼠标悬停在用户名旁边的数字上即可。  
- 把跨多个回复的引用汇总成列表：把鼠标悬停在 `>>` 上即可。  
- 选中文字并点击按钮即可添加「NG Words」，过滤你不想看的内容。  
- 点击用户 ID 旁边的 + 即可隐藏你不喜欢的人的回复。

## 推荐的 5ch 搜索方式

~~如果你想搜索活跃帖与归档帖，甚至搜索帖子内容，我推荐用 Google，并用搜索词 `site:5ch.net <keyword>`。~~ 这在 2024 年很烂。现在最好的方式是用 [find.2ch.sc](https://find.2ch.sc/)。2ch.sc 是 5ch.net 的镜像站，属于 2channel 的「正统」站主 Hiroyuki Nishimura。这里带有 @net 的帖子与回复是从 5ch.net 镜像过来的，你也能很容易在 5ch.net 上找到对应帖子。

这个站的搜索栏也还行，用来搜活跃帖标题足够了。

## 说到底用 5ch 没意义？？／まとめサイト 介绍

5ch 有很多有趣的帖子，但也有大量帖子是クソスレ（垃圾帖），帖子里的回复也可能是クソレス（垃圾回复）。而且在 5ch 上找东西也挺难。

这就是まとめサイト登场的地方。这类网站会把有趣的帖子，以及帖子里有趣的回复摘出来，放到第三方网站上。它们通常也会专注于某一个主题。例如，有个 [Love Live! 的 5ch まとめ站](http://lovelivematocha.com/)，专门搬运ラブライブ！板的帖子。[ピコピコ通信](https://stkn-games.net/)是一个搬运游戏相关 5ch 板帖子的まとめ站。[アルファルファモザイク](https://alfalfalfa.com/)则更像是综合性的まとめ站。

在我看来，まとめサイト才是日本版的「刷 Reddit」替代品。你光刷まとめサイト就能娱乐好几个小时。  
几乎每个爱好／兴趣都有对应的まとめサイト，你直接 Google 搜就行。你可以在这里看到一个まとめ站推荐列表：  
[【完全版】おすすめまとめサイト30選！2chなどジャンル別に調査！](https://monamona2525.com/archives/59506)

## 5ch 著名粪坑板

    - なんでも実況J  
    - なんでも実況G  
    - ニュー速VIP  
    - ニュー速(嫌儲)   
    - 東アジアニュース+
    - なんでもあり   
    - 難民  
    - ハード・業界

ニュー速 和 なんでもあり 的 NSFW（BBSPINK）版本只能用日本 IP 访问；BBSPINK 的大部分内容也只能用日本 IP 访问。

## NEW: エッヂ

**2025：**由于 5ch 站主的极端无能，这个站被脚本刷屏与 DDoS 攻击盯上已经有一段时间了，导致很多人无法使用。像 4chan 这类网站很容易通过引入 CAPTCHA 和使用 Cloudflare 解决这个问题，但不知为何 5ch 的站主做不到。截至 2025 年，几乎没人再用 5ch 的 なんでも実況J 和 なんでも実況G 了；用户转移到了一个叫「エッヂ」的网站。现在「なんJ」指的是エッヂ上的板，而不是 5ch 上的那个。

URL: <https://bbs.eddibb.cc/liveedge/>

它的文化氛围基本和 5ch 的 なんでも実況J 一样，所以如果你熟悉 5ch，用法也差不多。因此本指南里写的东西大概有 90% 仍然适用。

### 在 エッヂ 发帖

你在日本国外也能比较容易地在 エッヂ 发帖。你只需要一个日本 IP（VPN 可以）。

要发帖，先点进一个帖子，然后点顶部的「書き込み」。接着在「本文」字段里输入你想发的内容，并点「書き込む」。系统会在弹窗里显示一段代码；复制这段代码。  
![edge](https://learnjapanese.moe/img/edge01.png)  
点击「はい」，进入[授权页面](https://bbs.eddibb.cc/auth-code)。在这里你需要通过 CAPTCHA，并把刚才的代码粘贴进去。  
![edge](https://learnjapanese.moe/img/edge02.png)  
验证通过后，你会得到一个授权 token，把它粘贴到 mail 字段里即可。![edge](https://learnjapanese.moe/img/edge03.png) 然后就完成了，你的发帖就能通过！

## Talk.jp

![Image](https://learnjapanese.moe/img/2ch09.png)

URL: <https://talk.jp/>

Talk.jp 是 5ch 的一个衍生站，最近因为 5ch 的烂站主与最流行的 5ch 专用浏览器 Jane Style 的开发者发生矛盾而出现。作为回应，Jane Style 的开发者创建了 Talk.jp，并在 Jane Style 里移除了 5ch 支持，把它变成 Talk.jp 专用浏览器。Jane Style 曾经是很流行的 5ch 专用浏览器，这意味着：下载了更新的人将不再浏览 5ch，而是浏览 Talk.jp。不过话虽如此，这其实也没从 5ch「偷走」太多流量。

Talk.jp 拥有 5ch 最热门的一些板块，并且网页设计更容易用。

## 术语

### スレ

Thread（帖子／串）。

### レス

Response（回复）。

### 板

Board（板块）。

### sage

通常你在 5ch 发帖后，会把帖子顶到板块顶部。你可以在发帖时把 `sage` 填进 Email 字段来阻止顶帖。大约 20 年前不使用 sage 会被看不起，而这种 sage 文化基本保留了下来。使用 `sage` 发帖的用户，名字会显示成紫色。

### 自治

基本就是 5ch 的版务／管理。管理得好的板块会有「自治スレ」，你可以在里面向版务抱怨被管理。

### 実況

5ch 里的「実況」指的是在某个事件正在发生时实时讨论它。这经常被 5ch 用户反感，因此大多数板块默认不允许「実況」。允许実況的板块，通常名字里会有 実況，或规则里写着 実況OK／実況可。

### DAT落ち

帖子被归档，导致你无法再回复。DAT落ち 可能发生在：板块里新帖数量超过板块容量，或者帖子达到 1000 回复时。5ch 帖子的原始数据存储在 .dat 文件里，所以 dat 会「掉落」。

### VIP

最初在 20 年前，它指的是会得到特殊待遇的板块；但现在它某种程度上带有「收容所」的意味，因为名字里带 VIP 的板块因帖子内容而臭名昭著。例子包括[ニュー速VIP](https://mi.5ch.net/news4vip/)。

### コテハン

5ch 通常是匿名的，但你也可以带名字发帖，这叫 コテハン。

### トリップ/酉/鳥

这类似于[コテハン](https://learnjapanese.moe/2ch/#_8)，但「トリップ」是通过一个只有你知道的特殊字符串生成的：它会变成另一段字符串，作为你的トリップ。你想让别人能特别识别你时，可能会用トリップ。你可以这样生成：`<name> #<random string>`

### 垢版

垢BAN／アカウントBAN 的另一种写法。名字看起来像是在封号，但其实只是指向 donguri 页面链接。

### 大砲

当你有 UPLIFT 时，你可以在站内成为「Hunter」。你可以对你怀疑是 troll 的人发射「橡子炮」（どんぐりキャノン），把对方的 donguri 等级重置为 0。

### !extend:checked:vvvvv:1000:512

这是一个你可以写在 5ch 帖子首帖（OP）里的命令，用来强制开启[コテハン](https://learnjapanese.moe/2ch/#_8)模式。这是一种防 troll 的措施，因为它能让每个成员以「[ﾜｯﾁｮｲ](https://learnjapanese.moe/2ch/#_10)」加一段特殊代码的形式被识别。管理良好的板块往往要求所有帖子都必须启用它。你也经常会在多 part 的连载帖里看到 OP 模板包含它。5ch 的 ID 会在日期变化或换 IP 时重置，所以仅靠 ID 不够。人们会发多行 `!extend:checked:vvvvv:1000:512` 来提醒别人：当帖子 dat 落ち、需要新开 OP 时别忘了带上它。  
更严格的版本会用更多 v 来显示每个发帖者的 IP（`!extend:checked:vvvvvv:1000:512`），但比较少见。

### 狼

モーニング娘 板。

### ﾜｯﾁｮｲ

当帖子 OP 里包含 `!extend:checked:vvvvv:1000:512` 时，你发帖后会在名字旁显示的内容（带特殊代码）。

### ROMる

（Read Only Memory）潜水／围观。你会做的就是这个。

### AA

ASCII art，也包括 Shift-JIS art。

### イッチ

发 OP 的人。来自「>\>1」。

### 人大杉

这是一个有时会出现的报错信息：当你尝试在 [5ch/2ch過去ログ](https://kakolog.jp/) 里查看内容时可能会看到。它是「人多過ぎ」的一个誤字版本。当把 .dat 转成 HTML 的過去ログ 服务器过载时，就会出现它。

### アフィ / アフィカス

アフィ 指的是 affiliate 类型的まとめ站：它们把 5ch 的過去ログ帖子搬到まとめ站上。这些站满屏广告、靠刷点击赚钱，也就意味着它们在从 5ch 的帖子里赚钱。5ch 用户非常厌恶这种行为；以至于 5ch 站主把站内所有帖子都做了版权声明，使得把帖子搬到其他站变成违法。即便如此，まとめ站依然存在，而且不会消失。カス 是日语里类似「渣滓」的词。
