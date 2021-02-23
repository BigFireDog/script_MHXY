import random
import time
import tkinter
from operator import itemgetter
import win32com.client

offset = 36
intX = 0
intY = 0

# 定义图片路径
Treasure_Map = './image/宝图.bmp'
she_yao_xiang = './image/摄药香.bmp'
shijian = './image/时间.bmp'
quxiao_bmp = ['./image/取消.bmp', './image/取消1.bmp']
map_x_bmp = ['./image/map_x_bmp.bmp', './image/map_x_bmp_1.bmp']
map_y_bmp = ['./image/map_y_bmp.bmp', './image/map_y_bmp_1.bmp']
x_no_1 = ['./image/x_no_1.bmp', './image/x_no_1_1.bmp']
y_no_1 = ['./image/y_no_1_1.bmp', './image/y_no_1.bmp']
qianwang_bmp = './image/qianwang.bmp'
kongwei_bmp = './image/kongwei.bmp'
zhandou = './image/战斗.bmp'
zidongzhandou = './image/自动战斗.bmp'
xiang_bmp = './image/xiang.bmp'
feifei_bmp = './image/feifei.bmp'
tie_bmp = './image/qita/铁.bmp'
shu_bmp = './image/qita/书.bmp'
weapon_70_bmp = './image/zhuangbei70/weapon/刀70.bmp|./image/zhuangbei70/weapon/刺70.bmp|./image/zhuangbei70/weapon/宝珠70.bmp|./image/zhuangbei70/weapon/对剑70.bmp|./image/zhuangbei70/weapon/杖70.bmp|./image/zhuangbei70/weapon/枪70.bmp|./image/zhuangbei70/weapon/棒70.bmp'
weapon_60_bmp = './image/zhuangbei60/weapon/剑60.bmp|./image/zhuangbei60/weapon/宝珠60.bmp|./image/zhuangbei60/weapon/对剑60.bmp|./image/zhuangbei60/weapon/扇子60.bmp|./image/zhuangbei60/weapon/灯笼60.bmp|./image/zhuangbei60/weapon/环60.bmp|./image/zhuangbei60/weapon/镰刀60.bmp|./image/zhuangbei60/weapon/鞭子60.bmp'
other_70_bmp = './image/zhuangbei70/other/帽子70.bmp|./image/zhuangbei70/other/腰带70.bmp|./image/zhuangbei70/other/鞋70.bmp|./image/zhuangbei70/other/项链70.bmp'
other_60_bmp = './image/zhuangbei60/other/60女衣.bmp|./image/zhuangbei60/other/头盔60.bmp'
high_gemstone_bmp = './image/baoshi/光芒.bmp|./image/baoshi/舍利子.bmp|./image/baoshi/月亮石.bmp'
low_gemstone_bmp = ''
high_wubao_bmp = ''
low_wubao_bmp = ''
gold_dew = './image/qita/金柳露.bmp'
elixir = './image/qita/内丹.bmp'
# 检查XY输入窗口范围的坐标
find_map_xy_intxy = [[85, 34 + offset], [414, 27 + offset]]
# 所在地图的窗口
map_zone = [55, 12 + offset, 126, 30 + offset]
# 提示信息对话框位置
massage_box_zone = [364, 188 + offset, 555, 214 + offset]
# 坐标显示窗口位置
xy_zone = [56, 32 + offset, 121, 49 + offset]
# 使用按钮坐标
shiyong = [244, 232 + offset]
# 背包按钮坐标
daoju = [655, 396 + offset]
# 仓库背包取消按钮坐标
quxiao = [619, 29 + offset]
# 长安地图取消按钮坐标
quxiao_ditu = [647, 29 + offset]
# 地图按钮坐标
ditu = [23, 32 + offset]
pingbi = [25, 145 + offset]
huifu = [27, 386 + offset]
# 仓库编号,1号仓库使用2,5 即8号仓库....
# story_list=([2,0],[2,1],[2,2],[2,3],[2,4],[3,0],[3,1],[3,2],[3,3],[3,4],[4,0],[4,1],[4,2],[4,3],[4,3],[4,4])
# 长安地图前往按钮坐标
changan_qianwang = [316, 53 + offset]

# 仓库管理员坐标
npc_story = [370, 183 + offset]

# 对话框默认按钮位置
default_button = [573, 246 + offset]

# 地图xy坐标抓取范围,0号为左上角坐标,1号为右下角坐标
find_map_xy_intxy_offset = [5, 33]

# 长安地图输入按钮
changan_ditu_inputbox_X = [165, 48 + offset]
changan_ditu_inputbox_Y = [246, 50 + offset]

# 地图X输入坐标的list
# ditu_input_X的n号元素依次为1，2，3，4，5，6，7，8，9，0，确定按钮坐标
ditu_input_X_1 = [0, 0]
ditu_input_offset = 62
ditu_input_X_4 = [ditu_input_X_1[0], ditu_input_X_1[1] + ditu_input_offset]
ditu_input_X_7 = [ditu_input_X_4[0], ditu_input_X_4[1] + ditu_input_offset]

ditu_input_X = [[ditu_input_X_1[0], ditu_input_X_1[1]], [ditu_input_X_1[0] + ditu_input_offset, ditu_input_X_1[1]],
                [ditu_input_X_1[0] + ditu_input_offset * 2, ditu_input_X_1[1]],
                [ditu_input_X_1[0], ditu_input_X_1[1] + ditu_input_offset],
                [ditu_input_X_4[0] + ditu_input_offset, ditu_input_X_4[1]],
                [ditu_input_X_4[0] + ditu_input_offset * 2, ditu_input_X_4[1]],
                [ditu_input_X_4[0], ditu_input_X_4[1] + ditu_input_offset],
                [ditu_input_X_7[0] + ditu_input_offset, ditu_input_X_7[1]],
                [ditu_input_X_7[0] + ditu_input_offset * 2, ditu_input_X_7[1]],
                [ditu_input_X_4[0] + ditu_input_offset * 3, ditu_input_X_4[1]],
                [ditu_input_X_4[0] + ditu_input_offset * 3, ditu_input_X_4[1] + ditu_input_offset]]

ditu_input_Y_1 = [ditu_input_X_1[0] + 75, ditu_input_X_1[1]]
ditu_input_Y_4 = [ditu_input_Y_1[0], ditu_input_Y_1[1] + ditu_input_offset]
ditu_input_Y_7 = [ditu_input_Y_4[0], ditu_input_Y_4[1] + ditu_input_offset]

ditu_input_Y = [[ditu_input_Y_1[0], ditu_input_Y_1[1]], [ditu_input_Y_1[0] + ditu_input_offset, ditu_input_Y_1[1]],
                [ditu_input_Y_1[0] + ditu_input_offset * 2, ditu_input_Y_1[1]],
                [ditu_input_Y_1[0], ditu_input_Y_1[1] + ditu_input_offset],
                [ditu_input_Y_4[0] + ditu_input_offset, ditu_input_Y_4[1]],
                [ditu_input_Y_4[0] + ditu_input_offset * 2, ditu_input_Y_4[1]],
                [ditu_input_Y_4[0], ditu_input_Y_4[1] + ditu_input_offset],
                [ditu_input_Y_7[0] + ditu_input_offset, ditu_input_Y_7[1]],
                [ditu_input_Y_7[0] + ditu_input_offset * 2, ditu_input_Y_7[1]],
                [ditu_input_Y_4[0] + ditu_input_offset * 3, ditu_input_Y_4[1]],
                [ditu_input_Y_4[0] + ditu_input_offset * 3, ditu_input_Y_4[1] + ditu_input_offset]]

# 物品为通用的时候的消息框坐标
all_item_message = (165, 106 + offset, 258, 137 + offset)
# 物品为书的时候详细消息框位置
shu_message = (114, 192 + offset, 239, 211 + offset)
# 物品为铁的时候消息框位置
shu_message = (111, 197 + offset, 244, 228 + offset)
# 物品为宝石的时候消息框位置
baoshi_message = (114, 217 + offset, 247, 306 + offset)
# 物品为装备时候消息框位置
item_message=(114,394+offset,237,469+offset)
# 飞行符在背包的位置
feifei = [0, 0]

