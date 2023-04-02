import os

class file_scanner():
    def __init__(self):
        self.entities = []
    
    def scan_directory(self, directory, recursive, lvl):
        self.display_tree(directory, recursive, lvl)
        return self.entities
        

                    
    def display_tree(self, directory, recursive, lvl, floor=0):
        try:
            with os.scandir(directory) as dir:
                for i, entity in enumerate(dir):
                    if entity.is_file():
                        print("│    "*floor+("├─") + entity.name)
                    elif entity.is_dir() and recursive:
                        print("│    "*floor+"├─" + entity.name)
                        if lvl>0:
                            self.display_tree(entity.path, recursive, lvl-1, floor+1)
                        else:
                            print("│    "*floor+"├─" + entity.name)
                    else:
                        print("│    "*floor+"├─" + entity.name)
                    self.entities.append(entity)
        except PermissionError:
            print("│    "*floor+("└─") + "Access Denied: " + directory)