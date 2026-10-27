# GitHub 有一套 D:也有 同步

## 結構

GitHub:
- github.com/johnyu4916/yu-bazi-v29-clean
- 8個工作流 .github/workflows/*.yml
- WORKFLOW_MANAGEMENT_LIST.md 版控
- 引擎 V29.3
- 知識庫 14KB

D:
- D:\openclaw-brain\yu-bazi-v29-clean
- 同樣 8個工作流
- 同樣 WORKFLOW_MANAGEMENT_LIST.md
- 同樣 引擎 V29.3
- 同樣 知識庫
- 加上 logs/ 完整Log
- 加上 acer_hardware_full.json 真實硬體

## 同步命令

Acer上 D槽同步到GitHub：

```bash
cd D:\openclaw-brain\yu-bazi-v29-clean
git add .
git commit -m "同步 D:到GitHub"
git push origin main
```

GitHub同步到D槽：

```bash
cd D:\openclaw-brain\yu-bazi-v29-clean
git pull origin main
```
