class FileManager:
    def __init__(self):
        pass

    def read_file(self, filepath):
        lines = []

        try:
            with open(filepath, 'r', encoding="utf-8") as file:
                for line in file:
                    clean_line = line.replace("\n", "")
                    lines.append(clean_line)

            print(f'File has been successfully read from [{filepath}]')
        except Exception as error:
            print(f'Unexpected error: {error}')
            return

        return lines

    def save_file(self, source_lines, target_filepath):
        try:
            if (len(source_lines) == 0):
                raise Exception(
                    f'The source array is empty, so there is no point in saving something, lol')

            with open(target_filepath, "w", encoding="utf-8") as file:

                for line in source_lines:
                    file.write(line + "\n")

            print(f'File has been successfully written in [{target_filepath}]')
        except Exception as error:
            print(f'Unexpected error: {error}')

    def filter_lines(self, source_lines, target):
        try:

            lines = source_lines
            result = []

            for line in lines:
                if (target in line):
                    clean_line = line.replace("\n", "")
                    result.append(clean_line)

            if (len(result) == 0):
                raise Exception(f'No lines with the "{target}" was found')

            print(f'Lines has been successfully filtered [{result}]')
        except Exception as error:
            print(f'Unexpected error: {error}')
            return

        return result