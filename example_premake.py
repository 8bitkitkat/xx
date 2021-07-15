#!/usr/bin/env python3

BINARY = "HelloWorld"


import sys
if sys.argv[1] == "bootstrap":
    import requests
    url = "https://raw.githubusercontent.com/8bitkitkat/xx/master/xx.py"
    r = requests.get(url, allow_redirects=True)
    open("xx.py", "wb").write(r.content)
    exit(0)


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
