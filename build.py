"""Build the GitHub Pages site from the original Markdown files."""

from dataclasses import dataclass
from datetime import date, datetime, time, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
import re
import shutil
import tempfile
from urllib.parse import quote
import xml.etree.ElementTree as ET

from jinja2 import Environment, FileSystemLoader, StrictUndefined, select_autoescape
from markdown_it import MarkdownIt
import yaml


ROOT = Path(__file__).resolve().parent
SITE_URL = "https://qingketsing.github.io"
CHINA_TIME = timezone(timedelta(hours=8))
CATEGORIES = {
    "/latest/": "全部",
    "/tech/": "技术",
    "/life/": "生活",
    "/thinking/": "随想",
    "/review/": "评测",
}
templates = Environment(
    loader=FileSystemLoader(ROOT / "templates"),
    autoescape=select_autoescape(["html"]),
    undefined=StrictUndefined,
    trim_blocks=True,
    lstrip_blocks=True,
)
# Several older posts begin paragraphs with <br>. Parse those as inline breaks
# so Markdown and C++ type names on the following lines still render as text.
markdown = MarkdownIt("commonmark", {"html": True}).disable("html_block")
markdown.enable(["table", "strikethrough"])


@dataclass
class Post:
    slug: str
    title: str
    date: date
    author: str
    category: str
    music: dict
    html: str

    @property
    def url(self):
        return f"/blog/{quote(self.slug)}/"


def render_markdown(body):
    tokens = markdown.parse(body)
    # Retain the old site's heading links, including Chinese fragments.
    used = set()
    for index, token in enumerate(tokens):
        if token.type == "heading_open":
            stem = re.sub(r"[^\w\- ]", "", tokens[index + 1].content.lower()).replace(" ", "-")
            anchor = stem
            suffix = 1
            while anchor in used:
                anchor = f"{stem}-{suffix}"
                suffix += 1
            used.add(anchor)
            token.attrSet("id", anchor)
    return markdown.renderer.render(tokens, markdown.options, {})


def load_post(source):
    data = source.read_text(encoding="utf-8-sig")
    header = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", data, re.DOTALL)
    if not header:
        raise ValueError(f"Missing front matter in {source.name}")
    meta = yaml.safe_load(header[1])
    year, month, day = map(int, re.split(r"[-/]", str(meta["pubDate"])))
    return Post(
        slug=source.stem,
        title=meta["title"],
        date=date(year, month, day),
        author=meta.get("author") or meta.get("auther") or "青稞",
        category=meta.get("type") or meta.get("category", ""),
        music=meta.get("music") or {},
        html=render_markdown(data[header.end():]),
    )


def write_feed(site, posts):
    rss = ET.Element("rss", version="2.0")
    channel = ET.SubElement(rss, "channel")
    for tag, value in {
        "title": "Jiawei Liu",
        "link": SITE_URL + "/",
        "description": "青稞的技术、生活与随想",
        "language": "zh-CN",
    }.items():
        ET.SubElement(channel, tag).text = value
    for post in posts:
        item = ET.SubElement(channel, "item")
        ET.SubElement(item, "title").text = post.title
        ET.SubElement(item, "link").text = SITE_URL + post.url
        ET.SubElement(item, "guid").text = SITE_URL + post.url
        published = datetime.combine(post.date, time.min, CHINA_TIME)
        ET.SubElement(item, "pubDate").text = format_datetime(published)
        ET.SubElement(item, "description").text = post.html
    ET.indent(rss)
    ET.ElementTree(rss).write(site / "rss.xml", encoding="utf-8", xml_declaration=True)


def build(site):
    posts = [load_post(path) for path in sorted((ROOT / "src/blogs").glob("*.md"))]
    posts.sort(key=lambda post: post.date, reverse=True)
    if not posts:
        raise ValueError("No Markdown articles found")
    shutil.copytree(ROOT / "public", site)
    (site / ".nojekyll").touch()

    def page(folder, template, path, title="", **context):
        target = site / folder / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        html = templates.get_template(template + ".html").render(
            path=path, title=title, site_url=SITE_URL,
            year=datetime.now(CHINA_TIME).year, **context,
        )
        target.write_text(html + "\n", encoding="utf-8")

    page("", "home", "/", posts=posts)
    page("about", "about", "/about/", "关于")
    for url, category in CATEGORIES.items():
        listing = posts if url == "/latest/" else [p for p in posts if p.category == category]
        page(url.strip("/"), "archive", url, "文章" if url == "/latest/" else category,
             categories=CATEGORIES, posts=listing)
    for post in posts:
        if post.music:
            for key in ("audioSrc", "coverSrc"):
                asset = site / post.music[key].lstrip("/")
                if not asset.is_file():
                    raise FileNotFoundError(f"{post.slug}: {asset.name}")
        page(Path("blog") / post.slug, "post", post.url, post.title, post=post)
    write_feed(site, posts)
    return len(posts)


if __name__ == "__main__":
    # Prepare a complete site first. A malformed article leaves the last preview usable.
    with tempfile.TemporaryDirectory(dir=ROOT, prefix=".site-build-") as temporary:
        stage = Path(temporary)
        count = build(stage / "site")
        output = ROOT / "dist"
        if output.exists():
            output.rename(stage / "previous")
        try:
            (stage / "site").rename(output)
        except OSError:
            if (stage / "previous").exists():
                (stage / "previous").rename(output)
            raise
    print(f"Built {count} articles in {output}")
