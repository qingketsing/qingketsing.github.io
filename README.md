# Virtual Venus 🌟

一个基于 Astro 构建的现代化个人博客网站，使用 Tailwind CSS 进行样式设计。

## 项目简介

本项目是一个静态博客网站，专注于分享技术、生活、思考和回顾等内容。网站采用现代化的设计理念，支持响应式布局，为读者提供良好的阅读体验。

## 技术栈

- **框架**: [Astro](https://astro.build/) v5.13.5
- **样式**: [Tailwind CSS](https://tailwindcss.com/) v4.1.12
- **排版**: @tailwindcss/typography
- **地图**: Leaflet v1.9.4
- **数学公式**: KaTeX
- **包管理**: pnpm v10.14.0

## 项目结构

```
virtual-venus/
├── public/                    # 静态资源
│   ├── *.jpg, *.png          # 图片资源
│   ├── *.mp3                 # 音频文件
│   └── katex/                # KaTeX 数学公式渲染库
├── src/
│   ├── assets/               # 项目资源
│   ├── components/           # 组件目录
│   │   ├── Navi.astro       # 导航栏组件
│   │   └── introduction.astro # 介绍组件
│   ├── layouts/              # 布局模板
│   ├── pages/                # 页面目录
│   │   ├── index.astro      # 首页
│   │   ├── about.astro      # 关于页面
│   │   ├── latest.astro     # 最新文章
│   │   ├── tech.astro       # 技术文章
│   │   ├── life.astro       # 生活随笔
│   │   ├── thinking.astro   # 思考文章
│   │   ├── review.astro     # 回顾文章
│   │   └── blog/
│   │       └── [slug].astro # 动态博客页面
│   ├── blogs/                # Markdown 博客文章
│   └── styles/
│       └── global.css       # 全局样式
├── astro.config.mjs          # Astro 配置
├── tailwind.config.mjs       # Tailwind 配置
├── tsconfig.json            # TypeScript 配置
└── package.json             # 项目依赖
```

### 安装依赖
```bash
pnpm install
```

### 开发模式
```bash
pnpm dev
```
访问 http://localhost:4321

### 构建生产版本
```bash
pnpm build
```

### 预览生产版本
```bash
pnpm preview
```

## 内容管理

### 添加新文章
1. 在 `src/blogs/` 目录下创建新的 `.md` 文件
2. 文件头部添加 frontmatter：
   ```yaml
   ---
   title: "文章标题"
   pubDate: "2025-01-01"
   description: "文章描述"
   author: "作者"
   category: "tech" # tech, life, thinking, review
   tags: ["标签1", "标签2"]
   ---
   ```
3. 编写文章内容

### 博客分类
- **tech**: 技术相关文章
- **life**: 生活随笔和日常分享
- **thinking**: 思考和观点文章
- **review**: 回顾和总结文章

## 自定义配置

### 导航栏
在 `src/components/Navi.astro` 中修改导航项：
```javascript
const navItems = [
  { name: '首页', href: '/' },
  { name: '关于', href: '/about'},
  // 添加更多导航项
];
```

### 样式定制
- 全局样式：`src/styles/global.css`
- Tailwind 配置：`tailwind.config.mjs`
- 组件样式：在各个 `.astro` 文件的 `<style>` 标签中


欢迎提交 Issue 和 Pull Request 来改进这个项目。
