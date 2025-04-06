import os
import sys
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

def search_files(dir, fildExt):
    rsltFiles = []

    for root, dirs, files in os.walk(dir):
        for f in files:
            if f.endswith('.{}'.format(fildExt)):
                rsltFiles.append(path_conv('{}\\{}'.format(root, f)))

    return rsltFiles

if __name__ == '__main__':
    
    root_folders = list_folder('.')
    for index, value in enumerate(root_folders):
        print('  {:02d}: {}'.format(index, value))
    
    choose_id = input('enter folder id to process rename: ')
    choose_id = choose_id.split()

    for i in choose_id:

        if not i.isdigit():
            continue

        i = int(i)
        if i >= len(root_folders):
            break
        
        jpg_list = search_files(root_folders[i], 'jpg')

        for f in jpg_list:
            if '-Enhanced-NR' in f:
                os.rename(f, f.replace('-Enhanced-NR', ''))
    
exit(0)