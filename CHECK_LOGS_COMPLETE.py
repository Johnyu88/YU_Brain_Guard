
import os, glob
checks = [
    ("任務交代Log", ["logs/TASKS.md", "telegram/task_assignment_log.py"]),
    ("完成回報Log", ["logs/COMPLETION.md", "telegram/completion_report.py"]),
    ("PR報告Log", ["telegram/daily_pr_report.py"]),
    ("資源交接Log", ["telegram/resource_handover_report.py"]),
    ("工作流執行Log", ["telegram/workflow_execution_log.py"]),
    ("管理清單", ["WORKFLOW_MANAGEMENT_LIST.md"]),
    ("版本歷史", ["VERSION_HISTORY.md"]),
    ("引擎", ["knowledge_slicer_V29.3_strict_whitelist.py"]),
    ("知識庫", ["kb_complete_body_map_V28.3_full_sources.json"]),
]
complete=0
for name, paths in checks:
    found=False
    for pat in paths:
        if os.path.exists(pat) or glob.glob(pat):
            found=True
            break
    if found:
        print(f"✅ {name} 完備")
        complete+=1
    else:
        print(f"❌ {name} 未建")
print(f"完備 {complete}/{len(checks)}")
