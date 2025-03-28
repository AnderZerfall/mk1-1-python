import sys
from file_manager import FileManager 

def main():
    print('Test manager init')
    manager = FileManager();
    lines = manager.read_file('text.txt')
    filtered_lines = manager.filter_lines(lines, 'boo')
    manager.save_file(filtered_lines, 'filtered.txt')

main()