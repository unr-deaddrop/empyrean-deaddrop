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
    logging.basicConfig(
        level="NOTSET",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True,
                              tracebacks_suppress=[click])]
    )

    logging.getLogger("rich")
    console = Console()

    # We'll use a static configuration already fixed in /src/config.py. It
    # won't change between builds or versions - the idea is "build once, touch
    # never."
    # config = Config()
    # config_data = config.get_config()

    # Create the build environment/directory by copying the src directory into
    # a new build folder
    make_env = MakeEnv()
    make_env.make_env()
    make_env.get_src()
    
    # write_config = WriteConfig(config_data)
    # write_config.write_config()

    # Perform in-place obfuscation against the build directory.
    do_obfuscate = DoObfuscate()
    do_obfuscate.run()

    # Build the code, bundle using PyInstaller
    build = Build()
    build.get_pyinstaller()
    build.get_upx()
    build.build()


if __name__ == "__main__":
    main()
