#!/bin/bash
# =====================================================
# DAILY INTELLIGENCE - Combined News Sync Script
# Runs at 8:00 AM daily
# Combines: World News + AI & Fintech + Cyber Security
# =====================================================

set -e

WORKSPACE="/Users/rolandint/.openclaw/workspace"
REPO_DIR="/tmp/daily-news"

echo "================================================"
echo "🗞️  DAILY INTELLIGENCE SYNC - $(date)"
echo "================================================"

# Step 1: Run Python script to fetch and update news
echo "📰 Step 1: Fetching latest news..."
cd "$WORKSPACE"
/usr/bin/python3 "$WORKSPACE/scripts/daily_intelligence.py"

# Step 2: Clone repo if not exists, otherwise pull
echo "📥 Step 2: Syncing GitHub repo..."
if [ -d "$REPO_DIR/.git" ]; then
    cd "$REPO_DIR"
    git pull origin main || true
else
    rm -rf "$REPO_DIR"
    gh repo clone rolandmoint/daily-news "$REPO_DIR"
fi

# Step 3: Copy updated files
echo "📋 Step 3: Copying updated files..."
cp "$WORKSPACE/news_data.json" "$REPO_DIR/"
cp "$WORKSPACE/index.html" "$REPO_DIR/"

# Step 4: Commit and Push
echo "📤 Step 4: Pushing to GitHub..."
cd "$REPO_DIR"
TODAY=$(date +'%Y-%m-%d')

if [[ -n $(git status --porcelain) ]]; then
    git add -A
    git commit -m "🗞️ Daily Briefing: $TODAY [Automated]"
    git push origin main
    echo "✅ SUCCESS: News deployed to Vercel!"
    echo "🌐 URL: https://daily-news-lac.vercel.app/"
else
    echo "ℹ️ No changes to push."
fi

echo "================================================"
echo "🎯 SYNC COMPLETE: $(date)"
echo "================================================"