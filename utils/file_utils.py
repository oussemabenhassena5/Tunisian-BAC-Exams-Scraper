import os


def create_directories(path):
    """Create directories if they don't exist."""
    if path and not os.path.exists(path):
        os.makedirs(path)


def delete_empty_folders(path):
    """Delete empty folders recursively."""
    for root, dirs, files in os.walk(path, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")
            except OSError:
                pass
