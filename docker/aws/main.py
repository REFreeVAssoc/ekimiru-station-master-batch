import sys
sys.path.append('./src')
import batch  # noqa: E402


def handler(event, context):
    return batch.mainCmd(event)
