import os
import random
import string

class FileOrganizerModule:
    """
    Parent class for all File Organizer modules. Provides common functionality.

    Attributes:
    - entities: a list of file or directory entities in a given directory
    """

    def __init__(self):
        self.entities = []


    def get_files(self, directory, recursive, lvl):
        """
        Recursively collects all file entities in a directory and its subdirectories.

        Args:
        - directory: the directory to scan for files
        - recursive: whether or not to search subdirectories for files
        - lvl: the depth of subdirectories to search

        Returns:
        None
        """
        self.check_if_dir(directory)
        try:
            with os.scandir(directory) as dir:
                for i, entity in enumerate(dir):
                    if entity.is_file():
                        self.entities.append(entity)
                    elif entity.is_dir() and recursive and lvl > 1:
                        self.get_files(entity.path, recursive, lvl)
        except PermissionError:
            pass
        
        return self.entities
    
    def get_files_with_ext(self, ext):
        """ Returns a list of files with a given extension. """
        return [file for file in self.get_files(".", True, 2) if os.path.splitext(file)[1]==ext]
        
        
    def check_if_dir(self, directory):
        """
        Checks if a given directory exists and is a directory.

        Args:
        - directory: the directory to check

        Returns:
        - True if the directory exists and is a directory, else False
        """
        if not os.path.realpath(directory):
            print("Not a directory")
            return False


    def check_if_file(self, file):
        """
        Checks if a given file exists and is a file.

        Args:
        - file: the file to check

        Returns:
        - True if the file exists and is a file, else False
        """
        if not os.path.isfile(file):
            print("Not a file")
            return False
        return True
    
    def get_file_name(self, file):
        """
        Returns the name of a given file.

        Args:
        - file: the file to get the name of

        Returns:
        - the name of the file
        """
        return os.path.basename(file)
    
    def get_file_creation_date(self, file):
        """
        Returns the creation date of a given file.

        Args:
        - file: the file to get the creation date of

        Returns:
        - the creation date of the file
        """
        return os.path.getctime(file)
    
    
    def get_random_string(self, length=10):
        """
        Returns a random string of a given length.

        Args:
        - length: the length of the random string

        Returns:
        - a random string of a given length
        """
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))