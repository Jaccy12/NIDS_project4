"""
Feature Extraction Module for NIDS

This module computes statistical features
from packets inside a sliding window.

Features computed:
1. Packet size mean
2. Packet size variance
3. TCP flag counts
4. Inter-arrival time mean
"""

import statistics


class FeatureExtractor:

    def __init__(self):
        """
        Initialize feature extractor.
        """

        pass

    # ==========================================================
    # MAIN FEATURE EXTRACTION FUNCTION
    # ==========================================================

    def extract(self, packets):
        """
        Extract statistical features from packets.

        Parameters:
        packets : list of Packet objects

        Returns:
        dictionary of computed features
        """

        # -----------------------------
        # Packet sizes
        # -----------------------------

        sizes = [p.size for p in packets]

        size_mean = statistics.mean(sizes)

        # Handle variance safely
        if len(sizes) > 1:
            size_variance = statistics.variance(sizes)
        else:
            size_variance = 0

        # -----------------------------
        # Flag counts
        # -----------------------------

        flag_counts = {
            "flag_SYN": 0,
            "flag_ACK": 0,
            "flag_FIN": 0,
            "flag_RST": 0
        }

        for p in packets:

            if p.flags in flag_counts:
                flag_counts["flag_" + p.flags] += 1

        # -----------------------------
        # Inter-arrival times
        # -----------------------------

        timestamps = [p.timestamp for p in packets]

        inter_arrivals = []

        for i in range(1, len(timestamps)):

            diff = timestamps[i] - timestamps[i - 1]

            inter_arrivals.append(diff)

        if len(inter_arrivals) > 0:

            interarrival_mean = statistics.mean(
                inter_arrivals
            )

        else:

            interarrival_mean = 0

        # -----------------------------
        # Combine all features
        # -----------------------------

        features = {

            "size_mean": size_mean,

            "size_variance": size_variance,

            "interarrival_mean": interarrival_mean,

            **flag_counts
        }

        return features