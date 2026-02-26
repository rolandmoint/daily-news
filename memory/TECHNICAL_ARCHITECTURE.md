# 🚀 GitHub + Vercel 完整集成指南

**創建日期**: 2026-02-18
**適用對象**: Roland Wong 的 AI 助手們
**用途**: 管理 GitHub 倉庫並部署到 Vercel

---

## 📋 目錄
1. [基礎設置](#基礎設置)
2. [GitHub 管理](#github-管理)
3. [Vercel 部署](#vercel-部署)
4. [完整工作流程](#完整工作流程)
5. [給 AI 助手的指令](#給-ai-助手的指令)

---

## 基礎設置

### 1. GitHub CLI 認證
```bash
# 檢查狀態
gh auth status

# 登入
gh auth login
# 選擇 HTTPS → 按 Enter → 在瀏覽器完成授權

# 測試
gh repo list
```

### 2. Vercel CLI 認證
```bash
# 安裝 Vercel CLI
npm i -g vercel

# 登入
vercel login
# 按 Enter 打開瀏覽器 → 完成授權

# 測試
vercel --version
```

---

## GitHub 管理

### 倉庫操作
```bash
# 列出所有倉庫
gh repo list --limit 50

# 創建新倉庫
gh repo create my-project \
  --public \
  --description "Project description" \
  --source=. \
  --push

# 克隆現有倉庫
cd /tmp
gh repo clone rolandmoint/existing-project
cd existing-project
```

### Git 基本操作
```bash
# 檢查狀態
git status

# 添加所有更改
git add -A

# 提交（訊息要清晰）
git commit -m "✨ Add new feature - What changed - Why it changed"

# 推送
git push origin master

# 拉取最新更改
git pull origin master
```

### GitHub Pages（靜態網站）
```bash
# 方式 1：透過 API
gh api repos/OWNER/REPO/pages \
  --method POST \
  -f source='{"branch":"master","path":"/"}'

# 方式 2：手動設置
# 1. 訪問 https://github.com/OWNER/REPO/settings/pages
# 2. Source → Deploy from a branch
# 3. Branch: master / (root)
# 4. 點擊 Save
```
**GitHub Pages 網址**: `https://rolandmoint.github.io/REPO_NAME/`

---

## Vercel 部署

### 方法 1：Git 集成（推薦）
**步驟**：
1. 將代碼推送到 GitHub
2. 訪問 https://vercel.com/dashboard
3. 點擊 "Add New Project"
4. 選擇 GitHub 倉庫
5. 點擊 "Deploy"

**自動部署**：每次推送到 GitHub，Vercel 自動重新部署

### 方法 2：Vercel CLI
```bash
# 進入項目目錄
cd /tmp/my-project

# 初始化 Vercel
vercel

# 回答問題：
# - Set up "my-project"? [Y/n] → Y
# - Which scope? → 選擇你的帳號
# - Link to existing project? [y/N] → N
# - What's your project name? [my-project] → 按 Enter

# 生產環境部署
vercel --prod
```

### 方法 3：一次性部署
```bash
# 不需要 Git，直接部署本地文件夾
cd /tmp/my-project
vercel deploy
```

### Vercel 常用命令
```bash
# 查看部署狀態
vercel --version

# 查看日誌
vercel logs

# 移除項目
vercel remove my-project

# 切換團隊/帳號
vercel switch
```

---

## 完整工作流程

### 場景：創建新網站並部署
```bash
# ===== 步驟 1：本地開發 =====
mkdir -p /tmp/my-new-site
cd /tmp/my-new-site

# 創建基礎文件
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
EOF

# ===== 步驟 2：GitHub 倉庫 =====
# 初始化
git init

# 創建 GitHub 倉庫並推送
gh repo create my-new-site \
  --public \
  --description "My new website" \
  --source=. \
  --remote=origin \
  --push

# ===== 步驟 3：Vercel 部署 =====
# 方法 A：CLI 部署
vercel --prod

# 方法 B：網頁設置
# 1. 打開 https://vercel.com/dashboard
# 2. Import Git Repository
# 3. 選擇 my-new-site
# 4. Deploy

# ===== 步驟 4：驗證 =====
# Vercel 會提供網址，例如：
# https://my-new-site.vercel.app
```

### 場景：更新現有網站
```bash
# 1. 進入項目
cd /tmp/my-project

# 2. 修改文件（例如更新 index.html）
# ... 編輯文件 ...

# 3. 提交到 Git
git add -A
git commit -m "🎨 Update design - Changed color scheme - Improved layout"
git push origin master

# 4. 如果使用 Vercel Git 集成，會自動部署
# 5. 如果使用 CLI：
vercel --prod
```

---

## 給 AI 助手的指令

### 標準指令集
```
## GitHub 指令
當我說：
- 「列出 project」 → gh repo list
- 「創建 project 叫 XXX」 → gh repo create XXX --public --source=. --push
- 「push 改動」 → git add -A && git commit -m "Update" && git push

## Vercel 指令
當我說：
- 「deploy 呢個 project」 → vercel --prod
- 「deploy 去 vercel」 → 先確認有 GitHub 倉庫，然後在 vercel.com 導入
- 「睇下 deploy 狀態」 → vercel logs

## 完整流程
當我說「整個新 website」：
1. 創建本地目錄和文件
2. git init
3. gh repo create --public --source=. --push
4. vercel --prod 或在 vercel.com 導入
5. 提供網址俾我
```

---

## 📁 重要連結
| 服務 | 連結 | 用途 |
|------|------|------|
| GitHub | https://github.com/rolandmoint | 倉庫管理 |
| Vercel Dashboard | https://vercel.com/dashboard | 部署管理 |
| GitHub Pages | https://rolandmoint.github.io/ | 靜態網站 |

---

## ⚠️ 常見問題
### Q: Vercel deploy 失敗
```bash
# 檢查錯誤
vercel --debug

# 常見原因：
# 1. 未登入 → vercel login
# 2. 無項目 → 先創建 GitHub 倉庫
# 3. 構建錯誤 → 檢查 package.json
```

### Q: GitHub push 被拒絕
```bash
# 檢查權限
gh auth status
# 重新認證
gh auth login
```

### Q: 如何選擇部署平台？
| 平台 | 適合場景 | 網址格式 |
|------|---------|---------|
| GitHub Pages | 靜態 HTML/CSS/JS | github.io/REPO |
| Vercel | React/Next.js/Node | vercel.app |

---

**最後更新**: 2026-02-18
**文件位置**: memory/TECHNICAL_ARCHITECTURE.md
