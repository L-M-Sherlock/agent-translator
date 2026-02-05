# 日语输入（打字）

[Japanese typing](https://learnjapanese.moe/ime/)

如今的电脑和手机都支持输入日语字符；而在电脑上用于输入日语字符的系统通常被称为 IME（Input Method Editor，输入法编辑器）。

## Windows

在 Windows 上，你只要把日语（Japanese）加入 Windows 的语言列表，就能启用日语 IME。

### 安装 IME

Windows 11 / Windows 10

在 Windows 11 上，你可以通过下面路径添加 IME：

-   Settings → Time & language → Language & region
-   然后点击 Add a language，找到 **Japanese** 并点击 Next

在 Windows 10 上，你可以通过下面路径添加 IME：

-   Settings → Time & Language → Language（左侧栏）
-   然后在 Preferred languages 下点击 Add a language，找到 **Japanese** 并点击 Next

默认设置会安装一些可选功能，例如语言包、语音识别与手写支持；同时也会安装我们需要的必需功能，例如 basic typing（IME）。如果你只需要 IME，就不必勾选任何可选项。

### 使用 IME

安装 IME 后，你可以通过切换到「Japanese」键盘布局来使用它。

你可以用下面任意一种方式切换：

-   点击任务栏右下角的「ENG」，并选择「Japanese (Microsoft IME)」
-   使用 `Win`+`Space` 快捷键在不同键盘布局之间循环切换

开始使用 IME 前，先点进一个文本框，例如 Windows 搜索框、浏览器地址栏或 Notepad 窗口。

#### 输入模式（Input Modes）

日语键盘布局有多种输入模式，但你大概率只会用其中两种。两种模式如下：

#### 半角英数（直接输入）与平假名（Romaji 输入）

它们分别对应「A」和「あ」图标。任务栏会有一个指示器告诉你当前处于哪种模式。  
直接输入模式会像英文键盘一样，直接输入键盘上的字母。  
平假名输入模式会在你输入时启动 IME，并尝试把你的输入解释为日语。

你可以用下面任意一种方式在两种模式间切换：

-   点击任务栏里的 A 或 あ 图标
-   使用 `Alt`+`\`` 快捷键（注：`\`` 是 `1` 左边的那个键）

Windows 会按**应用**记住你上一次的输入模式；这不是系统全局设置。  
默认模式是直接输入（A 图标），所以当你想输入日语时，你很可能会频繁用到 `Alt`+`\``。

一个臭名昭著的 IME 小毛病

![ime in top left corner](https://learnjapanese.moe/img/ime1.png)  
大多数现代应用在文本框未聚焦时会忽略 IME；但一些老 Windows 程序（例如 Computer Management）以及 Java 应用（例如 Minecraft）可能会在文本框未聚焦时也把 IME 激活到「あ」模式。  
你会看到 IME 出现在屏幕左上角，就像上图这样。你可以自己试：打开 Computer Management，用 `Alt`+`\`` 切到「あ」模式，然后开始打字。  
因此，保持在 A 模式（或用 `Win`+`Space` 切回英文键盘）是个好习惯，避免它碍事。

在「あ」模式下，你现在可以试着输入一些词：

-   こんにちは（输入：`konnnitiha`，然后按 `Enter` 完成编辑）
-   案内（输入：`annnai`，按 `Space` 选择「案内」这个候选，然后按 `Enter` 完成编辑）
-   私は日本語を勉強しています（输入：`watasihanihonngowobennkyousiteimasu`，用 `Tab` 选择自动补全候选，用 `Space` 切换不同转换，然后按 `Enter` 完成编辑）
-   コレハカタカナニュウリョクテストデス（输入：`korehakatakananyuuryokutesutodesu`，用 `F7` 把整段输入转换为片假名，然后按 `Enter` 完成编辑）
-   記号も入力できます←→（输入：`kigoumonyuuryokudekimasu`，用 `Tab` 自动补全转换，然后按 `Enter` 完成编辑；接着输入 `hidari` 并用 `Space` 在候选里找左箭头，按 `Enter` 完成编辑；然后输入 `migi` 并用 `Space` 找右箭头，最后再按一次 `Enter` 完成编辑）
-   かきくけこabc（输入：`kakikukeko`，然后按住 `Shift` 输入 `abc`，再按 `Enter`。按住 `Shift` 输入可以让你在当前编辑中快速切换到直接输入模式。）
-   `１２３123`（输入：`123`，然后按 `Shift`+`Caps Lock` 临时切换到直接输入，再输入一次 `123`。最后按 `Enter` 完成）
-   `ＡＢＣ`（按住 `Shift`，输入 `abc`，然后按 `Enter` 完成编辑）

**edit（编辑）到底是什么？**简单来说，IME 必须对你输入的文本进行「编辑」，才能把它显示成你想要的正确形式。IME 当前正在「编辑」的文本会带下划线。编辑缓冲区里如果堆了太多文字，会让事情更复杂；所以一般的好习惯是：当你得到想要的形式后，就用 `Enter` 来「完成」或「提交」编辑。

你可能注意到我用 `ti` 来输入「ち」。这是訓令式（Kunrei-shiki）的罗马字标准。我这么做是因为它比输入 `chi` 更快。使用 IME 并不要求訓令式；你也可以用平文式（Hepburn）romaji 输入，照样能用，只是 は／わ 例外（必须分别输入 `ha` 和 `wa`）。（你可以试试输入：`chikurin`、`an'nai`、`on'na`）

你可能也注意到了：IME 能输入一些奇怪的大号数字和字母。这些叫全角字符（full-width characters）。顾名思义，它们更「宽」，用来匹配日语字符的宽度（比拉丁字符更宽），从而更符合日文排版标准、看起来更统一。这个例子能很直观看出来：`あいうえおＡＢＣＤＥＦABCDEF`  
全角字符只能在「あ」模式下输入：你可以在开始一次编辑之前按住 `Shift` 再输入，或者在编辑过程中按 `F9`。

你可以在 Copilot 或 Notepad 里随便试试 IME！

## Microsoft IME 速查表

在非 JIS 键盘上，Microsoft IME 的基础速查表如下：

完成并提交编辑：`Enter`  
丢弃当前编辑：`Esc`  
转换（再次按下可切换候选）：`Space`  
自动补全（或循环候选）：`Tab`  
浏览候选：`Up` 和 `Down`，或用数字键快速选择  
在平假名与直接输入之间切换：`Alt`+`\``  
转换为平假名：`F6`  
转换为片假名：`F7`  
转换为半角片假名：`F8`  
转换为全角 romaji：`F9`  
转换为 romaji：`F10`  
重新转换：`Win`+`/`  
撤销上一次编辑：`Ctrl`+`Z`  
改回平假名（已提交的编辑不适用）：`Ctrl`+`Backspace`  
用 Bing 搜索候选：`Ctrl`+`B`  
输入日元符号：输入 `えん`，然后在候选里找 `¥`  
输入任意符号：输入日文读法并在候选里找。例如 `らむだ` 可以得到希腊字母 `λ`，`ぽんど` 可以得到英镑符号 `£`，`みぎ` 可以得到 `→`，等等。

默认情况下，日语 IME 会使用英语 US 键盘布局（`Shift`+`Num 2` = `@`）。  
官方支持的唯一另一个选项是 JIS 键盘布局：你可以把 IME 的硬件键盘布局改成 *Japanese keyboard (106/109 key)* 并重启电脑来切换。但如果你没有带 無変換 键等的实体 JIS 键盘，就不要这么做。

