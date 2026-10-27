# 開始測試第一條 有問題開log 改 繼續試 做直到對

## 第一條：PR工作流

檔案：.github/workflows/pr-workflow.yml
測試：TEST_FIRST_WORKFLOW.py
Log：logs/first_workflow_test.log

## 流程

1. GitHub有一套 D:也有一套
   - GitHub: github.com/johnyu4916/yu-bazi-v29-clean
   - D: D:\openclaw-brain\yu-bazi-v29-clean

2. 開始測試第一條
   ```bash
   cd D:\openclaw-brain\yu-bazi-v29-clean
   python TEST_FIRST_WORKFLOW.py
   ```

3. 有問題 開log
   ```bash
   type logs\first_workflow_test.log
   # 或
   cat logs/first_workflow_test.log
   ```

4. 改
   - 如果 白名單審核失敗 有跟切片沒關字眼
     → 改 knowledge_slicer_V29.3_strict_whitelist.py 移除黑名單字眼
   - 如果 財入庫失敗
     → 改 check_cai_po_yin_vs_cai_ru_ku 財入戌庫不破印
   - 如果 12時撞牆
     → 改 final_converge_duan 入庫就是沒錯了不動

5. 繼續試 做直到對
   ```bash
   python TEST_FIRST_WORKFLOW.py
   # 重試 直到 ✅ 成功
   ```

6. 成功後 推送 GitHub
   ```bash
   git add knowledge_slicer_V29.3_strict_whitelist.py logs/first_workflow_test.log
   git commit -m "第一條測試通過 12時財入庫不撞牆 白名單審核"
   git push origin main
   ```

7. Telegram回報
   ```
   今天做了多少 pr
   ```
   OpenClaw回報 第一條通過

## 成功標準

- 無錯誤訊息 白名單通過
- 財入庫成功 午火見戌 財入戌庫守印
- 12時窮舉全過 財入庫不撞牆
- 隨機5八字不爆
- 入庫就是沒錯了不動了再動就是錯

## Log完備

- logs/first_workflow_test.log 每次測試記錄
- logs/TASKS.md 任務交代
- logs/COMPLETION.md 完成回報
- logs/WORKFLOW_EXECUTION.md 工作流執行
