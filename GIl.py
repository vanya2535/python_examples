"""
Python Global Interpreter Lock (GIL) — это своеобразная блокировка,
позволяющая только одному потоку управлять интерпретатором Python. Это означает, 
что в любой момент времени будет выполняться только один конкретный поток.
Thread — это отдельный поток выполнения. Это означает,
что в вашей программе могут работать две и более подпрограммы одновременно. 
Но разные потоки на самом деле не работают одновременно: это просто кажется.
Задача мьютекса — обеспечить такой механизм,
чтобы доступ к объекту в определенное время был только у одного потока. 
Семафор — это средство для синхронизации доступа к какому-то ресурсу.
Его особенность заключается в том,
что при создании механизма синхронизации он использует счетчик.
Счетчик указывает нам, сколько потоков одновременно могут
получать доступ к общему ресурсу.
"""
import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    threads = list()

    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
