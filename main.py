import sys
from file_manager import FileManager 

def main():
    print('Test manager init')
    manager = FileManager();
    lines = manager.read_file('text.txt')
    print(manager.filter_lines(lines, 'boo'))

main()