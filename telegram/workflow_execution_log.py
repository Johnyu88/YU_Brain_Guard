
import datetime, os
LOG_FILE = "logs/WORKFLOW_EXECUTION.md"
def log_exec(name, status):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"\n## {name} {now} {status}\n"
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    open(LOG_FILE, "a", encoding="utf-8").write(entry)
    print(f"工作流 {name} {status}")
if __name__ == "__main__":
    log_exec("pr-workflow.yml", "通過")
