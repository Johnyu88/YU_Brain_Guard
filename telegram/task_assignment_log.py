
import datetime, os
TASKS_FILE = "logs/TASKS.md"
def assign_task(task_id, title, desc):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n## {task_id} {title} {now}\n- {desc}\n- 狀態 已交代\n"
    os.makedirs(os.path.dirname(TASKS_FILE), exist_ok=True)
    open(TASKS_FILE, "a", encoding="utf-8").write(entry)
    print(f"任務已交代 {task_id}")
if __name__ == "__main__":
    assign_task("TASK-001", "PR工作流", "pr-workflow.yml 12時財入庫")
    assign_task("TASK-002", "推送工作流", "push-workflow.yml")
    assign_task("TASK-003", "資源交接", "誠實盤點26.3%")
