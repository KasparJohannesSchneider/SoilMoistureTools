class DataPoint:
    def __init__(self):
        self.time = None
        self.value = 0

    def __int__(self, time, value):
        self.time = time
        self.value = value

    def get_time(self):
        return self.time

    def get_value(self):
        return self.value




