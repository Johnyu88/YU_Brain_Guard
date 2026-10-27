#!/bin/bash
# 大腦聯繫手腳 Linux程式策略

echo "=== 大腦聯繫手腳 Linux程式 ==="

# 策略1 Git Remote
echo "[1] Git Remote 同步"
cd D:\openclaw-brain\yu-bazi-v29-clean 2>/dev/null || cd /mnt/d/openclaw-brain/yu-bazi-v29-clean 2>/dev/null || cd .
git status
git log --oneline -3 -- WORKFLOW_MANAGEMENT_LIST.md

# 策略2 Linux程式 WSL
echo "[2] Linux程式 WSL"
if command -v wsl &> /dev/null; then
    wsl bash -c "cd /mnt/d/openclaw-brain/yu-bazi-v29-clean && python3 TEST_FIRST_WORKFLOW.py"
else
    python3 TEST_FIRST_WORKFLOW.py 2>/dev/null || python TEST_FIRST_WORKFLOW.py
fi

# 策略3 Remote
echo "[3] Remote程式 Telegram"
python telegram/daily_pr_report.py 2>/dev/null || echo "待Acer上跑"

echo "=== 完成 ==="
