class BlockErrors:
    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type in self.err_types:
            return True 
        return False