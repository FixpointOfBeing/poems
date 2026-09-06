#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Markdown 诗集 -> PDF 排版脚本
--------------------------------
把「一页一首诗」的 markdown 诗集转成 PDF：
  * 封面：第一行为 # 书名，其后到第一个分页符为引言
  * 每首诗：## 标题 + *日期* + 正文（空行分段，逐行保留）
  * 一首诗独占一页（长诗自动续页，下一首强制另起一页）
  * 字体：中文用霞鹜文楷 (LXGW WenKai)，需先在系统中安装
用法：
  python3 md2pdf.py                 # 使用默认文件
  python3 md2pdf.py 输入.md 输出.pdf
依赖：pip install weasyprint
"""
import argparse
import html
import re

from weasyprint import HTML

PAGE_BREAK = '<div style="page-break-after: always;"></div>'

CSS = """
@page { size: A6; margin: 12mm 10mm; }
* { box-sizing: border-box; }
body { font-family: "LXGW WenKai", "霞鹜文楷", "Source Han Sans CN", "DejaVu Sans", sans-serif; margin: 0; padding: 0; }
.cover { height: 120mm; display: flex; flex-direction: column; justify-content: center; }
.cover .booktitle {
  font-size: 16pt; font-weight: 500; text-align: center;
  line-height: 1.7; letter-spacing: 1pt;
}
.cover .epigraph { margin-top: 10mm; text-align: center; font-size: 10.5pt; line-height: 2; color: #555; }
.pagebreak { page-break-after: always; }
h2.title {
  font-size: 12pt; font-weight: 700; text-align: center;
  margin: 0 0 2mm 0; line-height: 1.6;
}
.date { text-align: center; font-size: 8pt; color: #8a8a8a; margin: 0 0 9mm 0; font-style: italic; }
.poem {
  font-size: 10pt; line-height: 2.05;
  white-space: pre-line;
}
"""


def esc(s):
    return html.escape(s, quote=False)


def split_pages(text):
    """按分页符切分；若无分页符，则以 ## 标题切分。"""
    if PAGE_BREAK in text:
        blocks = [b.strip("\n") for b in text.split(PAGE_BREAK)]
    else:
        blocks = []
        cur = []
        for line in text.split("\n"):
            if line.startswith("## "):
                if cur:
                    blocks.append("\n".join(cur))
                    cur = []
            cur.append(line)
        if cur:
            blocks.append("\n".join(cur))
    return [b for b in blocks if b.strip()]


def parse_poem(block):
    """解析一首诗：标题(##)、日期(*yyyy-mm-dd*)、按空行切分的诗节。"""
    title = None
    date = None
    stanzas = []
    cur = []

    def flush():
        if cur:
            stanzas.append(cur[:])
            del cur[:]

    for line in block.split("\n"):
        s = line.strip()
        if s.startswith("## "):
            title = s[3:].strip()
        elif re.fullmatch(r"\*\d{4}-\d{2}-\d{2}\*", s):
            date = s.strip("*")
        elif s == "":
            flush()
        else:
            cur.append(line)
    flush()
    assert title, block[:60]
    return title, date, stanzas


def build(text):
    blocks = split_pages(text)
    parts = ["<style>\n%s\n</style>" % CSS]

    cover_lines = [l for l in blocks[0].split("\n") if l.strip()]
    title_line = cover_lines.pop(0)
    assert title_line.startswith("# "), title_line

    poems = [parse_poem(b) for b in blocks[1:]]

    parts.append('<div class="cover">')
    parts.append('<div class="booktitle">%s</div>' % esc(title_line[2:]))
    if cover_lines:
        ehtml = "<br>".join(esc(l) for l in cover_lines if l.strip())
        parts.append('<div class="epigraph">%s</div>' % ehtml)
    parts.append("</div>")
    parts.append('<div class="pagebreak"></div>')

    for i, (title, date, stanzas) in enumerate(poems):
        parts.append('<h2 class="title">%s</h2>' % esc(title))
        if date:
            parts.append('<div class="date">%s</div>' % esc(date))
        body = "\n\n".join("\n".join(st) for st in stanzas)
        parts.append('<div class="poem">%s</div>' % esc(body))
        if i < len(poems) - 1:
            parts.append('<div class="pagebreak"></div>')

    return "\n".join(parts)


def main():
    ap = argparse.ArgumentParser(description="诗集 Markdown -> PDF")
    ap.add_argument("input", nargs="?", default="我的生命，像很久之前的太平洋.md")
    ap.add_argument("output", nargs="?", default=None)
    args = ap.parse_args()

    out = args.output or re.sub(r"\.md$", ".pdf", args.input)
    text = open(args.input, encoding="utf-8").read()
    HTML(string=build(text)).write_pdf(out)
    print("pdf:", out)


if __name__ == "__main__":
    main()
