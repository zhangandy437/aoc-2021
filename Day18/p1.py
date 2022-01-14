def input(path):
    f = open(path, "r")
    lines = f.read().splitlines()
    f.close()
    return lines