import public
import win32com.client

def init_script(title, x, y):
    dm = win32com.client.Dispatch('dm.dmsoft')  # 调用大漠插件
    dm.SetDict(0, "./front/dm_soft.txt") # 设定字库路径
    dm.SetDict(1, "./front/dm_soft_for_intxy.txt")
    dm.SetDict(2, "./front/item_level.txt")
    dm_ret = dm.UseDict(0)  # 使用字库0
    # 获取句柄
    try:
        public.time.sleep(1)
        handle = dm.FindWindow("Qt5QWindowIcon", title)
        if handle != 0:
            print('Find the Game!')
            # 绑定窗口
            #dm_ret = dm.BindWindow(handle, "gdi", "windows", "windows", 0)
            dm_ret = dm.BindWindow(handle, "normal", "windows", "windows", 0)
            # 设置窗口位置#
            dm.MoveWindow(handle, x, y)

            # 设置窗口大小

            dm_ret = dm.SetWindowSize(handle, 747, 452)
            # 原始窗口大小为:747,452
        else:
            print('unfind game')
    except:
        print('The program don\'t found the Game!')


