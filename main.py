import re
from typing import Set

MAX_LENGTH = 255


def check_for_not_valid_name(pattern: str, input: str) -> bool:
    return re.match(pattern, input) is None


def get_set_of_unique_filenames(files: []) -> Set:
    set_of_files = set()
    set_of_files_doublicate = set()
    for file in files:
        if check_for_not_valid_name('^[A-Za-z0-9]*$', file):
            continue
        if file in set_of_files:
            set_of_files_doublicate.add(file)
        else:
            set_of_files.add(file)
    #order of valid files aren't documented
    return set_of_files.difference(set_of_files_doublicate)


def DFS(X: dict) -> None:
    global depth, path, buffer_path
    # check for max length
    cur_len = len(path) + sum((len(i) for i in path))
    if cur_len >= MAX_LENGTH:
        depth -= 1
        return

    for i, (key, val) in enumerate(X.items()):
        # check for alpha and digit
        if check_for_not_valid_name('^[A-Za-z0-9]*$', key):
            continue
        path = path[:depth]
        path.append(key)
        if isinstance(val, dict):
            depth += 1
            DFS(val)
        else:
            # check for duplicate files and not valid naming
            unique_files = get_set_of_unique_filenames(val)
            if len(unique_files) == 0:
                return
            else:
                path.append(unique_files.pop())

    if len(buffer_path) < len(path):
        buffer_path = path
    depth -= 1


def biggestPath(X: dict) -> str:
    # print(f'input: {X}')
    global depth, path, buffer_path
    depth = 0
    path = []
    buffer_path = []
    DFS(X)
    result = '/' + '/'.join(str(i) for i in buffer_path)
    return result


if __name__ == '__main__':
    pass


