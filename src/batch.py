import os
import sys
import click
import json

sys.path.append(os.path.dirname(__file__))
"""
Write your module
Ex. import hoge
"""
from utilities.logger.logging import log, get_logger  # noqa: E402

logger = get_logger()


@log(logger)
def mainCmd(event={'default': 'value'}):
    """
    Main batch command
    Edit this function
    """
    try:
        text = f'Hello Batch from {os.environ["ENV"]} using Python {sys.version}!\nEvent Object is {event}'
        logger.info(text)
    except Exception as e:
        logger.error(e)
        return e
    return "Hello, Python Batch!"


@click.command()
@click.option('--arg', '-o', default='{"data": "test"}')
def main(arg):
    """
    debug on local
    """
    arg = json.loads(arg)
    mainCmd(arg)


if __name__ == "__main__":
    main()
