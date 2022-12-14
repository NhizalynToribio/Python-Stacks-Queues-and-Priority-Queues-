print("**************** PROGRAMMED BY: *****************")
print("************** NHIZALYN TORIBIO ****************")
print("*************** BSCOE 2 - 2 *******************")
print("**Python Stacks, Queues, and Priority Queues **")
print("**** Thread Safe Queues - Priority Queue *****")

# importing argparse, LifoQueue, PriorityQueue, Queue and threading
import argparse
from queue import LifoQueue, PriorityQueue, Queue
import threading

from random import randint
from time import sleep

from random import choice, randint
from itertools import zip_longest

from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel

from dataclasses import dataclass, field
from enum import IntEnum

# This section shows the QUEUE TYPE WITH def main(args)
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}


def main(args):
    buffer = QUEUE_TYPES[args.queue]()
    products = PRIORITIZED_PRODUCTS if args.queue == "heap" else PRODUCTS
    producers = [
        Producer(args.producer_speed, buffer, products)
        for _ in range(args.producers)
    ]


    consumers = [
        Consumer(args.consumer_speed, buffer)
        for _ in range(args.consumers)
    ]

    for producer in producers:
        producer.start()

    for consumer in consumers:
        consumer.start()

    view = View(buffer, producers, consumers)
    view.animate()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queue", choices=QUEUE_TYPES, default="heap")
    parser.add_argument("-p", "--producers", type=int, default=3)
    parser.add_argument("-c", "--consumers", type=int, default=2)
    parser.add_argument("-ps", "--producer-speed", type=int, default=1)
    parser.add_argument("-cs", "--consumer-speed", type=int, default=1)
    return parser.parse_args()