# 香在背包位置
xiang = [0, 1]

# 背包框坐标起始位置参数
box = [348, 95 + offset]
box_offset = [52, 52]
# 背包物品中心坐标参数,为了双击
box_intxy = [368, 100 + offset]
# 仓库界面坐标中心起点位置参数
story_1 = [101, 143 + offset]
story_box_offset = [53, 53]

# 仓库界面背包中心坐标位置参数
story_box = [386, 144 + offset]
# 仓库界面仓库物品框坐标位置参数
story_storybox = [81, 117 + offset]
story_storybox_offset = [52, 51]

# 仓库界面仓库背包物品框坐标位置参数
story_boxbox = [364, 115 + offset]
# 仓库界面仓库背包物品框中心点击坐标位置参数
story_boxbox_intxy = [386, 140 + offset]
# 仓库编号面板起始位置参数
story_num_intxy_begin = [117, 90 + offset]
# 仓库编号面板偏移量
story_num_intxy_offset = [55, 55]

# 存放宝图归类后的自身坐标与队应的仓库编号
Treasure_Map_story_list = []

# 取消按钮坐标范围
quxiao_intxy = [394, -7 + offset, 724, 200 + offset]

# 地图名称显示范围
ditu_name_intxy = [60, 7 + offset, 120, 27 + offset]
# 依次为x输入框,y输入框,前往,关闭按钮 长安城 江南野外 建邺城 东海湾傲来国 女儿村 花果山 北俱芦洲 长寿郊外 长寿村 大唐境外 狮驼岭 墨家村 大唐国境 五庄观 朱紫国 麒麟山

'''for_gotoxy_intxy = [[164, 50, 243, 47, 318, 48, 647, 30], [200, 63, 278, 60, 354, 60, 612, 46],
                    [163, 48, 234, 47, 314, 47, 654, 31], [249, 66, 328, 66, 403, 62, 565, 47],
                    [231, 49, 305, 47, 381, 46, 582, 31], [200, 136, 201, 176, 206, 210, 580, 25],
                    [205, 65, 281, 64, 360, 61, 607, 47], [203, 63, 280, 59, 361, 60, 609, 44],
                    [232, 65, 310, 64, 385, 63, 582, 46], [279, 57, 352, 57, 434, 57, 532, 41],
                    [136, 131, 212, 130, 290, 128, 676, 112], [199, 59, 276, 60, 352, 61, 611, 40],
                    [253, 125, 248, 164, 250, 197, 535, 11], [207, 33, 288, 34, 364, 30, 603, 14],
                    [207, 62, 276, 62, 359, 62, 610, 44], [209, 45, 287, 44, 366, 45, 604, 26],
                    [200, 65, 275, 62, 357, 66, 611, 43], [205, 62, 284, 62, 357, 65, 610, 44]]'''
# 仓库宝图排序
story_map_name_list = ['北', '境外', '国境', '长寿', '女儿', '建邺', '花果', '南', '东', '傲来', '五庄', '朱紫', '狮驼', '普陀', '墨家', '墨家', '麒']

for_gotoxy_intxy = [[203, 63, 280, 59, 361, 60, 609, 44], [136, 131, 212, 130, 290, 128, 676, 112],
                    [207, 33, 288, 34, 364, 30, 603, 14], [232, 65, 310, 64, 385, 63, 582, 46],
                    [200, 136, 201, 176, 206, 210, 580, 25], [163, 48, 234, 47, 314, 47, 654, 31],
                    [205, 65, 281, 64, 360, 61, 607, 47], [200, 63, 278, 60, 354, 60, 612, 46, 41],
                    [249, 66, 328, 66, 403, 62, 565, 47], [231, 49, 305, 47, 381, 46, 582, 31],
                    [207, 62, 276, 62, 359, 62, 610, 44], [209, 45, 287, 44, 366, 45, 604, 26],
                    [199, 59, 276, 60, 352, 61, 611, 40], [205, 62, 284, 62, 357, 65, 610, 44],
                    [253, 125, 248, 164, 250, 197, 535, 11], [200, 65, 275, 62, 357, 66, 611, 43],
                    [164, 50, 243, 47, 318, 48, 647, 30], [279, 57, 352, 57, 434, 57, 532, 41]]

# 仓库位置列表
story_num_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1],
                  [2, 2], [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [4, 0], [4, 1], [4, 2], [4, 3],
                  [4, 4]]


def story_all_box_item():
    close_all()
    goto_intxy()
    pass


def click(x=0):
    # move_mouse
    # click
    x = x + random.uniform(0.0, 0.1)
    dm.LeftDown()
    time.sleep(x)
    dm.LeftUp()
    pass


def click_r(x=0):
    # move_mouse
    # click
    x = x + random.uniform(0.0, 0.1)
    dm.RightDown()
    time.sleep(x)
    dm.RightUp()
    pass


def double_click(x=0):
    # move_mouse
    # click
    # x = x + random.uniform(0.1, 0.2)
    click()
    # time.sleep(x)
    click()
    # time.sleep(x)


def left_click(x, y):
    move_mouse(x, y)
    print("left_click: " + str(x) + "," + str(y))
    time.sleep(random.uniform(0.2, 0.3))
    click()
    time.sleep(random.uniform(0.2, 0.3))


def left_double_click(x, y):
    move_mouse(x, y)
    print("left_double_click: " + str(x) + "," + str(y))
    time.sleep(random.uniform(0.2, 0.3))
    double_click()
    time.sleep(random.uniform(0.2, 0.3))


def right_click(x, y):
    move_mouse(x, y)
    time.sleep(random.uniform(0.1, 0.2))
    click_r()
    time.sleep(random.uniform(0.2, 0.1))


def move_mouse(x, y):
    # move_aside_mouse
    rd_x = random.randint(0, 5)
    rd_y = random.randint(0, 5)
    # dm.MoveTo(x , y)
    xx, yy = (x + rd_x, y + rd_y)
    dm.MoveTo(xx, yy)
    return (xx, yy)


def reset_mouse(t=0, x=2000, y=2000):
    move_mouse(x, y)
    time.sleep(t + random.random() / 2)


def check_box(item_path=''):
    # 查找存放在背包道具的坐标
    item_list = []
    print('========')
    # 查找指定图片的坐标
    for i in range(0, 4):
        for j in range(0, 5):
            xy = dm.FindPic(box[0] + box_offset[0] * j, box[1] + box_offset[1] * i, box[0] + box_offset[0] * (j + 1),
                            box[1] + box_offset[1] * (i + 1),
                            item_path, "777777", 1.0, 0, intX, intY)
            if xy[1] > 0 and xy[2] > 0:
                print(i, j)
                item_list.append([i, j])

    return item_list


def check_stroy(item_path=''):
    # 查找存放在仓库道具的坐标
    sleep(0.5)
    item_list = []
    print('========')
    # 查找指定图片的坐标
    for i in range(0, 4):
        for j in range(0, 5):
            xy = dm.FindPic(story_storybox[0] + story_storybox_offset[0] * j,
                            story_storybox[1] + story_storybox_offset[1] * i,
                            story_storybox[0] + story_storybox_offset[0] * (j + 1),
                            story_storybox[1] + story_storybox_offset[1] * (i + 1),
                            item_path, "666666", 0.9, 0, intX, intY)
            '''get_picture(story_storybox[0] + story_storybox_offset[0] * j,
                                    story_storybox[1] + story_storybox_offset[1] * i,
                                    story_storybox[0] + story_storybox_offset[0] * (j + 1),
                                    story_storybox[1] + story_storybox_offset[1] * (i + 1) ,
                                    str(i) + str(j) + '.bmp')'''
            if xy[1] > 0 and xy[2] > 0:
                print(i, j)
                item_list.append([i, j])

    return item_list


