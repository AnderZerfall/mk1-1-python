class FileManager:
    def __init__(self):
        pass
    
    def read_file(self, filepath):
        lines = []
        
        with open(filepath, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        
        return lines;
    
    # def save_file(self):
    #     return

    # def filter_file(self):
    #     return