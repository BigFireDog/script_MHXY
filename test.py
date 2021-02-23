import win32com.client
import public
import init
import  auto_dig_all
import multipro_ui
import archive
import ntplib
import time
dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
dm.SetDict(0, "./front/dm_soft.txt") # 设定字库路径
dm.SetDict(1, "./front/dm_soft_for_intxy.txt")
dm.SetDict(2, "./front/item_level.txt")
dm_ret = dm.UseDict(2)  # 使用字库0
init.init_script('夜神模拟器1', 0, 0)
#goto_other_map_list = [beiju, datangjingwai, guojing, changshou, nver, jianye, huaguo, jiangnan, donghaiwan, aolai,wuzhuanguan, zhuzhi, shituo, putuo, mojia, qilin,]

# 10 开始 北俱芦洲,大唐境外,大唐国境,长寿郊外,女儿村,建邺城,花果山,江南野外,东海湾,傲来国,五庄观,朱紫国,狮驼岭,普陀山,墨家村,麒麟山,长安城,长寿村
#public.check_box_empty_num()
'''print(public.check_story_box_empty_num())
print(public.check_story_empty_num())'''

#print(public.where_am_i())
#public.left_click(331,274 + public.offset)
#print(len(public.for_gotoxy_intxy))

'''get_picture(story_storybox[0] + story_storybox_offset[0] * j,
                        story_storybox[1] + story_storybox_offset[1] * i + offset,
                        story_storybox[0] + story_storybox_offset[0] * (j + 1),
                        story_storybox[1] + story_storybox_offset[1] * (i + 1) + offset,
                        str(i) + str(j) + '.bmp')'''
'''window_is_used=[1,1,1,1]
archive.arch_all_story_tra_map('夜神模拟器1', 0, 0, 0, window_is_used)'''
s = dm.Ocr(public.all_item_message[0], public.all_item_message[1], public.all_item_message[2], public.all_item_message[3], "D0CF18-2F3017", 0.8)
print(s)
