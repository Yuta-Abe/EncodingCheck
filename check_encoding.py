import sys
import os

def check_encoding(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            file.read()
        print(f"File {file_path} is {encoding} encoded.")
        return True
    except UnicodeDecodeError:
        print(f"File {file_path} is not {encoding} encoded.")
        return False

def main(directory):
    all_files_encoded_correctly = True
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not check_encoding(file_path):
                all_files_encoded_correctly = False
    if not all_files_encoded_correctly:
        sys.exit(1)

if __name__ == "__main__":
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(directory)
