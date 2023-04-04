from . import FileOrganizerModule
import re

class FileMover(FileOrganizerModule.FileOrganizerModule):
    def __init__(self):
        super().__init__()
        self.files_to_move = []
        
        
    def move_files(self, files, destination):
        pattern = re.compile(r'^(?P<name>.*)\.(?P<ext>.*)$')
        for file in files:
            match = pattern.match(file)   
            if match:
                if match.group('name') == '*':
                      self.files_to_move =[file for file in super().get_files('.', False, 0) if super().get_file_name(file).endswith(match.group('ext'))]
                      print(self.files_to_move)
            