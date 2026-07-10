#!/usr/bin/env python3
"""把 src/template.html 里的图片占位符替换成 base64，生成仓库根目录的 index.html。

用法（在仓库根目录运行）：
    python3 src/build.py
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

IMAGES = {
    "__TBS__": "c_tbilisi.jpg",
    "__KZB__": "c_kazbegi.jpg",
    "__IST__": "c_istanbul.jpg",
    "__CAP__": "c_cappadocia.jpg",
    "__BKK__": "c_bangkok.jpg",
    "__BKF__": "c_bkkfood.jpg",
}

html = (SRC / "template.html").read_text(encoding="utf-8")
for token, filename in IMAGES.items():
    data = base64.b64encode((SRC / "img" / filename).read_bytes()).decode()
    html = html.replace(token, f"data:image/jpeg;base64,{data}")

page = '<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8">\n' + html + "\n</html>"
(ROOT / "index.html").write_text(page, encoding="utf-8")
print(f"index.html 已生成，大小 {len(page) // 1024} KB")
