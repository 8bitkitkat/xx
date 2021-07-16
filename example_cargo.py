#!/usr/bin/env python3

# Admittedly this example is a little useless,
# given cargo was a big inspiration for this

import os
if not os.path.exists("xx.py"):
    print("downloading xx.py ... ", end="", flush=True)
    import requests
    url = "https://raw.githubusercontent.com/8bitkitkat/xx/master/xx.py"
    r = requests.get(url, allow_redirects=True)
    open("xx.py", "wb").write(r.content)
    print("done")


import xx as x
Action = x.Action


cleanFiles = [
    "target",
    "Cargo.lock"
]


@Action("clean")
def clean():
    x.remove(cleanFiles)


@Action("build|b")
def build():
    x.osrun("cargo build")


@Action("run|r")
def run():
    x.osrun("cargo run")


@Action("check|c")
def run():
    x.osrun("cargo check")


if __name__ == '__main__':
    x.main()
