from os import listdir, stat, rename
from os.path import isfile, join
from datetime import datetime, timedelta

def getOldFiles(directory, current_time, files):
    directory_nodes = listdir(directory)
    for node in directory_nodes:
        path = join(directory, node)
        if isfile(path):
            thirty_days_ago = (current_time - timedelta(minutes=1)).timestamp()
            file_creation_time = stat(path).st_birthtime
            if file_creation_time < thirty_days_ago:
                files.append((directory, node))
            continue
        getOldFiles(path, current_time, files)

def moveToStaging(staging_directory, files):
    for directory, filename in files:
        original_path = f"{directory}/{filename}"
        new_path = f"{staging_directory}/{filename}"
        print(f"{original_path} -> {new_path}")
        rename(original_path, new_path)