from contextlib import contextmanager

@contextmanager
def ropen(file, method):
    a = open(file, method)
    yield a
    a.close()

class ctxt:
    def __init__(self, file, method):
        self.file = open(file, method)
    def __enter__(self):
        return self.file
    def __exit__(self, type, value, traceback):
        self.file.close()
        return True
