
import os
import re

#sheet music location
path_to_music = '\\Dropbox\\0 Library\\Music\\0 Sheet Music & Transcriptions'
drive_letter = 'C'
full_path_to_folder = drive_letter + ':' + path_to_music
os.chdir(full_path_to_folder)

#set list names
set_lists = ('open_mic', 'jam_session', 'solo_acoustic', 'piano', 'learning',
    'looper', 'kids')

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

print_set_list('learning')

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

