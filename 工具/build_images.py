# -*- coding: utf-8 -*-
"""產生 24 張教材圖卡（SVG）→ 教學網頁/media/img/*.svg 與 media/thumb/*.svg

風格：米白底、墨綠線條、橘色重點，扁平幾何，適合投影與列印。
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import IMAGES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "教學網頁", "media", "img")
THUMB_DIR = os.path.join(ROOT, "教學網頁", "media", "thumb")

W, H = 800, 600
BG = "#FAF7F0"
INK = "#35544A"
INK2 = "#6B7B72"
ACC = "#C06A2B"
SOFT = "#E4EFE7"
SOFT2 = "#F6E7D8"
RED = "#C0392B"
BLUE = "#2C5F8A"

FONT = "'Microsoft JhengHei','Noto Sans TC','PingFang TC',sans-serif"


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def txt(x, y, s, size=28, fill=INK, weight="700", anchor="middle", opacity=1.0):
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" '
            f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" '
            f'opacity="{opacity}">{esc(s)}</text>')


def rect(x, y, w, h, r=12, fill="none", stroke=INK, sw=4, opacity=1.0):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}" opacity="{opacity}"/>')


def circ(cx, cy, r, fill="none", stroke=INK, sw=4, opacity=1.0):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}" opacity="{opacity}"/>')


def line(x1, y1, x2, y2, stroke=INK, sw=4, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" '
            f'stroke-width="{sw}" stroke-linecap="round"{d}/>')


def path(d, fill="none", stroke=INK, sw=4, dash=None):
    ds = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round"{ds}/>')


# ─────────────────────────── 各圖卡 ───────────────────────────

def v01():
    """視力檢查站：視力表 E"""
    o = [circ(400, 300, 190, fill=SOFT, stroke="none", sw=0)]
    o.append(txt(400, 190, "視 力 檢 查 站", 34, INK))
    rows = [(56, 3, "#C0392B"), (44, 4, INK), (34, 5, INK2), (24, 6, INK2)]
    y = 235
    for fs, n, col in rows:
        total = n * fs * 1.5
        x = 400 - total / 2 + fs * 0.4
        for i in range(n):
            o.append(txt(x + i * fs * 1.5, y, "E", fs, col))
        y += fs * 1.55
    o.append(txt(400, 500, "每學期一次，檢查是為了我自己", 24, INK2, "400"))
    return "".join(o)


def v02():
    """視力表怎麼看"""
    o = [rect(230, 110, 340, 340, 20, "#fff", INK, 4)]
    rows = [(52, 2), (40, 3), (30, 4), (22, 5)]
    y = 190
    for fs, n in rows:
        total = n * fs * 1.6
        x = 400 - total / 2 + fs * 0.45
        for i in range(n):
            o.append(txt(x + i * fs * 1.6, y, "E", fs, INK))
        y += fs * 1.5
    o.append(line(600, 150, 690, 150, ACC, 5))
    o.append(path("M 690 150 L 668 138 M 690 150 L 668 162", stroke=ACC, sw=5))
    o.append(txt(645, 130, "遮一眼", 22, ACC))
    o.append(txt(400, 512, "一眼一眼測，不偷看才準確", 26, INK2, "400"))
    return "".join(o)


def v03():
    """0.8 複檢線"""
    o = [line(120, 300, 680, 300, INK2, 6)]
    for i, val in enumerate(["0.1", "0.3", "0.5", "0.8", "1.0", "1.2"]):
        x = 140 + i * 104
        big = val == "0.8"
        o.append(line(x, 300, x, 270 if not big else 240, RED if big else INK, 5))
        o.append(txt(x, 240 if big else 250, val, 30 if big else 24,
                     RED if big else INK, "800" if big else "600"))
    o.append(rect(390, 150, 130, 52, 26, RED, "none", 0))
    o.append(txt(455, 186, "複檢線", 26, "#fff"))
    o.append(txt(400, 400, "低於 0.8 → 到眼科進一步檢查", 30, INK))
    o.append(txt(400, 452, "視力值只是篩檢，不是診斷", 24, INK2, "400"))
    return "".join(o)


def v04():
    """眼睛的構造"""
    o = [path("M 140 300 Q 400 110 660 300 Q 400 490 140 300 Z", "#fff", INK, 5)]
    o.append(circ(330, 300, 74, SOFT2, ACC, 4))
    o.append(circ(330, 300, 34, ACC, "none", 0))
    o.append(path("M 470 190 Q 560 300 470 410", "none", RED, 4))
    o.append(line(330, 150, 330, 226, INK2, 3, "8 8"))
    o.append(txt(330, 132, "水晶體", 24, ACC))
    o.append(line(520, 430, 470, 370, INK2, 3, "8 8"))
    o.append(txt(560, 452, "視網膜", 24, RED))
    o.append(txt(400, 540, "水晶體對焦，視網膜接收影像", 26, INK2, "400"))
    return "".join(o)


def v05():
    """正常眼與近視眼"""
    o = [txt(220, 120, "正常", 28, INK), txt(580, 120, "近視", 28, RED)]
    for cx, col, focal in ((220, INK, 400), (580, RED, 330)):
        o.append(path(f"M {cx-130} 300 Q {cx} 200 {cx+130} 300 Q {cx} 400 {cx-130} 300 Z", "#fff", col, 4))
        o.append(path(f"M {cx-130} 300 Q {cx} 290 {cx+130} 300", "none", INK2, 3))
        o.append(line(cx - 120, 260, focal, 300, col, 2, "6 6"))
        o.append(line(cx + 120, 260, focal, 300, col, 2, "6 6"))
        o.append(circ(focal, 300, 9, col, "none", 0))
    o.append(txt(400, 480, "影像落在視網膜「前面」→ 看遠模糊", 28, INK))
    o.append(txt(400, 530, "近視不會自己好，只能減緩", 24, INK2, "400"))
    return "".join(o)


def v06():
    """睫狀肌與水晶體"""
    o = [circ(400, 280, 170, SOFT, "none", 0)]
    o.append(path("M 400 150 Q 470 280 400 410 Q 330 280 400 150 Z", SOFT2, ACC, 5))
    o.append(line(300, 190, 350, 240, BLUE, 5))
    o.append(line(500, 190, 450, 240, BLUE, 5))
    o.append(txt(270, 175, "放鬆", 24, BLUE))
    o.append(txt(530, 175, "收縮", 24, BLUE))
    o.append(path("M 350 240 L 330 226 M 350 240 L 330 254", stroke=BLUE, sw=4))
    o.append(path("M 450 240 L 470 226 M 450 240 L 470 254", stroke=BLUE, sw=4))
    o.append(txt(400, 500, "看近：睫狀肌收縮、水晶體變厚", 27, INK))
    o.append(txt(400, 545, "一直看近 = 一直收縮 = 疲勞", 24, INK2, "400"))
    return "".join(o)


def v07():
    """3010 護眼原則"""
    o = [circ(400, 260, 150, "#fff", INK, 6)]
    o.append(path("M 400 260 L 400 150", stroke=ACC, sw=9))
    o.append(path("M 400 260 L 500 300", stroke=INK, sw=7))
    o.append(circ(400, 260, 8, INK, "none", 0))
    for i in range(12):
        import math
        a = math.radians(i * 30)
        x1, y1 = 400 + 132 * math.sin(a), 260 - 132 * math.cos(a)
        x2, y2 = 400 + 118 * math.sin(a), 260 - 118 * math.cos(a)
        o.append(line(x1, y1, x2, y2, INK2, 3))
    o.append(txt(400, 460, "用眼 30 分鐘", 32, INK))
    o.append(txt(400, 510, "休息 10 分鐘，看遠方", 30, ACC))
    o.append(txt(400, 556, "休息不是換成看手機", 22, INK2, "400"))
    return "".join(o)


def v08():
    """30–40 公分距離"""
    o = [circ(180, 300, 26, "#fff", INK, 5), circ(180, 300, 11, INK, "none", 0)]
    o.append(rect(430, 220, 260, 170, 8, "#fff", INK, 5))
    o.append(line(440, 260, 680, 260, "#D8D2C4", 3))
    o.append(line(440, 292, 640, 292, "#D8D2C4", 3))
    o.append(line(440, 324, 660, 324, "#D8D2C4", 3))
    o.append(line(210, 390, 420, 390, ACC, 5))
    o.append(path("M 210 390 L 230 380 M 210 390 L 230 400", stroke=ACC, sw=5))
    o.append(path("M 420 390 L 400 380 M 420 390 L 400 400", stroke=ACC, sw=5))
    o.append(txt(315, 432, "30–40 公分", 30, ACC))
    o.append(txt(400, 520, "距離太近，眼睛要多用力", 26, INK2, "400"))
    return "".join(o)


def v09():
    """戶外 120 分鐘"""
    o = [circ(250, 190, 80, SOFT2, ACC, 5)]
    for i in range(8):
        import math
        a = math.radians(i * 45)
        o.append(line(250 + 96 * math.cos(a), 190 + 96 * math.sin(a),
                      250 + 124 * math.cos(a), 190 + 124 * math.sin(a), ACC, 6))
    o.append(circ(250, 190, 46, ACC, "none", 0))
    o.append(circ(520, 250, 34, "#fff", INK, 5))
    o.append(path("M 520 284 L 520 400", stroke=INK, sw=6))
    o.append(path("M 520 310 L 470 350", stroke=INK, sw=6))
    o.append(path("M 520 310 L 572 350", stroke=INK, sw=6))
    o.append(path("M 520 400 L 480 470", stroke=INK, sw=6))
    o.append(path("M 520 400 L 562 470", stroke=INK, sw=6))
    o.append(txt(400, 530, "每天戶外 120 分鐘", 34, INK))
    o.append(txt(640, 200, "1 2 0", 40, ACC))
    return "".join(o)


def v10():
    """光線怎麼安排"""
    o = [path("M 210 130 L 270 130 L 300 200 L 180 200 Z", SOFT2, ACC, 4)]
    o.append(line(240, 200, 240, 230, INK, 5))
    o.append(path("M 180 200 L 300 200 L 380 380 L 100 380 Z", "#FFF6E5", "none", 0))
    o.append(rect(90, 380, 620, 16, 4, INK2, "none", 0))
    o.append(rect(300, 300, 200, 80, 6, "#fff", INK, 4))
    o.append(line(316, 330, 470, 330, "#D8D2C4", 3))
    o.append(line(316, 350, 440, 350, "#D8D2C4", 3))
    o.append(txt(400, 470, "光線充足，從寫字手的對側來", 28, INK))
    o.append(txt(400, 520, "同時開大燈，減少明暗差", 24, INK2, "400"))
    return "".join(o)


def v11():
    """3C 用眼時間表"""
    o = [rect(300, 110, 200, 330, 24, "#fff", INK, 5)]
    o.append(rect(320, 140, 160, 240, 8, SOFT, "none", 0))
    o.append(circ(400, 415, 9, INK2, "none", 0))
    o.append(txt(400, 200, "30", 62, ACC))
    o.append(txt(400, 246, "分鐘", 24, INK2))
    o.append(line(340, 280, 460, 280, INK2, 3))
    o.append(txt(400, 330, "休息 10", 34, INK))
    o.append(rect(560, 220, 130, 62, 12, SOFT2, "none", 0))
    o.append(txt(625, 262, "計時器", 24, ACC))
    o.append(txt(400, 510, "滑手機、看影片都算近距離用眼", 26, INK))
    o.append(txt(400, 552, "愈專心，愈要記得抬頭", 22, INK2, "400"))
    return "".join(o)


def v12():
    """護眼食物"""
    o = [path("M 210 220 Q 250 180 270 260 Q 280 360 240 380 Q 190 360 190 280 Z", SOFT2, ACC, 4)]
    o.append(path("M 230 190 L 250 160", stroke="#3F7D5A", sw=6))
    o.append(txt(232, 320, "A", 40, ACC))
    for i, (cx, col) in enumerate(((400, "#4B5D8A"), (450, "#3F5A8A"), (425, "#5A6C9C"))):
        o.append(circ(cx, 260 + (i % 2) * 34, 30, col, "none", 0))
    o.append(txt(425, 200, "花青素", 24, "#4B5D8A"))
    o.append(path("M 560 220 Q 620 190 650 260 Q 660 340 610 350 Q 560 330 560 270 Z", SOFT, "#3F7D5A", 4))
    o.append(txt(605, 300, "C", 40, "#3F7D5A"))
    o.append(txt(400, 470, "均衡飲食：維生素 A、C、花青素", 28, INK))
    o.append(txt(400, 520, "食物是加分，不是護眼神藥", 24, INK2, "400"))
    return "".join(o)


def d01():
    """口腔檢查站：牙齒＋放大鏡"""
    o = [circ(400, 300, 190, SOFT, "none", 0)]
    o.append(path("M 400 140 Q 480 140 500 220 Q 512 300 486 400 Q 470 470 440 470 "
                  "Q 418 470 412 400 Q 406 350 388 350 Q 370 350 364 400 Q 358 470 336 470 "
                  "Q 306 470 290 400 Q 264 300 276 220 Q 296 140 400 140 Z", "#fff", INK, 6))
    o.append(circ(520, 250, 62, "none", ACC, 6))
    o.append(line(566, 296, 620, 350, ACC, 10))
    o.append(txt(400, 540, "口腔檢查站", 34, INK))
    return "".join(o)


def d02():
    """牙齒的構造"""
    o = [path("M 400 130 Q 470 130 488 210 Q 500 290 478 390 Q 462 460 436 460 "
              "Q 416 460 410 390 Q 405 345 388 345 Q 371 345 366 390 Q 360 460 334 460 "
              "Q 308 460 292 390 Q 270 290 282 210 Q 300 130 400 130 Z", SOFT2, ACC, 5)]
    o.append(path("M 400 170 Q 448 170 460 225 Q 470 285 452 360 Q 440 415 420 415 "
                  "Q 408 415 404 360 Q 400 330 388 330 Q 376 330 372 360 Q 366 415 350 415 "
                  "Q 330 415 318 360 Q 300 285 310 225 Q 322 170 400 170 Z", "#fff", INK, 3))
    o.append(path("M 400 250 Q 420 250 424 290 Q 428 330 418 350 Q 410 360 404 350 "
                  "Q 396 330 396 290 Q 398 250 400 250 Z", RED, "none", 0))
    o.append(line(300, 200, 240, 180, INK2, 3, "6 6"))
    o.append(txt(190, 172, "琺瑯質", 24, ACC))
    o.append(line(330, 330, 250, 330, INK2, 3, "6 6"))
    o.append(txt(196, 338, "象牙質", 24, INK))
    o.append(line(430, 350, 520, 300, INK2, 3, "6 6"))
    o.append(txt(560, 296, "牙髓", 24, RED))
    o.append(txt(400, 540, "三層構造，蛀到哪一層差很多", 26, INK2, "400"))
    return "".join(o)


def d03():
    """齲齒四要素"""
    o = [circ(400, 300, 180, SOFT, "none", 0)]
    items = [("牙齒", 300, 190), ("牙菌斑", 500, 190), ("糖", 300, 360), ("時間", 500, 360)]
    for name, cx, cy in items:
        o.append(circ(cx, cy, 74, "#fff", ACC, 5))
        o.append(txt(cx, cy + 10, name, 28, INK))
    o.append(line(374, 190, 426, 190, INK2, 4))
    o.append(line(374, 360, 426, 360, INK2, 4))
    o.append(line(300, 264, 300, 286, INK2, 4))
    o.append(line(500, 264, 500, 286, INK2, 4))
    o.append(txt(400, 508, "四個條件同時成立，才會蛀牙", 28, INK))
    o.append(txt(400, 552, "拿掉一個，就擋住了", 22, INK2, "400"))
    return "".join(o)


def d04():
    """牙菌斑"""
    o = [path("M 400 130 Q 470 130 488 210 Q 500 290 478 390 Q 462 460 436 460 "
              "Q 416 460 410 390 Q 405 345 388 345 Q 371 345 366 390 Q 360 460 334 460 "
              "Q 308 460 292 390 Q 270 290 282 210 Q 300 130 400 130 Z", "#fff", INK, 6)]
    pts = [(330, 230), (360, 200), (300, 300), (340, 330), (470, 240), (450, 300),
           (480, 350), (310, 380), (440, 390), (370, 440)]
    for x, y in pts:
        o.append(circ(x, y, 11, RED, "none", 0))
    o.append(txt(400, 530, "牙菌斑：緊黏牙面的細菌薄膜", 26, INK))
    return "".join(o)


def d05():
    """糖的陷阱"""
    o = [path("M 300 200 L 500 200 L 470 470 L 330 470 Z", "#fff", INK, 5)]
    o.append(path("M 310 270 L 490 270 L 470 470 L 330 470 Z", SOFT2, "none", 0))
    o.append(line(300, 200, 500, 200, INK, 6))
    o.append(rect(470, 130, 16, 130, 8, ACC, "none", 0))
    for i in range(3):
        o.append(rect(600, 400 - i * 44, 40, 40, 6, "#fff", ACC, 3))
    o.append(txt(620, 486, "糖", 26, ACC))
    o.append(txt(400, 540, "分次慢慢喝 = 牙齒泡在糖水裡", 26, INK))
    return "".join(o)


def d06():
    """貝氏刷牙法 45 度"""
    o = [rect(120, 380, 560, 26, 6, SOFT, "none", 0)]
    o.append(path("M 240 380 Q 240 250 340 250 Q 440 250 440 380 Z", "#fff", INK, 5))
    o.append(line(440, 380, 660, 220, INK, 14))
    o.append(line(660, 220, 700, 196, ACC, 14))
    o.append(path("M 330 380 L 400 330", stroke=RED, sw=4, dash="8 8"))
    o.append(path("M 330 380 Q 380 360 400 330", "none", BLUE, 4))
    o.append(txt(300, 470, "45°", 40, RED))
    o.append(txt(400, 540, "刷毛朝牙齦 45–60 度，兩顆兩顆震動", 26, INK))
    return "".join(o)


def d07():
    """刷牙兩顆兩顆"""
    o = []
    for i in range(2):
        x = 260 + i * 190
        o.append(path(f"M {x} 300 Q {x+48} 300 {x+56} 360 Q {x+62} 410 {x+42} 430 "
                      f"Q {x+24} 430 {x+20} 400 Q {x+16} 430 {x-2} 430 "
                      f"Q {x-22} 410 {x-16} 360 Q {x-8} 300 {x} 300 Z", "#fff", INK, 5))
    o.append(rect(200, 470, 400, 40, 20, SOFT2, "none", 0))
    o.append(txt(400, 500, "✓　✓", 30, ACC))
    o.append(txt(400, 552, "一次兩顆，照順序刷，才不會漏", 24, INK2, "400"))
    return "".join(o)


def d08():
    """牙線怎麼用"""
    o = []
    for i in range(3):
        x = 230 + i * 170
        o.append(path(f"M {x} 250 Q {x+60} 250 {x+70} 330 Q {x+76} 400 {x+52} 420 "
                      f"Q {x+30} 420 {x+28} 380 Q {x+26} 420 {x+2} 420 "
                      f"Q {x-24} 400 {x-18} 330 Q {x-10} 250 {x} 250 Z", "#fff", INK, 4))
        if i < 2:
            o.append(line(x + 66, 180, x + 66, 300, ACC, 5))
    o.append(txt(400, 500, "牙線貼著牙面上下刮，不要用力壓牙齦", 24, INK))
    o.append(txt(400, 548, "牙刷進不了的牙縫，只能靠它", 22, INK2, "400"))
    return "".join(o)


def d09():
    """含氟與定期檢查"""
    o = [rect(180, 160, 220, 240, 14, "#fff", INK, 5)]
    o.append(rect(180, 160, 220, 56, 14, SOFT, "none", 0))
    o.append(line(180, 216, 400, 216, INK, 4))
    for r in range(2):
        for c in range(3):
            o.append(rect(210 + c * 62, 246 + r * 62, 42, 40, 6, SOFT2 if (r + c) % 2 else "#fff", INK2, 2))
    o.append(path("M 560 180 L 620 200 L 620 300 Q 620 370 560 400 Q 500 370 500 300 L 500 200 Z", SOFT, ACC, 5))
    o.append(txt(560, 310, "F", 56, ACC))
    o.append(txt(400, 470, "含氟 1000ppm ＋ 每半年檢查", 26, INK))
    return "".join(o)


def d10():
    """乳牙與恆牙"""
    o = [path("M 250 240 Q 300 240 310 300 Q 318 360 302 400 Q 290 425 280 400 "
              "Q 272 425 258 400 Q 244 360 250 300 Q 254 240 250 240 Z", "#fff", INK, 4)]
    o.append(path("M 520 180 Q 600 180 620 270 Q 634 370 604 440 Q 586 490 562 490 "
                  "Q 542 490 536 440 Q 532 400 514 400 Q 496 400 492 440 "
                  "Q 486 490 462 490 Q 438 490 424 440 Q 396 370 410 270 Q 430 180 520 180 Z",
                  SOFT2, INK, 5))
    o.append(txt(280, 520, "乳牙", 26, INK2))
    o.append(txt(520, 540, "恆牙", 28, ACC))
    o.append(txt(400, 130, "乳牙蛀太深，會傷到下面的恆牙", 26, INK))
    return "".join(o)


def a01():
    """檢查站流程"""
    o = []
    labels = ["報到", "視力", "口腔", "結果"]
    for i, name in enumerate(labels):
        cx = 150 + i * 168
        o.append(circ(cx, 280, 62, "#fff" if i % 2 else SOFT, ACC, 5))
        o.append(txt(cx, 292, name, 28, INK))
        if i < 3:
            o.append(line(cx + 66, 280, cx + 100, 280, INK2, 5))
            o.append(path(f"M {cx+100} 280 L {cx+86} 270 M {cx+100} 280 L {cx+86} 290", stroke=INK2, sw=5))
    o.append(txt(400, 430, "拿到紀錄卡 → 看被畫圈的地方", 28, INK))
    o.append(txt(400, 486, "檢查是為了「發現」，不是「打分數」", 24, INK2, "400"))
    return "".join(o)


def a02():
    """我的行動方案"""
    o = [rect(200, 130, 400, 380, 16, "#fff", INK, 5)]
    for i in range(4):
        y = 200 + i * 84
        o.append(rect(240, y, 36, 36, 6, "none", ACC, 4))
        if i < 2:
            o.append(path(f"M 246 {y+18} L 256 {y+28} L 270 {y+8}", stroke=ACC, sw=6))
        o.append(line(300, y + 18, 560, y + 18, "#D8D2C4", 4))
    o.append(txt(400, 552, "選一個目標，做到兩週，再檢討", 26, INK2, "400"))
    return "".join(o)


BUILDERS = {k: globals()[k] for k in
            ["v01", "v02", "v03", "v04", "v05", "v06", "v07", "v08", "v09", "v10", "v11", "v12",
             "d01", "d02", "d03", "d04", "d05", "d06", "d07", "d08", "d09", "d10", "a01", "a02"]}


def wrap(code, name, body):
    kicker = {"v": "視力站", "d": "口腔站", "a": "行動站"}[code[0]]
    head = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'role="img" aria-label="{esc(name)}">'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>'
        f'{txt(60, 84, kicker, 26, ACC, "700", "start")}'
        f'{txt(60, 118, name, 34, INK, "800", "start")}'
        f'{line(60, 138, 160, 138, ACC, 4)}'
    )
    return head + body + "</svg>\n"


def main():
    os.makedirs(IMG_DIR, exist_ok=True)
    os.makedirs(THUMB_DIR, exist_ok=True)
    n = 0
    for code, name, group in IMAGES:
        svg = wrap(code, name, BUILDERS[code]())
        for d in (IMG_DIR, THUMB_DIR):
            with open(os.path.join(d, f"{code}.svg"), "w", encoding="utf-8") as f:
                f.write(svg)
        n += 1
    print(f"已產生 {n} 張圖卡 ×2（原圖＋縮圖）")
    print("輸出：", IMG_DIR)


if __name__ == "__main__":
    main()
