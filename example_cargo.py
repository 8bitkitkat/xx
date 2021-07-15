#!/usr/bin/env python3

# Admittedly this example is a little useless,
# given cargo was a big inspiration for this

import sys
if sys.argv[1] == "bootstrap":
    # download xx.py
    exit(0)
    pass


import xx as x
Action = x.Action


cleanFiles = [
    "target",
]


@Action("clean")
def clean():
    x.remove_paths(cleanFiles)


@Action("build|b")
def build():
    x.osrun("cargo build")


@Action("run|r")
def run():
    x.osrun("cargo run")


@Action("check|c")
def run():
    x.osrun("cargo check")


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
