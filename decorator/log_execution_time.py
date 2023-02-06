import functools
import time

# 日志记录


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper


@log_execution_time
def calculate_similarity(items):
    print("calculate_similarity")


if __name__ == '__main__':
    calculate_similarity("hello")