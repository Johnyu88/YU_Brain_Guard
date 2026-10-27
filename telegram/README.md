# Telegram 每日 PR 報告模板

## 你在 Telegram 上問：今天做了多少 pr

## OpenClaw 回報流程：

1. 收到 Telegram 訊息
2. cd D:\openclaw-brain\yu-bazi-v29-clean
3. 執行 python telegram/daily_pr_report.py
4. 檢查：
   - gh pr list 真實 PR 數量
   - git log --since=today 今日 commits
   - 跑 V29.3 測試 12時財入庫不撞牆
   - 白名單審核 無黑名單字眼
5. 生成 D:\openclaw-brain\logs\daily_pr_report_YYYY-MM-DD.md
6. 回傳到 Telegram

## 回報內容包含：

- 今日 PR 數量 真實 GitHub 上查的 不是假清單
- 今日 commits 數量
- 引擎狀態 V29.3 白名單 12時財入庫
- 知識庫誠實進度 26.3%
- 審核 跟切片沒關字眼有無出現
- 結論 今日進度多少 不合併等允許

## 範例

### 0進度時：

老闆 今日 PR 0個 沒推送算0進度 退回前紀錄點 V29.0 Clean 13KB

### 有進度時：

老闆 今日 PR 2個
- PR#1 引擎測試 財入庫不撞牆 已推 未合併
- PR#2 Acer硬體 空白待填 已推 未合併
今日 commits 2個 測試全過

## 守紀律

- 不猜 不編 Predator 16GB
- 沒推送上 GitHub 都當沒進度
- 多跳一步退回前紀錄點
- 跟切片沒關字眼出現就是錯誤訊息
