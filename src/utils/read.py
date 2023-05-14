def read_file(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.read()
        csv_list = [text.strip() for text in file_contents.split(',')]

        if csv_list[-1] == '':
            return csv_list[:-1]

        return csv_list
    