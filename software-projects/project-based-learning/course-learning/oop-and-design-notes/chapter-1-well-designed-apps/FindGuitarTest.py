class DogDoor:
    def __init__(self):
        self._open = False

    def open(self):
        print("The dog door opens.")
        self._open = True

    def close(self):
        print("The dog door closes.")
        self._open = False

    def is_open(self):
        return self._open

