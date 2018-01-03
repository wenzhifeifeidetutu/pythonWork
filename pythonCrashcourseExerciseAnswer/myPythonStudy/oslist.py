# coding=utf-8
import os;
"""导入os模块
定义rename_files函数
"""
def rename_files():
    #获得文件路径 mac下不用r
    file_list =  os.listdir(r"/Users/wenzhi/Downloads/prank");
    #打印出来
    print(file_list);
    #打印当前文件路径
    save_pwd = os.getcwd();
    print(save_pwd);
    #修改当前路径为文件路径
    os.chdir(r"/Users/wenzhi/Downloads/prank")
    print(os.getcwd());

    #循环修改文件名rename
    for file_name in file_list:
        print("old name: " + file_name + " is changed!" );
        os.rename(file_name, file_name.translate(None, "0123456789"));
    #修改为当前文件夹路径
    os.chdir(save_pwd);

rename_files();






