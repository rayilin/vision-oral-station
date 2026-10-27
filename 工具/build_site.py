# -*- coding: utf-8 -*-
"""把 content.py 的資料注入 index.html，並產生 media/images.js、複製下載檔"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import IMAGES, QUIZ10, SLIDES, VIDEOS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = os.path.join(ROOT, "教學網頁")


def js_array(items):
    body = ",\n  ".join(json.dumps(x, ensure_ascii=False) for x in items)
    return "[\n  " + body + "\n]"


def inject(html, marker, payload):
    start = f"/* {marker}-START */"
    end = f"/* {marker}-END */"
    i = html.index(start) + len(start)
    j = html.index(end)
    return html[:i] + "\n" + payload + "\n" + html[j:]


def build_images_js():
    rows = []
    for code, name, group in IMAGES:
        rows.append({
            "code": code, "name": name, "g": group,
            "h": f"media/thumb/{code}.svg", "f": f"media/img/{code}.svg",
        })
    text = "/* 教材圖卡清單（由 工具/build_site.py 產生） */\nconst IMAGES = " + js_array(rows) + ";\n"
    path = os.path.join(SITE, "media", "images.js")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"images.js：{len(rows)} 張")


def build_slides_block():
    return js_array([{"img": f"slides/slide{i:02d}.jpg"} for i in range(1, len(SLIDES) + 1)])


def build_videos_block():
    return js_array([{"t": v["t"], "id": v["id"],
                      "u": f"https://www.youtube.com/watch?v={v['id']}", "s": v["s"]}
                     for v in VIDEOS])


def main():
    path = os.path.join(SITE, "index.html")
    with open(path, encoding="utf-8") as f:
        html = f.read()
    html = inject(html, "QUIZ", js_array(QUIZ10))
    html = inject(html, "SLIDES", build_slides_block())
    html = inject(html, "VIDEOS", build_videos_block())
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"index.html：注入 QUIZ {len(QUIZ10)} 題、SLIDES {len(SLIDES)} 張、VIDEOS {len(VIDEOS)} 部")
    build_images_js()

    # 下載檔
    dl = os.path.join(SITE, "downloads")
    os.makedirs(dl, exist_ok=True)
    pairs = [
        (os.path.join(ROOT, "教案", "教案_視力口腔檢查站.docx"), "教案_視力口腔檢查站.docx"),
        (os.path.join(ROOT, "簡報", "視力口腔檢查站_教學簡報.pptx"), "視力口腔檢查站_教學簡報.pptx"),
        (os.path.join(ROOT, "教案", "學習單1_護眼行動檢核表.pdf"), "學習單1_護眼行動檢核表.pdf"),
        (os.path.join(ROOT, "教案", "學習單2_牙齒保衛戰.pdf"), "學習單2_牙齒保衛戰.pdf"),
        (os.path.join(ROOT, "教案", "測驗卷_視力口腔檢查站.pdf"), "測驗卷_視力口腔檢查站.pdf"),
    ]
    for src, name in pairs:
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(dl, name))
        else:
            print("  ⚠ 找不到：", src)
    print("下載檔複製完成")


if __name__ == "__main__":
    main()
