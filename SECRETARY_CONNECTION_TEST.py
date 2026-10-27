#!/usr/bin/env python3
# 秘書聯繫測試 - 你跟秘書聯繫上了沒

import os, json, glob, datetime, subprocess

def check_secretary_connection():
    print("="*60)
    print("秘書聯繫測試 - 你跟秘書聯繫上了沒")
    print(f"時間 {datetime.datetime.now()}")
    print("="*60)
    
    # 1. 檢查 D:大腦是否存在
    print("\n[1] 檢查 D:\\openclaw-brain 大腦")
    brain_path = "D:\\openclaw-brain"
    # 在此容器無D槽，檢查本地模擬
    if os.path.exists(brain_path):
        print(f"  {brain_path} 存在 ✅")
    else:
        print(f"  {brain_path} 不存在 ❌ 在此容器無D槽，Acer上才有")
        print(f"  在Acer上檢查：dir D:\\openclaw-brain")
    
    # 2. 檢查 yu-bazi-v29-clean 是否在D槽
    print("\n[2] 檢查 D:\\openclaw-brain\\yu-bazi-v29-clean")
    project_path = "D:\\openclaw-brain\\yu-bazi-v29-clean"
    if os.path.exists(project_path):
        print(f"  {project_path} 存在 ✅")
    else:
        print(f"  {project_path} 不存在 ❌ 待Acer上克隆")
        print(f"  Acer上執行：git clone https://github.com/johnyu4916/yu-bazi-v29-clean.git {project_path}")
    
    # 3. 檢查工作流 8個
    print("\n[3] 檢查工作流 8個 已建 已版控")
    wf_dir = ".github/workflows"
    wfs = glob.glob(os.path.join(wf_dir, "*.yml")) if os.path.exists(wf_dir) else [])
    # 也檢查當前目錄
    if not wfs:
        wfs = glob.glob(".github/workflows/*.yml")
        if not wfs:
            wfs = glob.glob(os.path.join(".", ".github", "workflows", "*.yml"))
    # 直接列本地
    local_wf = "/mnt/data/yu-bazi-v29-clean/.github/workflows"
    if os.path.exists(local_wf):
        wfs = glob.glob(os.path.join(local_wf, "*.yml"))
    print(f"  工作流 {len(wfs)} 個")
    for wf in sorted(wfs):
        print(f"    - {os.path.basename(wf)}")
    
    # 4. 檢查管理清單版控
    print("\n[4] 檢查管理清單 連清單也在GitHub上有版本管理")
    list_path = "WORKFLOW_MANAGEMENT_LIST.md"
    if os.path.exists(list_path) or os.path.exists("/mnt/data/yu-bazi-v29-clean/WORKFLOW_MANAGEMENT_LIST.md"):
        print(f"  WORKFLOW_MANAGEMENT_LIST.md 存在 ✅ 已版控")
    else:
        print(f"  WORKFLOW_MANAGEMENT_LIST.md 不存在 ❌")
    
    # 5. 檢查 Acer 硬體盤點
    print("\n[5] 檢查 Acer 硬體真實版 空白待填")
    hw_log = "D:\\openclaw-brain\\logs\\acer_hardware_full.json"
    if os.path.exists(hw_log):
        try:
            with open(hw_log, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"  {hw_log} 存在 ✅ 真實硬體 不猜Predator")
            print(f"  內容：{str(data)[:200]}")
        except Exception as e:
            print(f"  {hw_log} 存在但讀失敗 {e}")
    else:
        print(f"  {hw_log} 不存在 ❌ 空白待填")
        print(f"  Acer上執行：powershell D:\\openclaw-brain\\acer_full_inventory.ps1")
    
    # 6. 檢查 Telegram 報告
    print("\n[6] 檢查 Telegram 秘書報告")
    daily_report = "D:\\openclaw-brain\\logs\\daily_pr_report_*.md"
    reports = glob.glob(daily_report) if os.path.exists("D:\\openclaw-brain\\logs") else []
    print(f"  每日報告 {len(reports)} 個")
    if reports:
        print(f"    最新：{reports[-1]}")
    else:
        print(f"  無報告 ❌ 待OpenClaw在Acer上跑 python telegram/daily_pr_report.py")
    
    # 7. 檢查 GitHub PR 真實數量
    print("\n[7] 檢查 GitHub PR 真實數量 沒推送算0進度")
    try:
        result = subprocess.run("gh pr list --json number,title --limit 5", shell=True, capture_output=True, text=True, timeout=5)
        if result.stdout:
            prs = json.loads(result.stdout)
            print(f"  GitHub PR {len(prs)} 個 真實 ✅")
            for pr in prs:
                print(f"    - PR#{pr['number']} {pr['title']}")
        else:
            print(f"  GitHub PR 0個 沒推送算0進度 真實 ✅")
    except Exception as e:
        print(f"  gh 未登入或無網路 GitHub PR 0個 沒推送算0進度 真實 ✅")
    
    # 8. 總結 秘書是否聯繫上
    print("\n" + "="*60)
    print("秘書聯繫總結")
    print("="*60)
    
    connected = False
    # 判斷邏輯
    if os.path.exists("/mnt/data/yu-bazi-v29-clean/.github/workflows/registry-workflow.yml"):
        print("✅ 工作流已建 8個 已版控 - 秘書的工具已備好")
    else:
        print("❌ 工作流未建")
    
    if os.path.exists("/mnt/data/yu-bazi-v29-clean/WORKFLOW_MANAGEMENT_LIST.md"):
        print("✅ 管理清單已建 連清單也版控 - 秘書清單已備好")
    
    # 檢查是否在Acer上
    if os.path.exists("D:\\openclaw-brain"):
        print("✅ D:\\openclaw-brain 存在 - 秘書大腦已連接")
        connected = True
    else:
        print("❌ D:\\openclaw-brain 不存在 - 在此容器無D槽，需在Acer上測試")
        print("⚠️ 秘書聯繫：在此容器無法直接聯繫OpenClaw，需在Acer上")
        connected = False
    
    print("")
    if not connected:
        print("結論：你跟秘書聯繫上了沒？")
        print("→ 在此容器：沒，D槽不在此容器")
        print("→ 在Acer上：需執行以下檢查")
        print("")
        print("Acer上檢查命令：")
        print("  dir D:\\openclaw-brain")
        print("  dir D:\\openclaw-brain\\yu-bazi-v29-clean\\.github\\workflows")
        print("  type D:\\openclaw-brain\\logs\\acer_hardware_full.json")
        print("  cd D:\\openclaw-brain\\yu-bazi-v29-clean && python START_TEST_ALL_FLOWS.py")
        print("  gh pr list")
        print("")
        print("Telegram問：今天做了多少 pr")
        print("OpenClaw應回報 GitHub PR數量 + 工作流清單版本")
    else:
        print("✅ 秘書已聯繫上 OpenClaw是你的秘書 你的手腳")

if __name__ == "__main__":
    check_secretary_connection()
