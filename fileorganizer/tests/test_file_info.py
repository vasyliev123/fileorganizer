import unittest
import os
from datetime import datetime
from modules.file_info import file_info
from io import StringIO
import sys


class TestFileInfo(unittest.TestCase):

    def setUp(self):
        # Create a test directory and files
        if not os.path.exists('test_dir'):
            os.mkdir('test_dir')
            os.chdir('test_dir')
            with open('test_file1.txt', 'w') as f:
                f.write('test file content!')
            with open('test_file2.txt', 'w') as f:
                f.write('test file content!')
            os.mkdir('test_subdir')
            with open('test_subdir/test_file3.txt', 'w') as f:
                f.write('test file content!')
    os.chdir('test_dir')

    def tearDown(self):
        # Delete test directory and files
        os.chdir('..')
        os.rmdir('test_dir')

    def test_get_files_info(self):
        fi = file_info()
        capturedOutput = StringIO()     
        sys.stdout = capturedOutput   
        
        # Test getting info for a single file
        expected_output = "\nStats for: test_file1.txt\n  Size: 18 bytes\n  Created: " + \
                          datetime.fromtimestamp(os.stat('test_file1.txt').st_ctime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last modified: " + datetime.fromtimestamp(os.stat('test_file1.txt').st_mtime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last accessed: " + datetime.fromtimestamp(
                              os.stat('test_file1.txt').st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n"
        
        fi.get_files_info(['test_file1.txt'])
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

        # Test getting info for multiple files
        expected_output = "\nStats for: test_file1.txt\n  Size: 18 bytes\n  Created: " + \
                          datetime.fromtimestamp(os.stat('test_file1.txt').st_ctime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last modified: " + datetime.fromtimestamp(os.stat('test_file1.txt').st_mtime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last accessed: " + datetime.fromtimestamp(os.stat('test_file1.txt').st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n" + \
                          "\nStats for: test_file2.txt\n  Size: 18 bytes\n  Created: " + \
                          datetime.fromtimestamp(os.stat('test_file2.txt').st_ctime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last modified: " + datetime.fromtimestamp(os.stat('test_file2.txt').st_mtime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last accessed: " + datetime.fromtimestamp(
                              os.stat('test_file2.txt').st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n"
                          
        print(expected_output)
        fi.get_files_info(['test_file1.txt', 'test_file2.txt'])
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)

        # Test getting info for a directory
        expected_output = "\nStats for: test_file1.txt\n  Size: 18 bytes\n  Created: " + \
                          datetime.fromtimestamp(os.stat('test_file1.txt').st_ctime).strftime('%Y-%m-%d %H:%M:%S') + \
                          "\n  Last modified: " + datetime.fromtimestamp(os.stat('test_file1.txt').st_mtime).strftime('%Y-%m-%d %H:%M:%S') + \
            "\n  Last accessed: " + datetime.fromtimestamp(os.stat('test_file1.txt').st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n" + \
            "\nStats for: test_file2.txt\n  Size: 18 bytes\n  Created: " + \
            datetime.fromtimestamp(os.stat('test_file2.txt').st_ctime).strftime('%Y-%m-%d %H:%M:%S') + \
            "\n  Last modified: " + datetime.fromtimestamp(os.stat('test_file2.txt').st_mtime).strftime('%Y-%m-%d %H:%M:%S') + \
            "\n  Last accessed: " + datetime.fromtimestamp(os.stat('test_file2.txt').st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n" + \
            "\nStats for: test_subdir/test_file3.txt\n  Size: 18 bytes\n  Created: " + \
            datetime.fromtimestamp(os.stat('test_subdir/test_file3.txt').st_ctime).strftime('%Y-%m-%d %H:%M:%S') + \
            "\n  Last modified: " + datetime.fromtimestamp(os.stat('test_subdir/test_file3.txt').st_mtime).strftime('%Y-%m-%d %H:%M:%S') + \
            "\n  Last accessed: " + datetime.fromtimestamp(os.stat(
                'test_subdir/test_file3.txt').st_atime).strftime('%Y-%m-%d %H:%M:%S') + "\n"
        fi.get_files_info(['test_file1.txt', 'test_file2.txt', 'test_subdir'])
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), expected_output)
        
        self.tearDown()
        
