import logging
import os
import sys
from pathlib import Path
import click

sys.path.append('./')

# Load Env
try:
    with open('/service/src/env.yml') as f:
        os.environ.update(yaml.load(f, Loader=yaml.FullLoader))
except FileNotFoundError as e:
    os.environ["ENV"] = "Local"
    # Google Cloud Functions
    pass

# main batch command
def mainCmd(event):
    text=f'Hello Batch from {os.environ["ENV"]} using Python {sys.version}!'
    return text

# To debug on local
@click.command()
@click.option('--arg', '-o', default="DefaultValue")
def main(arg):
    mainCmd(arg)
if __name__ == "__main__":
    main()
