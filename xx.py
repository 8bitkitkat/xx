#!/usr/bin/env python3

import sys
import os
import glob
import shutil


# if any path to be deleted has a substring of one of these it is ignored
removeIgnoredPaths = []


actions = {}
def Action(tag, desc=""):
    def _(f):
        actions[tag] = (f, desc)
        return f
    return _


def osrun(cmd):
    print(cmd)
    os.system(cmd)


def __remove(path):
    print(f"deleting {path}")
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError(f"path '{path}' is not a file or dir.")


def remove_noignore(path):
    paths = glob.glob(path)
    for path in paths:
        if not os.path.exists(path):
            continue
        __remove(path)


def remove(path):
    paths = glob.glob(path)
    for path in paths:
        cont = False
        for ignored in removeIgnoredPaths:
            if ignored in path:
                cont = True
                break
        if cont:
            continue

        if not os.path.exists(path):
            continue

        __remove(path)


def remove_paths(paths):
    for path in paths:
        remove(path)


def mkdir(path):
    print(f"mkdir -p {path}")
    if not os.path.exists(path):
        os.makedirs(path)


def chdir(path):
    print(f"cd {path}")
    os.chdir(path)


def pushd(path):
    print(f"pushd {path}")
    os.chdir(path)


def popd():
    print("popd")
    os.chdir("../")


def print_usage():
    print(f"Usage: {sys.argv[0]} ACTION")


def print_actions():
    print("Actions:")
    for name in actions:
        print(f"\t{name}\t{actions[name][1]}")


@Action("help|h", "print this message")
def help():
    print_usage()
    print()
    print_actions()


def main():
    action = sys.argv[1]

    for key in actions:
        options = key.split("|")
        for x in options:
            if action == x:
                f = actions[key]
                f[0]()
                return

    print_usage()
    print(f"run '{sys.argv[0]} help' for more information")
    exit(2)


if __name__ == '__main__':
    main()