def check_stroy_box(item_path=''):
    # 查找存放在仓库道具的坐标
    item_list = []
    print('========')
    # 查找指定图片的坐标
    for i in range(0, 4):
        for j in range(0, 5):
            xy = dm.FindPic(story_boxbox[0] + story_storybox_offset[0] * j,
                            story_boxbox[1] + story_storybox_offset[1] * i,
                            story_boxbox[0] + story_storybox_offset[0] * (j + 1),
                            story_boxbox[1] + story_storybox_offset[1] * (i + 1),
                            item_path, "555555", 0.9, 0, intX, intY)
            '''get_picture(story_boxbox[0] + story_storybox_offset[0] * j,
                                    story_boxbox[1] + story_storybox_offset[1] * i ,
                                    story_boxbox[0] + story_storybox_offset[0] * (j + 1),
                                    story_boxbox[1] + story_storybox_offset[1] * (i + 1) ,
                                    str(i) + str(j) + '.bmp')'''
            if xy[1] > 0 and xy[2] > 0:
                print(i, j)
                item_list.append([i, j])

    return item_list


def check_box_open_status():
    # 检查包裹打开状态 1打开 0关闭
    dm_ret = dm.FindStr(353, 66 + offset, 381, 93 + offset, "道", "f7f2f3-333333", 1.0, intX, intY)
    if dm_ret[1] > 0:
        print("背包已打开!")
        return 1
    else:
        print("检查包裹状态未打开!")
        return 0


def close_box_or_story():
    print("准备关闭背包")
    # 仓库,背包取消判断
    dm_ret = dm.FindColor(541, 11 + offset, 725, 107 + offset, "285d89-000111", 1.0, 0, intX, intY)
    n = 0
    while dm_ret[0] > 0:
        left_click(intX, intY)
        dm_ret = dm.FindColor(541, 11 + offset, 725, 107 + offset, "285d89-000111", 1.0, 0, intX, intY)
        n = n + 1
        sleep(0)
        if n > 10:
            print("尝试10次未能取消仓库或者背包窗口,将在20秒后关闭程序")
            sleep(20)
            exit()
    return 0


def check_health():
    close_all()
    dm_ret = dm.FindColor(520, 29 + offset, 529, 39 + offset, "285d89-000111", 1.0, 0, intX, intY)
    if dm_ret[0] > 0:
        return 0
    else:
        return 1


def get_auto_fight_status():
    xy = dm.FindPic(434, 244 + offset, 504, 282 + offset, zidongzhandou, "898989", 0.8, 0, intX, intY)
    if xy[1] > 0:
        return 1
    else:
        return 0


def get_xiang_time_left():
    xy = dm.FindPic(620, 93 + offset, 651, 123 + offset, shijian, "898989", 0.9, 0, intX, intY)
    if xy[1] > 0:
        left_click(xy[1] + 15, xy[2] + 15)
    else:
        left_click(733, 122 + offset)

    if "剩" or "余" in xy:
        return 1
    else:
        return 0


def get_fight_status():
    xy = dm.FindPic(688, 370 + offset, 733, 415 + offset, zhandou, "222222", 0.9, 0, intX, intY)
    if xy[1] > 0:
        return 1
    else:
        return 0


def close_ditu():
    print("准备关闭地图")
    dm_ret = dm.FindColor(539, 13 + offset, 723, 109 + offset, "285d89-000111", 1.0, 0, intX, intY)
    n = 0
    while dm_ret[0] > 0:
        left_click(intX, intY)
        dm_ret = dm.FindColor(539, 13 + offset, 723, 109 + offset, "285d89-000111", 1.0, 0, intX, intY)
        n = n + 1
        sleep(0)
        if n > 10:
            print("尝试10次未能取消地图窗口,将在20秒后关闭程序")
            sleep(20)
            exit()
    return 0


def open_box():
    print("准备打开背包")
    if check_box_open_status() != 1:
        sleep(0)
        # 点击道具图标
        close_all()
        left_click(daoju[0], daoju[1])
    print("打开背包成功")


def get_box_image():
    for i in range(0, 4):
        for j in range(0, 5):
            dm_ret = dm.Capture(346 + 53 * j, 96 + 53 * i + offset, 346 + 53 * (j + 1), 96 + 53 * (i + 1) + offset,
                                './image/' + str(i) + str(j) + '.bmp')


def get_picture(intX, intY, intX1, intY1, file_name):
    dm_ret = dm.Capture(intX, intY, intX1, intY1, file_name)
    # img = cv2.imread(file_name)
    # cv2.imshow("Image", img)


def find_str_from_pic(intX, intY, intX1, intY1, rgb, string):
    intxx = 0
    intyy = 0
    dm_ret = dm.FindStr(intX, intY, intX1, intY1, string, rgb, 1.0, intxx, intyy)
    if len(dm_ret) > 0:
        return dm_ret
    else:
        print("在 " + str(intX) + "," + str(intY) + " - " + str(intX1) + "," + str(
            intY1) + " 中没有找到 \"" + string + "\" !!!")


def sleep(sleep_time):
    time.sleep(sleep_time + random.uniform(0.1, 0.2))


def get_map_x_1_intxy(x, y):
    dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, x_no_1[0], "222222", 0.7, 0, intX, intY)
    n = 0
    while dm_ret[1] < 0:
        if n == len(x_no_1):
            break
        dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, x_no_1[n], "222222", 0.7, 0, intX, intY)
        n = n + 1

    if dm_ret[1] > 0:
        print("找到X 1 输入框")
        return [dm_ret[1], dm_ret[2] + 5]
    else:
        left_click(x, y)
        flag = get_map_x_1_intxy(x, y)
        if flag[1] > 0:
            return [flag[0], flag[1]]
        else:
            print("未找到地图Y坐标1号按钮，退出")
            exit(17)

    '''
    
    dm_ret = dm.FindPic(56,7+offset,378,309+offset, x_no_1, "101010", 0.9,0, intX, intY)
    print(dm_ret)
    if dm_ret[0]>=0:
        return [dm_ret[1],dm_ret[2]+5]
        else:
        print("未找到地图Y坐标1号按钮，退出")
        exit(18)'''


def get_map_y_1_intxy(x, y):
    dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, y_no_1[0], "222222", 0.7, 0, intX, intY)
    n = 0
    print(dm_ret)
    while dm_ret[0] < 0:
        if n == len(y_no_1):
            break
        dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, y_no_1[n], "222222", 0.7, 0, intX, intY)
        print(dm_ret)
        print(len(y_no_1))
        print(n)
        n = n + 1

    if dm_ret[1] > 0:
        print("找到Y坐标 1 输入框")
        return [dm_ret[1], dm_ret[2] + 5]
    else:
        left_click(x, y)
        flag = get_map_y_1_intxy(x, y)
        if flag[1] > 0:
            return [flag[0], flag[1]]
        else:
            print("未找到地图Y坐标1号按钮，退出")
            exit(18)


def check_intxy(input_intx, input_inty):
    # 载入专用字库
    dm_ret = dm.UseDict(1)  # 使用字库0
    # 循环检查是否到达位置
    s = dm.Ocr(xy_zone[0], xy_zone[1], xy_zone[2], xy_zone[3], "dce2e4-555555", 0.9)
    n = 0
    for i in range(0, 2):
        old_s = ''
        old_s_count = 0
        while '(' + str(input_intx) + ',' + str(input_inty) + ')' not in s:
            print("未能到达 %s,%s ,继续等待人物移动" % (input_intx, input_inty))
            s = dm.Ocr(xy_zone[0], xy_zone[1], xy_zone[2], xy_zone[3], "dce2e4-555555", 0.9)

            if old_s == s:
                old_s_count = old_s_count + 1

            if old_s_count == 2:
                break
            print("当前坐标为: %s" % s)
            print("上一次地址为: %s" % old_s)
            old_s = s
            sleep(1)
    dm_ret = dm.UseDict(0)


