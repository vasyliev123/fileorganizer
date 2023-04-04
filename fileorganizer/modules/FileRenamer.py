import os
import datetime
import random
from . import FileOrganizerModule

class FileRenamer(FileOrganizerModule.FileOrganizerModule):
    """A module for renaming files."""

    def rename_files(self, files, new_name, multi=False, format=None, ext=None):
        """Rename one or more files with the given name.

        Args:
            files (list): A list of file paths to rename.
            new_name (str): The new name to use for the files.
            multi (bool, optional): If True, rename all files to the same name.
                If False (default), append a number to each file name to make it unique.
            format (str, optional): The format to use for the new name. Valid values
                are "date" to append the file creation date, "random" to append a random
                string, or None (default) to use only the new name.
            ext (str, optional): The extension to use for the new name. If None (default),
                use the extension of the original file.

        Raises:
            OSError: If an error occurs while renaming the file.

        """
        for file in files:
            if str(file).startswith('*'):
                for file in self.get_files_with_ext(str(file)[1:]):
                    self.rename_file(file, new_name, format, ext)
            elif self.check_if_file(file):
                if multi:
                    self.rename_file(file, new_name, format, ext)
                else:
                    self.rename_file(file, new_name, ext)

    def rename_file(self, file, new_name, format=None, ext=None):
        """Rename a single file with the given name.

        Args:
            file (str): The path to the file to rename.
            new_name (str): The new name to use for the file.
            format (str, optional): The format to use for the new name. Valid values
                are "date" to append the file creation date, "random" to append a random
                string, or None (default) to use only the new name.
            ext (str, optional): The extension to use for the new name. If None (default),
                use the extension of the original file.

        Raises:
            OSError: If an error occurs while renaming the file.

        """
        # Get the file's directory and base name
        dir_name, base_name = os.path.split(file)

        # If the new name has a file extension, remove it
        new_name, _ = os.path.splitext(new_name)

        # Get the original file's extension if none is provided
        if ext is None:
            _, ext = os.path.splitext(file)

        # Append a date or random string if requested
        if format == "date":
            date_str = datetime.datetime.fromtimestamp(super().get_file_creation_date(file).strftime("%Y%m%d_%H%M%S"))
            new_name = f"{new_name}_{date_str}"
        elif format == "random":
            rand_str = super().get_random_string()
            new_name = f"{new_name}_{rand_str}"

        # Add the new extension
        new_name += ext

        # Construct the new file path
        new_file = os.path.join(dir_name, new_name)

        # Rename the file
        try:
            os.rename(file, new_file)
        except OSError as e:
            raise OSError(f"Failed to rename file {file} to {new_file}: {e.strerror}") from e
