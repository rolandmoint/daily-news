#!/bin/bash

export PATH=/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
BACKUP_DIR="/Users/rolandint/.openclaw/workspace/BackupConf"
OPENCLAW_DIR="/Users/rolandint/.openclaw"

mkdir -p "$BACKUP_DIR"
cd "$OPENCLAW_DIR" || exit 1

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
BACKUP_FILE="$BACKUP_DIR/Nightly_$TIMESTAMP.tar.gz"

# Array of target files/directories relative to .openclaw
FILES=(
  "openclaw.json"
  "workspace/AGENTS.md"
  "workspace/HEARTBEAT.md"
  "workspace/IDENTITY.md"
  "workspace/MEMORY.md"
  "workspace/SOUL.md"
  "workspace/TOOLS.md"
  "workspace/USER.md"
  "workspace/memory"
)

# Conditionally append agent directory to avoid errors if missing
if [ -d "agents/main/agent" ]; then
  FILES+=("agents/main/agent/")
fi

# Run the archival process, silently
tar -czf "$BACKUP_FILE" "${FILES[@]}"

# Cleanup: Discard backups older than 30 days
find "$BACKUP_DIR" -type f -name 'Nightly_*.tar.gz' -mtime +30 -exec rm {} \;

# Double fail-safe constraint: retain exactly 30 backups by pure index count
# Tail lists items offset past 30, xargs processes for deletion
ls -1t "$BACKUP_DIR"/Nightly_*.tar.gz 2>/dev/null | tail -n +31 | xargs -I {} rm -- {}

echo "Backup successful: $BACKUP_FILE"