def check_intxy_one(input_intx, input_inty):
    # 载入专用字库
    dm_ret = dm.UseDict(1)
    # 循环检查是否到达位置
    s = dm.Ocr(xy_zone[0], xy_zone[1], xy_zone[2], xy_zone[3], "dce2e4-555555", 1.0)
    if '(' + str(input_intx) + ',' + str(input_inty) + ')' in s:
        dm_ret = dm.UseDict(0)
        return 1
    else:
        dm_ret = dm.UseDict(0)
        return 0


def goto_intxy(input_intx, input_inty, intxy_all):
    print("准备前往%d,%d" % (input_intx, input_inty))
    close_all()
    # 获得地图上的X,Y坐标输入窗口的坐标,前往按钮坐标
    # intxy_all = where_am_i()
    print(intxy_all)
    # 判断是否位于npc前
    sleep(0.5)
    flag = check_intxy_one(input_intx, input_inty)
    print(flag)
    if flag == 0 and intxy_all != 0:
        print("打开地图")
        # 点击地图按钮
        open_map()
        sleep(1.5)

        print("准备输入X坐标")
        # 点击输入X坐标窗口，弹出X坐标输入按钮
        left_click(intxy_all[0], intxy_all[1] + offset)
        sleep(0)

        ditu_input_X_1 = get_map_x_1_intxy(intxy_all[0], intxy_all[1] + offset)

        # 循环输入坐标X的值
        for j in [int(i) for i in str(input_intx)]:
            ditu_input(ditu_input_X_1, j)
        # 确定
        ditu_input(ditu_input_X_1, 10)

        print("输入Y坐标")
        # 点击输入y坐标窗口，弹出y坐标输入按钮
        left_click(intxy_all[2], intxy_all[3] + offset)
        ditu_input_y_1 = get_map_y_1_intxy(intxy_all[2], intxy_all[3] + offset)
        # 循环输入坐标Y的值
        for j in [int(i) for i in str(input_inty)]:
            ditu_input(ditu_input_y_1, j)

        ditu_input(ditu_input_y_1, 10)

        # 点击前往按钮
        sleep(0)
        left_click(intxy_all[4], intxy_all[5] + offset)
        # 关闭地图
        close_all()

        print("循环检查是否到达位置")
        # 循环检查是否到达位置
        check_intxy(input_intx, input_inty)
        print("到达 %s,%s" % (input_intx, input_inty))
        return 1
    else:
        print("到达 %s,%s" % (input_intx, input_inty))
        return 1


def qianwang(x, y):
    dm_ret = dm.FindPic(86, offset, 495, 297 + +offset, qianwang_bmp[0], "333333", 0.7, 0, intX, intY)
    n = 0
    while dm_ret[1] < 0:
        n = n + 1
        dm_ret = dm.FindPic(86, offset, 495, 297 + offset, qianwang_bmp[n], "333333", 0.7, 0, intX, intY)
        if n == len(qianwang_bmp):
            break
    if dm_ret[1] > 0:
        left_click(dm_ret[1] + 30, dm_ret[2] + 15)
    else:
        print("无法找到前往按钮")
        exit(13)


def chose_story(orc_string):
    print("需要仓库位置的宝图信息为: " + orc_string)
    if "境外" in orc_string:
        return [2, 0]
    if "唐境" in orc_string:
        return [2, 0]
    if "国境" in orc_string:
        return [2, 1]
    if "长寿" in orc_string:
        return [2, 2]
    if "女儿" in orc_string:
        return [2, 3]
    if "建邺" in orc_string:
        return [2, 4]
    if "花果" in orc_string:
        return [3, 0]
    if "南" in orc_string:
        return [3, 1]
    if "东" in orc_string:
        return [3, 2]
    if "傲来" in orc_string:
        return [3, 3]
    if "五庄" in orc_string:
        return [3, 4]
    if "朱紫" in orc_string:
        return [4, 0]
    if "狮驼" in orc_string:
        return [4, 1]
    if "普陀" in orc_string:
        return [4, 2]
    if "墨家" in orc_string:
        return [4, 3]
    if "麒" in orc_string:
        return [4, 4]
    if "麟" in orc_string:
        return [4, 4]
    if "北" in orc_string:
        return [1, 4]
    else:
        return [0, 0]


def where_am_i():
    close_all()
    dm_ret = dm.UseDict(0)
    print("检查人物位置")
    # 检查人物所属地图
    orc_string = dm.Ocr(61, 10 + offset, 121, 27 + offset, "27292e-333333", 0.9)
    print(orc_string)
    # 检查人物所属坐标
    if "境外" in orc_string:
        return for_gotoxy_intxy[1]
    if "唐境" in orc_string:
        return for_gotoxy_intxy[1]
    if "国境" in orc_string:
        return for_gotoxy_intxy[2]
    if "寿郊外" in orc_string:
        return for_gotoxy_intxy[3]
    if "长寿村" in orc_string:
        return for_gotoxy_intxy[17]
    if "儿" in orc_string:
        return for_gotoxy_intxy[4]
    if "女" in orc_string:
        return for_gotoxy_intxy[4]
    if "邺" in orc_string:
        return for_gotoxy_intxy[5]
    if "建" in orc_string:
        return for_gotoxy_intxy[5]
    if "花" in orc_string:
        return for_gotoxy_intxy[6]
    if "果" in orc_string:
        return for_gotoxy_intxy[6]
    if "南" in orc_string:
        return for_gotoxy_intxy[7]
    if "东" in orc_string:
        return for_gotoxy_intxy[8]
    if "傲" in orc_string:
        return for_gotoxy_intxy[9]
    if "来" in orc_string:
        return for_gotoxy_intxy[9]
    if "五" in orc_string:
        return for_gotoxy_intxy[10]
    if "庄" in orc_string:
        return for_gotoxy_intxy[10]
    if "朱" in orc_string:
        return for_gotoxy_intxy[11]
    if "紫" in orc_string:
        return for_gotoxy_intxy[15]
    if "狮" in orc_string:
        return for_gotoxy_intxy[12]
    if "驼" in orc_string:
        return for_gotoxy_intxy[12]
    if "普" in orc_string:
        return for_gotoxy_intxy[13]
    if "陀" in orc_string:
        return for_gotoxy_intxy[13]
    if "墨" in orc_string:
        return for_gotoxy_intxy[14]
    if "家" in orc_string:
        return for_gotoxy_intxy[14]
    if "麒" in orc_string:
        return for_gotoxy_intxy[15]
    if "麟" in orc_string:
        return for_gotoxy_intxy[15]
    if "北" in orc_string:
        return for_gotoxy_intxy[0]
    if "长安" in orc_string:
        return for_gotoxy_intxy[16]
    else:
        return 0


def drop_rabbish():
    tie_list = check_box(tie_bmp)
    for tie in tie_list:
        x = box_intxy[0] + box_offset[0] * tie[1]
        y = box_intxy[1] + box_offset[1] * tie[0]
        left_click(x, y)
        left_double_click(x, y)
        move_mouse(0, 0)


def check_box_open_status():
    # 检查包裹打开状态 1打开 0关闭
    dm_ret = dm.FindStr(353, 66 + offset, 381, 93 + offset, "道", "f7f2f3-333333", 1.0, intX, intY)
    if dm_ret[1] > 0:
        print("背包已打开!")
        return 1
    else:
        print("检查包裹状态未打开!")
        return 0


def open_story_num(story_num):
    flag = check_story_open_status()
    if flag != 1:
        close_all()
        goto_intxy(348, 243, where_am_i())
        sleep(0)
        open_story()


def check_story_open_status():
    # 检查仓库打开状态 1打开 0关闭
    dm_ret = dm.FindStr(83, 100 + offset, 140, 124 + offset, "", "eeeeef-444444", 1.0, intX, intY)
    if intX > 0:
        print("仓库已打开!")
        return 1
    else:
        print("检查仓库未打开!")
        return 0


