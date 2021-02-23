from multiprocessing import Process, Array, Lock,freeze_support
import archive, auto_dig
import init
import auto_dig_all
import tkinter as tk  # 使用Tkinter前需要先导入
import tkinter.messagebox
import os
import time
import ntplib
import get_item_type
allow_time='2021-02-01'

def init_all():
    init1 = Process(target=init.init_script, args=('夜神模拟器1', 0, 0,), )  # 必须加,号
    init2 = Process(target=init.init_script, args=('夜神模拟器2', 788, 0,), )
    init3 = Process(target=init.init_script, args=('夜神模拟器3', 0, 453,), )
    init4 = Process(target=init.init_script, args=('夜神模拟器4', 788, 453,), )
    init1.start()
    init2.start()
    init3.start()
    init4.start()


def multipro_arch1_stop():
    window_is_used[0] = 1
    archive1.terminate()
    print("已停止窗口1的归档进程")

def multipro_arch1():
    global archive1
    archive1 = Process(target=archive.arch_all_story_tra_map, args=('夜神模拟器1', 0, 0, 0, window_is_used))
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[0] == 1:
            try:
                archive1.start()
                # archive2.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器1的权限,可能正在执行其他任务")


def multipro_arch2_stop():
    window_is_used[1] = 1
    archive2.terminate()
    print("已停止窗口2的归档进程")


def multipro_arch2():
    global archive2
    archive2 = Process(target=archive.arch_all_story_tra_map, args=('夜神模拟器2', 788, 0, 1, window_is_used))
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[1] == 1:
            try:
                archive2.start()
                # archive2.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器2的权限,可能正在执行其他任务")


def multipro_arch3_stop():
    window_is_used[2] = 1
    archive3.terminate()
    print("已停止窗口3的归档进程")


def multipro_arch3():
    global archive3
    archive3 = Process(target=archive.arch_all_story_tra_map, args=('夜神模拟器3', 0, 453, 2, window_is_used), )

    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[2] == 1:
            try:
                archive3.start()
                # archive3.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器3的权限,可能正在执行其他任务")


def multipro_arch4_stop():
    window_is_used[3] = 1
    archive4.terminate()
    print("已停止窗口4的归档进程")


def multipro_arch4():
    global archive4
    archive4 = Process(target=archive.arch_all_story_tra_map, args=('夜神模拟器4', 788, 453, 3, window_is_used), )

    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[3] == 1:
            try:
                archive4.start()
                # archive4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器4的权限,可能正在执行其他任务")


def multipro_dig1_stop():
    window_is_used[0] = 1
    dig1.terminate()
    print("已停止窗口1的挖掘进程")

def multipro_dig1():
    global dig1
    dig1 = Process(target=auto_dig.auto_dig_start, args=('夜神模拟器1', 0, 0, 0, window_is_used,heyao_VarDis.get()))  # 必须加,号
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % (allow_multi_num))
    else:
        if window_is_used[0] == 1:
            try:
                dig1.start()
                # dig1.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器1的权限,可能正在执行其他任务")

def multipro_dig2_stop():
    window_is_used[1] = 1
    dig2.terminate()
    print("已停止窗口2的挖掘进程")

def multipro_dig2():
    global dig2
    dig2 = Process(target=auto_dig.auto_dig_start, args=('夜神模拟器2', 788, 0, 1, window_is_used,heyao_VarDis.get()))
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[1] == 1:  # 窗口未被占用
            try:
                dig2.start()
                # dig2.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器2的权限,可能正在执行其他任务")

def multipro_dig3_stop():
    window_is_used[2] = 1
    dig3.terminate()
    print("已停止窗口3的挖掘进程")

