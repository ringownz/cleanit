import os

count = [0]


# Make name unique
def make_unique(dest, name):
    filename, extension = os.path.splitext(name)
    counter = 1
    while os.path.exists(os.path.join(dest, f"{filename}{counter}{extension}")):
        counter += 1

    return f"{filename}{counter}{extension}"


# Move files to Expected path
def move_file(destination, source, name):
    oldName = os.path.join(source, name)
    newName = os.path.join(destination, name)

    # DONE: Verify if already exists file with same name THEN create new name
    if os.path.exists(newName):
        unique_name = make_unique(destination, name)
        newName = os.path.join(destination, unique_name)

    os.rename(oldName, newName)
    count[0] += 1
