# OpenClaw 任務 - 建造 PR 工作流 推送工作流 讓 OpenClaw 幫你執行

## 目標
建造 PR 工作流 推送工作流 讓 OpenClaw 幫你執行 應該是這個

## 你是誰
你是跑在 Acer 上的 OpenClaw，你的腦在 D:\openclaw-brain

## 任務1: 建造 PR 工作流
1. 在 D:\openclaw-brain\yu-bazi-v29-clean\.github\workflows\ 創建 pr-workflow.yml
2. 內容：跑 V29.3 Strict Whitelist 12時窮舉 財入庫不撞牆 隨機5八字不爆 白名單審核
3. 白名單只允許切片相關字眼 黑名單 GitHub Drive D: Acer PR 一出現就報錯退回

## 任務2: 建造推送工作流
1. 創建 push-workflow.yml
2. 內容：push 時 OpenClaw 自主檢查硬體 自主建知識庫 驗證無假 PR

## 任務3: 推送到 GitHub
1. git add .github/workflows/pr-workflow.yml .github/workflows/push-workflow.yml
2. git commit -m "PR工作流 推送工作流 OpenClaw自主執行 嚴格白名單 不騙"
3. git push origin feature/pr-workflow
4. gh pr create --title "PR工作流 推送工作流 OpenClaw幫你執行" --body "建造 pr工作流 推送工作流 讓 openclaw幫你執行 應該是這個吧 測試：12時財入庫不撞牆 白名單審核 隨機八字不爆 不合併等老闆允許"

## 守紀律
- 不猜 不編 Predator 16GB
- 每個PR必須有測試 財入庫 才能入庫
- 入庫就是沒錯了不動了再動就是錯
- 沒推送上 GitHub 都當沒進度 多說都是謊言
- 多跳一步 全部退回前紀錄點 V29.0 Clean 13KB

## 回報
推完後把 GitHub PR 連結貼到 Telegram /report