def multipro_dig3():
    global dig3
    dig3 = Process(target=auto_dig.auto_dig_start, args=('夜神模拟器3', 0, 453, 2, window_is_used,heyao_VarDis.get()), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[2] == 1:
            try:
                dig3.start()
                # dig3.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器3的权限,可能正在执行其他任务")

def multipro_dig4_stop():
    window_is_used[3] = 1
    dig4.terminate()
    print("已停止窗口4的挖掘进程")

def multipro_dig4():
    global dig4
    dig4 = Process(target=auto_dig.auto_dig_start, args=('夜神模拟器4', 788, 453, 4, window_is_used,heyao_VarDis.get()), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[3] == 1:
            try:
                window_is_used[3] = 0
                dig4.start()
                # dig4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器4的权限,可能正在执行其他任务")

def multipro_all_dig1():
    global all_dig1
    print("绑定进程")
    all_dig1 = Process(target=auto_dig_all.auto_dig_story_start, args=('夜神模拟器1', 0, 0, 0, window_is_used,heyao_VarDis.get()), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[0] == 1:
            try:
                window_is_used[0] = 0
                print("启动进程")
                all_dig1.start()
                # dig4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器1的权限,可能正在执行其他任务")

def multipro_all_dig1_stop():
    window_is_used[0] = 1
    all_dig1.terminate()
    print("已停止窗口1的挖掘进程")

def multipro_all_dig2():
    global all_dig2
    all_dig2 = Process(target=auto_dig_all.auto_dig_story_start, args=('夜神模拟器2', 788, 0, 1, window_is_used,heyao_VarDis.get()), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[1] == 1:
            try:
                window_is_used[1] = 0
                all_dig2.start()
                # dig4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器4的权限,可能正在执行其他任务")
def multipro_all_dig2_stop():
    window_is_used[1] = 1
    all_dig2.terminate()
    print("已停止窗口2的挖掘进程")

def multipro_all_dig3():
    global all_dig3
    all_dig3 = Process(target=auto_dig_all.auto_dig_story_start, args=('夜神模拟器3', 0, 453, 2, window_is_used,heyao_VarDis.get()), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[2] == 1:
            try:
                window_is_used[2] = 0
                all_dig3.start()
                # dig4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                pass
        else:
            print("无法获取模拟器4的权限,可能正在执行其他任务")
def multipro_all_dig3_stop():
    window_is_used[2] = 1
    all_dig3.terminate()
    print("已停止窗口3的挖掘进程")

def multipro_all_dig4():
    global all_dig4
    all_dig4 = Process(target=auto_dig_all.auto_dig_story_start, args=('夜神模拟器4', 788, 453, 3, window_is_used,heyao_VarDis.get()), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[3] == 1:
            try:
                window_is_used[3] = 0
                all_dig4.start()
                # dig4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                tk.messagebox.showwarning('warning', '窗口 4 挖掘完成')
        else:
            print("无法获取模拟器4的权限,可能正在执行其他任务")


def test():
    global get_type1
    get_type1 = Process(target=archive.arch_start, args=('夜神模拟器4', 0, 0, 0, window_is_used), )
    flag = 0
    for i in range(0, 3):
        if window_is_used[i] == 0:
            flag = flag + 1

    if flag == allow_multi_num:
        print("仅允许%d开" % allow_multi_num)
    else:
        if window_is_used[0] == 1:
            try:
                window_is_used[0] = 0
                get_type1.start()
                # dig4.join()
            except Exception as e:
                tkinter.messagebox.showerror('错误', repr(e))
            finally:
                tk.messagebox.showwarning('warning', '窗口 1 获取完成')
        else:
            print("无法获取模拟器1的权限,可能正在执行其他任务")

def multipro_all_dig4_stop():
    window_is_used[3] = 1
    all_dig4.terminate()
    print("已停止窗口4的挖掘进程")

def multipro_all_dig1_suspend():
    if process_stats[0] == 1:
        process_stats[0] = 0
        all_dig1.suspend()
        print('窗口1暂停运行')
    if process_stats[0] == 0:
        process_stats[0] = 1
        all_dig1.resume()
        print('窗口1恢复运行')

def multipro_all_dig2_suspend():
    if process_stats[1] == 1:
        process_stats[1] = 0
        all_dig2.suspend()
        print('窗口2暂停运行')
    if process_stats[1] == 0:
        process_stats[1] = 1
        all_dig2.resume()
        print('窗口2恢复运行')

def multipro_all_dig3_suspend():
    if process_stats[2] == 1:
        process_stats[2] = 0
        all_dig3.suspend()
        print('窗口3暂停运行')
    if process_stats[2] == 0:
        process_stats[3] = 1
        all_dig3.resume()
        print('窗口3恢复运行')

def multipro_all_dig4_suspend():
    if process_stats[3] == 1:
        process_stats[3] = 0
        all_dig4.suspend()
        print('窗口4暂停运行')
    if process_stats[3] == 0:
        process_stats[3] = 1
        all_dig4.resume()
        print('窗口4恢复运行')

def ntp_server():

    c = ntplib.NTPClient()
    fail_tag = 0
    try:
        response = c.request('ntp.aliyun.com')
    except:
        fail_tag = 1
    if fail_tag != 1:
        ts = response.tx_time
        _date = time.strftime('%Y-%m-%d', time.localtime(ts))
        if _date > allow_time:
            print("无使用许可")
            os._exit(88)
    else:
        os._exit(89)

if __name__ == '__main__':
    freeze_support()
    ntp_server()
    window_is_used = Array('i', [1, 1, 1, 1])
    global process_stats
    process_stats=[1,1,1,1]
    allow_multi_num: int = 4

    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('Welcome')

    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('350x550')  # 这里的乘是小x

    # 第5步，用户信息

    tk.Label(window, text='  窗口1     窗口2     窗口3     窗口4', font=('黑体', 11)).place(x=10, y=30)
    tk.Label(window, text='分类背包与仓库的宝图:', font=('黑体', 11)).place(x=10, y=53)
    tk.Label(window, text='自动挖掘仓库宝图:', font=('黑体', 11)).place(x=10, y=170)
    tk.Label(window, text='挖掘当前地图的宝图:', font=('黑体', 11)).place(x=10, y=350)
    tk.Label(window, text='调整窗口:', font=('黑体', 11)).place(x=10, y=485)
    #按钮
    archive1_button = tk.Button(window, text='开始', command=multipro_arch1)
    archive1_button.place(x=25, y=85)

    archive2_button = tk.Button(window, text='开始', command=multipro_arch2)
    archive2_button.place(x=105, y=85)

    archive3_button = tk.Button(window, text='开始', command=multipro_arch3)
    archive3_button.place(x=185, y=85)

    archive4_button = tk.Button(window, text='开始', command=multipro_arch4)
    archive4_button.place(x=265, y=85)

    archive5_button = tk.Button(window, text='停止', command=multipro_arch1_stop)
    archive5_button.place(x=25, y=130)

    archive6_button = tk.Button(window, text='停止', command=multipro_arch2_stop)
    archive6_button.place(x=105, y=130)

    archive7_button = tk.Button(window, text='停止', command=multipro_arch3_stop)
    archive7_button.place(x=185, y=130)

    archive8_button = tk.Button(window, text='停止', command=multipro_arch4_stop)
    archive8_button.place(x=265, y=130)

    all_dig1_button= tk.Button(window, text='开始', command=multipro_all_dig1)
    all_dig1_button.place(x=25, y=205)

    all_dig2_button = tk.Button(window, text='开始', command=multipro_all_dig2)
    all_dig2_button.place(x=105, y=205)

    all_dig3_button = tk.Button(window, text='开始', command=multipro_all_dig3)
    all_dig3_button.place(x=185, y=205)

    all_dig4_button = tk.Button(window, text='开始', command=multipro_all_dig4)
    all_dig4_button.place(x=265, y=205)


    all_dig5_button = tk.Button(window, text='停止', command=multipro_all_dig1_stop)
    all_dig5_button.place(x=25, y=255)

    all_dig6_button = tk.Button(window, text='停止', command=multipro_all_dig2_stop)
    all_dig6_button.place(x=105, y=255)

    all_dig7_button = tk.Button(window, text='停止', command=multipro_all_dig3_stop)
    all_dig7_button.place(x=185, y=255)

    all_dig8_button = tk.Button(window, text='停止', command=multipro_all_dig4_stop)
    all_dig8_button.place(x=265, y=255)

    all_dig9_button = tk.Button(window, text='暂/复', command=multipro_all_dig1_suspend)
    all_dig9_button.place(x=25, y=305)

    all_dig10_button = tk.Button(window, text='暂/复', command=multipro_all_dig2_suspend)
    all_dig10_button.place(x=105, y=305)

    all_dig11_button = tk.Button(window, text='暂/复', command=multipro_all_dig3_suspend)
    all_dig11_button.place(x=185, y=305)

    all_dig12_button = tk.Button(window, text='暂/复', command=multipro_all_dig4_suspend)
    all_dig12_button.place(x=265, y=305)

    dig1_button = tk.Button(window, text='开始', command=multipro_dig1)
    dig1_button.place(x=25, y=380)

    dig2_button = tk.Button(window, text='开始', command=multipro_dig2)
    dig2_button.place(x=105, y=380)

    dig3_button = tk.Button(window, text='开始', command=multipro_dig3)
    dig3_button.place(x=185, y=380)

    dig4_button = tk.Button(window, text='开始', command=multipro_dig4)
    dig4_button.place(x=265, y=380)

    dig5_button = tk.Button(window, text='停止', command=multipro_dig1_stop)
    dig5_button.place(x=25, y=430)

    dig6_button = tk.Button(window, text='停止', command=multipro_dig2_stop)
    dig6_button.place(x=105, y=430)

    dig7_button = tk.Button(window, text='停止', command=multipro_dig3_stop)
    dig7_button.place(x=185, y=430)

    dig8_button = tk.Button(window, text='停止', command=multipro_dig4_stop)
    dig8_button.place(x=265, y=430)

    init_button = tk.Button(window, text=' 调整位置 ', command=init_all)
    init_button.place(x=15, y=510)

    init_button = tk.Button(window, text=' 测试 ', command=test)
    init_button.place(x=105, y=510)

    #复选框
    heyao_VarDis = tk.IntVar()  # 用来获取复选框是否被勾选，通过heyao_VarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
    zidongheyao = tk.Checkbutton(window, text="战斗结束后是否补血                                                ", variable=heyao_VarDis,onvalue = 1, offvalue = 0)
    # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
    zidongheyao.select()  # 该复选框是否勾选,select为勾选, deselect为不勾选
    # sticky=tk.W  当该列中其他行或该行中的其他列的某一个功能拉长这列的宽度或高度时，设定该值可以保证本行保持左对齐，N：北/上对齐  S：南/下对齐  W：西/左对齐  E：东/右对齐
    zidongheyao.pack(anchor='e')
    # 第10步，主窗口循环显示
    window.mainloop()
