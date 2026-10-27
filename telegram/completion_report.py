
import datetime, os
COMPLETION_FILE = "logs/COMPLETION.md"
def report_completion(task_id, result):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n## {task_id} 完成 {now}\n- 結果 {result}\n- 狀態 已完成 待驗收\n"
    os.makedirs(os.path.dirname(COMPLETION_FILE), exist_ok=True)
    open(COMPLETION_FILE, "a", encoding="utf-8").write(entry)
    print(f"完成回報 {task_id}")
if __name__ == "__main__":
    report_completion("TASK-001", "PR工作流已建")
    report_completion("TASK-002", "推送工作流已建")
