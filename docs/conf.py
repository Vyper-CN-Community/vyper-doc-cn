# Vyper documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 26 11:18:29 2017.

import os

# i18n 说明:
# - 基准语言使用英文(en)，通过环境变量 READTHEDOCS_LANGUAGE 或 DOCS_LANGUAGE 覆盖
# - 翻译目录: locale/<lang>/LC_MESSAGES
# - 生成 .pot: sphinx-build -b gettext docs docs/_build/gettext
# - 更新 zh_CN: sphinx-intl update -p docs/_build/gettext -l zh_CN
# - 构建中文: set DOCS_LANGUAGE=zh_CN && sphinx-build -b html docs docs/_build/html/zh_CN

extensions = [
    "sphinx_copybutton",
    "sphinx.ext.intersphinx",
]

templates_path = ["_templates"]
master_doc = "toctree"

# General information about the project.
project = "Vyper"
copyright = "2017-2024 CC-BY-4.0 Vyper Team"
author = "Vyper Team (originally created by Vitalik Buterin)"

# 动态语言设置
language = os.environ.get("READTHEDOCS_LANGUAGE", os.environ.get("DOCS_LANGUAGE", "en"))
locale_dirs = ["locale/"]
gettext_compact = False

# -- Options for HTML output ----------------------------------------------
html_theme = "shibuya"
html_theme_options = {
    "accent_color": "purple",
    "twitter_creator": "vyperlang",
    "twitter_site": "vyperlang",
    "twitter_url": "https://twitter.com/vyperlang",
    "github_url": "https://github.com/vyperlang",
}
html_favicon = "logo.svg"
html_logo = "logo.svg"

# For the "Edit this page ->" link
html_context = {
    "source_type": "github",
    "source_user": "vyperlang",
    "source_repo": "vyper",
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Vyperdoc"


# -- Options for LaTeX output ---------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "Vyper.tex",
        "Vyper Documentation",
        author,
        "manual",
    ),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "vyper", "Vyper Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Vyper",
        "Vyper Documentation",
        author,
        "Vyper",
        "One line description of project.",
        "Miscellaneous",
    ),
]

intersphinx_mapping = {
    "brownie": ("https://eth-brownie.readthedocs.io/en/stable", None),
    "pytest": ("https://docs.pytest.org/en/latest/", None),
    "python": ("https://docs.python.org/3.10/", None),
}
