from pythanos.snap import Snap
from pathlib import Path
import shutil

# if __name__ == '__main__':
#     obj = Snap(r"E:\REQ\abcdefgh")
#     obj.is_valid_dir(do_on_err='delete')

# if __name__ == '__main__':
#     obj = Snap(r"E:\REQ\abcd")
#     obj.zip(root_dir=r"E:\REQ\abcd")
# a = False

# for i in Path(r"E:\REQ\New folder\5").iterdir():
#     if ''.join(i.suffixes) not in list(set(['.pdf'])):
#         print(i)

# for i in Path(r"E:\REQ\New Folder").iterdir():
#     a = True
#     print(type(i))
# else:
#     if a is False:
#         print("yes")
if __name__ == '__main__':
    obj = Snap(r"E:\REQ\abcd")
    obj.is_valid_dir(err_log_mode='json')

# print(Path(r"E:\REQ\New Folder").name)
# print(type(Path(r"E:\REQ\New Folder")))
# print(Path(Path(r"E:\REQ\New Folder")).name)

# print(Path(r"E:\REQ\New Folder").joinpath(r"E:\REQ\New Folder\abcd"))
# print(Path(r"E:\REQ\New folder\5\lattex.txt").suffixes)
# shutil.rmtree(Path(r"E:\REQ\New Folder1"))
# # for i in range(10000+1):
# #     obj.progbar(i, 10000, "yoyo")

# # obj = Snap("")
# print(obj.get_nth_dirs(r"C:\Users", n=1))

# # obj.group_by_exts(exts=['pdf', 'jpg'])
# obj.send_to_server(host="155")
