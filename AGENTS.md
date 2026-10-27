# 視力口腔檢查站（專案藍圖）

> 本檔為跨 Agent 通用的專案藍圖（AGENTS.md 開放標準）。任何 Agent 的每個 session 都應先讀本檔＋`handoff.md`。

## 專案簡介

康軒版國小**健康與體育五年級上學期**，單元一「健康學什麼」**第 2 課「視力口腔檢查站」**的完整教學專案，**3 節課（120 分鐘）**版本：

教案（DOCX）、教學簡報（PPTX 21 頁）、學習單 2 份、測驗卷、互動教學網頁
（課程地圖＋3 個互動實驗＋簡報播放器＋10 題測驗＋6 部影片＋抽籤計時器＋24 張圖庫＋下載區）、
兩人即時配對搶答遊戲（30 題題庫），部署到 GitHub Pages。

- 學習內容：`Da-Ⅲ-3` 視力與口腔衛生促進的保健行動
- 學習表現：`4a-Ⅲ-3` 主動地表現促進健康的行動
- 課程主軸：**檢查 → 發現 → 行動**（三節＝視力站、口腔站、行動站）

## 關鍵時程

（尚未排定；排課後補上三節日期）

## 目標與路線圖

- [x] 階段 0：確認單元定位（康軒 5 上 單元一 第 2 課，代碼 Da-Ⅲ-3／4a-Ⅲ-3）
- [x] 階段 1：內容單一來源 `工具/content.py`（7 概念、10 題測驗、30 題對戰、6 部影片）
- [x] 階段 2：24 張教材圖卡（SVG，程式產生，可重跑）
- [x] 階段 3：教學簡報 21 頁（16:9）＋1600×900 JPG（PowerPoint COM 匯出）
- [x] 階段 4：教案 13 節、學習單 2 份、測驗卷（DOCX 4 份 ＋ PDF 4 份，Word COM 轉檔）
- [x] 階段 5：教學網頁 11 區＋對戰（`battle.html`／`server.js`／30 題題庫）
- [x] 階段 6：靜態驗收 `verify_site.js` 36 項全過、瀏覽器實測（含 390px）
- [ ] 階段 7：上線 GitHub Pages
- [ ] 階段 8：對戰後端上 Render（Blueprint：service `vision-oral-battle`）→ 回填 `battle-api.js`
- [ ] 階段 9：Obsidian 創作庫筆記同步

## 資料夾結構

```
視力口腔檢查站/                    ← 本專案根目錄（獨立 git repo）
├── AGENTS.md                     專案藍圖（本檔）
├── handoff.md                    交接檔
├── render.yaml                   Render 藍圖（對戰後端，service: vision-oral-battle）
├── battle-server.js              Render 啟動入口 → 教學網頁/server.js
├── .github/workflows/pages.yml   GitHub Pages 部署（UNIT_DIR=教學網頁）
├── 教案/
│   ├── 教案_視力口腔檢查站.docx / .pdf
│   ├── 學習單1_護眼行動檢核表.docx / .pdf
│   ├── 學習單2_牙齒保衛戰.docx / .pdf
│   └── 測驗卷_視力口腔檢查站.docx / .pdf
├── 簡報/視力口腔檢查站_教學簡報.pptx
├── 工具/                         產生程式（全部可重跑）
│   ├── content.py                ★ 所有教材內容的單一來源（改內容改這裡）
│   ├── build_images.py           24 張 SVG → media/img＋thumb
│   ├── build_deck.py             21 頁簡報（已補 a:ea 中文字型）
│   ├── build_plan.py             教案
│   ├── build_sheets.py           學習單 2 份＋測驗卷
│   ├── build_questions.py        對戰 30 題題庫
│   ├── build_site.py             注入測驗／簡報／影片、產生 images.js、複製下載檔
│   └── docx_common.py            docx 共用工具（固定表格版面、表頭跨頁重複）
└── 教學網頁/
    ├── index.html                主網頁（11 區，含 QUIZ/SLIDES/VIDEOS 注入標記）
    ├── battle.html               對戰頁（檢查站知識王）
    ├── server.js                 對戰伺服器（區網／Render 共用，埠被占用會自動往後找）
    ├── questions.json            30 題題庫（含答案，Pages 部署時排除）
    ├── battle-api.js             雲端後端位址（空＝區網模式）
    ├── start-battle.bat          老師一鍵啟動區網對戰
    ├── slides/slide01–21.jpg     簡報圖（1600×900）
    ├── media/img/                24 張原圖 SVG（v01–v12、d01–d10、a01–a02）
    ├── media/thumb/              24 張縮圖
    ├── media/images.js           圖庫清單（給 index.html 用）
    ├── media/favicon.svg         網站圖示
    └── downloads/                教案、簡報、學習單、測驗卷
```

