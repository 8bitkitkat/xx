#!/usr/bin/env python3

import sys
if sys.argv[1] == "bootstrap":
    # TODO: download xx.py
    exit(0)
    pass


BINARY = "HelloWorld"

import xx as x
Action = x.Action


cleanFiles = [
    "build",
    "Makefile",
]


@Action("clean")
def clean():
    x.remove_paths(cleanFiles)


@Action("setup", "setup project for building")
def setup():
    print("setting project up for build")


@Action("build|b")
def build():
    setup()
    print("building project")


@Action("run|r")
def run():
    build()
    print("running project")


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
