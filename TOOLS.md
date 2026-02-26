# TOOLS.md - Local Notes

### OpenRouter API Configuration
- **Primary:**
  - **Base URL:** https://openrouter.fans/v1
  - **API Key:** sk-UYu4y4AtO0iaDihvfTxJJXETd2RZXD1OVRHsz33JDnfriANj
  - **Behavior:** This is the primary OpenRouter endpoint to be used.
- **Fallback:**
  - **Base URL:** https://openrouter.ai/api/v1
  - **API Key:** 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
  - **Behavior:** If the primary endpoint or key fails, attempt to use the fallback.

### Prefered Voice Settings
- **Language:** Traditional Chinese (Cantonese / zh-HK)
- **Voice Engine:** macOS `say` command
- **Selected Voice:** Wing (Premium)
- **Profile:** Mature, stable, "Man-style" Cantonese
- **Workflow:** Use `say` to export .aiff, then use `ffmpeg` to convert to .mp3 (libmp3lame) before sending.

## Notion API key
[REDACTED]

## Google Calendar Event 創建規則 (IMPORTANT!)

### 主理人與參與者設定
- **主理人 (Organizer):** `roland.mo.int@gmail.com` (系統服務帳號)
- **Roland 的郵箱:** `rickmacau721@gmail.com` (個人主要郵箱，作為參與者)
- **Vic 的郵箱:** `portugal.lx.mo@gmail.com` (作為參與者)

### 創建 Event 時的標準流程
```bash
# 創建 Event，主理人為 roland.mo.int，添加 Roland 和/或 Vic 為參與者
gog calendar create primary \
  --summary "活動名稱" \
  --from "時間" \
  --to "時間" \
  --attendees "rickmacau721@gmail.com,portugal.lx.mo@gmail.com"
```

### 關鍵規則
1. **永不直接使用 `rickmacau721@gmail.com` 作為主理人** - gog 無權限
2. **始終使用 `roland.mo.int@gmail.com` 作為主理人** - 已認證，有完整權限
3. **Roland 和 Vic 作為 `attendees`** - 他們會收到 Calendar 邀請通知
4. **避免混淆:** roland.mo.int@gmail.com 是「系統帳號」，rickmacau721@gmail.com 是「Roland 本人」

### 範例
- 「提我」或「提 Roland」→ 添加 `rickmacau721@gmail.com` 為參與者
- 「提我太太」、「提 Vic」、「提bay」、「提肥多」、「提Rva」→ 添加 `portugal.lx.mo@gmail.com` 為參與者
- 兩個都提 → 添加兩個郵箱
