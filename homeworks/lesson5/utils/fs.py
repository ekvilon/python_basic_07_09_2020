from os import path


def get_filename(script_file, name):
    return path.join(path.dirname(script_file), name)
