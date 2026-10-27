# 開始測試所有流程 - 需要我幫你開專案的時候 告訴我

## 老闆 現在開專案 開始測試所有流程

### 1. 開專案

在 Acer 上：

```bash
cd D:\openclaw-brain\yu-bazi-v29-clean
code .
# 或
explorer .
```

或在 GitHub Codespace / VSCode 開：

```bash
git clone https://github.com/johnyu4916/yu-bazi-v29-clean.git
cd yu-bazi-v29-clean
```

### 2. 開始測試所有流程

```bash
# 測試所有流程
python START_TEST_ALL_FLOWS.py
```

### 3. 測試 8個工作流

```bash
# 列出工作流
ls .github/workflows/

# 應該8個：
# pr-workflow.yml
# push-workflow.yml
# resource-handover-workflow.yml
# full-management-workflow.yml
# secretary-workflow.yml
# registry-workflow.yml
# knowledge-build-workflow.yml
# hardware-inventory-workflow.yml
```

### 4. 測試管理清單版本管理

```bash
# 查版本
git log --oneline -- WORKFLOW_MANAGEMENT_LIST.md
cat WORKFLOW_MANAGEMENT_LIST.md
cat WORKFLOW_REGISTRY.md
```

GitHub App: Code -> WORKFLOW_MANAGEMENT_LIST.md -> History

### 5. 測試引擎 12時財入庫不撞牆

```bash
python knowledge_slicer_V29.3_strict_whitelist.py
# 或
python -c "
import importlib.util
spec = importlib.util.spec_from_file_location('eng','knowledge_slicer_V29.3_strict_whitelist.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
eng = mod.KnowledgeSlicerV29_3_Strict()
bazi={'branches':['卯','午','子','午'],'tiangan':['乙','壬','壬','丙']}
liuyun={'branches':['午','戌','戌','申'],'tiangan':['丙','戊','甲','壬']}
print(eng.final_converge_duan(bazi, liuyun))
"
```

應該：無錯誤訊息 財入庫不撞牆

### 6. 測試 Telegram 報告

```bash
python telegram/daily_pr_report.py
python telegram/resource_handover_report.py
cat D:\openclaw-brain\logs\daily_pr_report_*.md
```

Telegram 問 OpenClaw：今天做了多少 pr

### 7. 測試推送 GitHub 真實PR

```bash
# 在 Acer 上 D:\openclaw-brain\yu-bazi-v29-clean\
git status
git add .
git commit -m "工作流管理清單 版本管理 連清單也版控 8個工作流"
git push origin main
gh pr list --json number,title
```

GitHub App 一查 PR 數量 真實算進度

### 8. 測試守紀律

- 沒推送算0進度
- 多跳一步退回前紀錄點 V29.0 Clean 13KB
- 跟切片沒關字眼出現就是錯誤訊息
- 連清單也在GitHub上有版本管理
- 不合併等老闆允許

### 完成

全部測試完 回報：

```
老闆 開始測試所有流程 完成
工作流 8個 已建 已版控
管理清單 2個 已版控
引擎 12時財入庫不撞牆 白名單通過
Telegram報告 已建
知識庫 26.3%誠實
GitHub PR 0個 真實
```

### OpenClaw 秘書

以後 openclaw 是你的秘書 建造好所有工作流 並有一個工作流管理清單
連清單也在GitHub上有版本管理
