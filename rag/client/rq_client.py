from redis import Redis
from rq import Queue


def get_queue(host:str = "localhost", port: str = "6379"):
    queue = Queue(connection=Redis(
        host=host, port=port
    ))
    return queue

