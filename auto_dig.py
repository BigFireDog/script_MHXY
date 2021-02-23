import public
import multipro_ui

# 使用前提,打开自动战斗
# 初始化脚本
def auto_dig_start(title, x, y, num, window_is_used,heyao_VarDis):
    try:
        window_is_used[num] = 0
        public.init_script(title, x, y)
        count = 0
        flag_out = 1
        while flag_out == 1:
            public.close_all()

            # 检查自动战斗,未打开则打开
            flag = public.get_auto_fight_status()
            print("准备打开自动战斗")
            if flag != 1:
                # 打开自动战斗,准备打开
                public.left_click(674, 27 + public.offset)
                public.sleep(0.5)
                public.left_click(651, 175 + public.offset)
                public.sleep(0.5)
                public.left_click(523,363 + public.offset)
                public.sleep(0.5)
                public.left_click(424, 156 + public.offset)
                public.sleep(0.5)
                public.left_click(425, 217 + public.offset)
                public.sleep(0.5)
                public.left_click(541, 289 + public.offset)
                public.sleep(0.5)
                public.left_click(622, 33 + public.offset)
                public.sleep(0.5)

            # 获取宝图信息
            Treasure_Map = public.get_Treasure_Map_intxy()
            public.sleep(0.5)
            print(Treasure_Map)
            # 加血
            if heyao_VarDis==1:
                public.jiaxue()

            # 初始化参数
            intxy_all = public.where_am_i()

            for i in range(0, int(len(Treasure_Map))):
                # 重置战斗
                public.left_click(549, 322 + public.offset)
                print("开始挖图")
                public.goto_intxy(Treasure_Map[i][0], Treasure_Map[i][1],intxy_all)
                public.open_box()
                public.sleep(2)
                public.left_click(Treasure_Map[i][2], Treasure_Map[i][3])
                public.left_double_click(Treasure_Map[i][2], Treasure_Map[i][3])
                public.close_all()
                public.sleep(1)
                # 判断战斗状态,如果进入战斗则等待
                n = 0
                while public.get_fight_status():
                    print("战斗中,等待1秒")
                    public.sleep(1)
                    n = n + 1
                    if n > 200:
                        break
                if heyao_VarDis == 1:
                    public.jiaxue()

            Treasure_Map = public.get_Treasure_Map_intxy()

            if len(Treasure_Map) == 0:
                print("\n=======背包内宝图挖掘完毕========")
                flag_out = 0
            else:
                count = count + 1
                print("\n==========背包内宝图未挖掘完毕,准备重新开始,当前未第%d次========" % count)

            # 背包清空或者挖掘三次后背包依然有宝图则退出
            if count == 3:
                print("\n===========挖掘3次背包内宝图依然未挖掘完毕,准备退出========")
                flag_out = 0

    except Exception as e:
        multipro_ui.tkinter.messagebox.showerror('错误', repr(e))
    finally :
        window_is_used[num] = 1