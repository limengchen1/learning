import os

path = os.getcwd()


# print(path)#获取当前目录路径
# dir_list=os.listdir(os.getcwd())
# print(dir_list)#获取当前路径下的目录和文件
# g=os.walk(path)
# # print(g)
# # print(next(g))
# # print(next(g))
# # print(next(g))
# print(os.path.abspath(path))#相对路径转化为绝对路径
# print(os.path.dirname(path))#当前路径的父目录
# print(os.path.basename(path))#获取当前文件目录名称
# print(os.path.split(path))
# print(os.path.join(os.path.split(path)[0],os.path.split(path)[1]))
# print(os.path.join('/Users/limengchen/PycharmProjects/demo_test','tests'))
# print(os.path.getsize(path))#文件大小
# print(os.path.isfile(path))#检查是否是文件
# print(os.path.isdir(path))#检查是否是文件夹
for dirpath, dirames, filenames  in os.walk(path):
    print('[' + dirpath + ']')
    for filename in filenames:
        print(os.path.join(dirpath, filename))


# 获取dirpath目录及子目录下的所有文件
def dir_list(dirpath):
    # 获取dirpath目录下所有的目录及文件
    path_list = os.listdir(dirpath)
    file_list = []
    for file in path_list:
        new_file_dir = os.path.join(dirpath, file)
        if os.path.isfile(new_file_dir):
            # 如果file是文件，添加到file_list
            file_list.append(file)
        elif os.path.isdir(new_file_dir):
            dir_list(new_file_dir)
    print(file_list)


dir_list(path)
# print(os.path.dirname('.pytest_cache'))
