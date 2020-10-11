# coding:utf-8

import grpc
import data_pb2 as pb2
import data_pb2_grpc as pb2_grpc
import time
import random

_HOST = 'localhost'
_PORT = '8008'


def test():
    while 1:
        time.sleep(1)
        data = str(random.random())
        yield pb2.TestDuplexStreamRequest(data=data)


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = pb2_grpc.TestDuplexStub(channel=conn)

    response = client.TestDuplexStream(test(),timeout=10)
    for res in response:
        print(res.result)


if __name__ == '__main__':
    run()
