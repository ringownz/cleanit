import os

# Paths to each type we are trying to organise
Desktop = os.path.expanduser("~/Desktop")  # Get desktop path


def get_paths(path_organised):

    Images = os.path.join(path_organised, "Images")
    Videos = os.path.join(Images, "Videos")
    Screenshots = os.path.join(Images, "Screenshots")
    Installers = os.path.join(path_organised, "Installers")
    Documents = os.path.join(path_organised, "Documents")
    Compressed = os.path.join(path_organised, "Compressed")

    result = (
        ('Videos', Videos),
        ('Screenshots', Screenshots),
        ('Installers', Installers),
        ('Documents', Documents),
        ('Compressed', Compressed),
        ('Images', Images)
    )

    return result
