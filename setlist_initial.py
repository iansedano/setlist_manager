
import os
import re

#sheet music location

path_to_music = '\\Dropbox\\0 Library\\Music\\0 Sheet Music & Transcriptions'
drive_letter = 'C'
full_path_to_folder = drive_letter + ':' + path_to_music
os.chdir(full_path_to_folder)


#making list of paths

print(os.getcwd())
print(os.walk("."))

'''
for root, dirs, files in os.walk("."):
    os.chdir(root)
    print('folder :' + root)
    for root, dirs, files in os.walk("."):
        print('files :')
        print(files)
    #for _dir in root:
    #    print(full_path_to_folder + '\\' + _dir)
        #return [f for f in files if f.endswith('.' + extension)]
'''

#"help - the beatles [open_mic solo_acoustic].txt"
#read the file into new file, then delete old file.

#list_of_full_paths = list_files('txt')

#print(list_of_full_paths)


set_lists = ('open_mic', 'jam_session', 'solo_acoustic', 'piano', 'learning',
    'looper', 'kids')

#making list of paths
list_of_full_paths = []
for root, dirs, files in os.walk("."):
    for filename in files:
        full_path = full_path_to_folder  + root[1:] + '\\' + filename
        list_of_full_paths.append(full_path)

list_of_txt_paths = []

for path in list_of_full_paths:
    if path.endswith('.txt'):
        list_of_txt_paths.append(path)


def make_set_list(set_list):
    regex = "\[.*" + set_list + ".*\]"
    for path in list_of_txt_paths:
        if re.search(regex, path):
            print(path)

make_set_list('learning')

def print_set_list(set_list):
    regex = "\[.*" + set_list + ".*\]"
    for path in list_of_txt_paths:
        if re.search(regex, path):
            os.startfile(path, "open")

#print_set_list('learning')


# takes out all [] tags with regex
def remove_all_tags():
    for path in list_of_txt_paths:
    print(re.sub('\[.*\]', '', path))



'''
pathlib

Python 3.4 introduced a new standard library
for dealing with files and paths called pathlib — and it’s great!

To use it,
you just pass a path or filename
into a new Path() object
using forward slashes
and it handles the rest:


    from pathlib import Path

    data_folder = Path("source_data/text_files/")

    file_to_open = data_folder / "raw_data.txt"

    f = open(file_to_open)

    print(f.read())

Notice two things here:

You should use forward slashes with pathlib functions.
The Path() object will convert forward slashes into the correct kind of slash
for the current operating system. Nice!
If you want to add on to the path,
you can use the / operator directly in your code.
Say goodbye to typing out os.path.join(a, b) over and over.

'''
