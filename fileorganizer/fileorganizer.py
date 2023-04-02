import importlib
import argparse
from modules.file_scanner import file_scanner
import sys
class fileorganizer():
    def __init__(self):
        print('File Organizer')
        self.parse_args()

    def parse_args(self):
        parser = argparse.ArgumentParser(description='File Organizer')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1.0')


        subparsers = parser.add_subparsers(dest='command', help='Subcommand to execute')

        scan_parser = subparsers.add_parser('scan', help='Scan a directory')
        scan_parser.add_argument('dir', help='Directory to scan', default='.', nargs='?')   
        scan_parser.add_argument('-r', '--recursive', dest='recursive', help='Scan subdirectories', action='store_false')
        scan_parser.add_argument('-lvl', '--level', dest='level', help='Level of subdirectories to scan', type=int, default=2)

        args = parser.parse_args()
        print(args)
        if args.command == 'scan':
            file_scanner().scan_directory(args.dir, args.recursive, args.level)

    def run(self):
        pass        

if __name__ == '__main__':
    fileorganizer().run()