def close_all():
    print("准备关闭all")
    # 仓库,背包取消判断
    dm_ret = dm.FindPic(quxiao_intxy[0], quxiao_intxy[1], quxiao_intxy[2], quxiao_intxy[3], quxiao_bmp[0], "202020",
                        0.9, 2, intX, intY)
    n = 0
    while dm_ret[1] < 0:
        n = n + 1
        if n == len(quxiao_bmp):
            break
        dm_ret = dm.FindPic(quxiao_intxy[0], quxiao_intxy[1], quxiao_intxy[2], quxiao_intxy[3], quxiao_bmp[n], "202020",
                            0.9, 0, intX, intY)
    if dm_ret[1] > 0:
        print("找到关闭按钮,准备前往%d,%d关闭" % (dm_ret[1], dm_ret[2]))
        left_click(dm_ret[1] + 8, dm_ret[2] + 8)


'''
        dm_ret = dm.FindPic(quxiao_intxy[0],quxiao_intxy[1],quxiao_intxy[2],quxiao_intxy[3],quxiao_bmp, "202020", 0.9, 0, intX, intY)
        n = n + 1
        sleep(1)
        if n > 10:
            print("尝试10次未能取消仓库或者背包窗口,将关闭程序")
            exit(14)
    else:
        print("找到关闭按钮,准备前往%d,%d关闭" % (intX, intY))
        return 0
'''


def ditu_input(xy_int, num_int):
    if num_int == 0:
        left_click(xy_int[0] + 3 * ditu_input_offset, xy_int[1] + ditu_input_offset)
    elif num_int > 0 and num_int <= 3:
        left_click(xy_int[0] + (num_int - 1) * ditu_input_offset, xy_int[1])
    elif num_int > 3 and num_int <= 6:
        left_click(xy_int[0] + (num_int - 4) * ditu_input_offset, xy_int[1] + ditu_input_offset)
    elif num_int > 6 and num_int <= 10:
        left_click(xy_int[0] + (num_int - 7) * ditu_input_offset, xy_int[1] + ditu_input_offset * 2)
    else:
        print("错误的地图位置按钮输入")


def check_map_open_status():
    dm_ret = dm.FindPic(0, 0 + offset, 788, 250 + offset, qianwang_bmp, "555555", 0.8, 0, intX, intY)
    if dm_ret[1] > 0:
        return 1
    else:
        return 0


def open_map():
    print("打开地图")
    # 点击地图按钮
    m = 1
    n = 0
    close_all()
    left_double_click(ditu[0], ditu[1])
    while check_map_open_status() == 0:
        print("地图未打开,尝试重新打开")
        close_all()
        left_double_click(ditu[0], ditu[1])
        sleep(1)
    '''s = dm.Ocr(quxiao_intxy[0], quxiao_intxy[1], quxiao_intxy[2], quxiao_intxy[3], "D2D4D5-2D2B2A", 0.9)
    while m == 1:
        flag=check_map_open_status()
        if flag==1:
            m = 0
        else:
            n = n + 1
            if n == 3:
                m = 0
                return 0
            close_all()
            left_double_click(ditu[0], ditu[1])
            left_double_click(ditu[0], ditu[1])'''


def get_map_input_intxy():
    # 检查是否打开地图
    flag = check_map_open_status()

    if flag != 1:
        # 打开地图
        open_map()

    # 查找XY输入框的位置
    ##初始化输入框坐标
    intxy = []

    # 查询X坐标位置
    get_picture(56, 7 + offset, 378, 309 + offset, "map_x_bmp.bmp")
    dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, map_x_bmp[0], "333333", 0.8, 0, intX, intY)
    n = 0
    while dm_ret[1] < 0:
        n = n + 1
        if n == len(map_x_bmp):
            break
        dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, map_x_bmp[n], "333333", 0.8, 0, intX, intY)

    if dm_ret[1] > 0:
        print("找到X坐标输入框")
        intxy.append(dm_ret[1] + 40)
        intxy.append(dm_ret[2] + 5)

    # 查询Y坐标输入位置

    dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, map_y_bmp[0], "333333", 0.8, 0, intX, intY)
    n = 0
    while dm_ret[1] < 0:
        n = n + 1
        if n == len(map_y_bmp):
            break
        dm_ret = dm.FindPic(56, 7 + offset, 378, 309 + offset, map_y_bmp[n], "333333", 0.8, 0, intX, intY)

    if dm_ret[1] > 0:
        print("找到Y坐标输入框")
        intxy.append(dm_ret[1] + 40)
        intxy.append(dm_ret[2] + 5)
    '''xy = dm.FindPic(42,3+offset,371,218+offset, map_y_bmp,"101010", 0.9, 0, intX, intY)
    if xy[1] > 0 and xy[2] > 0:
        intxy.append(xy[1]+40)
        intxy.append(xy[2]+5)
    else:
        dm_ret_map = dm.FindStr(56, 7 + offset, 378, 309 + offset, "Y", "eeeeef-444444", 0.9, intX, intY)
        if dm_ret_map[1] > 0:
            intxy.append(xy[1] + 40)
            intxy.append(xy[2] + 5)
        else:
            print("无法找到Y输入框,退出")
            exit(16)'''

    if len(intxy) == 4:
        return intxy
    else:
        print("找到的xy输入框坐标位置不齐全,退出")
        exit(16)


def open_story():
    sleep(1)
    print("打开仓库")
    left_double_click(npc_story[0], npc_story[1])
    sleep(1)
    left_click(default_button[0], default_button[1])


def check_story_empty_num():
    print("检查仓库空位剩余空位")
    n = 0
    item = []
    for i in range(0, 4):
        for j in range(0, 5):
            aa = dm.GetAveRGB(story_storybox[0] + story_storybox_offset[0] * j + 20,
                              story_storybox[1] + story_storybox_offset[1] * i + 20,
                              story_storybox[0] + story_storybox_offset[0] * j + 30,
                              story_storybox[1] + story_storybox_offset[1] * i + 30)
            '''get_picture(story_storybox[0] + story_storybox_offset[0] * j + 0,
                        story_storybox[1] + story_storybox_offset[1] * i +  0,
                        story_storybox[0] + story_storybox_offset[0] * j + 53,
                        story_storybox[1] + story_storybox_offset[1] * i +  53, str(i) + str(j) + '.bmp')'''
            if aa == 'b8b0d8':
                item.append([i, j])
                n = n + 1
    print("当前仓库空位剩余: %d" % n)
    # 测试
    return item


def check_story_box_empty_num():
    print("检查仓库界面的背包空位剩余空位")
    n = 0
    item = []
    print("检查背包空位剩余空位")
    for i in range(0, 4):
        for j in range(0, 5):
            aa = dm.GetAveRGB(story_boxbox_intxy[0] + story_storybox_offset[0] * j - 10,
                              story_boxbox_intxy[1] + story_storybox_offset[1] * i - 10,
                              story_boxbox_intxy[0] + story_storybox_offset[0] * j + 10,
                              story_boxbox_intxy[1] + story_storybox_offset[1] * i + 10)
            '''get_picture(story_boxbox[0] + story_storybox_offset[0] * j + 20,
                              story_boxbox[1] + story_storybox_offset[1] * i + offset + 20,
                              story_boxbox[0] + story_storybox_offset[0] * j + 30,
                              story_boxbox[1] + story_storybox_offset[1] * i + offset + 30,str(i)+str(j)+'.bmp')'''
            print(aa)
            if aa == 'b8b0d8':
                n = n + 1
                item.append([i, j])
            if aa == '1b272c' and i == 3:
                if j == 0:
                    n = n + 1
                    item.append([i, j])
                if j == 1:
                    n = n + 1
                    item.append([i, j])
                if j == 2:
                    n = n + 1
                    item.append([i, j])
            if aa == '1b282e' and i == 3:
                if j == 3:
                    n = n + 1
                    item.append([i, j])
            if aa == '1b2b35' and i == 3:
                if j == 4:
                    n = n + 1
                    item.append([i, j])

    print("当前背包空位剩余: %d" % n)
    print("当前仓库界面的背包空位剩余: %d" % n)
    return item


