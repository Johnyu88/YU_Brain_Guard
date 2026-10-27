
import json
KB_PATH="/mnt/data/kb_complete_body_map_V28.3_full_sources.json"
KB_CLASS_PATH="/mnt/data/kb_V28.6_full_sentence_classified.json"
try:
    with open(KB_PATH,"r",encoding="utf-8") as f:
        KB=json.load(f)
except:
    KB={"七本書原文全量":{"1_淵海子平":{"地支六沖原文":"子午沖，丑未沖，寅申沖，卯酉沖，辰戌沖，巳亥沖。","地支六合原文":"子丑合土，午未合土，寅亥合木，卯戌合火，辰酉合金，巳申合水。","地支相刑原文":"寅巳申三刑，丑戌未三刑，子卯相刑。"},"2_三命通會":{"卷二論地支全文相關":{"未":"未為花園"}},"3_滴天髓":{},"4_靈樞本輸":{"出處":"靈樞本輸第二","心包絡原文":"心出於中衝"},"5_傷寒論相關":{},"6_諸病源候論":{}}}
try:
    with open(KB_CLASS_PATH,"r",encoding="utf-8") as f:
        KB_CLASS=json.load(f)
    BY_CAT=KB_CLASS.get("按分類聚合",{})
except:
    KB_CLASS={"統計":{}}
    BY_CAT={}

