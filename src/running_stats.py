"""
Running mean and variance using recurrence relations.Implements recurrence relations for
incremental mean and variance using Welford's method.
"""

class RunningStats:

    def __init__(self):

        # Number of values processed
        self.n = 0

        # Running mean
        self.mean = 0

        # Running squared difference
        self.M2 = 0

    def update(self, value):
        """
        Update statistics incrementally.
        """

        self.n += 1

        delta = value - self.mean

        self.mean += delta / self.n

        delta2 = value - self.mean

        self.M2 += delta * delta2

    def get_mean(self):
        return self.mean

    def get_variance(self):

        if self.n < 2:
            return 0

        return self.M2 / self.n