## 重建方式（順序不能顛倒）

```powershell
$py = "D:\ai-agent-ep03\.venv\Scripts\python.exe"
$p  = "C:\Users\rayi\Documents\健康教育教學專欄\視力口腔檢查站"

& $py "$p\工具\build_images.py"        # 1. 24 張圖卡
& $py "$p\工具\build_deck.py"          # 2. 簡報 pptx
# 3. PowerPoint COM 匯出 JPG
powershell -File "C:\Users\rayi\.config\opencode\skills\teaching-unit-site\scripts\pptx_to_jpg.ps1" `
  -Pptx "$p\簡報\視力口腔檢查站_教學簡報.pptx" -OutDir "$p\教學網頁\slides"
& $py "$p\工具\build_plan.py"          # 4. 教案
& $py "$p\工具\build_sheets.py"        # 5. 學習單＋測驗卷
# 6. Word COM 轉 PDF（四份）
powershell -File "C:\Users\rayi\.config\opencode\skills\teaching-unit-site\scripts\docx_to_pdf.ps1" -Docx "$p\教案\教案_視力口腔檢查站.docx"
& $py "$p\工具\build_questions.py"     # 7. 對戰題庫
& $py "$p\工具\build_site.py"          # 8. 最後注入（必須在 docx／pptx／PDF 都產完後跑）
```

- **不要用 LibreOffice** 轉中文 PDF／JPG：一律用 **Word COM**（docx→PDF）與 **PowerPoint COM**（pptx→JPG）。
- `build_site.py` 可重複執行（marker 注入具幂等性），但下載檔必須先存在。
- 驗收：`$env:UNIT_DIR=$p; node "$env:USERPROFILE\.config\opencode\skills\teaching-unit-site\scripts\verify_site.js"`
  （36 項，含答案分布 `max ≤ 15`、Pages 排除清單、Render 藍圖、`.gitignore` 含 `.env`）

## 同步層級

| 層級 | 平台 | 位置 | 讀取時機 |
|------|------|------|---------|
| L1 | 本地 | `AGENTS.md`＋`handoff.md` | 每個 session |
| L2 | GitHub | `rayilin/vision-oral-station`（私有） | 指定時 |
| L3 | Obsidian | `創作庫/視力口腔檢查站/專案工作流程.md` | 有需要時 |

## 已上線網址

（部署後填寫）

- 教學網頁：
- 對戰頁：
- 雲端對戰後端：`https://vision-oral-battle.onrender.com`（`/api/health`）

## 與其他專案的關係

- 位於 `C:\Users\rayi\Documents\健康教育教學專欄\`，**是獨立的 git repo**（領域不同，不與自然科學專欄混放）。
- 範本專案：`C:\Users\rayi\Documents\自然科學教學專欄\磁鐵好好玩\`（同一條產線、已上線）。
- 可重用技能：`teaching-unit-site`、`teaching-site`、`officecli`、`pptx`
- **一台 Render 服務只能綁一個 repo**：磁鐵那台叫 `magnets-battle`，本單元用 `vision-oral-battle`。

## 工作約定

- 任何 Agent、任何電腦：**開工先讀 `handoff.md`，收工必更新 `handoff.md`**
- 修改共用檔案前先讀最新內容，避免覆蓋其他 Agent 的變更
- 所有回應與文件使用繁體中文
- 修改前先確認計畫，優先保留原有資料結構
- 改教材內容一律改 `工具/content.py`，再重跑建置（不要手改產出的 docx／pptx）

## 安全與隱私（不可違反）

- **不把 API key、密碼、憑證寫進 repo**，也不要貼進 `AGENTS.md`／`handoff.md`；一律放 `.env` 並列入 `.gitignore`
- **學生資料只用座號**，不出現姓名、學號、班級以外的個資、照片或聯絡方式
- `questions.json`（含答案）**不得上 GitHub Pages**；Pages workflow 已排除，驗收會檢查
- 答案與解析只出現在教師用測驗卷與對戰後端，網站前端只有 10 題測驗的即時回饋
