import sys
import shutil
from typing import Callable
from pathlib import Path

def iter_files_recursively(directory: Path, cb: Callable) -> None:
    for item in directory.iterdir():
        if item.is_dir():
            iter_files_recursively(item, cb)
        else:
            if item.exists():
                cb(item)
                  
def copy_file_to(output_dir: Path) -> None:
    def copy_file(file: Path) -> None:
        file_path = file.absolute()
        if str(file_path).startswith(str(output_dir)):
            return
        
        file_extension = file.suffix[1:]

        if file_extension == '':
            file_extension = 'no_extension'
        
        destination_dir = output_dir / file_extension

        if not destination_dir.exists():
            destination_dir.mkdir(parents=True)
        try:
            shutil.copy2(file_path, destination_dir)
        except FileNotFoundError as _:
            print("File not found or not available", file_path)
        
    return copy_file

def main():
    if len(sys.argv) >= 2:
        input_dir = Path(sys.argv[1])
        output_dir = Path(sys.argv[2]) if len(sys.argv) == 3 else Path.cwd() / "dist"

        if input_dir.exists():
            iter_files_recursively(input_dir, copy_file_to(output_dir))
        else:
            print(f"Directory {input_dir} not found")
    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()