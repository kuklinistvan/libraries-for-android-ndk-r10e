#!/usr/bin/env python3

from pykuklin.shellutils import shell

from pathlib import Path
import os
from glob import glob

from multiprocessing import Process

DIR = Path(os.path.dirname(os.path.realpath(__file__))).absolute()

def cli_entry():
    os.chdir(DIR)

    processes = []

    print("Running in parallel")

    for cf in glob("**/conanfile.py"):
        p = Process(target=conan_export, args=(cf,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
        
def conan_export(path) -> None:
    shell(['conan', 'export', path])
    

if __name__ == "__main__":
    cli_entry()