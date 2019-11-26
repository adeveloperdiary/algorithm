import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    arr = list()
    if path.strip(' ') == "":
        return []
    else:
        paths = os.listdir(path)
        parent = path

        if paths is None or len(paths) == 0:
            return []
        else:
            for p in paths:
                if os.path.isfile(os.path.join(parent, p)) and p.endswith(suffix):
                    arr.append(os.path.join(parent, p))

                if os.path.isdir(os.path.join(parent, p)):
                    child_arr = find_files(suffix, os.path.join(parent, p))
                    arr.extend(child_arr)

    return arr


if __name__ == '__main__':
    print(find_files(".c", "testdir"))
    print(find_files(".c", ""))