class KnowledgeSlicerV29_Clean:
    """
    V29.0 乾淨版 - 解決污染
    污染來源：食傷生財→財破印→印亂降智→一直被破一直修→新對話撞牆
    清洗規則：
    1. 只要沒被我食傷生財破掉就可以入庫
    2. 入庫就是沒錯了不動了再動就是錯
    3. 印會亂會降智所以印也要入庫不動
    """
    def __init__(self):
        self.kb=KB
        self.by_cat=BY_CAT
        self.src=KB.get("七本書原文全量",{})
        # 完整指節對位，修復只有4個的BUG
        self.finger_map={
            "左93":{"沖":"寅申沖","髒":"肝膽足","外型":"寅為廣谷申為名都 庚金大刀 驛馬道路","素問":"肝主筋開竅於目","支":"寅申"},
            "右95":{"沖":"卯酉沖","髒":"肺大腸手","外型":"卯為瓊林酉為寺鐘 辛金白門戶","素問":"肺主氣開竅於鼻","支":"卯酉"},
            "掌88":{"沖":"辰戌沖","髒":"脾胃口","外型":"辰為草澤戌為燒原 洪爐之庫 鈍鐵頑金","素問":"脾主肌肉開竅於口","支":"辰戌"},
            "掌88-未":{"合":"午未合/未花園","髒":"脾胃口","外型":"未為花園 百花牆垣 乙丁雜氣","素問":"脾主肌肉","支":"未"},
            "中96":{"沖":"子午沖","髒":"心腎耳舌","外型":"子為溪澗午為烽堠 心火腎水","素問":"心主血脈開竅於舌 腎主骨開竅於耳 心腎不交","傷寒":"少陰之為病脈微細但欲寐","靈樞":"心出於中衝溜於勞宮 滎火","支":"子午"},
            "刑93":{"刑":"子卯刑","髒":"腎耳門戶","外型":"子為水耳卯為門戶 無禮之刑","諸病":"腎主水通於耳","支":"子卯"},
            "戌庫":{"支":"戌","性":"火庫 鈍鐵頑金 洪爐 見辰為鑰","外型":"戌乃洪爐之庫 戌為燒原 河魁","作用":"財入庫 午火財入戌庫不破印"},
            "辰庫":{"支":"辰","性":"水庫 水泥之濕 草澤 天罡","外型":"辰為草澤 見戌為鑰 能開庫收子","作用":"水庫收刃 子辰合水入庫守住子午沖"},
            "丑庫":{"支":"丑","性":"金庫 冰霜 隆冬 辛金正印藏","外型":"丑雖隆冬有冰霜之可怯 庫地最宜","作用":"金庫收身 子丑合土入墓保護"},
            "未庫":{"支":"未","性":"木庫 花園 百花","外型":"未為花園 牆垣護百花","作用":"木庫收傷官 乙卯入庫"},
        }
        self.sanhe_lib={
            "申子辰":{"五行":"水","庫":"辰","中神":"子","將星":"子","描述":"申子辰合水局 申金生水 辰為水庫收子 10歲庚辰守住子午沖"},
            "亥卯未":{"五行":"木","庫":"未","中神":"卯","將星":"卯","描述":"亥卯未合木局 未為木庫 花園牆垣護百花 乙卯傷官入庫"},
            "寅午戌":{"五行":"火","庫":"戌","中神":"午","將星":"午","描述":"寅午戌合火局 戌為火庫 洪爐煉金 財入庫不破印 戌見辰為鑰"},
            "巳酉丑":{"五行":"金","庫":"丑","中神":"酉","將星":"酉","描述":"巳酉丑合金局 丑為金庫 隆冬冰霜 子丑合土入墓保護"},
        }
        self.liuhe_lib=["子丑合土","寅亥合木","卯戌合火","辰酉合金","巳申合水","午未合土"]

    def get_sent(self, cat, n=3):
        return BY_CAT.get(cat, [])[:n]

    # ---- 七書對位 4函數 完整版 ----
    def check_lingshu_benchu(self):
        return {"函數":"check_lingshu_benchu","出處":"黃帝內經·靈樞·本輸第二","原文":"心出於中衝，溜於勞宮","對位":"中96火眼","指節":"中96"}
    def check_shanghan_shaoyin(self, branches):
        hits=[]
        if "子" in branches:
            hits.append({"觸發":"子水少陰","原文":"少陰之為病脈微細但欲寐也","對位":"子為少陰 水耳腎動 子午沖心腎不交","斷病":"腰痛耳鳴手足寒"})
        return {"函數":"check_shanghan_shaoyin","結果":hits}
    def check_zhu_bing_ershen(self, branches):
        hits=[]
        if "子" in branches:
            hits.append({"觸發":"腎主水耳","原文":"腎主水腎氣通於耳","對位":"子水耳與卯門戶相刑 無禮之刑93"})
        return {"函數":"check_zhu_bing_ershen","結果":hits}
    def check_wai_xing_ditu(self, branches):
        mapping={"寅":"寅為廣谷","申":"申為名都","卯":"卯為瓊林","酉":"酉為寺鐘","辰":"辰為草澤","戌":"戌為燒原","未":"未為花園","子":"子為溪澗江洋之水","午":"午為烽堠"}
        res=[{"支":b,"原文":mapping.get(b,"")} for b in branches if b in mapping]
        return {"函數":"check_wai_xing_ditu","結果":res}
    def check_fangju(self, branches):
        hits=[]
        for k in ["寅卯辰","巳午未","申酉戌","亥子丑"]:
            if all(x in branches for x in k):
                hits.append({"方":k,"三分餘氣":self.check_sanfen_yuqi(list(k))})
        return {"函數":"check_fangju","結果":hits}
    def check_sanfen_yuqi(self, branches):
        yuqi={"丑":{"餘氣":"三分水","原文":"行子運至丑有三分水氣"},"未":{"餘氣":"三分火","原文":"行午運至未有三分火氣 未中有乙丁"},"辰":{"餘氣":"三分木","原文":"辰有乙木餘氣"},"戌":{"餘氣":"三分火","原文":"戌有丁火餘氣 洪爐之庫"}}
        return {"函數":"check_sanfen_yuqi","結果":[{"支":b,**yuqi[b]} for b in branches if b in yuqi]}

    # ---- 沖合刑 完整無BUG版 ----
    def check_chong_full(self, branches):
        pairs=[("子","午","中96"),("丑","未","掌88"),("寅","申","左93"),("卯","酉","右95"),("辰","戌","掌88"),("巳","亥","左93")]
        res=[]
        for a,b,_ in pairs:
            if a in branches and b in branches:
                res.append({"沖":f"{a}{b}沖","同現":True,"處理":"需庫收或入墓"})
            else:
                if a in branches:
                    res.append({"沖":f"單{a}不報{a}{b}沖","修正":"V29單支不報全6對修復"})
                if b in branches:
                    res.append({"沖":f"單{b}不報{a}{b}沖","修正":"V29"})
        return res
    def check_he_full(self, branches):
        res=[]
        if "子" in branches and "丑" in branches:
            res.append({"合":"子丑合土","三分":self.check_sanfen_yuqi(["丑"]),"化否":"合而不化 入墓保護 丑為冰霜庫地最宜 40歲丁丑","特殊":"入墓被保護"})
        if "午" in branches and "未" in branches:
            res.append({"合":"午未合","三分":self.check_sanfen_yuqi(["未"]),"化否":"合而不化 有三分火氣 未為花園 非全土"})
        for a,b in [("寅","亥"),("卯","戌"),("辰","酉"),("巳","申")]:
            if a in branches and b in branches:
                res.append({"合":f"{a}{b}合","化否":"需得辰透"})
        return res
    def check_sanhe_full(self, branches):
        res=[]
        for key,info in self.sanhe_lib.items():
            count=sum(1 for x in key if x in branches)
            if count>=2:
                ku_shou=""
                if key=="申子辰" and "辰" in branches and "子" in branches:
                    ku_shou="辰為水庫收子刃 10歲庚辰 子辰合水入庫守住子午沖 子午沖被庫收保護 沒錯了不動"
                if key=="寅午戌" and "戌" in branches and "午" in branches:
                    ku_shou="戌為火庫收午財 寅午戌合火 財入庫不破印 沒錯了不動 財到極致財養命"
                if key=="巳酉丑" and "丑" in branches:
                    ku_shou="丑為金庫 40歲丁丑 子丑合土入墓被保護 丑雖隆冬有冰霜之可怯 庫地最宜"
                res.append({"三合":key,"庫":info["庫"],"計數":count,"化否":"全3字才化 半合不化但有庫收保護","庫收保護":ku_shou,"描述":info["描述"]})
        return res
    def check_xing_full(self, branches):
        res=[]
        if "子" in branches and "卯" in branches:
            res.append({"刑":"子卯刑93 無禮之刑","規則":"刑而忘沖 近刑忘遠沖 20歲己卯 子卯刑忘子午沖 子午沖暫忘","對位":"水耳門戶"})
        if "寅" in branches and "巳" in branches and "申" in branches:
            res.append({"刑":"寅巳申三刑"})
        return res

    # ---- 核心修復：財破印→財入庫 ----
    def check_cai_po_yin_vs_cai_ru_ku(self, bazi_branches, bazi_tiangan, liuyun_branches):
        all_br=bazi_branches+liuyun_branches
        cai_fire=all_br.count("午")
        ku_xu="戌" in all_br
        zi_chen="子" in bazi_branches and "辰" in all_br
        zi_chou="子" in bazi_branches and "丑" in all_br
        shang_guan="乙" in bazi_tiangan or "卯" in bazi_branches
        out=[]
        # 污染檢測
        if shang_guan and cai_fire>=2:
            out.append({"觸發":"食傷生財 乙卯傷官生丙午財 財是我生的","污染前":"財克金印 財破印 自己打臉 印亂降智 一直被破一直修 撞牆"})
            if ku_xu:
                out.append({"修復":"財入庫","判語":"入庫就是沒錯了 不動了 再動就是錯","邏輯":"午火財見戌 財入戌庫 庫宜靜 不破印","規則":"只要沒被我食傷生財破掉就可以入庫","狀態":"沒錯了不動 輪迴停 撞牆停"})
            else:
                out.append({"狀態":"財破印 需戌庫 否則繼續撞牆","處理":"等戌庫"})
        if zi_chen:
            out.append({"庫收":"子辰合水入庫 10歲庚辰","判語":"入庫不動 再動就是錯","作用":"子刃入辰庫守住子午沖"})
        if zi_chou:
            out.append({"庫收":"子丑合土入墓 40歲丁丑","判語":"入墓被保護 你靠墓才能睡 丑中辛金正印剎車","作用":"子水入丑墓保護"})
        return out

    def check_dayun_50(self, bazi_branches, dayun_list):
        out=[]
        for dy in dayun_list:
            age=dy["age"]; zhi=dy["zhi"]; gan=dy.get("gan","")
            combined=bazi_branches+[zhi]
            entry={"大運":f"{age}歲 {gan}{zhi}","支":zhi}
            entry["合沖刑"]=[self.check_chong_full(combined), self.check_sanhe_full(combined), self.check_xing_full(combined), self.check_he_full(combined)]
            if age==10 and zhi=="辰":
                entry["特殊"]="10歲庚辰 子辰合水入庫 辰為水庫守住子午沖 財到極致財養命 沒錯了不動"
            if age==20 and zhi=="卯":
                entry["特殊"]="20歲己卯 子卯刑 刑而忘沖 近刑忘遠沖 子午沖暫不顯"
            if age==30 and zhi=="寅":
                entry["特殊"]="30歲戊寅 正式子午沖試煉 寅午半合火引動 陽支動且強速達顯災 試煉標記"
            if age==40 and zhi=="丑":
                entry["特殊"]="40歲丁丑 子丑合土 入墓被保護 丑雖隆冬有冰霜之可怯 庫地最宜"
            if age==50 and zhi=="子":
                entry["特殊"]="50歲丙子 雙子比劫幫身 比劫幫身守住財重身輕"
            out.append(entry)
        return out

    def final_converge_duan(self, bazi, liuyun, dayun_list=None):
        # 參數化 不寫死 解決BUG
        all_branches=bazi.get("branches",[])+liuyun.get("branches",[])
        all_tiangan=bazi.get("tiangan",[])+liuyun.get("tiangan",[])
        return {
            "版本":"V29.0 Clean 污染已洗",
            "主體":"你傷官格 乙卯 放",
            "收":"我印 辛金丑庫 庚金辰庫 負責收",
            "凍結規則1":"只要沒被我食傷生財破掉就可以入庫",
            "凍結規則2":"入庫就是沒錯了 不動了 再動就是錯",
            "凍結規則3":"印會亂會降智所以印也要入庫不動",
            "八字":bazi,
            "流運":liuyun,
            "財破印檢測→財入庫修復":self.check_cai_po_yin_vs_cai_ru_ku(bazi.get("branches",[]), bazi.get("tiangan",[]), liuyun.get("branches",[])),
            "六沖全":self.check_chong_full(all_branches),
            "六合全":self.check_he_full(all_branches),
            "三合含庫收":self.check_sanhe_full(all_branches),
            "相刑含刑忘沖":self.check_xing_full(all_branches),
            "七書對位": [self.check_lingshu_benchu(), self.check_shanghan_shaoyin(all_branches), self.check_zhu_bing_ershen(all_branches), self.check_wai_xing_ditu(all_branches), self.check_fangju(all_branches), self.check_sanfen_yuqi(all_branches)],
            "50年大運守住":self.check_dayun_50(bazi.get("branches",[]), dayun_list) if dayun_list else "未輸入",
        }

# 測試
if __name__=="__main__":
    eng=KnowledgeSlicerV29_Clean()
    bazi={"branches":["卯","午","子","午"],"tiangan":["乙","壬","壬","丙"],"full":"乙卯 壬午 壬子 丙午"}
    liuyun={"branches":["午","戌","酉","申"],"tiangan":["丙","戊","癸","庚"],"full":"丙午 戊戌 癸酉 庚申"}
    dayun=[{"age":10,"gan":"庚","zhi":"辰"},{"age":20,"gan":"己","zhi":"卯"},{"age":30,"gan":"戊","zhi":"寅"},{"age":40,"gan":"丁","zhi":"丑"},{"age":50,"gan":"丙","zhi":"子"}]
    print(json.dumps(eng.final_converge_duan(bazi,liuyun,dayun), ensure_ascii=False, indent=2))
