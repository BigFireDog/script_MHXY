# 前言
 - 此是一个基于大漠插件3.1233的梦幻西游自动挖宝脚本,能实现一键清理背包仓库,一键挖掘仓库所有宝图并输出收益清单,笔记本屏幕不大,仅支持同屏4开。
 - 测试客户端为夜神多开器,不能改变多开器的名称 名称必须为夜神模拟器1.夜神模拟器2,夜神模拟器3..依次类推
 - 

# 结构说明
- │  .gitignore
- │  archive.py                 #清理背包并前往仓库存放模块
- │  auto_dig.py                #挖掘当前背包内所有宝图模块
- │  auto_dig_all.py            #递归挖掘25个仓库内所有宝图模块
- │  dm.dll                     #大漠插件注册dll
- │  error_code                 #错误代码
- │  get_item_type.py           #收益统计
- │  init.py                    #插件初始化
- │  multipro_ui.py             #UI界面
- │  public.py                  #公共模块,包含所有基础模块,如移动,点击,搜索背包/仓库等
- ├─front                       #字体文件夹
- │      dm_soft.txt            #基础字体
- │      dm_soft_for_intxy.txt  #识别坐标专用字体
- │      item_level.txt│        #识别道具专用字体
- └─image                       #识图专用文件夹
    

# 注意事项
- 需要在客户端手动注册大漠插件
- 暂停功能涉及到各个阶段起点的判断,工作量较大尚未完成
- 仅用于学习,请勿实际使用,后果自负
