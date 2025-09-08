---

# 中文文档构建说明

本项目为 Vyper 智能合约语言的中文文档翻译项目。

## 环境配置

### 安装依赖

推荐使用 `uv` 包管理器进行依赖管理：

```bash
# 安装文档构建依赖
uv pip install -e .[docs]

# 或者使用传统 pip（如果缺少某些包，需要单独安装）
pip install sphinx==7.2.6 sphinx-copybutton==0.5.2 shibuya==2024.1.17 sphinx-intl>=2.1.0
```

### 文档构建

如果遇到 `'sphinx-build' is not recognized` 错误，请使用 `python -m sphinx` 替代：

```bash
# 构建英文文档（HTML）
python -m sphinx -b html docs docs/_build/html

# 生成翻译模板（POT 文件）
python -m sphinx -b gettext docs docs/_build/gettext

# 使用检查脚本验证构建（无警告/错误）
python scripts/check_docs.py
```

### 国际化工作流

```bash
# 初始化中文翻译（生成 PO 文件）
sphinx-intl update -p docs/_build/gettext -l zh_CN

# 构建中文文档
python -m sphinx -b html -D language=zh_CN docs docs/_build/html/zh_CN

# 检查翻译进度
python scripts/po_stats.py
```

## 翻译规范

* 参考 `TERMS.md` 获取术语翻译标准
* 使用 Poedit 等工具编辑 PO 文件
* 遵循中文技术文档书写规范
