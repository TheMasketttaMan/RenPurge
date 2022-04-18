import os
import sys

# killcount vars
foldersremoved = 0
filesremoved = 0

# list extensions to check by default
extensionsToCheck = ['.rpyc', '.rpyb', '.bak', '.rpymc', '.pyo']

# ask user if they want to kill saves, extend the list if they do
if str(input("Input y to purge saves and persistent data too, anything else to skip: ")) == 'y':
    extensionsToCheck.extend(['.save', 'persistent'])

# display what we'll actually destroy here
print("Extensions to purge: ", extensionsToCheck)

# ask bout empty folders
purgefolders = False
if str(input("Input y to purge empty folders too, anything else to skip: ")) == 'y':
    purgefolders = True

# turn ext list into a tuple
extensionsToCheck = tuple(extensionsToCheck)

# pre-launch safety check
os.chdir("..")
print("Working directory, should be 'project\\game': ", os.getcwd())
if str(input("Input y to proceed with the purge: ")) != 'y':
    sys.exit()

# the loop
print("Beginning the purge.")
for path, subdirs, files in os.walk(os.getcwd(), topdown=False):
    print("Scanning directory: ", path)
    for name in files:
        print("Checking file: ", name)
        if name.endswith(extensionsToCheck):
            os.remove(os.path.join(path, name))
            print("Deleting file: ", os.path.join(path, name))
            filesremoved += 1
        else:
            print("Skipping file: ", name)

    if purgefolders:
        if len(os.listdir(path)) == 0:
            os.rmdir(path)
            print("Deleting empty dir: ", path)
            foldersremoved += 1

print("Operation complete.")
print("Files purged: ", filesremoved)
if purgefolders:
    print("Empty folders purged: ", foldersremoved)
input("Press enter to quit.")
