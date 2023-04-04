import importlib
import argparse

import sys


class FileOrganizer():
    def __init__(self):
        self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description='File Organizer')
        parser.add_argument('-v', '--version',
                            action='version', version='%(prog)s 0.1.0')

        subparsers = parser.add_subparsers(
            dest='command', help='Subcommand to execute')

        scan_parser = subparsers.add_parser('scan', help='Scan a directory')
        scan_parser.add_argument(
            'dir', help='Directory to scan', default='.', nargs='?')
        scan_parser.add_argument(
            '-r', '--recursive', dest='recursive', help='Scan subdirectories', action='store_true')
        scan_parser.add_argument('-lvl', '--level', dest='level',
                                 help='Level of subdirectories to scan', type=int, default=2)

        info_paresr = subparsers.add_parser(
            'info', help='Get info about a file(s)')
        info_paresr.add_argument(
            'files', help='File to get info about', nargs='*')
        
        move_parser = subparsers.add_parser('move', help='Move a file(s)')
        move_parser.add_argument('files', help='File to move', nargs='+')
        move_parser.add_argument('destination', help='Destination to move file(s) to')
        
        rename_parser = subparsers.add_parser('rename', help='Rename a file(s)')
        rename_parser.add_argument('-m', '--multiple', dest='multiple', help='Rename multiple files', action='store_true')
        rename_parser.add_argument('-p', '--pattern', dest='pattern', help='Pattern to rename files', choices=['date', 'random'], default='date')
        rename_parser.add_argument('files', help='Files to rename', nargs='+')
        rename_parser.add_argument('-e', '--extension', dest='extension', help='Extension to rename files', default=None, nargs='?')
        rename_parser.add_argument('new_name', help='New name for file(s)')
        args = parser.parse_args()
        if args.command == 'scan':
            FileScanner = importlib.import_module('modules.FileScanner')
            FileScanner.FileScanner().display_file_tree(
                args.dir, args.recursive, args.level)
        elif args.command == 'info':
            FileInfo = importlib.import_module('modules.FileInfo')
            FileInfo.FileInfo().get_files_info(args.files)
            
        elif args.command == 'move':
            FileMover = importlib.import_module('modules.FileMover')
            FileMover.FileMover().move_files(args.files, args.destination)

        elif args.command == 'rename':
            FileRenamer = importlib.import_module('modules.FileRenamer')
            FileRenamer.FileRenamer().rename_files(args.files, args.new_name, args.multiple, args.pattern, args.extension)
    def run(self):
        pass


if __name__ == '__main__':
    FileOrganizer().run()
