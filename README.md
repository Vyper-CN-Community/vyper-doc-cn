# Vyper 中文文档（vyper-doc-cn）

面向 Vyper 开发者的中文文档翻译与构建项目。目标是与上游文档保持同步、提供一致的本地构建体验，并通过自动化流程持续更新翻译进度。

如果你也想参与翻译或校对，欢迎阅读下方的“如何贡献”。

## 快速开始（Windows + uv）

前置工具：

- Python 3.11+（系统可用）
- uv（推荐）<https://github.com/astral-sh/uv>

1. 创建并激活虚拟环境（cmd.exe）

```bat
uv venv
.venv\Scripts\activate
```

2. 安装文档依赖

```bat
uv pip install -e .[docs]
```

3. 构建英文文档

```bat
python -m sphinx -b html docs docs\_build\html
```

4. 生成翻译模板（POT）并初始化中文 PO

```bat
python -m sphinx -b gettext docs docs\_build\gettext
sphinx-intl update -p docs\_build\gettext -l zh_CN
```

5. 构建中文文档

```bat
python -m sphinx -b html -D language=zh_CN docs docs\_build\html\zh_CN
```

6. 严格检查（无警告/错误）

```bat
python scripts\check_docs.py
```

提示：若命令行提示找不到 sphinx-build，请总是使用 `python -m sphinx`。

## 翻译指南

- 术语：请参考 `TERMS.md`/`TERMS.csv`，保持术语一致。
- 工具：推荐使用 Poedit 或任意支持 PO 的编辑器；PO 文件位于 `docs/locale/zh_CN/LC_MESSAGES/`。
- 风格：遵循中文技术文档书写规范，注意中英文空格、标点、专有名词。
- 结构：不要改动源 RST 的标号与交叉引用锚点，如需调整在不影响引用的前提下进行。

建议流程：

1. 运行“快速开始”中的步骤 3-5 准备 PO 文件；
2. 编辑 PO，优先覆盖核心文档章节；
3. 本地构建中文 HTML，打开 `docs\_build\html\zh_CN\index.html` 自检；
4. 运行 `python scripts\check_docs.py` 确保无警告（-n、-W 严格模式）。

提交规范（PR/Commit）：

- 使用约定式提交（Conventional Commits），例如：
  - docs: 初次翻译 built-in-functions
  - docs: 修正 release-notes 链接重复锚点
- 本仓库的 PR 将通过语义化校验（`amannn/action-semantic-pull-request`）。

## 与上游保持一致（像官方一样构建）

- Sphinx 版本：见 `pyproject.toml` 与 `requirements-docs.txt`；主题使用 shibuya，已按上游配置。
- 构建配置：`docs/conf.py` 对齐上游，同时在严格模式下（-n -W）保持无警告。
- Read the Docs：仓库包含 `.readthedocs.yaml`，如需启用 RTD，请在 RTD 项目中指向本配置。

## CI 与自动化

- 上游文档同步：`.github/workflows/sync_docs.yml` 会每天检查上游 `vyperlang/vyper@master` 的 `docs/` 与 `README.*` 变更，自动创建同步 PR，并附带 gettext 统计摘要。
- 进度自动更新：`.github/workflows/update_readme_progress.yml` 在提交翻译或手动触发时，运行 `scripts/po_stats.py` 与 `scripts/update_readme_progress.py`，将翻译进度表写入 README 的标记区块。
- 静音重型 CI：针对仅修改文档的提交，已配置过滤：
  - `test.yml`：仅运行 docs 任务，其余 lint/test/fuzz/coverage 跳过；
  - `build.yml`、`codeql.yml`、`ghcr.yml`：对 docs-only 变更忽略触发，减少无关噪音。

## 翻译进度（自动更新）

以下区块由 CI 自动维护，请勿手动修改：

<!-- START:PO_STATS -->
尚无统计，等待 CI 生成…
<!-- END:PO_STATS -->

你也可以本地生成：

```bat
python scripts\po_stats.py > po_stats.json
python scripts\update_readme_progress.py
```

## 常见问题

- Sphinx 引用类型未解析：已在 `docs/conf.py` 使用 `nitpick_ignore` 屏蔽 Vyper 伪类型的严格校验，以保证 -n 下仍可通过。
- 重复锚点/链接名：优先使用匿名链接（`__`）或重命名本地锚点，避免跨文档冲突。
- Windows 路径：示例使用反斜杠路径；若使用 PowerShell，可改为 `/`。

## 参与我们

欢迎通过 Issues 认领章节或报告问题，也可以直接提交 PR。建议在 PR 描述说明：涉及章节、是否完整翻译/校对、是否通过本地严格检查。

感谢所有贡献者！
