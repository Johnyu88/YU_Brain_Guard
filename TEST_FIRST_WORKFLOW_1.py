
import os, datetime, traceback

LOG_FILE = "logs/first_workflow_test.log"

def log(msg):
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{now}] {msg}"
    print(line)
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    open(LOG_FILE, "a", encoding="utf-8").write(line + "\n")

def test_first():
    log("===== 開始測試第一條 =====")
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("engine", "knowledge_slicer_V29.3_strict_whitelist.py")
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        eng = mod.KnowledgeSlicerV29_3_Strict()
        log("引擎載入 V29.3 嚴格白名單版")
        
        bazi={"branches":["卯","午","子","午"],"tiangan":["乙","壬","壬","丙"]}
        liuyun={"branches":["午","戌","戌","申"],"tiangan":["丙","戊","甲","壬"]}
        res = eng.final_converge_duan(bazi, liuyun)
        
        if "錯誤訊息" in res:
            log(f"審核失敗 {res['錯誤訊息']}")
            raise ValueError("白名單失敗")
        log("白名單通過 無黑名單字眼")
        
        if not res.get("財入庫"):
            log("財入庫失敗")
            raise ValueError("財入庫失敗")
        log(f"財入庫成功 {res.get('財入庫')}")
        
        hours = ["子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
        for zhi in hours:
            ly = {"branches":["午","戌","戌",zhi],"tiangan":["丙","戊","甲","壬"]}
            r = eng.final_converge_duan(bazi, ly)
            if "錯誤訊息" in r:
                log(f"{zhi}時 錯誤訊息 {r}")
                raise ValueError(f"{zhi}時 白名單")
            if not r.get("財入庫"):
                log(f"{zhi}時 財入庫空 失敗 {r}")
                raise ValueError(f"{zhi}時 財入庫")
        log("12時窮舉全過 財入庫不撞牆")
        
        import random
        ganzhi = ["甲","乙","丙","丁","戊","己","庚","辛","壬","癸","子","丑","寅","卯","辰","巳","午","未","申","酉","戌","亥"]
        for i in range(5):
            rb = {"branches":[random.choice(ganzhi[10:]) for _ in range(4)], "tiangan":[random.choice(ganzhi[:10]) for _ in range(4)]}
            rl = {"branches":[random.choice(ganzhi[10:]) for _ in range(4)], "tiangan":[random.choice(ganzhi[:10]) for _ in range(4)]}
            eng.final_converge_duan(rb, rl)
        log("隨機5八字不爆 通過")
        
        log("===== 第一條測試 成功 ✅ 做直到對 完成 可以入庫 =====")
        log("入庫就是沒錯了不動了再動就是錯")
        return True
    except Exception as e:
        log(f"失敗 {e}")
        log(traceback.format_exc())
        log(f"有問題 開log {LOG_FILE} 改 繼續試")
        return False

test_first()
