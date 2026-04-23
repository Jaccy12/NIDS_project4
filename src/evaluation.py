"""
evaluation.py

Evaluate DTW-based intrusion detection system.
"""

import os
from matcher import Matcher


# ==========================================================
# LOAD MATCHER
# ==========================================================

base_dir = os.path.dirname(__file__)
template_file = os.path.join(base_dir, "..", "templates", "templates.json")

matcher = Matcher(template_file)


# ==========================================================
# TEST DATA (REALISTIC — NOT SAME AS TEMPLATES)
# ==========================================================

test_cases = [
    ("normal", [
        {"size_mean": 505, "interarrival_mean": 0.11, "flag_SYN": 0},
        {"size_mean": 515, "interarrival_mean": 0.12, "flag_SYN": 0}
    ]),

    ("port_scan", [
        {"flag_SYN": 1, "dst_port": 30},
        {"flag_SYN": 1, "dst_port": 31},
        {"flag_SYN": 1, "dst_port": 32}
    ]),

    ("dos", [
        {"flag_SYN": 1, "interarrival_mean": 0.002},
        {"flag_SYN": 1, "interarrival_mean": 0.0015}
    ])
]


# ==========================================================
# EVALUATION METRICS
# ==========================================================

predictions = []
labels = []

print("\nRunning Evaluation...\n")

for true_label, sequence in test_cases:

    pred_label, dist, conf = matcher.match(sequence)

    predictions.append(pred_label)
    labels.append(true_label)

    print("Actual:", true_label)
    print("Predicted:", pred_label)
    print("Distance:", dist)
    print("Confidence:", conf)
    print("-" * 40)


# ==========================================================
# CONFUSION MATRIX
# ==========================================================

def confusion_matrix(preds, labels):

    matrix = {}

    for p, l in zip(preds, labels):

        if l not in matrix:
            matrix[l] = {}

        if p not in matrix[l]:
            matrix[l][p] = 0

        matrix[l][p] += 1

    return matrix


# ==========================================================
# ACCURACY
# ==========================================================

def accuracy(preds, labels):
    correct = sum(p == l for p, l in zip(preds, labels))
    return correct / len(labels)


# ==========================================================
# PRINT RESULTS
# ==========================================================

print("\nConfusion Matrix:")
print(confusion_matrix(predictions, labels))

print("\nAccuracy:", accuracy(predictions, labels))