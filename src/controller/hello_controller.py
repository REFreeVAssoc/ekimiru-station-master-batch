"""
Write your module
Ex. import hoge
"""
from usecase.interactor.hello_usecase import Hello
from utilities.logger.logging import log, get_logger

logger = get_logger()


@log(logger)
def main_batch_controller(event):
    try:
        hello = Hello()
        text = hello.hello(event)
        logger.info(text)
    except Exception as e:
        logger.error(e)
        return e
    return text
