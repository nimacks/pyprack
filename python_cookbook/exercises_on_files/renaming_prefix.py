# create a program to rename prefixes in a directory with files
from pathlib import Path

# create a function to rename the files
def rename_files():
    root_dir = Path("python_cookbook/exercises_on_files/files")
    for file in root_dir.iterdir():
        if file.is_file():
            file.rename(file.with_name("prefix_" + file.name))
            
            
def list_directory():
    root_dir = Path("python_cookbook/exercises_on_files/files")
    names = root_dir.iterdir()
    text_files = [name for name in names if name.is_file()]
    text_files = [name for name in names if name.is_file()]
    print(text_files)
    
list_directory()