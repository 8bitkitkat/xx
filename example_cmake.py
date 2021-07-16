#!/usr/bin/env python3

BINARY = "HelloWorld"


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


@Action("clean")
def clean():
    x.remove("build")


# This is the main example
@Action("build|b")
def build():
    x.mkdir("build")
    x.pushd("build")
    x.osrun("cmake ../")
    x.osrun("make")
    x.popd()


@Action("run|r")
def run():
    build()
    print()
    x.osrun(f"./build/{BINARY}\n")


if __name__ == '__main__':
    x.main()
