import os
import sys
import shutil
import ntpath

def path_conv(path):
    if sys.platform.startswith('darwin'):
        return path.replace(ntpath.sep, os.sep)
    elif sys.platform.startswith('win'):
        return path.replace(os.sep, ntpath.sep)


def list_folder(dir:str) -> list[str]:
    ret_list = []

    for i in os.listdir(dir):
        if os.path.isdir(i) and not i.startswith('__') and not i.startswith('.') and not i.startswith('raw'):
            ret_list.append(i)

    return ret_list

ERR_ok = 0
ERR_dir_error = 1
ERR_mkdir_error = 2

def pick_file(dir:str, fExt:str, folder:str = None):

    if not os.path.isdir(dir):
        return 1
    
    fExt = fExt.upper()
    
    if folder == None:
        folde_name = fExt
    else:
        folde_name = folder

    if not os.path.isdir(path_conv('{}\\{}'.format(dir, folde_name))):
        if os.makedirs(path_conv('{}\\{}'.format(dir, folde_name))) != None:
            return ERR_mkdir_error
        
        
    for f in os.listdir(dir):
        if os.path.isdir(path_conv('{}\\{}'.format(dir, f))):
            continue
            
        actualExt = f.split('.')[-1]
        if actualExt.upper() == fExt:
            # print(path_conv('{}\\{}'.format(dir, f)), path_conv('{}\\{}\\{}'.format(dir, folde_name, f)))
            shutil.move(path_conv('{}\\{}'.format(dir, f)), path_conv('{}\\{}\\{}'.format(dir, folde_name, f)))
            
    return 0

def pick_multi_file(dir:str, fExtList:list[str], folder:str = None):
    ret = ERR_ok
    
    for i in fExtList:
        ret = pick_file(dir, i, folder)

        if ret != ERR_ok:
            return ret, i
        
    return ERR_ok, ''


if __name__ == '__main__':
    fileExtension = sys.argv[1:]

    print('Pick out file extension: ', end='')

    for i in fileExtension:
        print('.{} '.format(i), end='')

    print('')


    root_folders = list_folder('.')

    for index, value in enumerate(root_folders):
        print('  {:02d}: {}'.format(index, value))
    
    choose_id = input('enter folder id to process pick out: ')
    choose_id = choose_id.split()

    for i in choose_id:
        
        if not i.isdigit():
            continue

        i = int(i)
        if i >= len(root_folders):
            break
        
        ret, ext = pick_multi_file(root_folders[i], fileExtension, 'cameraJPG')
        if ret != ERR_ok:
            print('Unable to pick {} from folder:{}, error id: {}'.format(ext, root_folders[i], ret))

    
exit(0)