def get_intxy():
    pass


def takefirst(elem):
    return elem[0]


def takeSecond(elem):
    return elem[1]


def get_Treasure_Map_intxy():
    dm_ret = dm.UseDict(0)
    Treasure_Map_story_list_a = []
    flag = 0
    m = ''
    # 打开道具
    if check_box_open_status() == 0:
        open_box()

    # 开始查看宝图
    # 获得宝图位置

    xy_list = check_box(Treasure_Map)
    print(xy_list)

    print("查找宝图所属地图与坐标")
    # 查找宝图所属地图与坐标
    for xy_list_data in xy_list:
        intxy = []
        print("当前检查%d,%d位置的背包" % (xy_list_data[0] + 1, xy_list_data[1] + 1))
        # 设定元素位置为编号n，每组两个元素
        # 将位置参数转换为坐标
        xy_int = [box_intxy[0] + box_offset[0] * xy_list_data[1], box_intxy[1] + box_offset[1] * xy_list_data[0]]
        # 双击宝图位置
        left_click(xy_int[0], xy_int[1])
        sleep(0.5)
        left_double_click(xy_int[0], xy_int[1])
        # left_double_click(xy_int[0], xy_int[1])
        sleep(0)
        move_mouse(0, 0)
        # 查找宝图所属地图与坐标
        # s = dm.Ocr(massage_box_zone[0],massage_box_zone[1],massage_box_zone[2],massage_box_zone[3], "D0CF18-2F3018", 1.0)
        s = dm.Ocr(massage_box_zone[0], massage_box_zone[1], massage_box_zone[2], massage_box_zone[3], "D0CF18-2F3018",
                   0.9)
        print(s)
        # 根据识别后的文字判断获得存放的仓库编号
        if len(s) == 0:
            print("================ERROR================")
            print("================ERROR================")
            print("未成功识别%d,%d的宝图信息" % (xy_list_data[0] + 1, xy_list_data[1] + 1))
            print("================ERROR================")
            print("================ERROR================")
            continue

        try:
            s = s.split('的')
            print(s)
            m = s[0]
            s = s[1].split(',')
            s = [int(i) for i in s]
            print(s)
            intxy.append(s[0])
            intxy.append(s[1])
            intxy.append(xy_int[0])
            intxy.append(xy_int[1])
            print(xy_int[0], xy_int[1])
            print(intxy)
        except:
            continue
        finally:
            pass

        # 将宝图坐标与仓库编号添加到list中
        if len(intxy) == 4:
            Treasure_Map_story_list_a.append(intxy)
            print("当前宝图坐标为: %s,%s" % (intxy[0], intxy[1]))
        else:
            print("未获取正确的宝图坐标信息,要求为4个数字,跳过")

    close_all()
    print(m)
    # 从左挖
    if '境外' in m or '花果' in m or '建邺' in m or '傲来' in m or '五庄' in m or '傲' in m:
        Treasure_Map_story_list_a = sorted(Treasure_Map_story_list_a, key=itemgetter(0))
        return Treasure_Map_story_list_a
    # 从下挖
    if '北' in m or '普' in m or '陀' in m or '墨' in m or '女' in m or '东' in m:
        Treasure_Map_story_list_a = sorted(Treasure_Map_story_list_a, key=itemgetter(1))
        return Treasure_Map_story_list_a
    # 从上挖
    if '南' in m or '朱' in m or '狮驼' in m or '长' in m:
        Treasure_Map_story_list_a = sorted(Treasure_Map_story_list_a, key=itemgetter(1), reverse=True)
        return Treasure_Map_story_list_a
    # 从右挖
    if '麒' in m or '麟' in m or '国境' in m:
        Treasure_Map_story_list_a = sorted(Treasure_Map_story_list_a, key=itemgetter(0), reverse=True)
        return Treasure_Map_story_list_a

    return Treasure_Map_story_list_a


def jiaxue():
    left_click(716, 5 + offset)
    left_click(582, 55 + offset)
    left_click(620, 5 + offset)
    left_click(470, 55 + offset)


def get_Treasure_Map_map_name_for_archive():
    dm_ret = dm.UseDict(0)
    Treasure_Map_story_list_a = []

    # 打开道具
    if check_box_open_status() == 0:
        open_box()

    # 开始查看宝图
    # 获得宝图位置
    xy_list = check_box(Treasure_Map)
    print(xy_list)

    print("查找宝图所属地图与坐标")
    # 查找宝图所属地图与坐标
    for xy_list_data in xy_list:
        print("当前检查%d,%d位置的背包" % (xy_list_data[0] + 1, xy_list_data[1] + 1))
        # 设定元素位置为编号n，每组两个元素
        # 将位置参数转换为坐标
        xy_int = [box_intxy[0] + box_offset[0] * xy_list_data[1], box_intxy[1] + box_offset[1] * xy_list_data[0]]
        # 双击宝图位置
        left_click(xy_int[0], xy_int[1])
        sleep(0.5)
        left_double_click(xy_int[0], xy_int[1])
        move_mouse(0, 0)
        # 查找宝图所属地图与坐标
        sleep(0)
        # s = dm.Ocr(massage_box_zone[0],massage_box_zone[1],massage_box_zone[2],massage_box_zone[3], "D0CF18-2F3018", 1.0)
        s = dm.Ocr(massage_box_zone[0], massage_box_zone[1], massage_box_zone[2], massage_box_zone[3], "D0CF18-2F3018",
                   0.9)
        print(s)
        # 根据识别后的文字判断获得存放的仓库编号
        story_num = chose_story(s)
        print(story_num)
        print("将要存放到%d,%d" % (story_num[0], story_num[1]))
        # 添加背包位置信息
        story_num.append(xy_list_data[0])
        story_num.append(xy_list_data[1])

        # 将宝图坐标与仓库编号添加到list中
        if len(story_num) == 4:
            Treasure_Map_story_list_a.append(story_num)
        else:
            print("未获取正确的仓库背包信息,位数不为4个,跳过")

    close_all()
    # Treasure_Map_story_list_a.sort(key=takefirst)
    Treasure_Map_story_list_a = sorted(Treasure_Map_story_list_a, key=itemgetter(0, 1))
    return Treasure_Map_story_list_a

def find_item_type_in_box_bak(x,y):
    # 是否为书      0
    # 是否为铁      1
    # 是否为70武器   2
    # 是否为60武器   3
    # 是否为70护甲   4
    # 是否为60护甲   5
    # 是否为高级五宝 6
    # 是否为低级五宝 7
    # 是否为高价值宝石 8
    # 是否为低价值宝石 9
    # 是否为金柳露     10
    # 是否为内丹       11
    # 是否为兽决       12
    type_list=(shu_bmp,tie_bmp,weapon_70_bmp,weapon_60_bmp,other_70_bmp,other_60_bmp, high_wubao_bmp,low_wubao_bmp,  high_gemstone_bmp, low_gemstone_bmp, gold_dew, elixir,elixir, )
    for i in range(len(type_list)):
        xy = dm.FindPic(box[0] + box_offset[0] * y, box[1] + box_offset[1] * x, box[0] + box_offset[0] * (y + 1),
                        box[1] + box_offset[1] * (x + 1),
                        type_list[i], "222222", 0.6, 0, intX, intY)
        if xy[0]>0:
            return (x,y,i)


def drop_unusefull_item():
    try:
        if check_box_open_status() == 0:
            open_box()
        item_list = find_harvest_item()
        for i in range(len(item_list)):
            find_item_type_in_box(item_list[i][0], item_list[i][1])
            #item_list[i].append(find_item_type_in_box(item_list[i][0], item_list[i][1]))
        print(item_list[i])
        pass
    except Exception as e:
        tkinter.messagebox.showerror('错误', repr(e))
    finally:
        pass

