from datetime import datetime


class board:
    def __init__(self, sampling_interval=1):  # sampling interval in seconds
        self.begin = datetime.now().timestamp()
        self.sampling_interval = sampling_interval
        self.num_of_bucket = 300 / sampling_interval
        self.buckets = [0] * self.num_of_bucket

    def hit(self):
        seq = int((datetime.now().timestamp() - self.begin) /
                  self.sampling_interval) % self.num_of_bucket
        self.buckets[seq] += 1

    def show(self):
        print(sum(self.buckets[0:]))


board = board()


def track_hit():
    board.hit()


def get_hit_count_last_5_minutes():
    board.show()
