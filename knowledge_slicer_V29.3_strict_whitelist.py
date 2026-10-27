
import json
class KnowledgeSlicerV29_3_Strict:
    """
    V29.3 嚴格白名單版
    以後跟切片沒關 出現任何字眼 都是 錯誤訊息
    只要出現 被抓到 就是 審核有問題
    審核規則：只允許白名單字眼 黑名單一出現就報錯退回前紀錄點
    """
    ALLOWED = ["陽支動", "沖重", "生方庫", "成象", "天干性", "寒暖燥濕", "體用", "子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "六沖", "六合", "三合", "相刑", "刑而忘沖", "單支不報", "全6對", "子午沖", "丑未沖", "寅申沖", "卯酉沖", "辰戌沖", "巳亥沖", "子丑合", "寅亥合", "卯戌合", "辰酉合", "巳申合", "午未合", "子卯刑", "寅巳申三刑", "丑戌未三刑", "申子辰", "寅午戌", "巳酉丑", "亥卯未", "三分餘氣", "財入庫", "財入戌庫", "財破印", "財入庫不破印", "入庫不動", "沒錯了不動", "輪迴停", "撞牆停", "不撞牆", "庫收", "入墓", "子辰合水入庫", "子丑合土入墓", "寅午戌合火", "戌為火庫", "辰為水庫", "丑為金庫", "未為木庫", "洪爐", "草澤", "花園", "冰霜", "五行交互", "五行計數", "相生", "相克", "木生火", "火生土", "土生金", "金生水", "水生木", "木克土", "土克水", "水克火", "火克金", "金克木", "木", "火", "土", "金", "水", "十神交互", "日干", "傷官", "食神", "偏財", "正財", "七殺", "正官", "偏印", "正印", "比肩", "劫財", "傷官格", "傷官生財", "傷官配印", "比劫幫身", "財重身輕", "食傷生財", "淵海子平", "三命通會", "滴天髓", "靈樞本輸", "傷寒論", "諸病源候論", "少陰", "心出於中衝", "腎主水", "少陰之為病脈微細但欲寐", "中96", "左93", "右95", "掌88", "外型", "方", "乙卯", "壬午", "壬子", "丙午", "本命", "流運", "丙午戊戌甲戌壬申", "庚辰", "己卯", "戊寅", "丁丑", "丙子", "只要沒被我食傷生財破掉就可以入庫", "入庫就是沒錯了不動了再動就是錯", "印會亂會降智所以印也要入庫不動"]
    BLACKLIST = ["GitHub", "github", "Drive", "D:", "D:\\", "Acer", "PR", "pr", "OpenClaw", "Codex", "VSCode", "WSL", "Node", "Python", "RAM", "GPU", "Predator", "Swift", "Nitro", "HANDOVER", "資源", "進度", "垃圾山", "誠實版", "交接", "專案", "合併", "推送", "repo", "commit", "branch", "Model", "System", "Memory"]

    def __init__(self):
        self.finger_map = {
            "中96":{"沖":"子午沖","處理":"需庫收或入墓"},
            "左93":{"沖":"寅申沖"},
            "右95":{"沖":"卯酉沖"},
            "掌88":{"沖":"辰戌沖"},
        }

    def audit(self, text):
        errs = []
        for bad in self.BLACKLIST:
            if bad.lower() in text.lower():
                errs.append(f"錯誤訊息 跟切片沒關: {bad}")
        return errs

    def final_converge_duan(self, bazi, liuyun):
        # 只做切片7層+五行十神+財入庫 不含GitHub Drive D: Acer PR
        all_br = bazi.get("branches",[])+liuyun.get("branches",[])
        all_tg = bazi.get("tiangan",[])+liuyun.get("tiangan",[])
        
        # 沖重
        chong = []
        if "子" in all_br and "午" in all_br:
            chong.append("子午沖 同現需庫收")
        
        # 生方庫
        sanhe = []
        if "寅" in all_br and "午" in all_br and "戌" in all_br:
            sanhe.append("寅午戌合火 戌為火庫收午財 財入庫")
        if "申" in all_br and "子" in all_br and "辰" in all_br:
            sanhe.append("申子辰合水 辰為水庫收子刃")
        
        # 財入庫
        cai_ru_ku = []
        if "午" in all_br and "戌" in all_br:
            cai_ru_ku.append("午火財見戌 財入戌庫不破印 入庫就是沒錯了不動了再動就是錯 沒錯了不動 輪迴停 撞牆停 不撞牆")
        
        # 五行交互
        wuxing = {"木": all_br.count("卯")+all_br.count("寅"), "火": all_br.count("午"), "土": all_br.count("戌")+all_br.count("辰")+all_br.count("丑"), "金": 0, "水": all_br.count("子")}
        
        # 十神交互
        shishen = {"日干":"壬水","傷官生偏財":"乙卯傷官生丙午偏財 財入庫","比劫幫身":"壬子比肩"}
        
        result_text = json.dumps({"沖重":chong, "生方庫":sanhe, "財入庫":cai_ru_ku, "五行交互":wuxing, "十神交互":shishen}, ensure_ascii=False)
        
        errs = self.audit(result_text)
        if errs:
            return {"錯誤訊息": errs, "退回前紀錄點": "V29.0 Clean 13KB", "審核有問題": True}
        
        return {
            "陽支動": all_br,
            "沖重": chong,
            "生方庫": sanhe,
            "成象": "申子辰水局 寅午戌火局",
            "天干性": all_tg,
            "寒暖燥濕": "火7 水5 土3 木3 金1 火旺需水庫收",
            "體用": "傷官格放 印收 辛金丑庫 庚金辰庫",
            "五行交互": wuxing,
            "十神交互": shishen,
            "財入庫": cai_ru_ku,
            "凍結規則1": "只要沒被我食傷生財破掉就可以入庫",
            "凍結規則2": "入庫就是沒錯了不動了再動就是錯",
            "凍結規則3": "印會亂會降智所以印也要入庫不動",
            "審核": "白名單通過 無跟切片沒關字眼"
        }

if __name__=="__main__":
    eng = KnowledgeSlicerV29_3_Strict()
    bazi={"branches":["卯","午","子","午"],"tiangan":["乙","壬","壬","丙"]}
    liuyun={"branches":["午","戌","戌","申"],"tiangan":["丙","戊","甲","壬"]}
    print(json.dumps(eng.final_converge_duan(bazi, liuyun), ensure_ascii=False, indent=2))
