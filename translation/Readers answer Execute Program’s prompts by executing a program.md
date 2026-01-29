# 读者通过执行一个程序来回答 Execute Program 的卡片

[Readers answer Execute Program’s prompts by executing a program](https://notes.andymatuschak.org/z9DRugkwcBv7iLRACEnWVDL)

类似于[助记媒介](https://notes.andymatuschak.org/zKPv6qkSErdRGqyryvgS2wS)，Execute Program 的课程将讲解文字与交互式卡片穿插呈现。但让 Execute Program 名副其实的核心构想，是每一次互动都涉及在内嵌解释器中执行一个程序。事实上，[Execute Program 没有不可执行的卡片](https://notes.andymatuschak.org/zYCRKm7HujiD6CNtcC9gnmk)。

例如，一节课可能会用几段文字介绍这样一个概念：在 SQL 中，你可以用 `SELECT column_name` 只选择某一列。然后它可能给出这样一张卡片：

```
exec(`CREATE TABLE cats (name STRING, age INTEGER)`);
exec(`INSERT INTO cats (name, age) VALUES (“Boromir”, 3), (“Aragorn”, 15)`);
exec(`SELECT name FROM cats`)
> 
```

读者的光标会停在最后一行；他们需要输入第一行表达式将求值出的结果。随后 Execute Program 会对读者输入的表达式进行求值（即按 JavaScript 执行），并将得到的值与测试值进行比较。

这看起来像 Quizlet 风格的抽认卡：你必须把正确答案敲进去；但它并不是。它是一个真正的解释器，会真的对你的程序求值。因此你可以写 `[{name: “Boromir”}, {name: “Aragorn”}]`，也可以写 `[“Boromir”, “Aragorn”].map(n => ({name: n})`——两者都正确。我喜欢这种设计模型，因为它让课程更接近真实语境：[赋能式环境会聚焦于所赋能之事](https://notes.andymatuschak.org/z2etsLyP1LJUwNDPCwvRdUG)。

更复杂的卡片被称为「problems」，它会给读者一段源代码清单，以及一个「目标表达式」——也就是最后一行所期望得到的值。例如：

```
function adds2(input: number) {
}
adds2(4)

// GOAL: 6
```

读者需要修改这段源代码清单，使其产出目标表达式。读者准备好之后，就执行他们的程序；系统会对其求值，并将输出与目标值比较。

一个相关、但更具野心的构想：[把 Shenzhen I/O 这样的游戏置于 IDE 之类的专业环境中，这意味着什么？](https://notes.andymatuschak.org/zFS2bUsK1vzv1M7cYcMFdCV)

也相关：[可执行书籍](https://notes.andymatuschak.org/zLNcy2JiH3AGNaZjYkHzK9P)

------

Q. Execute Program 的卡片会要求读者输入答案。这种互动与 Quizlet 的不同之处是什么？
A. 答案是在真实解释器里被求值，而不是仅做逐字对比。

Q. 为什么读者对 Execute Program 的卡片所给出的答案是「被求值」，而不是仅做逐字对比，这一点很重要？
A. 它允许读者在解题时拥有更贴近真实的灵活性。
