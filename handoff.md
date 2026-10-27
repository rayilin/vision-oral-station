# 交接檔（handoff.md）

> 任何 Agent、任何電腦接手前**必讀**；收工時**必更新**。本檔只放交接必需的精簡資訊，詳細脈絡放 Obsidian（L3）。

**最後更新：2026-10-27**

## ⏯️ 目前做到哪

**教材、網站、上線都已完成，只差 Render 對戰後端（需老師本人登入授權）。**

- 教學網頁已上線：<https://rayilin.github.io/vision-oral-station/>
- 對戰頁：<https://rayilin.github.io/vision-oral-station/battle.html>（目前走教室區網模式，雲端後端待建）
- 單元：康軒版 健體 5 上 單元一「健康學什麼」第 2 課「視力口腔檢查站」，3 節 120 分鐘
- 課綱：`Da-Ⅲ-3`（學習內容）／`4a-Ⅲ-3`（學習表現）
- 內容單一來源：`工具/content.py`（改內容只改這支，再重跑建置）

## ✅ 已完成（可重跑重建）

| 產出 | 檔案 | 狀態 |
|------|------|------|
| 24 張教材圖卡 | `教學網頁/media/img|thumb/*.svg` | v01–v12、d01–d10、a01–a02 |
| 簡報 21 頁 | `簡報/視力口腔檢查站_教學簡報.pptx` | 4 種版型（cover／three／steps／big） |
| 簡報 JPG | `教學網頁/slides/slide01–21.jpg` | 1600×900，PowerPoint COM |
| 教案 13 節 | `教案/教案_視力口腔檢查站.docx/.pdf` | 6 頁，表格固定版面 |
| 學習單 ① | `教案/學習單1_護眼行動檢核表.docx/.pdf` | 2 頁（正面檢核／背面 3010＋小約定） |
| 學習單 ② | `教案/學習單2_牙齒保衛戰.docx/.pdf` | 牙齒構造、四要素、刷牙、食物分類 |
| 測驗卷 | `教案/測驗卷_視力口腔檢查站.docx/.pdf` | 10 題＋答案解析頁 |
| 教學網頁 | `教學網頁/index.html` | 11 區、3 互動實驗、語音朗讀、簡報播放器、抽籤、計時器、圖庫、下載 |
| 對戰 | `教學網頁/battle.html`＋`server.js`＋`questions.json` | 30 題（答案分布 6/15/5/4），標題「檢查站知識王」 |

## 🧪 驗收結果

- `verify_site.js`：**36 項全過、0 失敗**
- 瀏覽器實測（Chrome／Playwright，1280×900 與 390×844）：
  - Hero、課程地圖、三張實驗卡、簡報播放器（21 張切換）、測驗（答錯顯示正解與解析）、
    影片縮圖載入、抽籤（抽過不重複、可重設）、計時器（預設 02:00、預設鍵、暫停／歸零）、
    圖庫（24 張、分類篩選、點圖放大）、對戰 iframe 離線時顯示啟動指引
  - 390px 無水平溢出（`scrollWidth == clientWidth`）
  - console **0 error**（已加 `media/favicon.svg` 消除 favicon 404）
- 區網對戰實測：兩個分頁配對成功 → 搶答計分 → 分數雙向同步（房間 9334）

## 🚧 進行中／待辦

1. **Render 部署對戰後端**（`vision-oral-battle`）→ 把網址填回 `教學網頁/battle-api.js` 第一行 → 重新 push
   - 這步需要老師本人登入 Render 點授權（Agent 沒有、也不該有 Render 憑證）
2. Obsidian `創作庫/視力口腔檢查站/專案工作流程.md`（**本次未完成：obsidian MCP 已斷線，需重啟 OpenCode**）
3. 排定三節課實際上課日期，補進 `AGENTS.md`「關鍵時程」

## ⚠️ 踩過的坑（務必記住）

1. **8765 埠被占用**：本機有另一個 pythonw 程式長期佔用 8765，區網對戰會啟不來。
   已改寫 `server.js`：被占用時**自動往後找 8766～8775**，並在終端機印出實際網址；
   `battle.html` 的教學文字也改成讀 `location.port`，不再寫死 8765。
2. **PowerShell 用 `Name='node.exe'` + `CommandLine -like '*server.js*'` 篩選會誤殺**
   `@bitbonsai/mcpvault`（Obsidian MCP）的 5 個 node 程序。要停自己的伺服器請用 PID 或
   `-like "*教學網頁*server.js*"` 這種更具體的條件。**本次已誤殺，需重啟 OpenCode 才會恢復 obsidian MCP。**
3. **`battle-api.js` 的驗證 regex 不忽略註解**：網址若寫在註解裡會被 `verify_site.js` 誤判為已設定。
   所以 `window.BATTLE_API` 必須放在**第一行**。
4. **數字型選項（0.5／0.8／1.0／1.2）不可旋轉**：對戰題庫洗牌選項時要排除，否則邏輯錯誤。
   題庫答案分布須維持 `max ≤ 15`。
5. `docx` 表格要 `tblLayout=fixed` ＋ 表頭 `tblHeader` ＋ 每列 `cantSplit`，否則跨頁會爆版。
6. `python-pptx` 只寫 `a:latin`，中文字型會掉 → 必須補 `a:ea`／`a:cs`（`build_deck.py` 的 `set_font`）。

## 🔑 環境

- Python：`D:\ai-agent-ep03\.venv\Scripts\python.exe`（3.12.9、python-docx 1.2.0、python-pptx 1.0.2）
- 轉檔腳本：`C:\Users\rayi\.config\opencode\skills\teaching-unit-site\scripts\pptx_to_jpg.ps1`、`docx_to_pdf.ps1`
- 驗收腳本：同目錄 `verify_site.js`（36 項）
- 靜態測試：`python -m http.server 8123`（在 `教學網頁/`）
- 區網對戰：`node server.js`（或雙擊 `start-battle.bat`）
- `gh` 不在預設 PATH，需先刷新：`$env:Path = [Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [Environment]::GetEnvironmentVariable("Path","User")`

## ▶️ 下一步（照順序做）

**已完成：**`git init` → 首次 commit → `gh repo create vision-oral-station` → Pages（`build_type=workflow`）→ 部署成功。

**剩下這一步（要老師本人操作）：**

1. 開 <https://dashboard.render.com/blueprints> → **New Blueprint Instance**
2. 選 repo `rayilin/vision-oral-station` → Apply（`render.yaml` 已寫好：service `vision-oral-battle`、`node battle-server.js`、健康檢查 `/api/health`）
3. 等約 2～3 分鐘，複製服務網址（形如 `https://vision-oral-battle.onrender.com`）
4. 回報網址，或自己改 `教學網頁/battle-api.js` **第一行**：
   `window.BATTLE_API = 'https://vision-oral-battle.onrender.com';`
5. commit＋push → Pages 自動重新部署 → 線上複驗 `battle.html` 能配對

```powershell
cd C:\Users\rayi\Documents\健康教育教學專欄\視力口腔檢查站
git add -A; git commit -m "接上 Render 對戰後端"; git push
gh run watch
```
