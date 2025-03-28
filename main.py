from file_manager import FileManager


def middle_test_func(source_filepath, target_filepath, target):
    manager = FileManager()
    lines = manager.read_file(source_filepath)
    filtered_lines = manager.filter_lines(lines, target)
    manager.save_file(filtered_lines, target_filepath)


def main():
    SOURCE_FILE = 'public/text.txt'
    TARGET_FILE = 'public/filtered.txt'
    TARGET = 'boo'
    middle_test_func(SOURCE_FILE, TARGET_FILE, TARGET)


main()
