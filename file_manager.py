class FileManager:
    def __init__(self):
        pass
    
    def read_file(self, filepath):
        lines = []
        
        try:
            with open(filepath, 'r', encoding="utf-8") as file:
                lines = file.readlines()
        except Exception as error:
            print(f'Unexpected error: {error}');
            return
        
        return lines;

    def filter_lines(self, source_lines, target):
        try:
            
            lines = source_lines
            result = []
        
            for line in lines:
                if (target in line):
                    result.append(line)
        
            if (len(result) == 0):
                raise Exception(f'No lines with the "{target}" was found');
        except Exception as error:
            print(f'Unexpected error: {error}');
            return;
        
        return result