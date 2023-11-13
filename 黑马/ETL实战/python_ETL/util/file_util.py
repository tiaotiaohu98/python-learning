# 导入相关数据包
import os


# 封装一个方法，用于获取指定目录下的所有文件信息
# 两种情况
# recursive=True 递归获取子目录下所有文件信息
# recursive=False 不递归获取子目录下所有文件信息
def get_dir_files_list(path='./', recursive=False):
    # 参数1：path 指定目录路径
    # 参数2：recursive 是否递归获取子目录下所有文件信息
    path_list = []
    
    file_names = os.listdir(path)

    for file_name in file_names:
        file_path = os.path.join(path, file_name) #获取文件的相对路径
        abs_path = os.path.abspath(file_path) #获取文件的绝对路径
        # sql插入时， \\会作为转义字符处理 故需要将\\替换为/
        abs_path = abs_path.replace("\\","/")
        
        if os.path.isfile(abs_path):
            path_list.append(abs_path)
        else:
            # 如果不是文件，则递归遍历子文件夹下的文件，并添加到子文件列表中
            if recursive:
                sub_path_list = get_dir_files_list(abs_path, True)
                path_list += sub_path_list
    return path_list

# 封装一个方法用于获取未处理的文件列表
def get_new_by_compare_lists(processed_list, all_list):
    # sql插入时， \\会作为转义字符处理 故需要将\\替换为/
    new_list = [x.replace("\\","/") for x in all_list if x not in processed_list]
    '''
        方法二：通过集合可以做差，计算
            缺点：会导致文的顺序被打乱
    '''
    # set1 = set(processed_list)
    # set2 = set(all_list)
    # new_list = list(set2-set1)
    return new_list

# if __name__ == '__main__':
#     print(get_dir_files_list('../test/test_dir', True))
#     list1 = [1,2]
#     list2 = [1,2,3,4,5]
#     print(get_new_by_compare_lists(list1,list2))
