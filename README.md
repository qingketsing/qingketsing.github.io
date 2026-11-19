# Jiawei Liu 的个人网站

[查看网站](https://qingketsing.github.io/) · [全部文章](https://qingketsing.github.io/latest/) · [RSS](https://qingketsing.github.io/rss.xml)

文章原稿在 `src/blogs/`。Python 在发布时将 Markdown 和 HTML 模板生成静态页面，浏览器直接读取 HTML 和 CSS。

## 本地预览

使用 Python 3.12，在项目根目录运行以下命令。

```sh
python -m pip install -r requirements.txt
python build.py
python -m http.server 8000 --bind 127.0.0.1 --directory dist
```

打开 <http://127.0.0.1:8000/>。修改原稿、模板或样式后，重新运行 `python build.py` 并刷新页面。推送到 `master` 后，GitHub Actions 自动构建并发布到 GitHub Pages。

## 写文章

在 `src/blogs/` 中添加 UTF-8 编码的 Markdown 文件，文件名决定文章的永久链接 `/blog/文件名/`。已有文章可修改标题，保留原文件名即可沿用历史链接。

```markdown
---
title: "文章标题"
pubDate: 2026-11-19
author: "青稞"
type: "随想"
---

这里是正文。
```

原站的 `auther` 字段和斜线日期格式同样可用。分类有技术、生活、随想和评测。带配乐的文章可沿用原稿里的 `music` 字段，音频和封面放在 `public/`。首页显示最新四篇，归档和 RSS 收录全部文章。

## 调整页面

- `templates/home.html` 和 `templates/about.html` 分别维护首页和关于页。
- `templates/base.html` 维护共用的页眉、导航和页脚。
- `public/site.css` 控制排版和移动端布局。
- `dist/` 是可重新生成的发布目录。
