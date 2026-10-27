#!/usr/bin/env python3
# 大腦聯繫手腳 Remote程式策略

import subprocess, os, json

def run_remote(cmd):
    print(f"Remote執行: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=10)
        print(result.stdout[:500])
        return result.stdout
    except Exception as e:
        print(f"失敗 {e}")
        return ""

print("=== 大腦聯繫手腳 Remote程式 ===")

# Remote1 GitHub
print("[1] Remote GitHub")
run_remote("git ls-remote https://github.com/johnyu4916/yu-bazi-v29-clean.git 2>&1 | head -5")

# Remote2 Telegram Bot (模擬)
print("[2] Remote Telegram Bot")
run_remote("python telegram/bot_handler.py 2>&1 | head -10")

# Remote3 OpenClaw Agent (模擬)
print("[3] Remote OpenClaw Agent")
if os.path.exists("OPENCLAW_SECRETARY_TODO.md"):
    print("任務文件存在 秘書可讀")
    with open("OPENCLAW_SECRETARY_TODO.md","r",encoding="utf-8") as f:
        print(f.read()[:500])

print("=== Remote完成 ===")
