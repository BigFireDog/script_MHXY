import public
import multipro_ui


# 初始化脚本
def arch_start(title, x, y, num, window_is_used):
    try:
        window_is_used[num] = 0
        public.init_script(title, x, y)
        public.close_all()
        # public.get_picture(578,228+public.offset,601,241+public.offset,'578.bmp')
        # 获取背包宝图列表
        public.drop_unusefull_item()
        Treasure_Map_story_list = public.get_Treasure_Map_map_name_for_archive()
        public.sleep(5)
        print(Treasure_Map_story_list)
        # 检查是否背包内有宝图,如果没有则在20秒后退出脚本
        if not Treasure_Map_story_list:
            print("未发现宝图,退出程序")
            return 1

        # 前往仓管NPC
        public.goto_intxy(348, 243,[164, 50, 243, 47, 318, 48, 647, 30])

        # 打开仓库
        public.sleep(0)
        public.open_story()
        print("归档宝图")
        # 归档宝图
        public.storing_Treasure_Map(Treasure_Map_story_list)
    except Exception as e:
        multipro_ui.tkinter.messagebox.showerror('错误', repr(e))
    finally:
        window_is_used[num] = 1

def arch_all_story_tra_map(title, x, y, num, window_is_used):
    try:
        public.init_script(title, x, y)
        window_is_used[num] = 0
        flag=public.where_am_i()
        if flag != [164, 50, 243, 47, 318, 48, 647, 30]:
            public.goto_map(26)

        # 清理背包
        arch_start(title, x, y, num, window_is_used)
        flag=0
        end=1
        i = 1
        while end==1:
            if i==10:
                break
            if flag==0:
                public.goto_intxy(348, 243, [164, 50, 243, 47, 318, 48, 647, 30])
                public.open_story()
                public.sleep(1)
            box_num = len(public.check_story_box_empty_num())
            public.choose_story(i)
            public.sleep(1)
            tre_map_list = public.check_stroy(public.Treasure_Map)
            print("发现%d号仓库有%s张宝图" % (i, int(len(tre_map_list))))
            if int(len(tre_map_list)) == 0:
                flag=1
                i=i+1
                continue
            for item in tre_map_list:
                xy_int = [public.story_1[0] + public.story_box_offset[0] * item[1],
                          public.story_1[1] + public.story_box_offset[1] * item[0]]
                # 双击宝图位置
                # public.left_click(xy_int[0], xy_int[1])
                public.left_double_click(xy_int[0], xy_int[1])
                box_num = box_num - 1
                if box_num == 0:
                    arch_start(title, x, y, num, window_is_used)
                    i=i-1
                    break
            i = i + 1
    except Exception as e:
        multipro_ui.tkinter.messagebox.showerror('错误', repr(e))
    finally:
        arch_start(title, x, y, num, window_is_used)
        window_is_used[num] = 1


