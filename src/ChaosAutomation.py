import os
from pathlib import Path
import src.paths as paths
import src.helpers as helpers


def chaos_automation(path_to_destroy, path_to_make_hell):
    # Chaos will merge in Downloads folder if doesnt exist
    if not os.path.exists(path_to_make_hell):
        path_to_make_hell = str(Path.home() / "Downloads")

    if not os.path.exists(path_to_destroy):
        path_to_destroy = paths.Desktop

    dictFolders = dict(paths.get_paths(path_to_destroy))
    # Moves files from each folder that was used while cleaning to Downloads

    for folder in dictFolders.values():
        print("folder:" + folder)
        if os.path.exists(folder):
            for filename in os.listdir(folder):
                if os.path.isfile(os.path.join(folder, filename)):
                    print("paths:" + filename)
                    helpers.move_file(path_to_make_hell, folder, filename)

    # If folders are empty then delete
    for folder in dictFolders.values():
        if os.path.exists(folder):
            if len(os.listdir(folder)) == 0:
                os.rmdir(folder)

    print(f"=> {helpers.count[0]} <= files moved from '{path_to_destroy}' to '{path_to_make_hell}' folder.")
    helpers.count[0] = 0
