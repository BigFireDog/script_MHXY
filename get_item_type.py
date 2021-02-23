import public
import multipro_ui


# 初始化脚本
def start(title, x, y, num, window_is_used):
    try:
        window_is_used[num] = 0
        public.init_script(title, x, y)
        public.open_box()
        item_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0], [2, 1],
                     [2, 2],
                     [2, 3], [2, 4], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4]]
        item_list_empty = public.check_box_empty_num()
        item_list4 = [i for i in item_list if i not in item_list_empty]
        for item in item_list4:
            # print('================')
            # print(item[0],item[1])
            print(public.find_item_type_in_box(item[0], item[1]))

    except Exception as e:
        multipro_ui.tkinter.messagebox.showerror('错误', repr(e))
    finally:
        window_is_used[num] = 1


