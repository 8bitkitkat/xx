#!/usr/bin/env python3

# Admittedly this example is a little useless,
# given cargo was a big inspiration for this

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
