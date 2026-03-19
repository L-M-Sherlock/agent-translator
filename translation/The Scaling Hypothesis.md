# 缩放假说

[The Scaling Hypothesis](https://gwern.net/scaling-hypothesis)

> 2020 年 5 月由 OpenAI 发布的 GPT-3，是迄今训练过的最大神经网络，规模超过此前记录一个数量级。
> 它以互联网文本数据进行训练，是 GPT-2 的后继者；GPT-2 曾以其自然语言理解与生成能力震惊所有人。
> 令大多数人（包括我自己）惊讶的是，这种规模的巨大提升并没有像许多人预期的那样遭遇收益递减甚至负收益；相反，OpenAI 预测的规模收益仍在持续兑现。
> 这些收益不只是比 GPT-2 学到了更多事实与文本，而是更具质变意味、也更令人惊讶地展现出[**元学习**](#meta-learning)：GPT-2 学会的是如何完成文本摘要之类常见自然语言任务，而 GPT-3 则学会了如何遵循指令，并从少量示例中学习新任务。
> （因此，GPT-3 的输出与交互都比 GPT-2 更迷人，也更像人类。）
>
> 尽管 GPT-3 的即时应用——比如我拿它写诗或写笑话——已经很不错，但 GPT-3 的短期含义要重要得多。
>
> 第一，按传统深度学习标准看，GPT-3 很贵；但按科研／商业／军事／政府预算的标准看，它又很便宜，而结果表明，模型完全可以做得更大。
> 第二，模型也完全可以做得强大得多，因为 GPT 本身是一条老路，已知在大处小处都存在缺陷，离“理想”的 Transformer 还差得很远。
> 第三，GPT-3 的能力来自对原始（无监督）数据的学习；长期以来，这一直是深度学习最薄弱的领域之一，并拖累了强化学习或机器人等其他方向的进展。像 GPT-3 这样的模型说明，大型无监督模型将成为未来深度学习系统的关键组件，因为它们可以被“插入”到系统中，立即提供对世界、人类、自然语言与推理的理解。
>
> 元学习还有一个更长远的含义：它展示了[**缩放红利**](#blessings-of-scale)——简单神经网络身上的问题会消失；当它们只是被做得非常大、用非常大的数据集、非常大的算力去训练时，就会变得更强、更可泛化、更像人类——尽管这些性质通常被认为需要复杂架构与花哨算法（而这种被感知到的需求推动了大量研究）。
> 无监督模型尤其受益于此，因为在互联网规模的文本这类大型语料上训练，会面对无数困难问题；这已经足以驱动元学习，尽管 GPT 在设计上根本不是为了元学习。
> （这一族现象，或许是因为神经网络在起作用时像是许多子网络的[集成](https://en.wikipedia.org/wiki/Ensemble_learning)，它们平均起来形成了一种奥卡姆剃刀：在小数据与小模型下，它们会学到数据里表面的、或者死记硬背的部分；但只要把问题做得足够难、足够丰富，它们就会被迫学会真正的学习。并且，当[元学习器学会摊销贝叶斯推断](https://gwern.net/backstop#deep-bayes)时，它们在跨任务训练中会内置信息丰富的先验，从而在样本效率与泛化能力上都大幅提升。）
>
> 缩放红利进一步支撑了一种激进理论：少数联结主义先驱（早期人工神经网络研究者）以及近来的深度学习研究者所持有的一种老式 AI 范式，也就是[**缩放假说**](#scaling-hypothesis)。
> 缩放假说认为，缩放红利正是 AGI 的秘密：智能“无非”是简单神经单元与学习算法，在一种（目前）尚不可及的规模上施加于多样经验。
> 随着不断增长的计算资源允许我们在所需规模上运行这些算法，神经网络将变得越来越智能。
>
> 什么时候？几十年前，Hans Moravec 等先驱根据类似摩尔定律的进步曲线估计：要到 2010 年代，才会有足够便宜的算力来做昆虫级原型系统；而到 2020 年代，首批低于人类水平但已具规模的系统才会变得可行。如今看，这些预测是站得住脚的。
> （尽管这一点得到了印证，缩放假说依然极不受欢迎，而且它也很难在事前证明，只能事后以**既成事实**证明自己。因此，即便 GPT-3 的结果在 OpenAI 开放有限公众访问、让人们可以亲自试用后终于吸引到一些公众注意力，我仍然不认为会有很多机构因此修改自己的研究哲学，更别提由此引爆什么“军备竞赛”了。）
>
> 更令人担忧的是，GPT-3 的缩放曲线、未被预料到的元学习，以及在各种“反 AI”挑战上的成功，都说明在未来学这个问题上，AI 研究者的预测就像一个没穿衣服的皇帝：他们没有任何连贯模型来解释 AI 进展是如何发生的、GPT-3 为什么可能、哪些具体成就应该触发警报、智能从何而来，也不会从任何被证伪的预测中学习。
> 他们主要关心的似乎是维持现状、安抚公众担忧，以及保持体面。
> 因而，他们对 AI 风险的评论毫无意义：无论缩放假说是真是假，他们都会发出同样的公开表态。
>
> 这取决于人们愿意对扩展深度学习投入多少资源，也取决于算力增长有多快；但无论如何，2020 年代都应该会很有意思——会是 S 曲线，还是奇点？
>
> 想了解更多机器学习缩放研究，可关注 [/r/MLScaling](https://www.reddit.com/r/mlscaling/) 子版块。若想看一个科幻短篇形式的虚构处理，可见 ["It Looks Like You're Trying To Take Over The World"](https://gwern.net/fiction/clippy)。若想看我在两年后的 2022 年 5 月写的后续，可见 ["Scaling Hypothesis Revisited"](https://gwern.net/scaling-hypothesis-revisited)；另见 [_Situational Awareness_](https://situational-awareness.ai/) 与 [_AI 2027_](https://ai-2027.com/)。

**去读这些示例**
关于 ["GPT-3: Language Models are Few-Shot Learners", Brown et al 2020](https://arxiv.org/abs/2005.14165#openai)（[诗歌示例](https://arxiv.org/pdf/2005.14165.pdf&org=openai#page=48)与我的后续 ["GPT-3 Creative Writing"](https://gwern.net/gpt-3)，可对比[我早先微调过的 GPT-2 诗歌](https://gwern.net/gpt-2)；[随机示例](https://justpaste.it/7eovk)；以及带有真实世界演示的 ["OpenAI API"](https://openai.com/blog/openai-api/)）

我强烈建议任何对 GPT-3 感兴趣的人，至少去快速浏览一下 OA 的[随机示例](https://justpaste.it/7eovk)，或者更好的是去看我在 “GPT-3 Creative Writing” 里的示例——只读论文、只看几张标准基准图，根本无法让你真正感受到和 GPT-3 一起工作是什么感觉，也感受不到它能做出多少基准测试遗漏掉的、五花八门的事情。

# 元学习

**学会学习。** 2020 年 5 月，OA 发布了人们期待已久的 [GPT-2](https://openai.com/index/better-language-models/) 后续版本——几乎没引起研究者的兴趣，没有博客文章，没有媒体造势，除了讥讽式的轻蔑外，几乎没有什么公开讨论——一个足以一统天下的模型：它比 GPT-2 大了 `117` 倍，拥有 `1750` 亿参数，语言生成能力也强大得多；它能解决从算术^[鉴于关于论文中算术基准的评论很多，我想指出，由于[BPE 编码问题](https://gwern.net/gpt-3#bpes)，这个算术基准很可能大大低估了 GPT-3 的能力：例如，仅仅加上逗号，就能显著提高它做 `5` 位数加法的能力。BPE 问题似乎也解释了它在字母重排／洗牌任务上大量糟糕表现。凡是需要字符级操作或理解的任务，都该记住这一点。]到英译，到解乱序字谜，到 SAT 类比题的各种问题——而这一切纯粹来自用文本示例进行提示，没有任何专门训练或微调，只是对大型互联网文本语料做下一词预测训练。
这意味着，GPT-3 的注意力机制起到了[“快速权重”](https://arxiv.org/abs/1610.06258#deepmind)的作用，并通过在足够多样的数据上训练而“学会了学习”^[关于隐式[元学习](https://www.reddit.com/r/reinforcementlearning/search/?q=flair%3AMetaRL&include_over_18=on&restrict_sr=on&sort=top)，参见：[Santoro et al 2016](https://arxiv.org/abs/1605.06065#deepmind)/[Wang et al 2018](https://gwern.net/doc/reinforcement-learning/meta-learning/2018-wang.pdf#deepmind)（[Botvinick commentary](https://www.lesswrong.com/posts/Wnqua6eQkewL3bqsF/matt-botvinick-on-the-spontaneous-emergence-of-learning)）/[Botvinick et al 2019a](https://www.cell.com/trends/cognitive-sciences/fulltext/S1364-6613\(19\)30061-0#deepmind)、[Clune 2019](https://arxiv.org/abs/1905.10985#uber)、[Schmidhuber 2015](https://arxiv.org/abs/1511.09249#schmidhuber)/[2018](https://arxiv.org/abs/1802.08864#schmidhuber)、[Weng 2018](https://lilianweng.github.io/lil-log/2018/11/30/meta-learning.html#openai)/[Weng 2019](https://lilianweng.github.io/lil-log/2019/06/23/meta-reinforcement-learning.html#openai)。]，迫使它做的事情不只是学习普通的文本关系。
就像几周前 OpenAI 的 [Jukebox](https://openai.com/research/jukebox) 一样（它本身也是缩放的一个惊人展示：直接合成带有极其逼真人声／乐器的**原始音频**音乐），GPT-3 的发布似乎几乎无声无息地沉了下去，所以我会比平时讲得更细一些。
# GPT 炫技

> “‘他们绝对讲道理。我认为这正是他们最鲜明的特征。是的，Erskine 先生，一个绝对讲道理的民族。我向你保证，美国人身上毫无荒唐可言。’‘太可怕了！’ Henry 勋爵叫道，‘蛮力我还能忍，可蛮横的理性简直让人受不了。那样使用理性本身就不公平，简直是在智力线以下出拳。’”
>
> 《道林·格雷的画像》，奥斯卡·王尔德

**“攻击只会越来越强。”** 两年前，[GPT-1](https://openai.com/research/language-unsupervised) 作为预训练手段已经颇有意思，还带着它那个可爱的“情感神经元”。
一年前，GPT-2 凭借出色的文本生成与微调能力，已经令人印象深刻。
而今年，GPT-3 之所以吓人，是因为它居然是一种诞生于 `2018` 年初、辉煌却已经过时的架构（之所以还在用，多半只是因为软件工程上更方便，整套基础设施都调试过了）；它和理论上可达到的规模相比既小又浅[^overhang][^overhang-NN]，架构也简单而统一^[例如，狭窄的上下文窗口会对它造成[严重限制](https://arxiv.org/pdf/2001.08361.pdf#page=25)，并推动人们去研究[高效注意力](https://gwern.net/doc/ai/nn/transformer/attention/index)。更广泛地说，GPT-3 几乎没有任何花活——没有用[大脑模仿学习](https://www.reddit.com/r/reinforcementlearning/comments/9pwy2f/wbe_and_drl_a_middle_way_of_imitation_learning/)或神经架构搜索来专门定制模型，没有在线超参数优化（可能能带来 [>3× 加速](https://arxiv.org/abs/2106.00958#openai)），甚至连宽度这类最基本的超参数都没去认真决定（而 [EfficientNet](https://arxiv.org/abs/1905.11946#google) 已经说明，即便是在“理解充分、手工优化到极致的朴素架构”里，这也会带来相当大的差别）。]，用最笨的方式训练（单向预测下一个文本 token），只用一种贫乏的模态（随机互联网 HTML 文本转储^[甚至不是 PDF——所以没有 Google Books、没有 Arxiv、没有 Libgen、没有 Sci-Hub……]），数据也很小（笔记本电脑都装得下），采样方式也很笨^[从语言模型里采样可以揭示它**拥有**哪些知识，却无法揭示它**缺少**哪些知识；而且人们普遍同意，当前像 top-_k_ 这样的粗糙启发式方法绝不可能是最优的。]，基准表现还被糟糕的提示词与数据分词问题（尤其是算术与常识推理）拖了后腿——然而，即便如此，它的第一版就已经展现出疯狂的运行时元学习能力，而且缩放曲线**仍然**没有弯折！
示例质量也前所未有地更好——无论是 GPT-3 发明新的黄段子^['一个男人去看医生，医生对他说：“我有一个好消息和一个坏消息要告诉你。”／男人说：“我现在承受不了坏消息，先告诉我好消息吧。”／医生说：“好消息是，你有一根 `18` 英寸长的阴茎。”／男人愣了一会儿，接着问：“那坏消息呢？”／医生说：“你的脑子长在那儿。”']，还是写（大体能跑的）关于数组旋转的 [JavaScript 教程](https://justpaste.it/7eovk#javascript)。

[^overhang]: 到 `2020` 年初，GPT-3 的算力成本几乎不超过几百万美元，因为此前大量缩放研究使得一次训练跑通成为可能，而它的运行成本也很低（第 `39` 页）：“即便是完整的 GPT-3 175B，从一个训练好的模型生成 `100` 页内容，成本也大约只有 `0.4 kW-hr`，也就是几美分的电费。”（同样，T5 也[只训练过一次](https://x.com/colinraffel/status/1313097438299910147)。）而以一个模型的成本，GPT-3 API 用户展示出来的效果，相当于你得到了数百个更小的专用模型；这些模型每一个都需要更多研究者、定制数据集、无数次训练与调参，而且还得假设它们本来就能被做出来。（未来的口号可以是：“一个模型，一个向量——一劳永逸。”）

    作为对比，[PDP-11](https://en.wikipedia.org/wiki/PDP-11) 因极其便宜而成为常见学术工作马，价格不过 `20,000` 美元（`1970` 年币值）；而第一台 [Lisp Machine](https://en.wikipedia.org/wiki/Lisp_Machine) 则要 `>$50,000`（`1972` 年币值）——对工作站来说很贵，但和那些独占价值数千万美元的大型机的研究者相比，已经算是捡便宜了。IBM 那个（除此之外毫无用处的）Deep Blue AI 项目，据说最终版本花了 `>$5m`（`1997` 年币值）；而那些 `>$100m`（`1997` 年币值）的说法，似乎是把 Hsu 的 _Behind Deep Blue_ 第 `187` 页提到的**宣传价值**估值给搞混了。像 [ITER](https://en.wikipedia.org/wiki/ITER) 这样的“大科学”项目，花的钱比这还多 `>5000×`，结果大多还是失败。（顺便一提，粒子物理学家现在又[回来要钱了](https://www.nature.com/articles/d41586-020-01866-9)，想拿到 `≫$24b`（`2020` 年币值）；想必是因为 LHC 那笔 `>$9b`（`2010` 年币值）投资带来了那么多科学革命与改变世界的突破，又或者是因为当年为了（最终没）建成 [SSC](https://en.wikipedia.org/wiki/Superconducting_Super_Collider) 花掉的 `$2b`（`1993` 年币值）实在太值了……）

    若是看全球计算资源与科研预算，GPT-3 其实几十年前就能做出来；那用今天的硬件与预算，我们到底还能做出什么，只是我们既不知道也不关心去做？硬件冗余**确实存在**。（另见 [_Whole Brain Emulation Roadmap_](https://gwern.net/doc/ai/scaling/hardware/2008-sandberg-wholebrainemulationroadmap.pdf) 与 ["2019 recent trends in GPU price per FLOPS"](https://aiimpacts.org/2019-recent-trends-in-gpu-price-per-flops/)。）
[^overhang-NN]: 此外，神经网络自身还存在额外的硬件冗余，因为训练与运行之间存在好几个数量级的不对称。迁移学习与元学习都比基础模型训练快得多。你甚至不需要任何梯度步——只靠示例——就可以“训练” GPT-3。你先为“一个统治一切的大模型”付出极其陡峭的前置成本，然后就能以极低的边际成本到处复用它。如果你训练出了一个模型，那么它一完成，你立刻就会得到（除别的之外）：

    - 在同一套硬件上并行运行成千上万个副本的能力

        - 在 AlphaGo 这样的语境里，我估计，如果你只是复用同一套硬件，对原模型的精确副本做树搜索，就能涨出几百分 ELO
    - 面向任何相关领域的元学习／迁移学习，把训练需求砍掉好几个数量级
    - 模型压缩／蒸馏，可以训练出体积、FLOPS 或延迟都只是其一小部分的学生模型（比例会随任务、方法、领域、可接受的性能下降、目标硬件等而差异极大，但往往可以夸张到 `1⁄100^th^`）
    - 在别处复用这个模型，立刻给其他模型充能（例如让 DRL 代理使用文本或图像嵌入）
    - 越做越会做／[经验曲线效应](https://en.wikipedia.org/wiki/Experience_curve_effects)（在信息技术里最强，在深度学习里也很强：[Hernandez & Brown 2020](https://arxiv.org/abs/2005.04305#openai)），因此下一个从零训练的模型可能会便宜得多。

        例如：在训练第一版 [OpenAI Five](https://en.wikipedia.org/wiki/OpenAI_Five)（OA5）DoTA2 代理的过程中，经历了所有迭代式模型架构与游戏升级之后，OA5 的第二个版本 ["Rerun"](https://arxiv.org/pdf/1912.06680.pdf#page=11&org=openai) 又从零训练了一遍。Rerun 只用了 `20%` 的训练量，就达到了“对最终版 OpenAI Five 的 `98%` 胜率”。
        正如作者所说：“理想的选择，是从一开始就用类似 Rerun 的训练方式；但这是不可能的——OpenAI Five 那条曲线代表了通向最终代码库、环境等的经验积累，没有那些经验，就不可能训练出 Rerun。”
    - 作为工程化出更高效模型的基线，通过消融与对比来改进原模型

奇怪的是，这种质变飞跃似乎在标准 NLP 基准中基本被忽视了。
在 Penn Tree Bank、LAMBADA 或 WinoGrande 这类指标的原始数值里，没有任何东西会让你预想到这些荒唐又有创造力的输出；元学习结果或许会，但前提是你原本就认为元学习很重要。
这让我觉得，一个有价值的后 GPT-3 贡献，应该是想办法为这类灵活文本生成能力建立基准（也许有点像 Chollet 基于图像的 [Abstraction and Reasoning Corpus (ARC)](https://arxiv.org/abs/1911.01547#google)）。
# 烤蛋糕

![GPT 真的是 AGI 的一部分吗——还是说这蛋糕本就是幻觉？（[LeCun 2019](https://gwern.net/doc/ai/scaling/2019-02-18-lecun-isscc-talk-deeplearninghardwarepastpresentandfuture.pdf#page=60)）](https://gwern.net/doc/ai/nn/2019-lecun-isscctalk-cake.png)

**不是全貌，但占了很大一块。** 它在每一个任务上都刷新了 SOTA 吗？没有，当然没有。
但问题不在于，我们能否像律师一样挑出任何一种它可能行不通的方式，而在于[是否存在某种它可能行得通的方式](https://gwern.net/forking-path)。
而且它还有很多方式可以做得更好（仅举几例，可见[“局限性”一节](https://arxiv.org/pdf/2005.14165.pdf&org=openai#page=34)）。
GPT-3 **会做**诸如开着机器人在旧金山四处向人类发射激光和火箭的事吗？不会，当然不会。
它“只不过”是一个文本预测模型，一个文本领域的白痴天才；但我们要记住，所谓白痴天才，离正常人也不过只差一次基因突变或一点脑损伤。
如果说强化学习是监督学习糖霜顶上的樱桃，而监督学习又是无监督学习蛋糕上的糖霜，那么现在看来，蛋糕胚终于开始发起来了。

![一个更好的 GPT-3 教训。](https://gwern.net/doc/ai/nn/cnn/2020-07-24-gwern-meme-moneyprinter-bitterlesson-gpt3.png)

**缩放仍然有效。** 我原本很惊讶，因为我之前预期的参数量更接近 `100b`，而且我以为 [CTRL](https://arxiv.org/abs/1909.05858#salesforce)/[Meena](https://arxiv.org/abs/2001.09977#google)/[MegatronLM](https://nv-adlr.github.io/MegatronLM)/[T5](https://arxiv.org/abs/1910.10683#google)/[Turing-NLG](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/)/[GPipe](https://arxiv.org/abs/1811.06965#google) 的表现说明，尽管有[那些缩放论文](https://en.wikipedia.org/wiki/Neural_scaling_law)[^scaling-papers]，缩放曲线恐怕已经开始弯折，到 `100b` 时，再继续扩大就很难自圆其说了。
然而，在最新版本的 ["the unreasonable effectiveness of data"](https://gwern.net/doc/ai/scaling/2009-halevy.pdf) 所展示的那种“曲线交叉”／“剪刀效应”里，神经方法最终会取胜（例如 [Banko & Brill 2001](https://gwern.net/doc/ai/scaling/2001-banko.pdf#microsoft)、[Brants et al 2007](https://gwern.net/doc/ai/scaling/2007-brants.pdf#google)、[Koehn & Knowles 2017](https://gwern.net/doc/ai/scaling/2017-koehn-figure3-bleuscoreswithvaryingamountsoftrainingdata.png)），而 GPT-3 在参数量翻倍的情况下，缩放因子却几乎没有明显变化：它的缩放关系依旧近似对数／幂律，和更小模型时一样，也和预测一致；它并没有进入那种收益实际停止、或者需要远超可行范围的投入增量才能继续提升的区间。
这说明，走向万亿参数不仅可行，而且有价值（这仍远在现有算力与预算承受范围之内，只需要几千张 GPU，以及大约 `$10`（`2020` 年币值）到 `$100m`（`2020` 年币值）的预算——这还是在假设没有改进的前提下，而改进当然会有，见 [Hernandez & Brown 2020](#hernandez-brown-2020-paper) 等），而且光从图上目测，像 [Winograd schema](https://en.wikipedia.org/wiki/Winograd_schema_challenge) 这样的基准 [WinoGrande](https://arxiv.org/abs/1907.10641#allen)，到了 `10t` 参数时大概就会被攻克。
这种缩放的可预测性非常惊人，它让缩放模型看起来更像统计学，而不像 AI。
（AI 就是那种做我们想让它做的事、却又不好使的统计学；而统计学，就是那种好使、却不做我们想让它做的事的 AI。）

[^scaling-papers]: 特别是，样本效率会随着模型规模增大而提升，直到达到算力效率最优的缩放点；而且 [GPT-2 只看一遍数据就能记住它](https://arxiv.org/abs/2012.07805)——考虑到真实世界数据分布具有长尾特性，这是一种[可取的性质](https://arxiv.org/abs/1906.05271#google)。（至于**不该**怎么做缩放论文，[Thompson et al 2020](https://arxiv.org/abs/2007.05558) 就是一个例子：和前面那些论文形成鲜明对比的是——而 Thompson 等人压根没提它们！——他们不是基于作者自己运行的、控制良好、曲线极紧、预测力极强的实验来推断缩放关系，而是试图从各种高度异质的研究论文里偶尔报告的数字中倒推出缩放曲线；不出所料，他们的曲线几乎什么都预测不了，而且看起来反正也严重高估了。）

    值得注意的是，追求大模型几乎完全是由 OpenAI 和工业界机构推动的（后者对远小得多的模型就已经满足），而学术界则表现出近乎彻底的无兴趣——甚至是厌恶、愤怒和否认（可以说，“green AI” 是嫉妒得发绿）。嘴上都说缩放假说“显而易见”、缩放是“早已预测到的”，可真正愿意去**做**的人却少得惊人。也许我们应该多关注人们在做什么，而不是他们在说什么；并记住，成功的学术共同体产出的是问题，而不是答案。

![GPT-3：其实也没用那么多算力——[3640 petaflop/s-day](https://arxiv.org/pdf/2005.14165.pdf#page=46&org=openai)，只是他们给 AlphaGo Zero 估计值 `1860` 的 `2×`。（历史图由我本人基于 ["AI and Compute", Amodei et al 2018](https://openai.com/research/ai-and-compute) 修改。）](https://gwern.net/doc/ai/nn/transformer/gpt/3/2019-11-07-amodei-aiandcompute-twodistincteras-gpt3modified.jpg)

**反缩放：捡了芝麻，丢了西瓜。** 以机器学习的标准看，GPT-3 是一个贵得离谱的模型：据估计，训练它可能要花掉相当于一只手都数得过来的那些机器学习研究者一年的成本（约 `$5m`（`2020` 年币值）^[大致接近 [Chuan Li](https://lambdalabs.com/blog/demystifying-gpt-3) 的估算，使用的是没有折扣的标价，而云计算的边际成本其实显著更低，所以折扣可能相当大。研发项目的总成本当然会高得多，但那会被后续所有模型与项目摊销。]），外加最多 `$30`（`2020` 年币值）的硬盘空间来存模型（`500--800GB`），以及每输出 `100` 页要花上几分钱的电（`0.4 kWH`）。
研究者担心进一步缩放的前景：机器学习真的负担得起那些成本高于 `0.1` 个 milli-Manhattan-Projects 的项目吗？^[曼哈顿计划花费约 `$2b`（`1946` 年币值）。]
就算它真能再次带来 AI 能力的大跃进，真要花到 `10` 个 milli-Manhattan-Projects，把 GPT-3 再放大 `100×`，换来一个在很多领域都像人的平凡东西，难道不是太贵了吗？
很多研究者觉得，这样的提议荒谬到足以彻底反驳继续扩展机器学习研究的想法；他们斩钉截铁地说，自己偏好的路线（你知道的，就是那些根本不管用的路线[^butcher]）会高效得多；他们还说，如果整个领域转而关注那些让一个穷困牧羊人拿着一台靠太阳能供电的旧笔记本就能做出来的研究，效率才会更高。^[仿佛我们活在一个只要足够努力许愿，研究生就能靠泡面预算上月球的世界里；仿佛评估里只盯着 CO~2~ 成本、不看收益，不像是一把只有一片刀刃的剪刀；又仿佛那些试图绕开大模型、直接造小模型的“green AI”路子，看起来并没有越来越徒劳、越来越像是在往坏账上继续砸钱，而且并不是所有 AI 研究里最不“绿色”的一类……在某种程度上，`2010` 年前后的前沿 AI 研究几乎都能靠研究生级别的钱——比如 `$1,000`（`2010` 年币值）的硬件——来完成，而此前此后几十年的 AI 研究都得益于重型算力，这本身就是对那个时代的控诉：它说明那时的研究是多么停滞、多么走进死胡同，以至于其技术路线如此狭隘、如此自废武功，竟无法从现成的大规模算力中受益。]
尽管如此，我认为我们仍应预期进一步缩放。
（`10×`？不，`10×` 不够酷。知道什么才酷吗？[`100--1000×`](https://www.reddit.com/r/slatestarcodex/comments/hys565/are_we_in_an_ai_overhang/fzezi7d/)，再配上一台[花哨的新超级计算机](https://news.microsoft.com/source/features/ai/openai-azure-supercomputer/)去训练。）
毕竟，先把东西做出来，再去把它做高效，总比事先就把高效做出来容易。

[^butcher]: 这让人想起那个顾客向屠夫抱怨的笑话：

    “你的肉卖 `\$10/lb`，可街对面那家只卖 `\$1`！”“那你去买他的啊。”“我倒想，可他没有肉。”“那我没肉的时候，也只卖 `\$1`。”

# 缩放

**缩放究竟能走多远？** 那些缩放论文表明，就绝对似然损失而言，我们过去几年看到的飞跃，连半程都还没走到；更别提每一次进一步下降究竟会对应成现实世界中的哪些新能力了。
缩放曲线很干净；出自 ["Scaling Laws for Neural Language Models", Kaplan et al 2020](https://arxiv.org/abs/2001.08361#openai)：

![深度学习缩放定律：算力、数据、模型参数。（[Figure 1](https://arxiv.org/pdf/2001.08361.pdf#page=3&org=openai)）](https://gwern.net/doc/ai/nn/transformer/gpt/2020-kaplan-figure1-dlscaling.jpg)

GPT-3 在这张图上大约处于 `~10^3^` 的位置，距离进一步降低损失仍有很大空间——尤其考虑到[外推本身的不确定性](https://arxiv.org/pdf/2001.08361.pdf#page=17&org=openai)：

![深度学习幂律外推：GPT-3 之外仍有空间。](https://gwern.net/doc/ai/nn/transformer/gpt/2020-kaplan-figure15-projectingscaling.png)

果不其然，GPT-3 模型的缩放定律在 [Kaplan et al 2020](#kaplan-et-al-2020) 之后又继续延伸了好几个数量级；出自 [Brown et al 2020](https://arxiv.org/pdf/2005.14165.pdf#page=11&org=openai)：

![GPT-3 继续按预测方式缩放。（注意 GPT-3 的曲线没有“弹回去”，而且它只训练了约 `0.5` 个 epoch，见 [Table 2.2](https://arxiv.org/pdf/2005.14165.pdf#page=9&org=openai)）](https://gwern.net/doc/ai/nn/transformer/gpt/2020-brown-figure31-gpt3scaling.png)

如果把验证损失减半就已经带来了如此惊人的收益，而前面还剩下这么大一截没走，那么当我们再把损失降到三分之一、再减半一次时，还会涌现出什么？
这到底会走多远？我们又该如何预测什么会在什么时候涌现？
Bueller？Bueller？
（另见 [Meena 的困惑度与人类感聊天机器人评分](https://gwern.net/doc/ai/2020-adiwardana-meena-figure1-humanratingsvslikelihood.png)、GPT-3 撰写新闻在不同参数规模下[欺骗人类的概率](https://gwern.net/doc/ai/nn/transformer/gpt/2020-brown-figure313-humanabilitytodetectmodelgeneratednewsstories.jpg)，以及 [Hendrycks et al 2020](https://arxiv.org/abs/2009.03300) 中 [GPT-3 模型规模与问答能力](https://gwern.net/doc/ai/nn/transformer/gpt/2020-hendrycks-figure1b-gpt3-qascaling.png)的图。）

## 缩放红利

> 把 GPT-3 那惊人的表现外推到未来，似乎说明生命、宇宙以及一切的答案，不过就是 `4.398` 万亿参数。
>
> [Geoff Hinton](https://x.com/geoffreyhinton/status/1270814602931187715)

**我们并不知道如何训练神经网络。** **缩放红利**指的是这样一种观察：对于深度学习来说，难问题反而比简单问题更容易解决——东西越大，一切就越好（这和研究里常见的情况正相反：小东西很难，大东西则根本不可能）。
神经网络／算力／数据／问题越大，它学得越快、学得越好、学得越稳定，等等。
一个在小 _n_ 下我们根本解不了的问题，到了百万乃至十亿量级的 _n_ 时，可能突然就变得直截了当。
“神经网络是懒的”：当我们把它们推离容易答案和廉价捷径时，它们其实能做的事远比我们逼它们做的多。
[bitter lesson](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) 告诉我们：越难、越大，越好。
（除了 GPT-3，也可以提一提最近半监督学习的进展，以及基于模型的 DRL 复兴。）

![AlphaGo Zero：“直接多堆几层就完事了，笑死！”](https://gwern.net/doc/reinforcement-learning/2017-12-24-gwern-meme-nnlayers-alphagozero.jpg)

**缩放红利：稳定性 → 泛化 → 元学习。** GPT-3 受制于它的训练方式与数据，但深度学习享有一种不可思议地有效的[维数福祉](https://en.wikipedia.org/wiki/blessing_of_dimensionality)——只要训练一个**大**模型，再配上**大量**数据，就会诱导出像元学习这样的更好性质，哪怕架构里根本没有显式写入任何相关机制；更一般地说，在更多、更难的任务上训练，会产生越来越像人的表现、泛化与鲁棒性。
GPT 的自然语言与编程语言模型、用于图像的 [iGPT](https://openai.com/index/image-gpt/)/[Vision Transformer](https://arxiv.org/abs/2010.11929#google)（以及某种程度上的 [GPT-f](https://arxiv.org/abs/2009.03393#openai)）都表明，只是把模型和数据集做大、完全不加监督，就能得到可与最佳（也是最复杂）替代方案竞争的结果，而且用的还是同一种简单架构；随着数据增加，它们会逐渐从肤浅表面相关，过渡到更像人类的大脑活动（[Schrimpf et al 2020](https://www.biorxiv.org/content/10.1101/2020.06.26.174482.full)）与语言偏置（例如 [Warstadt et al 2020](https://arxiv.org/abs/2010.05358)）。
实际上，在足够大规模下，你甚至未必需要复杂的注意力机制，因为全连接网络——很难想象还有什么比它更简单！——在许多任务上都[出奇地有效](https://gwern.net/doc/ai/nn/fully-connected/index)。
训练这类大模型时，人们通常还会使用像 Adam 这样简单的优化器——因为随着 batch size 增大，那些复杂优化器的优势会消失，而[简单优化器已经够好](https://arxiv.org/abs/2102.06356)了，而且内存效率更高。
[OA5](https://arxiv.org/pdf/1912.06680.pdf&org=openai#page=13) 不只是能扩展到数百万规模的 minibatch，甚至会因为[梯度噪声](https://openai.com/research/how-ai-training-scales)而在这个规模上[稳定下来](#ppo-dota2)。
与 OA5 类似，[BigGAN](https://arxiv.org/pdf/1809.11096#page=8&org=deepmind) 在 JFT-300M 这样的大规模图像数据集上也会稳定下来，并且受益于异常大的 minibatch；而 VAE（长期以来在清晰图像生成上一直是 GAN 或自回归模型的陪跑者）如果做得足够深，也会追上来（[Child 2020](https://arxiv.org/abs/2011.10650#openai)、[Vahdat & Kautz 2020](https://arxiv.org/abs/2007.03898#nvidia)）；与此同时，像 [BiT](https://arxiv.org/abs/1912.11370#google)^[一个有趣的冷知识：BiT 现在在预测（清洗并纠正后的）ImageNet 标签时，[准确度已经高于](https://arxiv.org/abs/2006.07159#google)原始 ImageNet 标签本身的准确度。]/[Dojolonga et al 2020](https://arxiv.org/abs/2007.08558#google)、[ResNeXt](https://arxiv.org/abs/1907.07640) 或 [Noisy Student](https://arxiv.org/abs/1911.04252#google) 这样的分类 CNN，则会随着规模增大而更好地迁移、并[变得更鲁棒](https://arxiv.org/abs/2007.00644)[且](https://arxiv.org/abs/2103.14586#google)出现更像人的错误^[图像缩放实验（如 Dojolonga et al 2020）有个有趣之处：即便在原始任务上的表现已经“平台化”、接近标签误差上限时，迁移学习仍会继续变好。显然，内部表征即便对纯分类任务来说已经够用、分数最多只能再涨一点点，仍会继续变得更像人——因为它在编码[暗知识](https://arxiv.org/abs/1503.02531#google)或更强的[对抗鲁棒性](https://arxiv.org/abs/2006.14536#google)？我在语言模型上也注意到，损失函数最后那一点点下降，似乎会对生成样本质量造成相当大的差别；也许是因为，只有当所有更容易的建模都完成后，这个懒惰的语言模型才会被迫榨出下一点性能，通过更正确地建模诸如逻辑、对象、世界知识等更复杂的东西。]；多模态学习则能在更少数据上产出更好的表征（例如 [ViLBERT](https://arxiv.org/abs/1912.02315#facebook)/[VideoBERT](https://arxiv.org/abs/1904.01766#google)，这也解释了 [OA 对大型多模态模型的兴趣](https://www.technologyreview.com/2020/02/17/844721/ai-openai-moonshot-elon-musk-sam-altman-greg-brockman-messy-secretive-reality/)）；而 RNN 甚至可以[预测视频](https://arxiv.org/abs/1911.01655#google)。
[AlphaStar](https://gwern.net/doc/reinforcement-learning/model-free/alphastar/2019-vinyals.pdf#deepmind) 靠着数百个彼此竞争的自博弈玩家覆盖可能策略，达到了人类水平。
像 [MetaMimic](https://arxiv.org/abs/1810.05017#deepmind) 这样的模仿学习式 DRL，则在数百个任务上泛化，以此训练深度网络。
只要给 [StyleGAN](https://arxiv.org/abs/1812.04948#nvidia) 足够深的 _w_ 嵌入，给 Jukebox 那样的系统足够多参数去训练原始音频，或者给 [relational networks](https://arxiv.org/abs/1706.01427#deepmind)/[GQN](https://gwern.net/doc/reinforcement-learning/model/2018-eslami.pdf#deepmind)/[Transformers](https://arxiv.org/abs/2002.05867) 足够多样本去逼迫因子分解，解缠结都会自发涌现。
（另见 [Hill et al 2019](https://arxiv.org/abs/1910.00571#deepmind)/[Chaplot et al 2017](https://arxiv.org/abs/1706.07230)/[Yu et al 2018](https://arxiv.org/abs/1802.01433#baidu)/[Lake 2019](https://arxiv.org/abs/1906.05381)/[Interactive Agents Group 2020](https://arxiv.org/abs/2012.05672#deepmind)。）
在数百万种领域随机化上训练 [Dactyl](https://arxiv.org/abs/1910.07113#openai)（或者[类人机器人](https://arxiv.org/abs/2304.13653#deepmind)），也会诱导出类似的隐式元学习：在每次运行调用期间，RNN 都会探测其环境，并把它对机器人手部控制的理解编码进隐藏状态；而 [DD-PPO](https://arxiv.org/abs/1911.00357#facebook) 通过两个数量级的缩放，超过了经典机器人规划器。
或者在 [Procgen](https://openai.com/research/procgen-benchmark) 与 [CoinRun](https://distill.pub/2020/understanding-rl-vision/#diversity-hypothesis) 里，当只在数百个关卡上训练时，代理会学会分别解决各个关卡，却在其他关卡上表现更差；但到上千个关卡时，它们就开始能泛化到未见过的关卡。（类似地，[语言模型预训练—微调](https://arxiv.org/abs/2101.11038#facebook)在数据集数量很少时会过拟合，但多样性足够后就会明显改善。）
[AlphaZero](https://gwern.net/doc/reinforcement-learning/model/alphago/2018-silver.pdf#deepmind) 证明了：仅仅训练一个更大的模型、给它更丰富的信号与职业级棋谱、完全不做搜索，也能下出真正超人的围棋——而 [MuZero](https://arxiv.org/abs/1911.08265#deepmind) 更进一步地证明了，只要把一个 RNN 端到端训练成在足够数据上预测奖励，就足以让 AlphaZero 过时，并且隐式学会树搜索（而且学得更好）。
如此等等，不一而足。
DeepMind 研究员 [Matthew Botvinick](#scholl-2020) 在谈到他们的元强化学习工作时说，他们原本很惊讶会发现元学习自己涌现出来，而且不管具体用了哪种架构都会发生：

> ……这种事就是会发生。从某种意义上说，你根本无法避免它发生。如果你有一个带记忆的系统，而这个记忆的功能又是由强化学习塑造的，并且这个系统是在一系列彼此相关的任务上训练的，那这件事就一定会发生。你没法阻止它。

借用 [Breiman](https://gwern.net/doc/ai/scaling/1995-breiman.pdf) 的问题，**为什么**？
为什么它们能够迁移和泛化？
为什么会有这些缩放红利？
既然可以证明存在性能相同的小模型，为什么我们还需要训练大模型？
为什么更大的模型不会过拟合（虽然它们[也可能会](https://arxiv.org/abs/1611.03530#google)），反而比更小的模型泛化得更好？
那个所谓的[“双降”](https://openai.com/research/deep-double-descent)现象到底又是怎么回事？

这些当然全都是——咳——关于神经网络的“深”问题，而且争议很大；但此刻，我会建议答案大概位于模型压缩／蒸馏、[“彩票假说”](https://ai.meta.com/blog/understanding-the-generalization-of-lottery-tickets-in-neural-networks/)、[贝叶斯神经网络](https://arxiv.org/abs/2002.08791)以及[学得表征](https://arxiv.org/abs/2007.00810#google)（比如 [circuits](https://distill.pub/2020/circuits/zoom-in/#openai)）这几支文献的某种混合地带。

大模型之所以有效，是因为它们在一个极其[高维](https://colah.github.io/posts/2014-03-NN-Manifolds-Topology/)的抽象空间里编码了数量惊人的子模型，代表着无数小子模型（[Orseau et al 2020](https://arxiv.org/abs/2006.12156#deepmind)）在[数据上做插值](https://gwern.net/doc/ai/scaling/2020-hasson.pdf)；其中很可能有某个子模型能够很好地解决问题，因此保证整个模型是可解的。
它们像一个集成体那样工作：尽管单个大模型内部存在无数会过拟合的子模型，但它们相互平均之后，会导向对简单解的偏好。
这种奥卡姆剃刀式的偏置，会让模型偏向那些足够灵活、可以逐渐扩展复杂度以匹配数据的简单解。

然而，“神经网络是懒的”：那些去记住局部数据、或者抓住表面特征的子模型，学起来最快，也最容易在内部表示。
如果模型、数据与算力都不够大、不够多样，那么到这种草草训练结束时，优化过程最终只会把你带到一个低损失的子模型，却漏掉了解题所需的重要部分。

另一方面，对于 GPT-3 这样的模型来说，它已经足够强大，以至于其子模型可以从写诗一路做到算术；而它训练所用的数据又多到，那些表面化模型也许在早期表现不错，但随后会逐渐落后于更抽象的模型。一个记住部分数据的子模型，确实比一个真正编码了算术的子模型要简单得多（一个神经网络大概可以在编码一个“加法”这类抽象算法所需的空间里，记住数万个加法例子的查找表条目），但它不可能记住 GPT-3 互联网规模数据集中**所有**显式或隐式的算术实例。
如果一个死记硬背的子模型真试图这么做，它就会变得极其庞大，从而受到惩罚。
最终，在见过足够多例子、经历足够多次更新之后，也许会发生一次相变（[Viering & Loog 2021](https://arxiv.org/pdf/2103.10948.pdf#page=22)）：这时，那个最简单、又能准确预测数据的“算术”模型，本身就**是**算术。
而元学习也是同理：当模型看过足够多只在每个样本内略有变化的算法实例后，把每个任务分开学就会变得困难，于是它学到的其实就是更通用的算法；这会产生损失更低的子模型，而那些竞争子模型要么预测得不好，要么膨胀得无法接受。
（GPT-2-1.5b 显然太小或太浅，还不足以轻易在编码元学习算法的子模型上做集成，或者说，它也许只是没有在足够多的数据上训练足够久，从而没能找到那些元学习器模型；而 GPT-3 找到了。）

所以，只要有足够的数据与算力，把模型推过那些容易、方便的子模型，一直推进到表达泛化、把感知因子分解为有意义潜在维度、根据描述去做任务级元学习、学习因果推理与逻辑等可取特质的子模型，那么模型越大，就越好。
只要材料在那儿，这件事就会发生。

## 缩放假说

强形式的**缩放假说**认为，一旦我们找到了一种可扩展的架构，比如自注意力或卷积——它们和大脑一样，可以相当均匀地应用于各种地方（例如 ["The Brain as a Universal Learning Machine"](https://www.lesswrong.com/posts/9Yc7Pp7szcjPgPsjf/the-brain-as-a-universal-learning-machine) 或 Hawkins 的观点）——我们就可以简单地训练越来越大的神经网络，而越来越复杂的行为会自然而然地涌现，因为那就是在所有任务与数据上实现优化的最容易方式。
更强的神经网络“无非”就是放大版的弱神经网络，正如人脑看起来也很像[放大版的灵长类大脑](https://gwern.net/doc/psychology/neuroscience/2012-herculanohouzel.pdf)。
当我在 `2004--2010` 年间刚开始对 AI 产生兴趣时，我对那些缩放假说的支持者一直高度怀疑（那时 AI 还困在只能做极窄任务的工具低谷里，像 `2028` 这样的年份看上去都遥不可及），因为那听起来很像数字神秘学，像一种“你把它造出来，它们自然就会来”的逻辑（那时我们当然还没有可以直接往上堆算力的通用算法）；但到了 `2020` 年，我不得不承认，是我错了，他们对了。
我们把算力造出来了，而算法**真的**随之而来；自 `2010` 年以来，缩放假说看起来也一年比一年更可信。

# 为什么预训练有效？

预训练论大致是这样说的：

![“Figure 1：通过三种不同阶段或曲线设想 NLP 研究的演化”（自然语言建模中的假想 S 曲线与进展；出自 [Cambria & White 2014](https://gwern.net/doc/ai/scaling/2014-cambria.pdf)）](https://gwern.net/doc/ai/scaling/2014-cambria-figure1-hypotheticalnlpprogresscurves.png)

可以这么说，人类就是 [AI 的蓝细菌](https://en.wikipedia.org/wiki/Great_Oxidation_Event)：我们不断排放出大量结构化数据，而这些数据本身又隐含地依赖于逻辑、因果、对象恒存、历史——以及所有那些好东西。
所有这一切都以隐式方式编码在我们的书写、视频以及“数据尾气”里。
一个要学会预测的模型，为了取得最佳表现，就必须学会理解这一切；当它把那些只需统计模式匹配的容易部分都预测掉以后，剩下的就是难的东西。
AI 批评者常说，自动驾驶或自然语言这类任务中的长尾场景，只有靠真正的泛化与推理才能解决；那么随之而来的结论就是：如果模型真的解决了长尾，它就必定学会了泛化与推理。

训练早期，模型先学到最粗糙的层次：比如某些字母如 `e` 比另一些字母如 `z` 更常见，大约每 `5` 个字符左右就会出现一个空格，等等。
它会从“预测均匀分布的字节”进步到一种看起来像 Base-60 编码的东西——字母数字混杂的乱码。
尽管这还很粗糙，但已经足以带来相当可观的绝对进步：一个随机预测器需要 `8 bits` 才能“预测”一个字节／字符，但只要它至少学会匹配字母和空格的频率，误差就几乎能减半到约 `5 bits`。^[这里的数字并不精确，只是用来说明问题；因为 BPE 并不对应任何直观单位，我这里会借用自己观察 char-RNN 时的经验，用“每字符损失”而不是 BPE 来说。]
由于它从每个字符中都能学到很多东西，而且学到的频率规律又很简单，所以这一步可以发生得极快，快到如果你不高频记录样本，甚至都不一定看得到这种改进。

随着训练推进，任务会变得更难。现在它开始学习哪些词是真实存在的，哪些词并不存在。它还不懂任何意义，但至少此时当你让它预测一个单词的后半部分时，它已经可以在某种程度上做到，从而再省下几 bit。
这一步要花一些时间，因为任何具体实例出现的频率都只是偶尔：某个词可能在十几个样本里都不出现一次，而要学的词却有成千上万。
再多下点功夫，它就学会了标点、复数形式、所有格这些确实存在的东西。
把这些拼起来，它可能又前进了一大步，把误差一路压到每字符 `3--4 bits`！
（尽管这种进步快得令人欣慰，但别搞错了：这仍然全是乱码。样本的拼写也许是对的，但一点意义也没有。）

可一旦模型已经学会了相当不错的英语词汇，以及正确的格式／拼写，接下来是什么？仅靠词内预测已经没多少油水了。
下一步就是抓取词与词之间的关联。哪些词倾向于先出现？哪些词会“聚成一团”，经常彼此靠近使用？
航海术语常常一起出现在海洋故事中，圣经段落会彼此相伴，美国历史维基百科条目也一样，诸如此类。
如果最后一个词是 “Jefferson”，那 “Washington” 多半不会离得太远，因此它就该在预测下一个字符时把赌注多压在 `W` 上；如果真出了 `W`，那就一路梭哈到 “ashington”。
这种词袋式方法的预测仍然很糟，但现在我们也许已经降到每字符 `<3 bits` 了。

接下来呢？它会停在这里吗？只要有足够数据，而且像“学英语词汇”这类早期学习没有把模型的学习能力全耗尽，那它就不会停。
渐渐地，像 “President” 或 “general” 或 “after” 这样的词，会开始向模型展示更微妙的相关性：“Jefferson was President after...”
有了许多这样的段落之后，词语 “after” 就开始在预测下一个词时变得有用了，而这种用途随后还能被推广开来。

到了这个阶段，损失大概已经降到 `2 bits` 左右：每再降低 `0.1 bit`，成本都会更陡，时间也会更长。
但现在，句子已经开始变得有意义了。
像 “Jefferson was President after Washington” 这样的句子，确实是在表达某种东西（当然，如果我们偶尔采样出 “Washington was President after Jefferson”，那你还能指望一个还没收敛的模型怎么样呢）。
任何刺耳的错误，都会立刻把我们从“模型已经理解了”的幻觉里撞出来，于是训练继续。
（大致从这里开始，Markov 链和 _n_-gram 模型会落后：它们可以记住越来越大的训练语料片段，但却无法解决越来越关键的句法任务，比如括号或引号配平，更别提从句法往语义上爬升了。）

现在训练变难了。语言里更微妙的层面也必须被建模，比如保持代词前后一致。
这之所以困难，一部分是因为模型犯错已经越来越少，另一部分则是因为相关文本片段之间的距离越来越远、越来越“长程”。
随着它继续进步，错误的绝对规模会急剧缩小。
拿姓名与性别代词的关联来说：“Janelle ate some ice cream, because he likes sweet things like ice cream”和“Janelle ate some ice cream, because she likes sweet things like ice cream”之间的区别，没有任何人类会看不出来，然而它其实只差了一个字母。
如果我们比较两个模型：一个完全不懂性别代词，只会随机猜 `he`／`she`；另一个则完美理解，总能猜出 `she`；那第二个模型的平均误差也不过只会降低到每字符 barely `<0.02 bits`！

尽管如此，随着训练继续，这些问题以及更多问题——比如模仿文体——都会被解决；最终，在损失降到 `1--2` 左右时（小型 char-RNN 在像莎士比亚或某些 Project Gutenberg 电子书那样的小语料上大概会收敛在这里），我们终于会得到听起来像人类写的一样的样本——至少能像上几句话。
这些最终样本也许会短暂地说服我们，但即便样本不错，除去重复循环等问题外，错误仍会不断累积：一个样本可能前面说某人“活着”，`10` 句之后却用上 “dead”；或者它会从预期的下一个论点歪到一个无关争论上去；或者某人做出物理上不太可能的事；又或者它只是继续写了一阵，却似乎根本**没往任何地方去**。

所有这些错误都远小于每字符 `<0.02 bits`；我们现在谈的已经不是 bit 的百分之一，而是连万分之一都不到。

预训练论主张，这一切还能继续往前走：我们可以把这种表现直接与执行同一客观任务的人类相比；而人类能做到更接近[每字符 `0.7 bits`](https://gwern.net/difference#efficient-natural-languages)。
那缺失的 `>0.4` 里面装着什么？

![“是啊，但聪明又不只是懂压缩方案！”“不，就是啊！”“糟了——他知道秘密了！！”](https://gwern.net/doc/cs/algorithm/information/compression/2004-ryannorth-dinosaurcomics-391.png)

嗯——是**一切**！模型错过的一切。
在开头，胡乱喷一堆随机词就已经够用了；但到了最后，它必须能一路推理穿过那些最难的文本场景，而这些场景需要因果性或常识推理。
每一次模型把放进冷冻柜的冰淇淋预测成会“融化”而不是“冻结”，每一次模型搞不清一个人到底是活着还是死了，每一次模型选了一个并不能帮助整篇“论文”走向最终结论的词，每一次模型缺乏心智理论，以至于无法压缩那些描写十几个人在晚宴上为权力彼此算计的新颖场景，每一次模型在逻辑、抽象、指令、问答这类地方陷入迷糊，不得不用更多 bit 去遮掩本该由人类通过思考、理解与预测直接处理掉的错误——这一切都算在里面。
对语言模型而言，真理就是那个能够不断把事情预测准的东西——因为真理只有一个，而错误有很多种。
这些认知突破中的每一个，都会让少量相关文本的预测略微变得更好一点；若想达到理想预测，所需要的就只能是真正的理解。

如果我们训练出了一个损失低到 `<0.7` 的模型，它在对话中、在被问冰淇淋问题时、在做 SAT 类比题时、在接受数学辅导时，生成的文本都与你无法和人类区分；如果对每一串文本，这个模型在预测下一个字符时都和你一样好，那我们又怎么能说它并**不真正**理解一切？
（别的不说，我们按定义就可以让它取代任何需要写文本的人类工作！）

**最后那几 bit 最深。** 这里的含义是，最后那几 bit 才是最有价值的 bit，而它们恰恰要求我们通常所谓的智能中最核心的部分。
[Collobert et al 2011](https://gwern.net/doc/psychology/linguistics/2011-collobert.pdf)：

> [Shannon 1951](https://www.princeton.edu/~wbialek/rome/refs/shannon_51.pdf) 通过让人类被试猜测即将出现的字符，估计英语的[熵](https://en.wikipedia.org/wiki/Entropy_(information_theory))为每字符 `0.6–1.3 bits`……[Teahan & Cleary 1996](https://gwern.net/doc/cs/algorithm/information/compression/1996-teahan.pdf) 使用变长字符 _n_-gram 得到了低至每字符 `1.46 bits` 的熵。人类被试当然会动用他们关于语言和世界的全部知识。
>
> 我们能否利用人类被试与简单 _n_-gram 模型之间那每字符 `0.2 bit` 的差距，学出英语的语法结构与世界的本性？

这里一个有帮助的类比，也许是我们的行动：在绝大多数情况下，所有人类都同样能把行动执行得很好。
我们都会把茶杯端起来而不掉下去，也都能抬腿下几千级台阶而一次都不摔。
对于日常行动（也就是构成大部分语料的那类事情），任何智力水平的人，只要有足够练习和反馈，都能把它做得相当好：他们会分别学会一套算法，把每一类问题单独解决得很好。^[如果你看了上千张标着 “dog” 的图片和上千张标着 “cat” 的图片，你完全可以只学两个独立分类器：一个识别狗，一个识别猫，而不去理解它们共享的属性，比如“被驯化的四足哺乳捕食者”。这在别人接着让你分类 “ferret” 图片时当然帮不上忙，但那又不是你现在要解决的问题；反正如果之后真给你很多雪貂图片，你还可以再学一个专门识别雪貂的分类器。]
而对于稀有问题，实例可能少到除了把答案背下来之外，根本做不了更好的事。
光谱中间那部分，则是那些和其他问题相似、但又**没那么**相似的问题；它们正是那种会奖励灵活元学习与泛化的问题，而许多中间型问题也许是[诱发这些能力](https://arxiv.org/abs/2205.05055#deepmind)所必需的（“神经网络是懒的”）。

人与人之间真正拉开差距的时候，是他们开始撞上那条由新奇选择、稀有选择、耗时几秒却影响一生的选择，以及那些永远得不到反馈的选择（比如死后会怎样）构成的长尾。
在一个人一生数百万次离散决策中，只需要做出一次坏决定，就足以把自己送进监狱或者送进坟墓。
决策质量上哪怕只是很小的绝对平均提升，如果它恰好发生在**那类**决策上，其重要性也会远超表面数值本身；这或许能让我们直觉上理解，为什么最后那几 bit 最难、也最深。
（为什么人类大脑会这么大，而黑猩猩这类动物似乎只花很小一部分代价，就能把那么多日常活动做得一样好？为什么语言值得？也许就是因为这些考量。也许我们最像人类的时候，不是在奔跑，而是在填写寿险表格。）

**怀疑的理由。** 预训练论在逻辑上无懈可击——一个模型若不理解、只靠**瞎猜**，怎么可能解决所有可能的刁钻问题？——但它始终没能真正说服我；它像一种既无法证伪、也无法让人真正信服的论证。
它感觉太像魔术把戏了：“这里有一些信息论，这里有人类基准，这里有一种把所有任务编码成序列预测问题的方法，嘿 presto——智能来了！”
有很多算法在某种意义上是图灵完备的，或者“通用”的；也有很多像 AIXI 那样在某种理论意义上解决 AI 的算法（Schmidhuber 那帮人就很喜欢这种可爱的算法，比如“适用于所有问题的最快算法”，只不过有个小问题：其中某些常数因子要求你有一台比宇宙还大的计算机）。

为什么预训练或序列建模就不是另一种这样的东西？
当然，**如果**模型的损失低到了某个程度，那它就必定是智能的；但你怎么证明这在实践中真的会发生？
（训练 char-RNN 确实很有趣，但它们可没真正颠覆深度学习。）
它也许需要比现存总量还多得多的文本，需要数不清的 PB 数据，才能让逻辑推理之类细微因素在一堆噪声和干扰中提供足够训练信号，从而训练出模型。
或者，也许你的模型太小，只能吸收那些简单表层信号；你得把它扩大 `100` 个数量级才能起作用，因为缩放曲线根本不配合。
或者，也许你的模型从根上就是坏的，而抽象之类东西压根需要完全不同的架构才能实现；不管你怎么搞，现有模型都会在糟糕表现上饱和。
或者，它确实能训练起来，但它会把所有时间都花在提升表层建模上，吸收越来越多字面的数据和事实，却永远无法如你所愿地升到更高层次的认知平面。
或者……

> “在 `1939` 年 `3` 月我参加的一次普林斯顿大学会议上，人们讨论了制造原子武器的可能性，以及秘密进行这种工作的必要性……[Bohr](https://en.wikipedia.org/wiki/Niels_Bohr) 说，这种稀有同位素若不把整个国家变成一座巨大工厂，就不可能从普通铀中分离出来。Bohr 担心这件事做得到，从而原子弹可能会被造出来——但他希望两件事都做不成。多年以后，Bohr 来到 Los Alamos 时，我正准备说一句‘你看……’；可还没等我开口，他就先说了：**‘你看，我早就说过，不把整个国家变成一座工厂，这事就做不成。而你们恰恰就这么干了。’**”
>
> [Edward Teller](https://en.wikipedia.org/wiki/Edward_Teller)^[第 `210--211` 页，“The Quiet Enemy”，收录于 [_The Legacy of Hiroshima_](https://gwern.net/doc/radiance/1962-teller-thelegacyofhiroshima.pdf)，Teller 1962。]

但显然，这条路其实本来就走得通。
甚至 RNN 大概也行——Transformer 固然好，但它们看起来主要还是效率问题。^[换个角度看那些“Transformer 其实像 RNN”或者[其实像 Hopfield 网络](https://arxiv.org/abs/2008.02217)的论文：这更像是在说明，Transformer 重要的地方并不在于它相对旧架构拥有某种本体上的新能力，而在于某种更底层的性质，比如它们更适合在当代硬件上高效训练。]
（训练大型 RNN 的成本高得多，而在多节点上做 BPTT 也更难工程化。）
它只是需要比任何人愿意冒险投入的更多的算力与数据；直到少数真信徒终于弄到了几百万美元的算力，这件事才真正发生。

- **Q**：有人曾经**定量地**预测过，这件事会在那个时间点、以那种方式发生吗？
- **A**：据我所知，没有。

---

- **Q**：未来那些进一步缩放的模型会学到什么？

  GPT-2-1.5b 在 WebText 验证集上的交叉熵损失约为 `~3.3`（根据 [Figure 4](https://gwern.net/doc/ai/nn/transformer/gpt/2019-radford-figure4-gpt2validationloss.jpg) 中 `~10` 的困惑度，且 log~2~(`10`) = `3.32`）。GPT-3 按 [Brown et al 2020](https://gwern.net/doc/ai/nn/transformer/gpt/2020-brown-figure31-gpt3scaling.png) 的图和缩放公式，已将该损失减半到约 `~1.73`（`2.57 × (3.64 × 10^3^)^\-0.048^`）。对一个假想的 GPT-4 来说，如果缩放曲线在交叉并遇到更强的收益递减之前，还能再沿算力方向延伸 `3` 个数量级左右（`100--1000×`），那么交叉熵损失将降到 `~1.24`（`2.57 × (3.64 × (10^3^ × 10^3^))^\-0.048^`）。

  如果 GPT-3 只是从 GPT-2 的水平出发，把绝对损失降低约 `50%`，就获得了这么多元学习与世界知识，那么在 GPT-3 之上再改善约 `~30%`，会带来什么能力？（据我所知，那样的损失下降仍然还达不到人类水平。[^human-perplexity]）如果损失降到 `≤1`，也许再加上更宽的上下文窗口或递归结构，又会带来什么？
- **A**：我不知道。

---
- **Q**：那有人知道吗？
- **A**：据我所知，没有。^[截至 `2020` 年 `12` 月，也就是半年之后，几乎没有研究者愿意公开留下记录，说出他们预测未来 `1t`、`10t` 或 `100t` 模型会或不会具备哪些具体能力，以及哪些尚缺的能力会在什么规模上涌现——正如也没有人曾成功公开预测 GPT-2 或 GPT-3 的具体能力一样。]

[^human-perplexity]: 人类和 GPT-2/GPT-3 在这些绝对预测表现上到底怎么比，很难说。现有关于人类／GPT-2／GPT-3 困惑度的基准，似乎只有 WebText、[Penn Tree Bank](https://gwern.net/doc/cs/algorithm/1993-marcus.pdf)（PTB；基于 [Brown Corpus](https://en.wikipedia.org/wiki/Brown_Corpus)）、[1 Billion Word](https://arxiv.org/abs/1312.3005)（1BW）和 [LAMBADA](https://arxiv.org/abs/1606.06031)。但覆盖很零散。

    我找不到 WebText 或 Penn Tree Bank 的人类基准，所以无法比较人类与 GPT-2/GPT-3 的困惑度（[GPT-2 PTB](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#page=5)：`35.7`；[GPT-3 PTB](https://arxiv.org/pdf/2005.14165.pdf#page=11&org=openai)：`20.5`）。

    [GPT-2](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#page=5) 在 1 Billion Word（1BW）基准上的困惑度是 `43`，而[人类困惑度](https://gwern.net/doc/ai/scaling/2017-shen.pdf)（高度外推得来）是 `12`（有趣的是，该文基于 `2012` 年的 LSTM RNN 外推出“距离达到人类表现还需要 `10` 到 `20` 年研究”），但这也许不是一个公平的基准（“我们的模型在 One Billion Word Benchmark 上仍明显逊于先前工作（[Chelba et al 2013](#chelba-et-al-2013)）。这很可能是因为它既是最大的数据集，又带有一些破坏性最强的预处理——1BW 在句子层面的打乱移除了所有长程结构。”），而且 1BW 也因数据污染而被移出了 GPT-3 的评测（“我们省略了该工作中 `4` 个与 Wikipedia 相关的任务，因为它们完全包含在我们的训练数据中；我们也省略了 one-billion word benchmark，因为其数据集有很大一部分包含在我们的训练集中。”）。

    LAMBADA 的基准结果是：[GPT-2 困惑度](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf#page=5) `8.6`，而 [GPT-3 困惑度](https://arxiv.org/pdf/2005.14165.pdf&org=openai#page=12)为 `3.0`（zero-shot）／`1.92`（few-shot）。[OA 声称](#gpt-2-blog)在他们关于 GPT-2 的博文里（但不在论文里）人类困惑度是 `1--2`，但他们没有给出来源，我也找不到。（作者们也许是在根据 LAMBADA 的构造方式做猜测：样本会被筛选，标准是两个独立人类标注者都给出同一个正确答案，而这就给出了人类预测该答案能力的下界。）

    总体来看，最佳猜测似乎是：GPT-3 目前的绝对误差大约仍是人类的两倍。这意味着，要靠现有缩放定律把剩余差距完全补上，需要相当大量（但远非不可能）的算力。如果我们不负责任地把 WebText 的缩放曲线继续外推，假设 GPT-3 在当前 `1.73` 的 WebText 困惑度下，其误差是人类的两倍（因此人类约为 `~0.86`），那么我们需要满足 `2.57 · (3.64 · (10^3^ · _x_))^\-0.048^ = 0.86`，其中 _x_ = `2.2e6`，也就是 GPT-3 算力的 `2,200,000×`。（这大致相当于美国入侵伊拉克的成本。）

    那什么时候才做得到呢？

    如果我们设想 [peak AI compute usage doubles every 3.4 months](#amodei-et-al-2018)，那么 `2.2e6` 相当于还要再翻 `22` 次——也就是 `6.3` 年，到 `2027` 年。大多数人都相信这条算力趋势很快就会断掉，而这类预测恰恰很好地说明了为什么！

    反过来看，[Hernandez & Brown 2020's](#hernandez-brown-2020-paper) 的估计是，扣除硬件与算法进步后，要达到某一固定性能水平的成本每 `16` 个月减半；所以如果 GPT-3 在 `2020` 年初的成本约为 `~$5m`（`2020` 年币值），那么到 `2021` 年中就会降到 `$2.5m`（`2020` 年币值），如此类推。同样地，一个达到 “GPT-human” 水平、需要 `2.2e6×` GPT-3 算力的系统，在 `2020` 年的成本大概会是 `$10`（`2020` 年币值）万亿美元量级，但在经历 `14` 次减半（`18` 年）后，到 `2038` 年就会降到 `$1b`（`2020` 年币值）。
# 前景

> 在解码问题中，我们所能拥有的最重要信息，就是知道自己正在读取的消息并非胡言乱语……类似地，当我们考虑原子反应、原子炸药这类自然问题时，我们能够公开的最大一条信息，就是它们**存在**。一旦科学家着手攻克一个他知道有答案的问题，他的整个心态都会改变。他其实已经走完了通往答案道路的大约 `50%`……**关于原子弹，本来有一个秘密是有可能保住的，但却毫无保留地泄露给了公众和所有潜在敌人，那就是它在建造上是可能的。** 给科学界一个如此重要的问题，并让他们确信它有答案；那么科学家的智力能力和现有实验设施的分布是如此广泛，以至于这个任务在世界任何地方被半独立地实现，都不过只是几年的事。
>
> [Norbert Wiener](https://en.wikipedia.org/wiki/Norbert_Wiener)，第 `124--125` 页，_[The Human Use of Human Beings](https://en.wikipedia.org/wiki/The_Human_Use_of_Human_Beings)_（着重为原文所有）

> 从事机器学习工作的人，根本不相信神经网络能做多少事。人们不相信大型神经网络可以被训练出来……想法其实一直都在，缺少的是海量监督数据和海量算力。一旦你有了[这两样东西]，还需要第三样东西——那就是**信念**。相信如果你把那些已经存在的合适材料，和大量数据、大量算力一起应用并混合起来，它**真的**会奏效。而这就是那块缺失的拼图。
>
> [Ilya Sutskever](https://www.youtube.com/watch?v=13CZPWmke6A&t=950#openai)[^Zaremba]

[^Zaremba]: 另见 [Sutskever 的 DRL 演讲](https://www.youtube.com/watch?v=w3ues-NayAs?t=712#openai)，以及 [Wojciech Zaremba](https://en.wikipedia.org/wiki/Wojciech_Zaremba) 关于 [OA5 的评论](https://www.youtube.com/watch?v=429QC4Yl-mA&t=1157s)（[文字稿](https://wandb.ai/wandb_fc/gradient-dissent/reports/What-could-make-AI-conscious-with-Wojciech-Zaremba-co-founder-of-OpenAI--Vmlldzo3NDk3MDI)）：

    >
    > - - **Lukas Biewald**：你觉得当时做 DoTA2 的那些工作，有多少是在根本性地推动机器学习向前走，又有多少是 DoTA 特有的问题？或者说，这两者甚至能分开吗？
    >   - **Wojciech Zaremba**：我觉得其中确实有相当一部分是 DoTA 特有的工作。同时，我也觉得它既比最优方案更重，却又同样很难。所以我记得在 DoTA 项目刚开始的时候，其实大家并不清楚该怎么着手。
    >
    >     当时很多人都说，现代强化学习根本不可能解决这个问题。于是大家去研究 off-policy、on-policy、[evolutionary strategies](https://arxiv.org/abs/1703.03864#openai)。真正让人吃惊的是，那些[早就存在的方法](https://arxiv.org/abs/1707.06347#openai)，在合适的规模下居然效果非常好。所以这是一个巨大的惊喜。我还记得在 OpenAI 做 DoTA 之前，就有人说也许强化学习已经走到死路了。可突然之间，现在的故事已经完全不一样了。
    >   - **L Biewald**：确实。
    >

我们能对未来的深度学习工作期待什么？
GPT-3 会不会引发一场军备竞赛，以至于很快我们就会若无其事地讨论一些如今看来荒诞到离谱的方案：例如一个规模扩大 `100×`、训练数据扩大 `100×`（视频／文本／以图像形式表示的 PDF／照片／机器人数据）的双向多模态 Transformer，再加上补充性的监督学习，作为一个类似 MuZero 的“学习 + 规划”型 DRL 智能体的骨干，并让它同时在成千上万个任务（比如编程）上运行？
[大体上，会。——编者，`2025-10-19`]

[硬件过剩](https://www.lesswrong.com/posts/N6vZEnCn6A95Xn39p/are-we-in-an-ai-overhang)的存在意味着，这里的限制因素与其说是硬件，不如说是人：会不会有哪个组织把 GPT-3 当成自己的“斯普特尼克时刻”，从而激进地投入缩放项目？
DeepMind 或 Google Brain 的 TPU pod 里，现在是不是正悄悄酝酿着一个等价于 GPT-4 的东西？
他们并不蠢，他们有硬件，有预算，也有人。

但我认为，他们缺的是一种愿景。
据我所见，他们根本没有这种东西，因为 Google Brain 和 DeepMind 并不像 OA 的 Sutskever、Amodei 等人那样相信缩放假说。
你只要翻翻机器学习圈的 Twitter，就能看到他们对缩放假说的轻蔑。
（GPT-3 发布已经过去四分之一个年头，还在继续；你能说出哪怕一个和 `17b` 的 Turing-NLG 一样大的 dense 模型吗——更别说比 GPT-3 更大的了？）

Google Brain 过于务实，也过于关注短期，不会去碰这种玄而又玄、又昂贵的投机，尽管 Quoc V. Le 的团队偶尔会让你惊讶一下。
他们会摆弄像 [GShard](https://arxiv.org/abs/2006.16668#google) 这样的[混合专家模型](https://gwern.net/doc/ai/scaling/mixture-of-experts/index)，但主要还是因为他们觉得那类东西很可能可以部署到 Google Translate 的生产环境里。^[生产服务，尤其是**免费**生产服务，通常都远远落后于最前沿实验室内部尚未发表的 SOTA。而对预测 AI 进展或 AI 风险来说，后者才是唯一真正重要的东西；但人们总喜欢用一些古怪指标来衡量 AI 进展，比如某个任意的免费服务去年能做到什么。经验法则是：如果你在用一个无需登录的免费服务，它的质量通常至少落后于 SOTA `2` 年；需要登录的免费服务，落后 `>1.5` 年；付费服务，落后 `>1` 年；而刚发布的研究论文，也往往落后 `>6` 个月。]

[Why didn't DeepMind do GPT-3?](https://rootnodes.substack.com/p/why-didnt-deepmind-build-gpt3)
DeepMind^[特别是 Demis Hassabis；至于 Shane Legg 的当前看法，我并不确定，不过考虑到他在创办 DeepMind 时做出的 2009 年预测的准确性，以及他在 2018 年的评论，他大概并没有太改变自己“AI 将由已经实现的指数级算力增长所赋能”的看法，也没有太改变他那个约 `2028` 年实现 AGI 的预测。（这也与最新的 Metaculus 预测一致。）] 所持有的，可以说是一种“弱缩放假说”：他们认为，AGI 需要我们“找到正确的算法”，相当于逐模块复制哺乳动物大脑；而这些模块虽然按当代标准看会极其庞大、极其昂贵（这也正是算力重要的原因——它能给我们“一种更强有力的工具，去寻找正确的算法”），但它们仍然需要被一块一块地发明出来、微调出来，在最终组装完成之前，几乎不会有太多风险或惊喜。
不过，每一块本身依然可以缩放：并不存在什么神奇的智能腺体，也不存在什么量子玄学，能在人类与例如黑猩猩或啮齿动物之间划出一条鲜明界线。
（尽管我们人类总是极尽夸张地欣赏自己那些像语言、逻辑之类的能力，但这些其实只是大脑基本能力之上的一些小修饰——每种生物都在解决同样的基本问题，比如探索、长期记忆、学习世界模型、把奖励与具体行动联系起来、元学习，等等。）
因此，一旦你有了鼠类水平的 AGI，那么人类水平的 AGI 也就只是“更多一些”而已。
（而且拿大鼠做实验可容易多了。）
这就是为什么 DM 会搞出像 [Agent57](https://deepmind.google/discover/blog/agent57-outperforming-the-human-atari-benchmark/) 这种把整个厨房都往墙上砸、看看什么会粘住的装置；也正因如此，他们才会如此强调神经科学，把它当作逆向工程大脑时的灵感来源与交叉授粉对象。
（另见 Sam Altman 在[播客访谈](https://gwern.net/doc/ai/nn/transformer/gpt/3/2020-10-06-exponentialview-samaltman-152648-s5e01-howgpt3isshapingouraifuture.mp3#t=2205)中关于 OA 相对那些算力更多但未点名竞争者的优势所作的评论：正因为缺算力，他们才会保持“小而聚焦”——“当然”像一家创业公司那样。）
当有人似乎想出了一个可以扩展、足以破解某个难题的架构，比如 AlphaZero 或 AlphaStar，他们就愿意猛踩油门把它做大；但除此之外，他们的计划就是在 ALE 上做渐进式改良，然后再推进到 [DMLab-30](https://arxiv.org/abs/1612.03801#deepmind)。
他们十年来一直在一口一口啃大脑的各个部分；如果一切顺利，大概还要再稳稳地啃上十年甚至二十年。
因为他们锁住了太多人才，又掌握了太多专有代码，并且相信这一切都是阻止竞争对手复制这个复杂大脑的巨大护城河，所以他们显得相当从容。
你不会看到 DM 在某个登月计划上“押上公司”；Google 的现金流不会凭空消失（而且还有 [DM 的预算](https://gwern.net/newsletter/2020/06#deepmind-budget)），而慢就是稳，稳就是赢。

再往外看，像 Tesla 或 FAIR 这样的其他大多数研究实验室，要么无关紧要，要么根本没兴趣。
中国 AI 公司则是个问号：隔着语言障碍，我似乎能隐约看到他们对 AGI 的兴趣，以及不像西方那样本能反对；像百度这样的公司也偶尔会放出重要研究（例如早期的缩放论文 [Hestness et al 2017](https://arxiv.org/abs/1712.00409#baidu)），但总体而言，中国 AI 可能被高估了，而且他们似乎患上了一种“荷兰病”——用于监控技术以及狭窄电商细分市场的资金太过充裕，以至于其他方向反而被忽视。

OA 没有像 DM 那样来自 Google 的长期资金，也没有那样庞大的人头数；它正在押一个类似创业公司的赌注：它知道一个重要而又秘密的真相——“缩放假说是真的！”
于是，像 PPO 这样的简单 DRL 算法叠在 RNN 或 Transformer 这种大型简单架构之上，就可能涌现出来，利用缩放的福祉，并通过元学习一路获得强大能力，再反过来带来更多资金，用于更多算力与进一步缩放，形成一个良性循环。
这就是为什么 OA 不得不修改它的公司形式：既没有巨额捐赠基金，也没有像 Google 那样钱包深不见底的赞助人，它从哪里拿钱去做缩放（或者雇那些年薪动辄数百万的机器学习工程师／研究员）？
OA 必须**自己赚**到这些必要的钱，所以就像 Mozilla Foundation 拥有 Mozilla Corporation（靠卖 Firefox 搜索引擎默认位赚钱），或者 Hershey 孤儿院拥有 Hershey Chocolate，或者女童子军把她们的饼干做成授权商品一样，OpenAI 从一个纯靠捐赠资助的非营利组织，变成了一个拥有营利性子公司／创业公司的非营利组织——“OpenAI LP”；后者可以接受投资，也可以开展营利活动。
在 OA 的控制之下，OA LP 就能去射月亮。
而如果 OA 错在相信了[图上直线之神](https://slatestarcodex.com/2018/11/26/is-science-slowing-down-2/)，那他们反正也不可能用 DM 偏好的路线去正面打赢 DM，终归只会成为一个陪跑的脚注，所以他们也没什么可后悔的。

尽管所有这些理论上都可以被竞争对手**相对**容易地复制（千万别低估调参和“秘制调料”会有多少）——只要他们真想做的话（毕竟，所需算力预算跟 Big Science 或 AlphaGo、AlphaStar、Waymo 这类投资相比，仍然微不足道）——但这些竞争对手缺少最最重要、也是再多钱或 GPU 都治不好的东西：对自己信念的勇气。
他们过于因循守旧，也在哲学上错得太深，以至于永远不会承认错误、不会尝试反超 OA，直到一切为时已晚。
当美国军方[甚至都不允许自己的开发者使用 Tensorflow 或 PyTorch](https://warontherocks.com/2020/10/trust-algorithms-the-army-doesnt-even-trust-its-own-ai-developers/) 时，或者当政府项目都笼罩在新冠疫情阴影下时，我们又怎么能严肃地谈什么军事版“曼哈顿计划”？
这听起来也许荒唐（按理说，Bitter Lesson／缩放假说现在已经累积了足够高的先验概率，理应被认真看待，并得到重大研究投入，以测试它到底能走多远，尤其是其后果如此重要），但你看看 OA **每一次**发布一个新的缩放假说例子时，外界是怎么反复批评它的：从 GPT-1 到 Dactyl，到 OA5，到 GPT-2，到 iGPT，再到 GPT-3……
借用圣奥古斯丁的话来说，大多数人对 Bitter Lesson 或缩放假说的反应都是：“请赐我缩放与算力——但别是现在。”^[当人们面临这样一个选择：是承认自己那些花哨的辛苦工作其实是死路一条，吞下 Bitter Lesson，然后开始为几千万美元的算力做预算；还是发一条轻蔑的推文，解释说“**其实**，GPT-3 说明缩放已经走进死胡同，它是环境灾难，而且无非只是模仿式智能”——大多数人都会赶紧去发推。]

一个关键指标将是，除了“老面孔”之外的组织是否也开始加入（Microsoft 的 [ZeRO-2](https://www.microsoft.com/en-us/research/blog/zero-2-deepspeed-shattering-barriers-of-deep-learning-speed-scale/) 团队已经做到了 [`1t` 规模训练](https://www.microsoft.com/en-us/research/blog/deepspeed-extreme-scale-model-training-for-everyone/)，此外还有 Nvidia、Salesforce、Allen、Google DM/GB、Connor/EleutherAI、Facebook FAIR），还是他们会继续否定缩放。
至少截至 `2020-10-26`，也就是 `152` 天之后，还没有任何模型接近 GPT-3；事实上，甚至没有任何模型超过 Turing-NLG 的 `17b`。^[像 GShard 这种混合专家模型，或者像 DynamicEmbedding 这样的嵌入，并不能和 GPT-3 这种“dense”模型相提并论，因为从某种意义上说，训练出带有数十亿“参数”的模型一直都很便宜、也很容易，比如超大的嵌入；但这些参数能做的事很少，更像是几百个浅层模型前后粘在一起。它们大概学不到 dense 模型在同等名义参数量下能学到的那些有趣东西。]
# 批评批评者

**持续追踪。** `2020` 年的 GPT-3，和任何例子一样，都很适合让我们回头看看过去十年。
回想起来很惊人：一个因为这些新的 “ResNets” 而兴奋得去读 PhD 的人，到现在甚至都可能还没毕业——连 ResNet 都还这么新，更别说 Transformer 了，而进展的速度就是这么快。
在 `2010` 年，全球所有真正相信深度学习的人，轻轻松松就能塞进一个中等大小的会议室里（这还得略微感谢一下，其中有 `3` 个人当时正忙着创办 [DeepMind](https://en.wikipedia.org/wiki/DeepMind)）。
`2010` 年时，一个对机器学习感兴趣的人**也许**读到过一些有意思的东西：比如那些古怪而顽固的连接主义死忠，用区区 `1--2` 百万参数识别手写数字；或者在标准语音识别隐马尔可夫模型上做一些不太起眼的神经网络改动。
在 `2010` 年，谁能预测接下来的 `10` 年里，深度学习会经历一场寒武纪大爆发，导致整个机器学习领域里的替代路线大规模灭绝；模型会扩展到 `175,000` 百万个参数；而这些巨型模型竟会自发地发展出所有这些能力？

没有人。也就是说，除了少数几个被 AI 圈（更不用说整个世界）当成故意自我欺骗的老派狂热分子的顽固连接主义者之外，没有人，比如 [Moravec](https://jetpress.org/volume1/moravec.htm)、Schmidhuber、[Sutskever](https://www.youtube.com/watch?v=13CZPWmke6A)、Legg 和 Amodei。

回头看时最令人震惊的一点，是意识到：如果你听对了人，那么这一切其实既不意外，也并不难预测。
`22` 年前，也就是 `1998` 年，Moravec 就指出，AI 研究可能具有欺骗性，而硬件限制意味着“智能机器研究在它最初的 `50` 年里并没有稳定进步，其中有 `30` 年只是在原地踏步！”，并预测，随着摩尔定律继续推进，“接下来的 `50` 年会比过去 `50` 年快得多。”
Moravec 进一步指出，快速进展的一部分原因在于硬件过剩：在连接主义革命开始很久之前，具备所需算力的超级计算机就已经存在了，但没人会被允许去用它们[^Jim-Gray]，因为它们都要被拿去做“更重要”的（也更有声望的）硬核 STEM 工作，比如“物理模拟”（也就是气候模拟和核弹）。^[令人惊讶的是，截至 `2020` 年，这**仍然**是真的：例如，我所见到的在 [Summit](https://en.wikipedia.org/wiki/Summit_(supercomputer)) 上完成的深度学习研究，只有[材料](https://arxiv.org/abs/1909.11150)、[科学](https://arxiv.org/abs/2005.00223)和[生物](https://arxiv.org/abs/2007.06225)。 （我在重新核查 Arxiv 时，确实发现了一篇使用 Summit 资源的非 STEM 论文：[Lin et al 2019](https://arxiv.org/abs/1910.00932#google)，关注的是训练视频分类模型时的系统工程问题。）] 而且“AI 研究必须等到算力变得更便宜时才能开始。”
所谓便宜，指的是大约 `~$1,000`（`1998` 年币值）的一台工作站；而便宜到足以匹敌人类的算力，会在 `2020s` 某个时候到来，`2010s` 则会出现廉价的蜥蜴到老鼠级系统。
结果也确实如此：深度学习革命通常被追溯到 `2012` 年的 [AlexNet](https://en.wikipedia.org/wiki/AlexNet)，那是一个研究生用 `2` 块 GTX 580 3GB GPU 做出来的[^Norvig]（上市标价大概是 `$500`（`2010` 年币值），整机成本也许是 `$1,500`（`2012` 年币值））。
`2020` 年，GPT-3 如期而至；而且如前所述，除了人们为 `2020s` 预测的大幅硬件算力增长之外，尽管摩尔定律整体上正在减速，我们仍有很多理由期待成本继续下降。^[[Jeff Dean](https://arxiv.org/abs/1911.05289#google) 指出：“也许有点不幸的是，就在我们终于开始拥有足够的计算性能去处理有趣的真实世界问题、而机器学习规模与适用性的大幅提升又带来了对额外计算资源的强烈渴求、以处理更大问题的时候，整个计算产业却经历了通用 CPU 性能同比提升的大幅放缓。” 在计算观下，这并非巧合：关键因素是算力，而不是算法；生物系统在许多任务上往往距离理论最优只有几个数量级，甚至更近；而越接近最优，进展就越慢；因此，就在人工计算终于开始做“有趣的真实世界问题”之时，它也必然正在逼近自己的极限。（当然，本来也可能不是这样：摩尔定律可能在距离生物效率差很多个数量级时就停下，也可能远远超过它很多个数量级，而 AI 又是由于别的原因才发生。）]

[^Jim-Gray]: 这看起来是很多评论者的一个盲点：他们默认只要必要资源**存在**，它就一定会被**使用**。例如，Jim Gray（卒于 `2007` 年）在 `1999` 年 `6` 月就[略带调侃地](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/ms_tr_99_50_turingtalk.pdf#page=11)谈到 Turing 的连接主义硬件论证，并指出（采用了一个对人脑算力的乐观下界估计）：

    > 台式机理应已经和蜘蛛或青蛙一样聪明，而超级计算机则理应正在逼近人类智能……所以，我们应该随时都能在这些超级计算机里看到智能了（开玩笑的）……[但我们没有看到，是因为] 我们还缺少某种**极其**根本性的东西。显然，我们为超级计算机准备的软件和数据库，根本不在未来十年通过图灵测试的轨道上。我们需要的是某种完全不同的东西。我们需要跳出框架的、激进的思考。
    >
    > 我们面前已经摆着一个谜题：基因组和大脑确实在起作用。但我们完全不知道答案是什么。理解这个答案，是一个极好的长期研究目标。

    借助事后之明，我们可以说：`1999` 年的超级计算机本来确实可能已经展现出远比实际更多的智能水平；同时，`1999` 年那些跑在超级计算机上的软件，也确实永远不可能导向有意义的 AI 进展；这两点之间并不存在什么特殊矛盾或神秘之处——只是因为根本没有人在尝试。没有哪个超级计算机的拥有者会允许它被一连占用好几年，只为完成那些细小却关键的迭代，让 RNN 或 CNN 这样的连接主义方法真正跑通。因此，某种完全不同、也确实激进的东西当然是需要的——但我们其实早就知道那个解法长什么样。
[^Norvig]: [Peter Norvig](https://en.wikipedia.org/wiki/Peter_Norvig) [举了一个例子](https://wandb.ai/wandb_fc/gradient-dissent/reports/Peter-Norvig-Google-s-Director-of-Research-Singularity-is-in-the-eye-of-the-beholder--Vmlldzo2MTYwNjk?galleryTag=gradient-dissent)，说明当研究生**买不起**让神经网络奏效所需的算力时，会发生什么：

    > **[Lukas Biewald](https://en.wikipedia.org/wiki/Lukas_Biewald)**：当你回头看深度学习时，会觉得它好像是突然出现的，但其实很多技术在你那本书里很早就已经有了。你觉得这个领域当时是漏掉了什么，还是说，仅仅是因为算力还不够，没法在足够大的规模上运行这些神经网络技术，从而让它们显示出比人们预期更好的效果？
    >
    > **Peter Norvig**：是的。我的意思是，如果你说“突然”，那就是：Hinton 已经折腾了 `30` 年计算机视觉和 image net 这件事，然后它突然就成了。可一旦成了，最大的差别我认为就是算力。当然，数据方面也有进步。所以我们才有了 [ImageNet](https://en.wikipedia.org/wiki/ImageNet)，因为 [Fei-Fei Li](https://en.wikipedia.org/wiki/Fei-Fei_Li) 等人收集了那个大型数据集，这非常重要。算法上当然也有一些差别，对吧？我们有了一个稍微不同的 [squashing function](https://en.wikipedia.org/wiki/Activation_function)。以前形状像这样 \\[[sigmoid](https://en.wikipedia.org/wiki/Sigmoid_function)\\]，现在形状像这样 \\[[ReLU](https://en.wikipedia.org/wiki/ReLU)\\]。我的意思是，我也不知道那到底有多重要，但我们确实学会了把 [stochastic gradient descent](https://en.wikipedia.org/wiki/stochastic_gradient_descent) 做得更好一点。我们也发现 [dropout](https://en.wikipedia.org/wiki/Dilution_(neural_networks)) 能给你带来更好的鲁棒性。
    >
    > 所以有一些小改进，但我想最大的一点大概还是算力。而且我清楚记得，`1981` 年左右，我还是伯克利研究生的时候，[Geoff Hinton](https://en.wikipedia.org/wiki/Geoff_Hinton) 来做过一个关于这些神经网络的报告。我们这些研究生同伴都觉得太酷了。于是我们说，‘走，回实验室把它实现出来。’
    >
    > 当然，那时候根本没有任何东西可以下载，所以我们得从零开始自己搭一切。我们先让它学会了 exclusive or \\[[XOR](https://en.wikipedia.org/wiki/XOR)\\]，然后又让它学会了一点稍微更复杂的东西。当时特别激动。接着我们把第一个真正的问题扔给它，它跑了一夜，还没收敛；我们又让它再跑一天，还是没收敛。于是我们就放弃了，重新回到那种基于知识的系统路线。但如果当时有今天的算力，它大概 `5` 秒钟就会收敛。

    按我的估算，Norvig 那次尝试所用的算力，相当于当代 GPU 时间的 `0.8` **毫秒**。

    （在 `~1981` 年，一台昂贵的 PC——折合相当于 `>$5,000`（`2020` 年币值）——可能会被一个强力 AI 实验室按每个研究生 `1` 台的标准分配；它还可能带有一个额外的 [Intel 8087](https://en.wikipedia.org/wiki/Intel_8087) 浮点 [coprocessor](https://en.wikipedia.org/wiki/coprocessor)，性能为 `50,000` FP64 FLOPS。保守地假设“跑一夜”加“再跑一天”不超过 `2` 天，那么 Norvig 的实验总共用了 `2d × 24h × 60m × 60s × 50,000 = 8×10^9^` FLOPS；而一块 `2020` 年、标价约 `~$10,000`（`2020` 年币值）的 Nvidia [A100](https://en.wikipedia.org/wiki/Ampere_(microarchitecture)) GPU，标称性能是 `9.7` FP64 TFLOPS，也就是 `9,700,000,000,000` FLOPS（而且在更有用的低精度模式如 FP32 下还要高得多，只不过 `1981` 年的机器学习并不知道这一点）；因此，`8×10^9^ / 9.7×10^12^ = 8×10^−4^` 秒，也就是 `0.8` 毫秒。）

过去 `10` 年不断加速的节奏，足以把任何人从教条的昏睡中惊醒，让他一下子坐直身子。
事实证明，这是 Hans Moravec 的世界，而我们其余人不过一直住在一个愚人的天堂里。
而 Moravec 的预测还剩 `28` 年……

很多人不只是没有抗拒，反而乐在其中的一种诱惑，就是陷入一种**职业性偏见**（déformation professionnelle），把任何模型都斥为“只不过”是这个或那个（“只不过是几十亿条 IF 语句”，或者“只不过是一堆乘法”，或者“只不过是几百万个被记住的网页”），只见树木，不见森林。Moravec 在评论棋类引擎时就谈过这一点：

> 这件事之所以值得注意，有很多原因，但其中有一点在这里尤其相关。在两场比赛期间，Kasparov 曾多次报告说，他在机器里看到了“心智”的迹象。在第二次比赛中，有时候他甚至担心幕后可能有真人在给 Deep Blue 输送战略洞见！……对于其他所有棋类计算机，他都能感受到一种机械式的可预测性，那来自它们毫无分辨力却有限的前瞻，以及对长期战略的缺失。而在 Deep Blue 身上，让他惊愕的是，他看到的却是一种“外星智能”。
>
> ……Deep Blue 的创造者们对它相较其他棋类机器的**量的**优势了如指掌，但他们缺乏棋艺上的理解，无法像 Kasparov 那样深刻欣赏它在下法**质地**上的差异。我认为，这种二分会在未来几年越来越频繁地出现。那些最了解高级机器人机制的工程师，将会是最后才承认它们拥有真正心智的人。从内部看，机器人无可争议地只是机器，依照机械原理行动，不管这些原理有多少层叠加；只有从外部把它们作为一个整体来欣赏时，智能的印象才会浮现。人脑也是如此：在神经生物学家的显微镜下，它并不会呈现出它在一场活跃对话中所展现的那种智能。

但当然，如果我们终有一天在 AI 上成功了，或者更一般地说，在还原论上成功了，那**必然是通过把 Y 还原为“只不过是 X”来实现的。**
证明某个需要智能的任务，可以由一个定义明确、并不包含“智能”的算法解决，这恰恰就是成功应有的样子！
（否则，你不过是把问题彻底偷换了，并把难题推到别处而已；计算机芯片是由晶体管构成的，不是什么特别微小的侏儒小人。）

> 只要 AI [OA5] 能探索，它就会在足够时间下学会……我们一直在等奇迹耗尽。我们一直在等撞墙，而我们似乎始终没有撞上墙。
>
> [Greg Brockman](https://qz.com/1311732/openai-built-gaming-bots-that-can-work-as-a-team-with-inhuman-precision)

> 给它算力，给它数据，它就会做出惊人的事情。这玩意简直就像——就像**炼金术！**
>
> [Ilya Sutskever](https://www.newyorker.com/magazine/2019/10/14/can-a-machine-learn-to-write-for-the-new-yorker)，`2019` 年夏

**事后看什么都一清二楚。** 就在 `2015` 年，[所有专家](https://news.ycombinator.com/item?id=9109140)还向我们保证，AGI 和缩放假说看起来都极其可疑：毕竟，总得先有某种能被缩放的东西；而且人们太容易盯着现有系统的缺陷，然后想象这些缺陷永远不会消失，进展随时都会在下个月左右进入 S 型平台期。
这有点像基因组革命：少数目光长远的预言者外推出 GWAS 所需的 _n_ 会指数增长，并很快带来强大的 PGS；而持重的专家们则对“失踪的遗传力”和生物学的神奇复杂性忧心忡忡，并嘲笑说，这样的 _n_ 要求本身就说明 GWAS 是个失败范式。结果，未来一开始来得很慢，随后却来得极快。
然而现在我们已经站在这里：向那些狂热分子致敬，让批评者感到羞愧与难堪吧！^[现在 GPT-3 的 few-shot 和 [T5 finetuning](https://arxiv.org/abs/2003.08380#google) 已经开始让 Gary Marcus 这样的人对 WinoGrande 略微感到不安，于是他们已经[开始准备](https://arxiv.org/abs/2004.13831)[各种借口](https://arxiv.org/abs/2201.02387)，解释为什么 Winograd schema [其实并**不算**](https://gwern.net/modus) 衡量常识推理／智能的好标准（因为所谓智能，当然就是 AI 还做不到的任何东西）。]
要是能回到 `10` 年前，哪怕只是 `5` 年前，去看看每个 AI 研究者读到这篇论文时脑袋爆炸的样子就好了……
可惜现在似乎也没见多少脑袋真的在爆炸，因为人类事后诸葛亮和找借口的能力是无穷无尽的（“那点效果我微调也能做出来，反正我本来就预测到了，多无聊”）；而且很不幸，[“没有火警铃”](https://intelligence.org/2017/10/13/fire-alarm/) 能为 AGI 拉响。
（如果你到现在还**确信**未来几十年 AGI 的概率几乎为零，那是为什么？
你有过——白纸黑字地——预测 GPT-3 这样的能力吗？
这真的是你所预期的、AI 失败前几十年的样子吗？
什么样的具体任务、什么样的具体数字，才会改变你的想法？
如果这些粗糙的、原型级、昆虫脑大小的深度学习系统并不走在成功道路上，那么这个世界与现在相比会有什么不同？）

**有权威，无问责。** 我们该如何看待专家？
对失败的预测，是由显赫、体面、严肃的人作出的。
他们以审慎的口吻谈论 AI 炒作为何过度、为何可能引发一次“AI 寒冬”，以及流行路线的根本缺陷，和为什么蛮力不可能奏效。
这些话在 `2014`、`2015`、`2016`……被反复说出。而他们错了。
据我所知，很少有人真正做出 **mea culpa**，或者认真反思过这件事。[^Feynman]
这是一个令人费解的失败，而我[以前也思考过](https://gwern.net/newsletter/2019/13#what-progress)它。

[^Feynman]: [Feynman](https://www.nasa.gov/history/rogersrep/v2appf.htm)：“文中多次提到先前的飞行；这些飞行被接受并取得成功，于是被当作安全性的证据。但侵蚀和泄漏并不是设计所预期的。它们是在警告某种东西出了问题。设备并没有按预期运行，因此存在一种危险：它可能以更大幅度偏离、以一种出人意料且尚未彻底理解的方式运行。这个危险之前没有导致灾难，并不能保证下一次也不会，除非我们已经完全理解了它。”

    这不禁让人想到中国皇帝以及 [Shaka Zulu](https://en.wikipedia.org/wiki/Shaka_Zulu) 对西方技术的灾难性轻蔑：他们的错误，不在于把那项技术视为现实中并不重要（它或许确实如此），也不在于没意识到自己在几千年来最重要的一场地缘政治变迁中已经落后了几个世纪，而在于没有承认自己根本解释不了为什么西方技术会如此快地变得如此强，因此也就无法知道它会不会继续变得更强。

**只做姿态，不做预测。** 然而，所有那些自以为见识高明的人说话时，都带着一种特定的声调；这种声音无论他们对还是错，听起来都一模一样。这种语气也出现在今年 `1` 月到 `3` 月的许多言论里；我们甚至还能在 `1940` 年《Scientific American》上一篇权威地命名为 ["Don't Worry---It Can't Happen"](https://gwern.net/doc/existential-risk/1940-sciam-harrington-nuclearweapons-dontworryitcanthappen.pdf) 的文章中听到它，那篇文章建议读者不必再担心这件事了，“回去睡觉吧”。
（那件事是原子弹；当时某些科学家已经停止公开谈论它，从而引起公众忧虑。可它不仅有可能发生，英国的原子弹项目当时其实已经启动了，而 `5` 年后，它确实发生了。）

**官僚制铁律：大教堂哥特式。** 这种语气，就是[权威](https://srconstantin.wordpress.com/2016/10/20/ra/)的声音。 \
权威的声音坚持让人保持冷静，不要“恐慌”（那是头号原罪）。 \
权威的声音向你保证，它不会发生（因为它不可能发生）。 \
权威的声音会抛出一些简单论证，解释为什么现状会继续维持，并且只考虑那种狂野新想法可能如何失败（却不考虑它所有可能成功的路径）。 \
这种声音不属于不确定性，也不处理不确定性；事情要么会发生，要么不会发生，而既然它不会发生，那就没有必要采取任何预防措施（你也不该担心，因为它不可能发生）。 \
这种声音不相信在图上画线（那是赤裸裸的数字神秘学）。 \
这种声音不会给出任何数值化预测（因为那样就可能被证伪）。 \
这种声音不会分享它的源代码（理由很复杂，复杂到无法向外行解释）。 \
这种声音反对诸如在志愿者身上进行随机实验这类不道德的事情（但会忽略其中的冒犯）。 \
这种声音没有一个关于未来的模型（因为一旦有模型，就意味着它并不是真的已经知道未来）。 \
这种声音非常在意自己的公众形象（以及其他同样发出这种声音的人对它说的不友善闲话）。 \
这种声音永远庄重、体面、资历光鲜（它会很高兴为你的国家级杂志和／或报纸写一篇专栏）。 \
这种声音只负责发声，而不接受别人对它发问（你不能问它：什么客观事实会让它改变想法）。 \
这种声音从不改变想法（直到它改变）。 \
这种声音从不对世界上的事件感到惊讶（它只会感到失望）。 \
这种声音建议你现在就回去睡觉。

当一个人谈论未来的可能性时，他声音里的语气究竟是什么样的？
# 附录
## 万物生于字节

> 像 GPT-3 这样强大的生成模型，会学会模仿智能体，并因此在被适当提示时变成智能体。这是在海量人类生成数据上训练的必然结果。而这可能是个问题。
>
> 人类数据（或者像 DRL 智能体这样的道德等价物）是否**必不可少**？而其他类型的数据，比如物理数据，是否就不存在这个问题？（于是，一种通过过滤数据来减少或消除隐藏智能体性的安全策略，是否可行？）
>
> 我的论点是否定的：智能体性并不是离散的，也不是什么非物质之物，而只是能力的一个普通连续谱；它在许多远远超出狭义“智能体”定义的语境中，对生成模型都很有用，比如在“意向立场”或用变分方法求解物理问题时。正如[由 DRL 诱发的能力](https://www.sciencedirect.com/science/article/pii/S0004370221000862#deepmind)中的其他能力——比如元学习、记忆、探索或推理——一样，“智能体性”也是一大类问题的有用工具，而一个被应用到这一类问题上的强大模型，在某个时刻就可能发展出关于智能体或心智理论之类的概念。
>
> 因此，在大规模条件下，一个非常广泛的问题范围，都可能出人意料地诱发出涌现的智能体性。

我之前曾论证过，GPT-3 明确表现出了智能体性，因为它正在从人类生成的文本数据中进行离线模仿学习（更具体地说，是行为克隆），因此它学会了许多真实或虚构智能体的生成模型。
这些生成模型提供了智能体能力，因为它们可以被用来提示模型去[“角色扮演”](https://gwern.net/gpt-3#roleplaying)——规划并采取行动，把环境引导进状态空间里很小的目标区域；而这不只是一个假设，也不只是局限于它内部模拟环境中行动与结果的文本记录，实际上只要给它执行器，就像 [SayCan](https://arxiv.org/abs/2204.01691#google) 那样，语言模型确实会在现实世界里做出这类事情。

这类系统或许从未“体验过现实世界”，也从未被刻意训练去模仿恶意智能体的精确行动序列，但这并不意味着它们不能泛化或模仿。
一个足够准确的智能体模拟，**就是**一个智能体。
（你完全可以设置一个提示，让 GPT-3 去模仿阿道夫·希特勒，然后问他该如何重新掌权并恢复对犹太人的灭绝行动，于是得到一个大致连贯的高层计划；这很糟糕，而且这种拟像甚至不必对应某个真实存在的人——邪恶的虚构角色同样能规划邪恶之事，因为要想象他们**会**想做什么可怕的事情，并不困难。）
这和人们已经接受的强化学习实例其实并没有太大区别，比如行为学习或离线强化学习：如果你是拿智能体产生的数据来训练——无论是人类数据，还是来自 DRL 智能体的记录数据——那么问题其实是：“你要怎么**不**从这些例子中学会如何行动，并具备追求目标的能力？”
大概只有当你是个愚蠢的模型、太小，或者给的数据太少时，才不会学到这些。

如果这些都不算“智能体”，那我也不知道什么才“真正”算智能体；至少，如果批评者坚持某种排除了这些系统的“智能体”定义，那我觉得也许我们干脆就该放弃“智能体”这个词——因为如果你给一个 SayCan 机器人下达“去拿一罐可乐给我带回来”的指令，它会利用图像输入构建一步步的计划，去寻找、取得并带回这罐可乐，而且在现实中的真实机器人上经常成功做到这一点；如果这都不算“智能体”，那我们就需要另一个词来指称这类非智能体系统，这样我们才有办法讨论它们的非智能体式危险。
（如果我们因为它们没有肢体就把它们定义成次级智能体，并因此把所有模型都定义成无害的非智能体，那就是一种不可接受的偷换概念，因为人们在第一次有机会把自己的模型接到人类、API、搜索引擎或机器人上时，所表现出来的轻率与漫不经心，已经到了夸张的程度——OpenAI 的 GPT-3 API 才刚在 `2020` 年 `7` 月上线不久，人们就已经在炫耀如何用它基本的 HTML/CSS/JS 能力去驱动网页浏览器；而大型语言模型的开发者，像 LaMDA 或 Adept，则表现出一种极不体面的急切，想让模型去查询任意 URL，甚至在他们的论文里都懒得说明这功能是不是实时启用的。
甚至在 AI 盒子这个概念还没被发明出来之前，所有人就已经决定为了让 AI 稍微更有用一点，而把它从盒子里放出来——这也毫不令人意外，毕竟，[工具型 AI **想要**成为智能体型 AI](https://gwern.net/tool-ai)。)

但人们也许会问，这套逻辑究竟能走多远：我们之所以会从工具型 AI 中涌现出智能体型 AI，是否**只是**因为我们拿了这么多由智能体生成的数据去训练它们？
如果我们扔掉人类文本语料——那些充满了人类如何规划、行动和实现目标的文本——或者扔掉塞满了智能体活动的视频数据集；再进一步，如果我们连图像数据集也删掉，因为它们不过是视频的快照，描绘的是智能体、行动以及充满智能体痕迹的环境；那么，我们最终得到的模型，是否就会变成一个现在“只是”一个（相对）安全的“工具型 AI”，里面再也不会潜伏任何智能体性？

我仍然会说，这种可能性依旧存在，而且甚至未必算小：智能体性不是某种离散的东西，而是一个连续谱；它是一种汇聚性的工具性驱动力／涌现能力，因为即便是在理解“非智能体性”事物时，它也同样有用。

### 一切不过是原子与虚空

首先，不可能存在任何有原则的、绝对刚性的、必然成立的区分，把“智能体性”数据与“自然”数据彻底分开。
因为在现实里也根本没有这种区分：所有“智能体性”，都是由像原子这样的非智能体性成分构造出来的。并不存在什么智能体粒子，也不存在什么让你接入“**真正的**决策制定™”的松果体。
一个具备智能体性的人类，和在太空中盘旋的一团尘埃、石头，或者一台计算机，都是由同样的基本事物构成的。
因此必然存在这样一种可能：只从（也许很多）原子的模拟开始，只从最原始的物理方程、原子与虚空开始，最终也能够重演宇宙的历史，并观察到生命起源、人类出现之类的事。于是，你就把非智能体性数据（物理方程）变成了智能体性数据。

好吧，但除非有一台超算机，否则这不太可能发生。
如果我们考虑的是现实层面的算力，比如当代神经网络，拿来训练的数据并不是“宇宙中的一切”，而只是某种看上去无害的数据——比如向下流动的河流的水文学数据（例如用于防洪），或太阳系轨道数据——那 surely 其中无论如何也不会演化出什么智能体性吧？再怎么建模冥王星混沌动力学，也不可能帮你建模天文学界围绕“冥王星算不算行星”的争斗动力学，对吧？

### 意向性解释立场

在这里，我依然持不同看法，并援引 [Daniel Dennett 的](https://en.wikipedia.org/wiki/Daniel_Dennett)[意向立场](https://en.wikipedia.org/wiki/Intentional_stance)。
事实上，人类确实会把这类自然系统当作智能体来建模。
我们发现，这类目的论解释对于许多自然系统中的直觉和捷径式推理都是不可或缺的。

#### 变分式解释

[Janus comments](https://www.lesswrong.com/posts/vJFdjigzmcXMhNTsx/simulators) 在谈到他们所强调的、可以说是 GPT-3 的一种“以世界建模为中心”的直觉时，拿它来对照我那种“以智能体为中心”的看法：

> 例如，Gwern 曾说过，任何人只要和 GPT 交互得够久，都会开始把它看成一个只在乎扮演各种角色的智能体。对我来说，这种框架很不自然，就像把物理学看成一个只在乎按照物理定律精确演化宇宙的智能体一样。往好了说，这个智能体只是一个本轮；而且它也兼容一些会生成可疑预测的解释。

我接受这种描述：它事实上是自然的，并不是在地心模型上硬加出来的某种繁复本轮，而更像日心说——更有力、更有用，也更简单。
它（以及日心说[^Wittgenstein]）让人觉得违反直觉，这的确有点遗憾，但它的优点已经被证明了。

[^Wittgenstein]: 我最喜欢的维特根斯坦轶事是这样的：日心说在所有人看来都像是假的，因为事情看起来根本**不像**地球以天文尺度的速度绕着恒星旋转，而像是地球完全静止、其他一切都围着它转（Anscombe `1963`，_An Introduction to Wittgenstein’s Tractatus_）：

    > 维特根斯坦确实建议过的一般方法，是“指出一个人并没有在他句子中的某些符号上赋予任何意义 [‘没有指称’？]”。我可以用维特根斯坦后来讨论问题的方式来说明这种方法。有一次，他见到我时问我：‘为什么人们会说，认为太阳绕地球转是自然的，而不是认为地球绕自身轴线转更自然？’ 我回答说：‘我想，是因为它看起来就像太阳在绕地球转。’ 他又问：‘那么，如果它**看起来像**地球在绕自身轴线转，那会是什么样子？’
    >
    > 这个问题让我意识到，在“它看起来像太阳绕地球转”这句话里，我此前其实根本没有给“看起来像”赋予任何相关意义。我的回应是把双手掌心向上摊开，从膝盖处开始做一个环形上举动作，同时身体后仰，并摆出[眩晕的](https://x.com/Brummo/status/1320138187763691520)[表情](https://www.youtube.com/watch?v=h714VOr-6nY)。‘正是这样！’ 他说。

如果一种意向立场让我们犯下拟人化谬误，说什么河神想要回归海洋（于是为了避免堤坝决口，我们必须献祭），那就是错的；但如果我们说，河流会努力寻找那条最优路径，以最小化它的重力势能或[自由能](https://en.wikipedia.org/wiki/Principle_of_minimum_energy)，那就是对的。
这种说法既真实，又具有预测效用，而且在数学上等价于另一种表述方式：把它写成“正向”的过程，一步一步、一个原子一个原子地计算，并最终得到同样的答案——只是通常更难求解而已。
（Ted Chiang 的 ["Story Of Your Life"](https://gwern.net/story-of-your-life) 就试图通过小说传达这种视角。）
而这类捷径是一种我们可以普遍使用的技巧：从河流下坡流动，到行星轨道，到光子在水中传播时[最小化旅行时间](https://en.wikipedia.org/wiki/Fermat%27s_principle)，再到进化动力学——我们不必一步一步地去理解它，而是把整个系统当成一个整体，通过[变分原理](https://en.wikipedia.org/wiki/Variational_principle)，把它看成是“想要”最小化（或最大化）某个简单的全局量（一个奖励），并因此选择会达到这一点的行动序列。
（“河流**想要**把自己的高度降到最低，所以我不必把它模拟到每一股水流的层面，只要看地图，就能知道它应该‘选择’先往左，再往右，然后在这片略有坡度的平地上蜿蜒而行。啊，看起来我猜对了。”）
然后，把这个模块化技巧往里一插，只需带入具体的系统和量，然后像一个智能体那样思考……^[这种联系绝不只是表面上的——很多 RL 研究都借用了物理学与变分原理的形式类比。]

哦哦，不妙了。“有预测效用”“捷径”“容易得多”“普遍适用”——这些全都是神经网络最爱的属性。
它天然就会偏爱这些。
既然存在一种 AI 安全研究者最讨厌的“一个奇怪小技巧”——例如采用目的论和变分推理——那它为什么还要试图用一堆彼此异构、计算代价高昂的把戏去分别解决每一个问题？

#### 诱发涌现很昂贵

当然，这种框架可能比直接解决问题更昂贵。
变分方法很强大，却也违反直觉；而模型往往还可以用许多更简单的近似或死记硬背来应付。
对于一个**单独**的问题，比如建模冥王星的轨道，模型不太可能学会任何变分方法。它为什么要学呢？既然只有 `1` 个系统和 `1` 个被最小化的量，那它们完全可以被直接默认掉。
这和其他[由预训练诱发的模型能力](#why-does-pretraining-work)是类似的：像归纳头、元学习、计数或推理这样的能力，必须自己“值回票价”，而且它们从一开始并不优于替代方案。
它们需要足够丰富的模型，才能可行地把这些能力算出来；需要足够的数据，把模型从那些更容易的解法里逼出来（那些解法会在少数稀有数据点上失败）；还需要足够多的训练，才能把各种可能性都走过一遍，最终收敛到更好的能力上。

#### 什么会诱发智能体性涌现？

不幸的是，这是个经验问题。
需要多少数据集？每个数据集要多大？它们之间要多么多样？甚至，“数据集”到底算什么——毕竟我们总是可以把它拆开或合并？
我们连 GPT-3 何时会发展出某种能力都很难预测，所以当然更不可能先验地断言：“建模冥王星是安全的，但一旦再扔进去几千个系外行星太阳系，就会开始诱发出一个‘定义系统／插入奖励／最大化’模块，并把智能体性重新带回来。”

##### 元胞自动机

甚至很难说，到底哪些数学或物理系统表现出了那种可以被推广到意向立场上的“最大化行为”。
那个极其抽象而简单的[元胞自动机](https://en.wikipedia.org/wiki/Cellular_automaton)——[Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)（GoL）——会不会诱发一种意向立场？

它没有智能体，没有生物性，也没有通常意义上的进化——但它确实包含许多小模式，可以被有效地[组块化](https://en.wikipedia.org/wiki/chunked)，从而帮助理解某一个具体的 GoL。
当然，人类会把 GoL 看成一堆小实体，比如 “gliders”；而一个拿随机初始化棋盘去训练的神经网络，也可能会看到同样的东西，因为大多数 GoL 模式都会消亡，或者收敛到像 [gliders](https://en.wikipedia.org/wiki/Glider_(Conway%27s_Life)) 或 [still-life](https://en.wikipedia.org/wiki/Still_life_(cellular_automaton)) 那样的固定点模式：把一个大的 GoL 棋盘组块成几个在“空旷空间”中游走、偶尔被 “still life” 打断的小 “gliders”，本来就是更简单的表示方式。

而一旦你开始谈论这些 “glider” 会四处游走，除非撞上一块会杀死它的 “still life” 方块，那你其实就已经很接近一种意向立场了——你不再是把 glider 看成对一百万个同等重要的细胞，按这条那条局部邻域规则机械应用后的必然结果，而是把它看成一个特定的、值得关注的实体，置于一个隐含且被忽略的死细胞背景之上；它会四处移动，要么飞向无穷远，要么迎来自己的毁灭。

所以，我可不想在 GoL 绝对不可能诱发任何迁移这件事上押太多注。

##### 图灵机

我们还能走得更广吗？
比如说，不是自然物理系统，也不是那些对人类来说格外有趣的特定抽象（GoL 在元胞自动机中之所以特殊，是因为它特别有趣；而我们会无视掉大量那些同样定义了一种元胞自动机、却根本没什么有趣行为的 CA 规则空间），而是所有图灵机。比如说，随机规则，加上一些按长度偏置采样的随机程序，然后我们把它们并行展开，把可用纸带视为一个序列预测问题。
毕竟，再没有比这更一般的可计算环境了。

###### 单个图灵机

在一个随机图灵机上训练，会不会带来智能体性的风险？

也许不会。
对于一个单独的图灵机，这可能会诱发出某些能力，比如遵循指令（理由和在源代码上做预训练——尤其是那些附带状态日志的源代码——会成为许多任务的强先验是一样的），但它似乎并不具备任何会诱发智能体性的特征。
随机图灵机程序并不会试图最小化或最大化什么；它们只是运行。
它们不会试图最大化运行时长（无论终止还是不终止），也不会试图尽量少写或尽量多写纸带位置，也不会试图实现某些特定图案。
模型只是学习图灵机规则，并在自身有限的前馈神经网络资源约束下，尽力去逼近它；最终，如果它可以迭代式或递归式地工作，它就会学会这些规则并完美泛化，而不会再有进一步学习发生。
把图灵机程序按是否停机来分类也没什么帮助：没错，Busy Beaver “想要”最大化某个东西，但那只是因为它按定义就是终止程序里运行时间最长的那个；而有更多图灵机程序则“很乐意”极快停机。
因此，预测停机状态也许能学到一些东西，但依然没有什么表面看来像智能体性的东西。

###### 图灵机元学习

这也许是因为这里只有一个图灵机，所以它类似于只在冥王星上训练。
也许更合适的设定，是在**很多**图灵机规则（以及每个规则内部的程序）上进行训练。
研究者真正会更感兴趣的，正是这个方向，因为很少有某个具体图灵机本身值得关注，而且我们也不知道什么才是唯一正确的图灵机™；我们更想要的是一个正在学会如何学习图灵机的神经网络，也就是元学习，而在从某个分布中抽取出的许多环境上训练神经网络，正是诱发元学习最简单的方式。
那么，如果我们训练一个模型去做“随机图灵机 + 随机程序”的序列预测，而且不进行复用，会怎样？
如果单个随机图灵机是无害的，那么所有图灵机一起呢？

嗯，好吧……
值得注意的是，Alan Turing 最初是如何引入图灵机形式主义的：那是一个一般性设定，在其中，一个**人**读取并执行一组关于如何在纸带上做标记的规则。
所以，即便在计算机作为工具、只会执行程序规定动作的原始表述里，我们也还是在中心放了一个小人！
这个小人可以对纸带做任何事情（而且只要指令不同，他也确实会这样做），但他想要的是准确遵循当前这套指令，直到做完为止。
在从 TM + 程序分布中抽出的每一次样本里，他都在遵循一套不同的指令；而现在，模型要做的则是推断他想要什么，以便尽可能快地开始通过重算来准确预测这个序列。

这就给了我们模块性、一个具体被执行的计算，以及一种强烈的优化压力：必须迅速“读懂”历史，并推断出新的规则是什么。
这未必能被干净地解释成某种奖励最大化，但它**确实**听起来很像任何人面对任意一种智能体时会做的事：逆向强化学习问题，也就是推断奖励函数，本来就可能难到离谱；在成功推断之前，我们往往先去推断局部规则与模式，而这些规则与模式会指向某些特定结果（状态空间中的某些区域）。
你也许不知道你的邻居为什么会做那件奇怪的事，但你能推断他会那么做，而不会像另一个智能体那样行事——甚至不会像他那位邪恶的同卵双胞胎那样行事。
推断图灵机规则，会不会是最简单、也最原始的一种“心智理论”？
也许吧。如果是这样，那么关于智能体性的可能性，就根本无处可逃了。

### 环境式智能体性

智能体性也许就像[图灵完备性](https://gwern.net/turing-complete)：即便在那些没有选择压力、也没有优化过程的环境里，它依然是一种过于有用、过于汇聚的能力，以至于你无法保证它不会出现。
一个系统越广泛、越强大，下一个功能或下一块数据就越可能把它推过那道坎，而设计一个**不**具备那种属性的系统，也就越困难。

智能体性可以从由智能体生成的数据中学到，因为智能体会生成极具选择性的资料。
或者，就算你仔细移除了这一切，它也可能来自对非人类数据的筛选。
或者，它也可能隐含在某种复制子系统的动力学之中。
或者，它可能来自无数那些具有这种解释方式的物理系统中的某一个，而这类解释在计算上更高效，因此任何在可实现算力与准确性之间做优化的神经网络，都会被推向这种解释方式。
或者，它也可能是对那些宏观统计有意义、而详细微观状态贡献很小的系统的一种良好简化。
或者，它可能仅仅源于在图灵机上的规则归纳元学习，因为智能体可能会遵循复杂的、可学习的策略集合，而驱动这些策略的奖励函数却是一个欠定的黑箱。

又或者……就像压不住图灵完备性一样，你刚把沉船上的一个洞补上，就会看到另一个漏点又冒出来。
你压不住一个好点子。
你唯一能做的，只是造出一个复杂系统，而据**你**所知，它还没有表现出智能体性；但很不幸，就像图灵完备性（或安全漏洞）一样，没有明显表现出智能体性，并不意味着它真的不存在。
模型不会告诉你，它只是在继续埋头降低自己的损失而已。
（“采样可以显示知识的存在，却无法显示知识的缺失。”）

对此我没有什么解决方案，只能再次建议：放弃那个诱人、方便、但错误的想法——即工具型 AI（不管你给它贴什么标签，不管叫“工具型 AI”“物理生成模型”还是“世界模拟器”），不可能或不会变成智能体型 AI。
它们很可能就是；而且它们越强，这种可能性就越大；而篡改数据并不是解决方案。
