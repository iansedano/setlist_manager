# Import the os module, for the os.walk function
import os

# Set the directory you want to start from

path_to_music = '\\Dropbox\\0 Library\\Music\\0 Sheet Music & Transcriptions'
drive_letter = 'C'
full_path_to_folder = drive_letter + ':' + path_to_music
os.chdir(full_path_to_folder)


for dirName, subdirList, fileList in os.walk('.'):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)


"""
dirName: The next directory it found.
subdirList: A list of sub-directories in the current directory.
fileList: A list of files in the current directory.
"""

print('\n\n\n\n\n\n\n\n\n\n')

for dirName, subdirList, fileList in os.walk('.', topdown=False):
    print('Found directory: %s' % dirName)
    for fname in fileList:
        print('\t%s' % fname)


# The extension to search for
exten = '.txt'

for dirpath, dirnames, files in os.walk('.'):
    for name in files:
        if name.lower().endswith(exten):
            print(os.path.join(dirpath, name))
