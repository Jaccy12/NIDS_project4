"""
matcher.py

Matches extracted feature sequences against stored attack templates using DTW.
"""

import json
from dtw import DTW


class Matcher:

    def __init__(self, template_file):

        with open(template_file, "r") as file:
            self.templates = json.load(file)

        self.dtw = DTW(window=3)

    # ==========================================================
    # FEATURE VECTOR CONVERSION
    # ==========================================================

    def _to_vector(self, feature_dict):

        return [
            feature_dict.get("size_mean", 0),
            feature_dict.get("size_variance", 0),
            feature_dict.get("interarrival_mean", 0),
            feature_dict.get("flag_SYN", 0),
            feature_dict.get("flag_ACK", 0),
            feature_dict.get("flag_FIN", 0),
            feature_dict.get("flag_RST", 0),
            feature_dict.get("dst_port", 0)
        ]

    # ==========================================================
    # MATCH FUNCTION
    # ==========================================================

    def match(self, feature_sequence):

        observed_vectors = [
            self._to_vector(f) for f in feature_sequence
        ]

        best_label = "unknown"
        best_distance = float("inf")

        for label, template_seq in self.templates.items():

            template_vectors = [
                self._to_vector(f) for f in template_seq
            ]

            dist = self.dtw.distance(
                observed_vectors,
                template_vectors,
                threshold=best_distance
            )

            if dist < best_distance:
                best_distance = dist
                best_label = label

        confidence = self.compute_confidence(best_distance)

        return best_label, best_distance, confidence

    # ==========================================================
    # IMPROVED CONFIDENCE SCALING
    # ==========================================================

    def compute_confidence(self, distance):

        if distance == float("inf"):
            return "Low"

        if distance < 500:
            return "High"
        elif distance < 1500:
            return "Medium"
        else:
            return "Low"