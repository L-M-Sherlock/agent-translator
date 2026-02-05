# agent-translator

本仓库用于将英文 Markdown 学习材料翻译为中文 Markdown，并尽量做到「信、达、雅」。译文面向中文读者，因此会在不改变原文 Markdown 结构的前提下，进行必要的本地化表述与术语统一。

更完整的协作规范与格式规则见 `AGENTS.md`；术语统一以 `GLOSSARY.md` 为准。

## 目录结构

- `translation/`：最终译文（会提交）。
- `source/`：待翻译原文（本地使用，不提交；见 `.gitignore`）。
- `done/`：已完成翻译的原文归档（本地使用，不提交；见 `.gitignore`）。
- `tmp/`：长文分段/草稿临时目录（不提交；交付前清空）。
- `csv/`：段落对齐导出（不提交；用于校验一一对应）。
- `html/`：抓取的网页原始 HTML（不提交）。
- `scripts/`：辅助脚本（格式检查、CSV 导出、抓取转换等）。

## 环境与工具

- Python：>= 3.11
- 环境管理：`uv`
- Python 格式化：`ruff`

初始化：

```bash
uv sync --dev
uv run ruff format scripts/*.py
```

## 翻译工作流（每篇文章）

1. 将原文（Markdown）放入 `source/`。
2. 翻译并输出到 `translation/<同名>.md`（保留段落结构与 Markdown 结构：标题、列表、链接、代码块、加粗等）。
3. 完成后把原文移动到 `done/`（用于本地对照与检查；不提交）。
4. 运行格式检查并按提示修正：

```bash
uv run python scripts/check_format.py
```

5. 导出段落对齐 CSV（用于确认「原文行」与「译文行」一一对应；不提交）：

```bash
uv run python scripts/export_csv.py --src done/<file>.md --trans translation/<file>.md
```

6. Git 提交：仅提交 `translation/`（以及必要时的 `GLOSSARY.md`、脚本修改等），不要提交 `source/`、`done/`、`csv/`、`tmp/`、`html/`。

## 抓取与转换（learnjapanese.moe）

脚本 `scripts/fetch_learnjapanese_moe.py` 会抓取页面并用 Pandoc 转为 Markdown，输出到：

- `html/<Title>.html`（原始页面，忽略提交）
- `source/<Title>.md`（待翻译原文，忽略提交）

运行：

```bash
uv run python scripts/fetch_learnjapanese_moe.py
```

依赖：

- 系统安装 `pandoc`
- Python 包：`requests`、`beautifulsoup4`（若环境缺失，可用 `uv pip install requests beautifulsoup4` 安装）

## 术语与格式要点（摘要）

- 术语统一：以 `GLOSSARY.md` 为准（例如：`prompt`（间隔重复语境）=「卡片」；`target language`=「目标语言」；`raw`（日语材料语境）=「生肉」；`raw listening`=「无字幕听力」；`VN`=「视觉小说」）。
- 禁止对中文使用斜体（`*中文*` / `_中文_`）。
- 链接与空格：按 `AGENTS.md` 的边界规则处理（中文链接与相邻中文可不加空格；英文标题链接与中文相邻需加空格）。
- 每篇文章标题下的第一个链接是原文链接：保留其英文链接文本与 URL，不翻译链接文本。

