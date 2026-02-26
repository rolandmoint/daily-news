#!/bin/bash

# OpenClaw Restore Script
BACKUP_CONF_DIR="/Users/rolandint/.openclaw/workspace/BackupConf"
OPENCLAW_DIR="/Users/rolandint/.openclaw"

# Check if a filename was provided
if [ -z "$1" ]; then
    echo "======================================"
    echo "🚑 OpenClaw Restore Tool"
    echo "======================================"
    echo "用法 (Usage): ./restore_backup.sh <備份檔案名.tar.gz>"
    echo ""
    echo "📂 最近的 10 個備份檔案 (Latest 10 backups):"
    ls -1t "$BACKUP_CONF_DIR" | grep '\.tar\.gz$' | head -n 10
    echo ""
    echo "請重新執行指令，並在後面加上你要還原的檔案名稱。"
    echo "例如: ./restore_backup.sh Nightly_2026-02-20_02-00-00.tar.gz"
    exit 1
fi

BACKUP_FILE="$BACKUP_CONF_DIR/$1"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ 錯誤: 找不到檔案 $BACKUP_FILE"
    exit 1
fi

echo "======================================"
echo "⚠️ 警告: 準備進行還原作業"
echo "======================================"
echo "這將會覆蓋你目前的 OpenClaw 設定檔 (openclaw.json)、"
echo "Agents 設定以及所有 Memory 檔案！"
echo "目標備份檔: $1"
echo ""

read -p "你確定要繼續嗎？ (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🛑 正在停止 OpenClaw Gateway..."
    openclaw gateway stop
    sleep 2

    echo "📦 正在解壓縮並覆蓋檔案..."
    tar -xzf "$BACKUP_FILE" -C "$OPENCLAW_DIR"
    
    if [ $? -eq 0 ]; then
        echo "✅ 檔案覆蓋成功！"
    else
        echo "❌ 解壓縮發生錯誤，請檢查檔案權限或磁碟空間。"
        exit 1
    fi

    echo "🚀 正在重新啟動 OpenClaw Gateway..."
    openclaw gateway start

    echo "🎉 還原完成！OpenClaw 已經浴火重生。"
else
    echo "🚫 還原作業已取消。"
fi
