import sys
import os.path
import json

# write a default config if it's not found
if not os.path.exists(os.path.join(os.getcwd(), "RenPurgeConfig.json")):
    print("Couldn't find config file, writing a default one")
    defaultConfig = {"extensions": ['.rpyc', '.rpyb', '.bak', '.rpymc', '.pyo', '.save', 'persistent'],
                     "delete empty folders": True,
                     "jump one directory upwards": False}
    with open('RenPurgeConfig.json', 'w') as configFile:
        json.dump(defaultConfig, configFile, indent=2)
        print("Default config file created")
    if str(input("Input y to proceed with default settings: ")) != 'y':
        sys.exit()

# open config file & load all config vars
config = open('RenPurgeConfig.json', 'r')
config = json.load(config)
purgefolders = config["delete empty folders"]
extensionsToCheck = config["extensions"]
jumpOneDirUp = config["jump one directory upwards"]

# killcount vars
foldersremoved = 0
filesremoved = 0

# turn ext list into a tuple
extensionsToCheck = tuple(extensionsToCheck)

# jump 1-dir upwards
if jumpOneDirUp:
    os.chdir("..")

# print what we're working with here
if purgefolders:
    print("Will delete empty folders")
else:
    print("Will not delete empty folders")

if jumpOneDirUp:
    print("Will jump one directory up from the RenPurge.exe path")
else:
    print("Will not jump one directory up from the RenPurge.exe path")

print("Extensions to delete: ", extensionsToCheck)
# pre-launch safety check
print("Working directory, MUST be 'project\\game': ", os.getcwd())
if str(input("Input y to proceed: ")) != 'y':
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
input("\nPress enter to quit.")
