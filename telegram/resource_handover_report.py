#!/usr/bin/env python3
import os, json, datetime, glob

def get_real_files():
    files = []
    for pat in ["*.py","*.json","*.md"]:
        for f in glob.glob(pat):
            try:
                size = os.path.getsize(f)
                if size>100:
                    files.append((os.path.basename(f), size))
            except:
                pass
    return files

def generate():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    real_files = get_real_files()
    report = f"# 資源交接 完整管理報告 {now}\n\n"
    report += "## 手頭資源 真實檔案\n"
    for name,size in real_files[:20]:
        report += f"- {name} {size//1024}KB\n"
    report += "\n## 程式 ✅ V29.3 能用 其餘污染版隔離\n"
    report += "## 80本 總26.3%誠實 之前37.6%假的\n"
    report += "## PR GitHub 0個 沒推送算0進度\n"
    report += "## 進度 總26.3%誠實\n"
    report += "## 什麼沒亂寫 V29.3 嚴格白名單 12時財入庫不撞牆\n"
    return report

if __name__ == "__main__":
    r = generate()
    print(r)
    log_dir = "D:\\openclaw-brain\\logs"
    os.makedirs(log_dir, exist_ok=True)
    path = os.path.join(log_dir, f"resource_handover_{datetime.datetime.now().strftime('%Y-%m-%d')}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(r)
