import os
import shutil


def list_folder(dir:str) -> list[str]:
    ret_list = []

    for i in os.listdir(dir):
        if not i.startswith('__'):
            ret_list.append(i)

    return ret_list

ERR_ok = 0
ERR_dir_error = 1
ERR_mkdir_error = 2


def separate_file(dir:str, fExt1:str, fExt2:str) -> int:

    if not os.path.isdir(dir):
        return 1
    
    fExt1 = fExt1.upper()
    fExt2 = fExt2.upper()
    
    if not os.path.isdir('{}\{}'.format(dir, fExt1)):
        if os.makedirs('{}\{}'.format(dir, fExt1)) != None:
            return ERR_mkdir_error
        
    if not os.path.isdir('{}\{}'.format(dir, fExt2)):
        if os.makedirs('{}\{}'.format(dir, fExt2)) != None:
            return ERR_mkdir_error
    
    for f in os.listdir(dir):
        if f.endswith('.' + fExt1):
            shutil.move('{}\{}'.format(dir, f), '{}\{}\{}'.format(dir, fExt1, f))
            
        if f.endswith('.' + fExt2):
            shutil.move('{}\{}'.format(dir, f), '{}\{}\{}'.format(dir, fExt2, f))

    return 0


if __name__ == '__main__':
    root_folders = list_folder('.')

    for index, value in enumerate(root_folders):
        print('  {:02d}: {}'.format(index, value))

    choose_id = input('enter folder id to separate NFE and JPG:')
    choose_id.split()
    choose_id = [int(item) for item in choose_id if item.isdigit()]

    for i in choose_id:
        if i >= len(root_folders):
            break
        
        ret = separate_file(root_folders[i], 'NEF', 'JPG')
        if ret:
            print('Unable to process folder:{}, error id: {}'.format(root_folders[i], ret))

    os.system('pause')
    