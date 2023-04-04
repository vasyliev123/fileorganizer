import os
from datetime import datetime
from . import FileOrganizerModule


class FileInfo(FileOrganizerModule.FileOrganizerModule):
    """A class for retrieving and displaying file information."""

    def __init__(self):
        """Initializes the FileInfo object."""
        super().__init__()
    
    
    def get_files_info(self, files=None):
        """
        Retrieves file information for the specified files and directories.

        Args:
            files (list): A list of file paths or directories to retrieve information for.
                If None, retrieves information for all files in the current directory.
        """
        if not files:
            # No files provided, get info for all files in the current directory
            super().get_files('.', False, 0)
        else:
            # Iterate over the provided files/directories
            for file in files:
                # If the file exists and is a regular file, display its info
                if super().check_if_file(file):
                    self.display_file_info(file)

    
    
    def display_file_info(self, entity):
        """
        Displays information for the specified file.

        Args:
            entity (str): The file path to retrieve information for.
        """
        # Get the file's stats
        stats = os.stat(entity)
        # Display the file's info
        print("\n" +"Stats for: " + entity)
        print("  Size: " + str(stats.st_size) + " bytes")

        # Display creation time
        created_time = datetime.fromtimestamp(stats.st_ctime)
        print("  Created: " + created_time.strftime('%Y-%m-%d %H:%M:%S'))

        # Display last modified time
        modified_time = datetime.fromtimestamp(stats.st_mtime)
        print("  Last modified: " + modified_time.strftime('%Y-%m-%d %H:%M:%S'))

        # Display last accessed time
        accessed_time = datetime.fromtimestamp(stats.st_atime)
        print("  Last accessed: " + accessed_time.strftime('%Y-%m-%d %H:%M:%S'))
        
        # Display extension
        extension = os.path.splitext(entity)[1]
        print("  Extension: " + extension)
