# 修复字体

[Fixing your font](https://learnjapanese.moe/font/)

![Chinese vs Japanese font](https://learnjapanese.moe/img/font1.png)

默认情况下，你的电脑／手机会用中文字体来显示汉字。日文字形的汉字看起来会略有不同；如果你学的是中文字形而不是日文字形，可能会对你造成负面影响。

**检查你的浏览器当前是否在使用日文字体**

在日文字体和中文字体之间差异最明显的一个字是[直](https://jisho.org/search/%E7%9B%B4%20%23kanji)，它出现在词[直す](https://jpdb.io/search?q=%E7%9B%B4%E3%81%99)（naosu）里，意思是「治好、治愈、修复」。

![中文字体（DengXian）下的 naosu](https://learnjapanese.moe/img/font2.png)

![日文字体（IPAex Gothic）下的 naosu](https://learnjapanese.moe/img/font3.png)

如果你的「直」看起来像第二张图，恭喜：你在使用日文字体；如果不是，就去改字体。

## Windows 11

方法 1：手动设置字体 方法 2：设置日语显示语言

1.  打开 Settings（`Win`+`I`）
2.  进入 **System** \> **Optional features.**
3.  点击 **"View features"**（在 "Add an optional feature" 旁边）
4.  在搜索框输入 **"Japanese"**
5.  勾选 **Japanese supplemental fonts**
6.  点击 **Next**，然后点 **Install**

高级用户：Powershell

你也可以用 **Windows Powershell（Administrator）**安装日文字体：

    Add-WindowsCapability -Online -Name Language.Fonts.Jpan~~~und-JPAN~0.0.1.0

不需要重启。

这是一种确保汉字以日文字形显示的可靠方法。

1.  进入 **Settings** \> **Time & language** \> **Language & region**。
2.  点击 **Add a language**。
3.  搜索 `Japanese`
4.  选中并点击 **Next**。
5.  勾选 **Set as my Windows display language**。同时确保也勾选了 "Language Pack" 和 "Basic Typing"。
6.  点击 **Install**。
7.  下载完成后，Windows 会提示你 **Sign out** 以应用新的 UI。

然后进入浏览器的字体设置，把字体改成下面这些：

Standard font: Meiryo UI  
Serif font: Yu Mincho  
Sans-serif font: Meiryo  
Monospace: MS Gothic

## macOS

你只需要在 System Preferences 里把日语加到首选语言里。  
 \> System Preferences，然后点击 Language & Region。点击 General，然后 Add a language 并选择 Japanese 日本語。

## Linux

你的 locale 里应该包含 `ja_JP.UTF-8`。如果没有，请在 `/etc/locale.gen` 里取消注释 `#ja_JP.UTF-8 UTF-8`，然后运行：

    sudo locale-gen

接着安装 [noto-fonts-cjk](https://archlinux.org/packages/extra/any/noto-fonts-cjk/) 包。它在 Arch 官方仓库里，并且在 Arch 上安装时会自动设置必要的 fontconfig 规则。

如果其中**任何**部分不适用于你（比如发行版不同、字体不同、安装方式不同），fontconfig 可能已经正确设置，也可能没有。  
如果你不知道怎么检查，最简单的方法是：在 `~/.config/fontconfig/conf.d` 目录下创建一个包含必要 fontconfig 规则的新文件（如果目录不存在就先创建），用于日文文本。你可以参考 Arch Wiki 的这一节：[this](https://wiki.archlinux.org/title/Font_configuration/Examples#Japanese)，或参考 tatsumoto-ren 提供的这个优秀示例配置文件：[this](https://github.com/tatsumoto-ren/dotfiles/blob/main/.config/fontconfig/conf.d/99-japanese-fonts.conf)。

#### 注意事项

#### 浏览器

##### Chromium 系

即便配置正确，中文字体也可能仍然会残留（我也不知道为什么），所以你可能需要强制设置：

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEyIDE2YTIgMiAwIDAgMSAyIDIgMiAyIDAgMCAxLTIgMiAyIDIgMCAwIDEtMi0yIDIgMiAwIDAgMSAyLTJtMC02YTIgMiAwIDAgMSAyIDIgMiAyIDAgMCAxLTIgMiAyIDIgMCAwIDEtMi0yIDIgMiAwIDAgMSAyLTJtMC02YTIgMiAwIDAgMSAyIDIgMiAyIDAgMCAxLTIgMiAyIDIgMCAwIDEtMi0yIDIgMiAwIDAgMSAyLTIiPjwvcGF0aD48L3N2Zz4=) \> **Settings** \> 左侧点击 **Appearance** \> **Customize fonts**

Standard font: Noto Sans CJK JP Regular  
Serif font: Noto Serif CJK JP Regular  
Sans-serif font: Noto Sans CJK JP Regular

##### Firefox

除非 Firefox 把日语设为自己的语言之一，或者网页（或网页的某个部分）明确声明为日语（`lang="ja"`），否则它往往会回退成中文字形。这是因为中文字体通常覆盖的字符更全。  
要对抗这个问题，请这么做：

1.  打开一个新标签页，进入 `about:config`
2.  点击警告页面（如果出现）
3.  搜索 `font.cjk_pref_fallback_order`
4.  把 `ja` 移到整个值的最前面

逗号很重要。

它们用于分隔这串语言值；注意别手滑删掉一个逗号。

Before: ![Firefox settings 1](https://learnjapanese.moe/img/font10.png)

After: ![Firefox settings 2](https://learnjapanese.moe/img/font11.png)

## Android

把日语（长这样：日本語）添加为第二语言即可；除非你把它移到最顶端，否则不会改变你的显示语言。

![Android settings](https://learnjapanese.moe/img/font9.jpg)

## iOS

添加日语键盘（假名输入或 romaji 输入都行）应该就能解决。

## Anki

我觉得 Anki 卡片里用中文字体看起来最糟，因为假名会是 sans-serif，而汉字会是 serif，而且比例不对，而且还是中文字形，整体看起来就非常违和。

![天哪。很多人的卡片真的长这样。](https://learnjapanese.moe/img/font4.png)

当你在系统里安装好日文字体后，它应该会自动改成日文字体。如果没有，你就需要强制设置。

### 在 Anki 里强制使用日文字体

IPAex Gothic 是一个不错的日语 sans-serif 字体，我推荐用于 Anki。你可以在[这里](https://moji.or.jp/wp-content/ipafont/IPAexfont/ipaexg00401.zip)下载。

把字体安装到系统里，然后重启。

Windows：双击并点击 Install  
macOS：把字体拖进 Font Book  
Linux：把文件移到 `~/.local/share/fonts/`，然后运行 `fc-cache -f -v`

接着在 Anki 里点击「Add」，再点「Cards」，再点「Styling」，然后按你的需要修改 font family。

    .card {
     font-family: IPAexGothic; /* here is where you set font */
    }

你也可以把字体文件放进 Anki 的 collection.media 目录来改字体。

Windows：`C:\Users\<user>\AppData\Roaming\Anki2\(profile)\collection.media`  
macOS：`~/Library/Application Support/Anki2/(profile)/collection.media`  
Linux：`~/.local/share/Anki2/(profile)/collection.media`  
Android：`/storage/emulated/0/AnkiDroid/collection.media`

然后在 Anki 里点击「Add」，再点「Cards」，再点「Styling」，然后按你的需要修改 font family。

不要一字不差地照抄！

只加你没有的部分就行。

    .card {
     font-family: CustomFont; /* here is where you set font */

     @font-face { 
        font-family: CustomFont; src: url('ipaexg.ttf'); } /* here is where you define the font */

    }  

预览：

![带完整日语释义。](https://learnjapanese.moe/img/font5.png)

![带双语释义。](https://learnjapanese.moe/img/font6.png)

另外也要改 Anki 「编辑器」的字体：点击「Add」然后点「Fields」，把每个字段的 Editing font 改成下面任意一种（或任何你确定是日文字体的字体）。

IPAexGothic  
Meiryo  
MS Gothic  
Yu Gothic  
Hiragino Kaku Gothic Pro  
Noto Sans CJK JP Regular

## Yomichan

Yomichan 的字体应该会跟随你的浏览器字体变化；如果没有，你也可以强制它使用日文字体。

使用 Popup CSS……

    .kanji-link {
       font-family: IPAexGothic;
    }

    .source-text {
       font-family: IPAexGothic;
    }

    .gloss-content {
       font-family: IPAexGothic;
    }

    .tag-label-content {
       font-family: IPAexGothic;
    }

![使用 IPAex ゴシック字体的日文单语释义。](https://learnjapanese.moe/img/font7.png)

