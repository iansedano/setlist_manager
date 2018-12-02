
import os
import re

#sheet music location
path_to_music = '\\Dropbox\\0 Library\\Music\\0 Sheet Music & Transcriptions'
drive_letter = 'C'
full_path_to_folder = drive_letter + ':' + path_to_music
os.chdir(full_path_to_folder)

#set list names
set_lists = ('open_mic', 'jam_session', 'solo_acoustic', 'piano', 'learning',
    'looper', 'kids', 'pop')

#making list of paths
list_of_full_paths = []
for root, dirs, files in os.walk("."):
    for filename in files:
        full_path = full_path_to_folder  + root[1:] + '\\' + filename
        list_of_full_paths.append(full_path)

#making list of txt files
list_of_txt_paths = []
for path in list_of_full_paths:
    if path.endswith('.txt'):
        list_of_txt_paths.append(path)


def print_set_list(set_list):
    regex = "\[.*" + set_list + ".*\]"
    for path in list_of_txt_paths:
        if re.search(regex, path):
            print(path)

#print_set_list('learning')

def open_set_list(set_list):
    regex = "\[.*" + set_list + ".*\]"
    for path in list_of_txt_paths:
        if re.search(regex, path):
            os.startfile(path, "open")

#open_set_list('learning')


# takes out all [] tags with regex
def remove_all_tags():
    for path in list_of_txt_paths:
        print(re.sub('\[.*\]', '', path))


#generating md5
import hashlib

def md5_list(list_of_paths):
    md5s = []
    for path in list_of_paths:
        md5s.append(hashlib.md5(open(path, 'rb').read()).hexdigest())
    return(md5s)

md5_txts = md5_list(list_of_txt_paths)

#making dictionary with md5s as keys
keys = md5_txts
values = list_of_txt_paths
txt_dict = dict(zip(keys,values))
print(txt_dict)


#changing working directory to script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


#writing dict to file
import json

json.dump(txt_dict, open("txt_dict",'w'))


# script to get creation date for file to check if same file...
import platform

def creation_date(path_to_file):
    """
    Try to get the date that a file was created, falling back to when it was
    last modified if that isn't possible.
    See http://stackoverflow.com/a/39501288/1709587 for explanation.
    """
    if platform.system() == 'Windows':
        return os.path.getctime(path_to_file)
    else:
        stat = os.stat(path_to_file)
        try:
            return stat.st_birthtime
        except AttributeError:
            # We're probably on Linux. No easy way to get creation dates here,
            # so we'll settle for when its content was last modified.
            return stat.st_mtime
