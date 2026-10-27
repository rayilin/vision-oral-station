# -*- coding: utf-8 -*-
"""產生對戰題庫 questions.json（30 題）與題目統計"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import BATTLE30

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "教學網頁", "questions.json")


def main():
    if len(BATTLE30) < 30:
        raise SystemExit(f"題庫只有 {len(BATTLE30)} 題，至少要 30 題")
    texts = [q["q"] for q in BATTLE30]
    dup = {t for t in texts if texts.count(t) > 1}
    if dup:
        raise SystemExit("題目重複：" + "、".join(dup))

    # 只留伺服器需要的欄位（答案不會出現在前端）
    data = [{"q": q["q"], "o": q["o"], "a": q["a"], "e": q["e"]} for q in BATTLE30]
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    dist = [0, 0, 0, 0]
    for q in BATTLE30:
        dist[q["a"]] += 1
    print(f"questions.json：{len(data)} 題")
    print("答案分布 A/B/C/D =", "/".join(map(str, dist)))
    print("輸出：", OUT)


if __name__ == "__main__":
    main()
