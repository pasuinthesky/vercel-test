from datetime import datetime


class board:
    def __init__(self, num_of_bucket=300):
        self.begin = datetime.now().timestamp()
        self.num_of_bucket = num_of_bucket
        self.bucket_size = 300 / num_of_bucket
        self.buckets = [0] * num_of_bucket

    def hit(self):
        seq = int((datetime.now().timestamp() - self.begin) /
                  self.bucket_size) % self.num_of_bucket
        self.buckets[seq] += 1

    def show(self):
        print(sum(self.buckets[0:]))


board = board()


def track_hit():
    board.hit()


def get_hit_count_last_5_minutes():
    board.show()
