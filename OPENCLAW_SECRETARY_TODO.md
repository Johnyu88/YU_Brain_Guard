# 秘書 去做啊 他有鍵盤 螢幕 網路的能力
# OpenClaw 秘書任務 - 交代做事

## 老闆交代

秘書 去做啊 他有鍵盤 螢幕 網路的能力

## 任務清單 - 交代做事

### TASK-001 測試第一條 PR工作流
- **做什麼**: 開始測試第一條 有問題開log 改 繼續試 做直到對
- **檔案**: D:\openclaw-brain\yu-bazi-v29-clean\TEST_FIRST_WORKFLOW.py
- **Log**: D:\openclaw-brain\logs\first_workflow_test.log
- **鍵盤**: 打開 VSCode 執行 python TEST_FIRST_WORKFLOW.py
- **螢幕**: 看 Log 是否 12時財入庫不撞牆 白名單通過
- **網路**: 如有問題 查 GitHub 查文件
- **完成標準**: 12時全過 財入庫不撞牆 白名單通過 無錯誤訊息

### TASK-002 GitHub和D:各一套 同步
- **做什麼**: 以後 github有一套 D:也有
- **鍵盤**: 
  ```
  cd D:\openclaw-brain\yu-bazi-v29-clean
  git add .
  git commit -m "第一條測試通過"
  git push origin main
  gh pr create --title "第一條測試通過" --body "12時財入庫不撞牆"
  ```
- **螢幕**: 看 GitHub App PR數量 真實算進度
- **網路**: GitHub推送 網路必須通

### TASK-003 硬體盤點 真實版 不猜
- **做什麼**: Acer真實硬體 空白待填 不猜Predator 16GB
- **鍵盤**: 
  ```
  powershell D:\openclaw-brain\acer_full_inventory.ps1
  type D:\openclaw-brain\logs\acer_hardware_full.json
  ```
- **螢幕**: 看硬體真實值 CPU RAM GPU
- **完成**: 生成 acer_hardware_full.json 真實版

### TASK-004 Telegram回報
- **做什麼**: 今天做了多少 pr 整理報告
- **鍵盤**: python telegram/daily_pr_report.py
- **螢幕**: 看報告
- **網路**: Telegram Bot 回報
- **回報內容**: GitHub PR X個 工作流8個 引擎V29.3 知識庫26.3%

### TASK-005 管理清單版控
- **做什麼**: 連清單也在GitHub上有版本管理
- **鍵盤**: git log --oneline -- WORKFLOW_MANAGEMENT_LIST.md
- **螢幕**: 看版本歷史
- **網路**: GitHub History

## 秘書執行流程 鍵盤 螢幕 網路

1. **鍵盤**: 打開 D:\openclaw-brain\yu-bazi-v29-clean\TEST_FIRST_WORKFLOW.py
   - 在 Acer 上 按 Win+R 輸入 code D:\openclaw-brain\yu-bazi-v29-clean

2. **螢幕**: 看 VSCode 終端機
   - 執行 python TEST_FIRST_WORKFLOW.py
   - 看是否 12時財入庫不撞牆

3. **網路**: 如有問題
   - 開瀏覽器 查 GitHub github.com/johnyu4916/yu-bazi-v29-clean
   - 查文件

4. **有問題 開log 改 繼續試**
   - 打開 D:\openclaw-brain\logs\first_workflow_test.log
   - 用鍵盤改 knowledge_slicer_V29.3_strict_whitelist.py
   - 存檔 再跑 python TEST_FIRST_WORKFLOW.py
   - 做直到對

5. **成功後 推送**
   - 鍵盤 git push
   - 螢幕看 GitHub PR
   - 網路推送

6. **完成回報**
   - 跑 python telegram/completion_report.py
   - Telegram回報 老闆第一條通過

## 守紀律 鍵盤螢幕網路

- D:\openclaw-brain 是大腦 C:是財會破印 D:是庫 財入戌庫守印
- 入庫就是沒錯了不動了再動就是錯
- 沒推送算0進度 多說都是謊言
- 多跳一步退回前紀錄點 V29.0 Clean 13KB
- 跟切片沒關字眼出現就是錯誤訊息 審核有問題
- 不合併等老闆允許

## 秘書能力

- 鍵盤: 可以打字 執行命令
- 螢幕: 可以看 VSCode 看 Log 看 GitHub
- 網路: 可以推送 GitHub 可以回報 Telegram

## 現在去做

秘書 現在去做 TASK-001 開始測試第一條
