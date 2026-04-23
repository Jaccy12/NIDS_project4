"""
dtw.py

Implements Dynamic Time Warping (DTW) for comparing feature sequences.

Includes:
- Cost matrix computation
- Early abandonment (dynamic threshold)
- Sakoe-Chiba band optimization
"""

import math


class DTW:

    def __init__(self, window=None):
        """
        window : Sakoe-Chiba band width
        """
        self.window = window

    # ==========================================================
    # DTW DISTANCE
    # ==========================================================

    def distance(self, seq1, seq2, threshold=None):
        """
        Compute DTW distance between two sequences.

        seq1, seq2 = list of feature vectors
        threshold = early abandonment threshold
        """

        n = len(seq1)
        m = len(seq2)

        # Sakoe-Chiba band
        w = self.window if self.window else max(n, m)
        w = max(w, abs(n - m))

        # Initialize matrix (dictionary for sparse storage)
        dtw_matrix = {}

        dtw_matrix[(-1, -1)] = 0

        for i in range(n):
            for j in range(m):

                # Apply band constraint
                if abs(i - j) > w:
                    continue

                cost = self.euclidean(seq1[i], seq2[j])

                prev = min(
                    dtw_matrix.get((i - 1, j), float("inf")),
                    dtw_matrix.get((i, j - 1), float("inf")),
                    dtw_matrix.get((i - 1, j - 1), float("inf"))
                )

                current_cost = cost + prev
                dtw_matrix[(i, j)] = current_cost

                # ==================================================
                # EARLY ABANDONMENT (FIXED)
                # ==================================================
                if threshold is not None and current_cost > threshold:
                    return float("inf")

        return dtw_matrix.get((n - 1, m - 1), float("inf"))

    # ==========================================================
    # EUCLIDEAN DISTANCE
    # ==========================================================

    def euclidean(self, v1, v2):
        """
        Compute Euclidean distance between two feature vectors.
        """

        total = 0

        for a, b in zip(v1, v2):
            total += (a - b) ** 2

        return math.sqrt(total)