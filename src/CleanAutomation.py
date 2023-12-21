import os
import src.paths as paths
import src.extensions as extensions
import src.helpers as helpers


# Method to organise files in param --pathToClean and move it to specific folders in --pathToCleanTo
def clean_automation(pathToCleanFrom, pathToCleanTo):
    print("\n"+"Cleaning Process RUNNING".center(40, "-"))

    if not os.path.exists(pathToCleanFrom):
        # Se não existir path que se pretende limpar, procura dar clean ao Desktop
        pathToCleanFrom = paths.Desktop

    if not os.path.exists(pathToCleanTo):
        # Se não for definido um path para criar novas pastas, então cria onde está a limpar
        pathToCleanTo = pathToCleanFrom

    # Path para as pastas de limpeza que serão criadas
    paths_To_clean_folder = paths.get_paths(pathToCleanTo)
    dictFolders = dict(paths_To_clean_folder)

    # DONE : Verify if folders to organise exist, else create it
    for folder in dictFolders.values():
        if not os.path.exists(folder):
            os.makedirs(folder)

    # DONE : CYCLE ALL FILES
    for filename in os.listdir(pathToCleanFrom):

        # DONE : CONDITIONS
        if filename.startswith("Screenshot "):
            # DONE: if name contains Screenshot add to folder Screenshots
            helpers.move_file(dictFolders['Screenshots'], pathToCleanFrom, filename)
        elif filename.endswith(tuple(extensions.video)):
            # DONE: if contain video extensions add to folder Images/Videos
            helpers.move_file(dictFolders['Videos'], pathToCleanFrom, filename)
        elif filename.endswith(tuple(extensions.compressed)):
            # TODO: if zip Then extract folder
            helpers.move_file(dictFolders['Compressed'], pathToCleanFrom, filename)
        elif filename.endswith(tuple(extensions.installers)):
            helpers.move_file(dictFolders['Installers'], pathToCleanFrom, filename)
        elif filename.endswith(tuple(extensions.document)):
            helpers.move_file(dictFolders['Documents'], pathToCleanFrom, filename)
        elif filename.endswith(tuple(extensions.image)):
            helpers.move_file(dictFolders['Images'], pathToCleanFrom, filename)  # DONE : MOVE FILE

    print(f"=> {helpers.count[0]} <= files moved from '{pathToCleanFrom}' to '{pathToCleanTo}' folder.")
    helpers.count[0] = 0