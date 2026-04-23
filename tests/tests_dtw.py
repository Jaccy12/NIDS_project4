"""
tests_dtw.py

Simple DTW test case.
"""

import sys
import os

# ==========================================================
# FIX: Add project root to Python path
# ==========================================================
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now this import will work
from src.dtw import DTW


def test_basic_dtw():

    seq1 = [
        [1, 2],
        [2, 3],
        [3, 4]
    ]

    seq2 = [
        [1, 2],
        [2, 2],
        [3, 5]
    ]

    dtw = DTW(window=2)

    distance = dtw.distance(seq1, seq2)

    print("DTW distance:", distance)


if __name__ == "__main__":
    test_basic_dtw()