def find_item_type_in_box(x,y):
    try:
        # 是否为书      10
        # 是否为铁      11
        # 是否为70武器   12
        # 是否为60武器   13
        # 是否为70护甲   14
        # 是否为60护甲   15
        # 是否为高级五宝 16
        # 是否为低级五宝 17
        # 是否为高价值宝石 18
        # 是否为低价值宝石 19
        # 是否为金柳露     20
        # 是否为内丹       21
        # 是否为兽决       22
        #type_list=(other_70_bmp,other_60_bmp, high_wubao_bmp,low_wubao_bmp, shu_bmp,tie_bmp, high_gemstone_bmp, low_gemstone_bmp, gold_dew, elixir,elixir, )
        dm.SetDict(0, "./front/dm_soft.txt")  # 设定字库路径
        dm.SetDict(2, "./front/item_level.txt")
        dm_ret = dm.UseDict(2)
        intx=box_intxy[0]+box_offset[0]*y
        inty=box_intxy[1]+box_offset[1]*x
        left_click(intx, inty)
        sleep(1)
        s = dm.Ocr(all_item_message[0], all_item_message[1], all_item_message[2], all_item_message[3], "D0CF18-2F3017", 0.8)
        print(s)
        dm.SetDict(2, "./front/item_level.txt")
        dm_ret = dm.UseDict(2)
        a = dm.Ocr(item_message[0], item_message[1], item_message[2], item_message[3], "D0CF18-2F3017", 0.8)
        print(a)
        return 0
        if s=='百炼精铁' :
            pass
        if s=='装备制作书':
            pass
        if '金' in s and '露' in s :
            pass
        if s=='神秘石' or s=='红宝石' or s=='蓝宝石' or s=='绿宝石' or s=='黄宝石':
            return 19
        if s=='舍利子' or s=='红玛瑙' or s=='太阳石' or s=='翡翠石' or s=='黑宝石' or s=='光芒石' or s=='月亮石':
            pass
        if s=='金刚石' or s=='定魂珠' or s=='夜光珠' or s=='龙鳞':
            pass
        if s=='避水珠' :
            pass
        if '内丹' in s:
            pass
        if '要诀' in s:
            pass
        #以上都不是说明是装备
        #抓取环装信息
        s = dm.Ocr(item_message[0], item_message[1], item_message[2], item_message[3], "D0CF18-2F3017", 0.8)
        if '五行'in s and '防御'in s:
            #为衣服
            s=(s.split("五行")[0].split('等级'))[1]
            if s=='70':
                return 12
            if s == '60':
                return 13
        if '五行' in s and '防御' not in s:
            #武器
            s = (s.split("五行")[0].split('等级'))[1]
            if s == '70':
                return 14
            if s == '60':
                return 15
        if '等级' in s:
            #其他防装
            pass
        get_picture(all_item_message[0],all_item_message[1],all_item_message[2],all_item_message[3],str(x)+str(y)+'.bmp')
        print(s)
        dm_ret = dm.UseDict(0)
    except Exception as e:
        tkinter.messagebox.showinfo('错误', repr(e))

