import os
import sys
import click
import json
import yaml
sys.path.append(os.path.dirname(__file__))
"""
Write your module
Ex. import hoge
"""
from logger.logging import log, get_logger  # noqa: E402

logger = get_logger()

# Load Env
try:
    with open('/service/src/env.yml') as f:
        os.environ.update(yaml.load(f, Loader=yaml.FullLoader))
except FileNotFoundError:
    os.environ["ENV"] = "local"
    # Google Cloud Functions
    pass

"""
Main batch command
Edit this function
"""


@log(logger)
def mainCmd(event='{"default": "value"}'):
    try:
        event = json.loads(event)
        text = f'Hello Batch from {os.environ["ENV"]} using Python {sys.version}!\nEvent Object is {event}'
        logger.info(text)
    except Exception as e:
        logger.error(e)
        return e
    return "Hello, Python Batch!"

# To debug on local


@click.command()
@click.option('--arg', '-o', default='{"data": "test"}')
def main(arg):
    mainCmd(arg)


if __name__ == "__main__":
    main()
