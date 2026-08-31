from pathlib import Path


def scan_directory(directory):
    path = Path(directory)

    if not path.exists():
        raise FileNotFoundError(
            f"Directory does not exist: {directory}"
        )

    if not path.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {directory}"
        )

    files = []
    directories = []

    for item in path.rglob("*"):
        if item.is_file():
            files.append(item)
        elif item.is_dir():
            directories.append(item)

    return files, directories