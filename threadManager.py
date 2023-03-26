import threading
from multiprocessing import cpu_count
from helper import loadAndDivide

def verifyThreads(threadCount: int):
    if threadCount > cpu_count():
        threadCount = cpu_count()
        print(f"Too many threads, using {threadCount} instead")
    return threadCount