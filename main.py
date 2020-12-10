import time
from multiprocessing import Process, Pool


def print_num(num=0):
    """ Print a specific number five times, each per 100ms

    Args:
        num (int): The specific number we want to print

    Returns:
        None: Result will print to standard output directly

    """
    for _ in range(5):
        time.sleep(0.1)
        print('{}'.format(num), end='')


if __name__ == '__main__':
    # 1. First way: with process
    processes = []
    for i in range(1, 4):
        p = Process(target=print_num, args=(i,))
        processes.append(p)
        p.start()

    # Join each process
    for process in processes:
        process.join()

    print('')

    # 2. Second way: with Pool
    with Pool(3) as p:
        p.map(print_num, [1, 2, 3])
