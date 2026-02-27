# DAILY_NEWS_REQUIREMENTS.md - 網頁更新絕對準則

## 1. 核心邏輯
- **結果先行**：Rolend 必須喺網頁見到正確日期、正確內容、且功能完整嘅新聞。
- **數據驅動**：必須透過更新 `news_data.json` 內容，再由 `update_news.py` 生成 `index.html`。**禁止手動修改 index.html 的正文內容**，以免破壞 Layout。

## 2. 內容要求
- **日期精準**：新聞日期必須係今日（Asia/Shanghai 時區）。
- **中英文對照**：每條新聞必須包含 `en_title`, `cn_title`, `en_summary`, `cn_summary`。
- **分類清晰**：必須保留原有分類（AI, Fintech, Cyber Security, World News）。
- **Link 有效**：必須提供真正嘅新聞 Link。
- **歷史保留**：新新聞必須 prepending (加入) 到舊新聞前面，唔可以剷咗舊有嘅新聞。

## 3. UI/UX 要求
- **保持原始 Layout**：嚴禁修改原本嘅 CSS 樣式同 HTML 結構。
- **支持分類顯示**：網頁必須能夠按類別展示新聞。

## 4. 自動化 PUSH 準則
- 執行前必須 `git pull --rebase`。
- 執行後必須 `git push origin main --force` 確保覆蓋衝突。
- 成功後必須用 `web_fetch` 進行 Fact Check。