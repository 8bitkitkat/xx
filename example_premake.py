#!/usr/bin/env python3

BINARY = "HelloWorld"


import sys
if sys.argv[1] == "bootstrap":
    # download xx.py
    exit(0)
    pass


import xx as x
Action = x.Action


cleanFiles = [
    "build",
    "*.make",
    "Makefile",
]


@Action("clean")
def clean():
    x.remove_paths(cleanFiles)


@Action("setup", "setup project for building")
def setup():
    x.osrun("premake5 gmake2")


@Action("build|b")
def build():
    setup()
    x.osrun("make")


@Action("run|r")
def run():
    build()
    print()
    x.osrun(f"./build/Debug/{BINARY}\n")


@Action("cb", "clean; build")
def csb():
    clean()
    build()


@Action("cr", "clean; run")
def csb():
    clean()
    run()


if __name__ == '__main__':
    x.main()
