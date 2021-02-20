from time import time


def timeit(f):
    def timed(*args, **kw):
        start = time()
        result = f(*args, **kw)
        end = time()
        print('Took', round(end - start, 3), 'seconds')
        return result

    return timed
