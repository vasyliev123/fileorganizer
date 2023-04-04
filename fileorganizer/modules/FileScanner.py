import os
from . import FileOrganizerModule

class FileScanner(FileOrganizerModule.FileOrganizerModule):
    def __init__(self):
        super().__init__()
        self.entities = []
    
    def display_file_tree(self, directory, recursive, lvl, floor=0):
        """
        Display a tree-like structure of the files and directories under the specified directory.

        Args:
        - directory (str): Path to the directory to scan.
        - recursive (bool): A boolean indicating whether to scan the subdirectories recursively or not.
        - lvl (int): An integer indicating the number of levels of subdirectories to scan.
        - floor (int): The depth of the current directory relative to the root directory.

        Returns:
        - None
        """

        # check if the directory exists and is accessible
        super().check_if_dir(directory)

        try:
            with os.scandir(directory) as dir:
                # loop through all the files and directories in the directory
                for i, entity in enumerate(dir):
                    if entity.is_file():
                        # display file name with appropriate indentations
                        print("│    "*floor+("├─") + entity.name)
                    elif entity.is_dir() and recursive:
                        # display directory name with appropriate indentations
                        print("│    "*floor+"├─" + entity.name)

                        if lvl>1:
                            # scan the subdirectories recursively
                            self.display_file_tree(entity.path, recursive, lvl-1, floor+1)
                        else:
                            # display the subdirectory name without scanning its contents
                            print("│    "*floor+"├─" + entity.name)
                    else:
                        # display the name of non-file and non-directory entities
                        print("│    "*floor+"├─" + entity.name)

                    # add the entity to the list of scanned entities
                    self.entities.append(entity)

        except PermissionError:
            # handle permission errors
            print("│    "*floor+("└─") + "Access Denied: " + directory)
