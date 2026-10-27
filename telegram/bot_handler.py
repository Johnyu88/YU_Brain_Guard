# D:\openclaw-brain\telegram\bot_handler.py
# Telegram 問 今天做了多少 pr 整理一份報告

# 當 Telegram 收到：
# /pr_report 或 今天做了多少 pr
# OpenClaw 執行：

# 1. cd D:\openclaw-brain\yu-bazi-v29-clean
# 2. python telegram/daily_pr_report.py
# 3. 讀 D:\openclaw-brain\logs\telegram_last_report.md
# 4. 回傳到 Telegram

# 範例回覆：

# 老闆 今日 PR 報告 2026-10-27 23:00
# GitHub 上 PR 0 個
# 沒推送算0進度
# 引擎 V29.3 白名單通過 12時財入庫不撞牆
# 知識庫 26.3%誠實

# 如果有 PR：

# 老闆 今日 PR 報告
# GitHub 上 PR 2 個
# - PR#1 V29.0 Clean 13KB 財入庫不撞牆
# - PR#2 Acer硬體真實版 空白待填
# 今日 commits 2 個
# 測試全過 不合併等你允許

# 守紀律：
# - 不猜 不編
# - 沒推送算0進度
# - 多跳一步退回前紀錄點
# - 跟切片沒關字眼出現就是錯誤訊息 審核有問題

def handle_telegram_query(query):
    if "做了多少 pr" in query or "pr_report" in query or "/report" in query:
        # 執行報告
        import subprocess
        subprocess.run("python telegram/daily_pr_report.py", shell=True, cwd="D:\openclaw-brain\yu-bazi-v29-clean")
        with open("D:\openclaw-brain\logs\telegram_last_report.md", "r", encoding="utf-8") as f:
            return f.read()
    return "未知指令 請用 /pr_report 或 今天做了多少 pr"
