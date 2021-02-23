import public
import archive
import auto_dig
import multipro_ui

# 使用前提,打开自动战斗
# 初始化脚本
def auto_dig_story_start(title, x, y, num, window_is_used, heyao_VarDis):
    try:
        #初始化
        window_is_used[num] = 0
        public.init_script(title, x, y)
        public.close_all()
        public.left_click(370, 93 + public.offset)
        public.left_click(206, 283 + public.offset)
        public.left_click(601, 141 + public.offset)
        public.left_click(370, 202 + public.offset)
        where = public.where_am_i()
        if where != [164, 50, 243, 47, 318, 48, 647, 30]:
            print("准备前往长安")
            public.goto_map(26)
        #清理背包
        archive.arch_start(title, x, y, num, window_is_used)
        public.sleep(0)
        public.goto_intxy(348, 243,[164, 50, 243, 47, 318, 48, 647, 30])
        public.open_story()
        archive_list = public.find_arch_item()
        public.story_all_item_for_dig(archive_list)

        for i in range(10, 26):
            #取宝图
            public.choose_story(i)
            tre_map_list = public.check_stroy(public.Treasure_Map)
            print("发现%d号仓库有%s张宝图" % (i, int(len(tre_map_list))))
            if int(len(tre_map_list))==0:
                continue
            for item in tre_map_list:
                xy_int = [public.story_1[0] + public.story_box_offset[0] * item[1],
                          public.story_1[1] + public.story_box_offset[1] * item[0]]
                # 双击宝图位置
                #public.left_click(xy_int[0], xy_int[1])
                public.left_double_click(xy_int[0], xy_int[1])
            public.close_all()

            #挖宝图
            #public.goto_map(i)
            tag = public.goto_map(i)
            if tag == 0:
                print("未能成功前往目的地,跳过本次挖宝")
                if public.where_am_i() != [164, 50, 243, 47, 318, 48, 647, 30]:
                    print("准备前往长安")
                    public.goto_map(26)
                archive.arch_start(title, x, y, num, window_is_used)
                break

            #temp = public.where_am_i()
            #while public.for_gotoxy_intxy[i-10] != temp:
            #   public.goto_map(i)

            auto_dig.auto_dig_start(title, x, y, num, window_is_used, heyao_VarDis)

            #回城
            if public.where_am_i() != [164, 50, 243, 47, 318, 48, 647, 30]:
                public.goto_map(26)

            #清理背包
            #archive.drop_unusefull_item(title, x, y, num, window_is_used)
            archive.arch_start(title, x, y, num, window_is_used)
            public.goto_intxy(348, 243,[164, 50, 243, 47, 318, 48, 647, 30])
            public.open_story()
            archive_list = public.find_arch_item()
            public.story_all_item_for_dig(archive_list)
    except Exception as e:
        multipro_ui.tkinter.messagebox.showinfo('错误', repr(e))
    finally:
        multipro_ui.tkinter.messagebox.showinfo('完成', '%d 挖掘完成' %(num+1))
        window_is_used[num] = 1


