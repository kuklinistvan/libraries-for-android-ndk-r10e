#!/usr/bin/env python3

from pykuklin.shellutils import working_directory, shell

from pathlib import Path
import os

DIR = Path(os.path.dirname(os.path.realpath(__file__))).absolute()

import click

@click.command()
def cli_entry():
    os.chdir(DIR)
    with working_directory("ulfius/src"):
        shell(['rm', 'ulfius.c'])
        shell(['ln', '-s', '../../ulfius.c'])

    with working_directory("orcania-src/src"):
        shell(['rm', 'orcania.c'])
        shell(['ln', '-s', '../../orcania.c'])


if __name__ == "__main__":
    cli_entry()