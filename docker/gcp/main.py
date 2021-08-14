import sys
sys.path.append('./src/')
import batch

def handler(event, context):
    print(event)
    test='hoge'
    return batch.mainCmd(test)