def find_useful_item():
    # 类型
    # 1兽决
    item_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2],
                 [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
    item_list_used = check_stroy_box(xiang_bmp) + check_stroy_box(
        feifei_bmp) + check_stroy_box(Treasure_Map)
    print("剔除的列表为:")
    print(item_list_used)
    item_list3 = [i for i in item_list if i not in item_list_used]
    print("剔除宝图与香,飞飞的位置为:")
    print(item_list3)
    item_list_empty = check_story_box_empty_num()
    print("空列表为:")
    print(item_list_empty)
    item_list4 = [i for i in item_list3 if i not in item_list_empty]
    print("需要保存的列表为:")
    print(item_list4)


def check_box_empty_num():
    n = 0
    list = []
    print("检查背包空位剩余空位")
    for i in range(0, 4):
        for j in range(0, 5):
            aa = dm.GetAveRGB(box_intxy[0] + box_offset[0] * j,
                              box_intxy[1] + box_offset[1] * i,
                              box_intxy[0] + box_offset[0] * j + 20,
                              box_intxy[1] + box_offset[1] * i + 20)
            '''get_picture(box_intxy[0] + box_offset[0] * j ,
                              box_intxy[1] + box_offset[1] * i,
                              box_intxy[0] + box_offset[0] * j + 20,
                              box_intxy[1] + box_offset[1] * i + 20, str(i) + str(j) + '.bmp')'''
            if aa == 'b8b0d8':
                list.append([i, j])
                print(i, j)
                n = n + 1
    print("当前背包空位剩余: %d" % n)
    return list



'''def check_story_box_empty_num():
    n=0
    list=[]
    print("检查背包空位剩余空位")
    for i in range(0, 4):
        for j in range(0, 5):
            aa = dm.GetAveRGB(story_boxbox[0] + box_offset[0] * j +20,
                              story_boxbox[1] + box_offset[1] * i +20,
                              story_boxbox[0] + box_offset[0] * j + 30,
                              story_boxbox[1] + box_offset[1] * i + 30)
            

            if aa == 'b8b0d8':
                list.append([i,j])
                print(i, j)
                n = n + 1
    print("当前背包空位剩余: %d" % n)
    return list'''


def storing_Treasure_Map(list_tmp):
    last = [5, 5, 5, 5]
    for i in range(0, int(len(list_tmp))):
        intxy_story_num = [story_num_intxy_begin[0] + story_num_intxy_offset[0] * list_tmp[i][1],
                           story_num_intxy_begin[1] + story_num_intxy_offset[1] * list_tmp[i][0]]
        print(list_tmp[i])
        print("准备选择仓库")
        if last[0] == list_tmp[i][0] and last[1] == list_tmp[i][1]:
            # 不检查位置直接存
            xy_int = [story_box[0] + story_num_intxy_offset[0] * list_tmp[i][3],
                      story_box[1] + story_num_intxy_offset[1] * list_tmp[i][2]]
            left_double_click(xy_int[0], xy_int[1])
            # left_double_click(xy_int[0], xy_int[1])
        else:
            left_click(155, 358 + offset)
            sleep(1)
            left_click(intxy_story_num[0], intxy_story_num[1])
            xy_int = [story_box[0] + story_num_intxy_offset[0] * list_tmp[i][3],
                      story_box[1] + story_num_intxy_offset[1] * list_tmp[i][2]]
            left_double_click(xy_int[0], xy_int[1])

        # 检查位置
        '''if check_story_empty_num() > 0:
            xy_int = [story_box[0] + story_num_intxy_offset[0] * list_tmp[i][3],
                      story_box[1] + story_num_intxy_offset[1] * list_tmp[i][2]]
            # 双击宝图位置
            left_click(xy_int[0], xy_int[1])
            sleep(0)
            left_double_click(xy_int[0], xy_int[1])
        else:
            print("仓库满了!")
            exit(19)'''
        last = list_tmp[i]


def init_script(title, x, y):
    # 获取句柄
    try:
        time.sleep(1)
        handle = dm.FindWindow("Qt5QWindowIcon", title)
        if handle != 0:
            print('Find the Game!')
            # 绑定窗口
            dm_ret = dm.BindWindow(handle, "gdi", "windows", "windows", 0)

            # 设置窗口位置#
            dm.MoveWindow(handle, x, y)

            # 设置窗口大小

            dm_ret = dm.SetWindowSize(handle, 747, 452)
            # 原始窗口大小为:747,452
        else:
            print('unfind game')
    except:
        print('The program don\'t found the Game!')


# 1,飞行符背包位置xy,飞行符点击位置
# 2,goto坐标,到达后点击的位置xy
# 3,goto npc的坐标位置,到达后点击npc的位置,点击传送按钮
# 4,吃香
# 5,检查是否成功进入下一张
changan = [[1, 457, 180 + offset]]
guojing = [[2, 10, 3, 24, 366 + offset], [4]]
putuo = guojing + [[3, 221, 60, 367, 180 + offset, 614, 205 + offset]]
wuzhuanguan = guojing + [[2, 5, 79, 16, 174 + offset], [2, 632, 79, 699, 138 + offset]]
jiangnan = [[2, 540, 2, 705, 271 + offset], [4]]
jianye = [[1, 466, 247 + offset]]
aolai = [[1, 583, 287 + offset]]
donghaiwan = aolai + [[3, 168, 15, 374, 183, 615, 189 + offset], [4]]
nver = aolai + [[2, 8, 141, 18, 53 + offset]]
huaguo = aolai + [[2, 216, 142, 707, 83 + offset], [4]]
changshou = [[1, 297, 117 + offset]]
changshoujiaowai = changshou + [[2, 147, 7, 704, 272 + offset], [4]]
beiju = changshoujiaowai + [[3, 60, 67, 370, 208 + offset, 623, 195 + offset]]
zhuzhi = [[1, 331, 274 + offset]]
datangjingwai = zhuzhi + [[4], [2, 4, 4, 17, 355 + offset]]
shituo = datangjingwai + [[2, 7, 49, 14, 211 + offset]]
mojia = datangjingwai + [[3, 238, 112, 368, 88 + offset, 608, 128 + offset]]
qilin = zhuzhi + [[4], [2, 3, 111, 18, 53 + offset]]

# 按照仓库排序创建列表
goto_other_map_list = [beiju, datangjingwai, guojing, changshoujiaowai, nver, jianye, huaguo, jiangnan, donghaiwan,
                       aolai,
                       wuzhuanguan, zhuzhi, shituo, putuo, mojia, qilin, changan]


def goto_map(num):
    # 判断当前地图是否为目的地
    close_all()
    '''if num!=26 or close_tag==0:
        left_click(370,93+offset)
        left_click(206,283+offset)
        left_click(601,141+offset)
        left_click(370, 202+offset)'''
    if for_gotoxy_intxy[num - 10] == where_am_i():
        print("到达目的地")
        return 1

    for list in goto_other_map_list[num - 10]:
        close_all()
        s = ''
        if list[0] == 1:
            try:
                feifei_flag = where_am_i()
                open_box()
                xy_int = [box_intxy[0] + box_offset[0] * feifei[1], box_intxy[1] + box_offset[1] * feifei[0]]
                left_click(xy_int[0], xy_int[1])
                sleep(0)
                left_double_click(xy_int[0], xy_int[1])
                sleep(0)
                left_click(list[1], list[2])
                sleep(3)
                while feifei_flag == where_am_i():
                    open_box()
                    left_click(xy_int[0], xy_int[1])
                    sleep(0)
                    left_double_click(xy_int[0], xy_int[1])
                    sleep(0)
                    left_click(list[1], list[2])
                    sleep(3)
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                close_all()
        if list[0] == 2:
            n = 0
            try:
                s_bak = where_am_i()
                goto_intxy(list[1], list[2], s_bak)
                left_click(list[3], list[4])
                sleep(3)
                while s == where_am_i():
                    n = n + 1
                    if n > 3:
                        return 0
                    s = where_am_i()
                    goto_intxy(list[1], list[2], s)
                    left_click(list[3], list[4])
                    print(s_bak)
                    print(s)
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        if list[0] == 3:
            try:
                s_bak = where_am_i()
                goto_intxy(list[1], list[2], s_bak)
                sleep(0.5)
                left_click(list[3], list[4])
                sleep(0.5)
                left_click(list[5], list[6])
                sleep(0.5)
                while where_am_i() == s_bak:
                    goto_intxy(list[1], list[2], where_am_i())
                    sleep(0.5)
                    left_click(list[3], list[4])
                    sleep(0.5)
                    left_click(list[5], list[6])
                    sleep(0.5)
                    print(s_bak)
                    print(s)

            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        if list[0] == 4:
            try:
                open_box()
                xy_int = [box_intxy[0] + box_offset[0] * xiang[1], box_intxy[1] + box_offset[1] * xiang[0]]
                left_click(xy_int[0], xy_int[1])
                sleep(0)
                left_click(shiyong[0], shiyong[1])
                close_all()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
    sleep(3)
    if for_gotoxy_intxy[num - 10] == where_am_i():
        print("到达目的地")
        return 1
    else:
        print("未到达目的地")
        return 0


def find_harvest_item():
    item_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2],
                 [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
    sleep(0)
    item_list_used = check_box(xiang_bmp) + check_box(feifei_bmp) + check_box(Treasure_Map)
    print("剔除的列表为:")
    print(item_list_used)
    item_list3 = [i for i in item_list if i not in item_list_used]
    print("剔除宝图与香,飞飞的位置为:")
    print(item_list3)
    item_list_empty = check_box_empty_num()
    print("空列表为:")
    print(item_list_empty)
    item_list4 = [i for i in item_list3 if i not in item_list_empty]
    print("需要保存的列表为:")
    print(item_list4)
    if item_list4 != []:
        return item_list4
    else:
        return []

def find_arch_item():
    item_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2],
                 [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
    sleep(0)
    item_list_used = check_stroy_box(xiang_bmp) + check_stroy_box(feifei_bmp) + check_stroy_box(Treasure_Map)
    print("剔除的列表为:")
    print(item_list_used)
    item_list3 = [i for i in item_list if i not in item_list_used]
    print("剔除宝图与香,飞飞的位置为:")
    print(item_list3)
    item_list_empty = check_story_box_empty_num()
    print("空列表为:")
    print(item_list_empty)
    item_list4 = [i for i in item_list3 if i not in item_list_empty]
    print("需要保存的列表为:")
    print(item_list4)
    if item_list4 != []:
        return item_list4
    else:
        return []


def find_arch_item_in_story_box():
    item_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1], [2, 2],
                 [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
    item_list_used = check_stroy(xiang_bmp) + check_stroy(feifei_bmp) + check_stroy(Treasure_Map)
    item_list3 = [i for i in item_list if i not in item_list_used]
    print("剔除宝图与香飞飞的位置为:")
    print(item_list3)
    item_list_empty = check_box_empty_num()
    print("空列表为:")
    print(item_list_empty)
    item_list4 = [i for i in item_list3 if i not in item_list_empty]
    print("需要保存的列表为:")
    print(item_list4)
    if item_list4 != []:
        return item_list4
    else:
        return []


def choose_story(num):
    intxy_story_num = [story_num_intxy_begin[0] + story_num_intxy_offset[0] * story_num_list[num - 1][1],
                       story_num_intxy_begin[1] + story_num_intxy_offset[1] * story_num_list[num - 1][0]]
    print(intxy_story_num)
    print("准备选择仓库")
    x = 0
    dm.moveto(177, 350 + offset)
    x = x + random.uniform(0.0, 0.1)
    dm.LeftDown()
    time.sleep(x)
    dm.LeftUp()
    left_click(intxy_story_num[0], intxy_story_num[1])


def get_out_for_story(num, item):
    choose_story(num)


def story_all_item_for_dig(item_list):
    print(item_list)
    if not item_list:
        return 1
    for i in range(2, 10):
        print("打开%d仓库" % i)
        choose_story(i)
        sleep(1)
        unuse_num = len(check_story_empty_num())
        if unuse_num > 0:
            for j in range(unuse_num):
                print("准备存放第%d个物品" % int(j + 1))
                if item_list != []:
                    item = item_list.pop()
                    print("准备存放%d,%d位置的物品" % (item[0], item[1]))
                    xy_int = [story_box[0] + story_num_intxy_offset[0] * item[1],
                              story_box[1] + story_num_intxy_offset[1] * item[0]]
                    left_double_click(xy_int[0], xy_int[1])
                else:
                    return 1
        else:
            continue


dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
dm.SetDict(0, "./front/dm_soft.txt")  # 设定字库路径
dm.SetDict(1, "./front/dm_soft_for_intxy.txt")
dm_ret = dm.UseDict(0)  # 使用字库0
