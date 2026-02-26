# 🚑 OpenClaw 災難復原指南 (Disaster Recovery Guide)

如果 OpenClaw 出現嚴重設定錯誤、或者你唔小心鏟錯嘢，唔使驚，我哋有每日自動備份！

## 步驟一：開啟 Terminal

打開 Mac 嘅 Terminal (終端機)。

## 步驟二：執行 Restore Script

我哋寫咗一個專屬嘅還原工具，佢會幫你自動處理「停止服務 -> 覆蓋檔案 -> 重新啟動」嘅整個過程。

首先，搵出你想還原嘅 Backup 檔案名。
喺 Terminal 輸入以下指令（如果你唔記得檔案名，就咁行呢句，佢會列出最近 10 個備份畀你睇）：

```bash
/Users/rolandint/.openclaw/workspace/scripts/restore_backup.sh
```

## 步驟三：選擇並輸入檔案名

當你揀定咗要還原邊一日嘅備份，就將個檔案名加喺指令後面：

```bash
/Users/rolandint/.openclaw/workspace/scripts/restore_backup.sh Nightly_2026-02-20_02-00-00.tar.gz
```

(請將 `Nightly_2026-02-20_02-00-00.tar.gz` 替換成你想還原嘅實際檔案名)

## 步驟四：確認還原

Script 會問你確唔確定要覆蓋，輸入 `y` 然後按 Enter。

**系統會自動幫你：**
1. 🛑 停咗 OpenClaw Gateway。
2. 📦 將你揀嘅 Backup 解壓縮並精準覆蓋 `openclaw.json`、`workspace` 等設定。
3. 🚀 重新啟動 OpenClaw。

搞掂！OpenClaw 就會變番你 Backup 嗰日嘅狀態啦！🍏✨
