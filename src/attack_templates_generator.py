"""
Generates labeled attack templates.

Creates:
- normal traffic template
- port scan template
- DoS template

These templates simulate real attack behavior
for DTW matching.
"""

import json
import random


# ==========================================================
# FEATURE VECTOR GENERATORS
# ==========================================================

def normal_feature():
    """Simulate normal traffic behavior"""

    return {
        "size_mean": random.randint(400, 800),
        "size_variance": random.randint(500, 1000),
        "interarrival_mean": round(random.uniform(0.01, 0.1), 3),
        "flag_SYN": 0,
        "flag_ACK": 1,
        "flag_FIN": 0,
        "flag_RST": 0
    }


def port_scan_feature():
    """Simulate port scan behavior"""

    return {
        "size_mean": random.randint(40, 100),
        "size_variance": random.randint(50, 200),
        "interarrival_mean": round(random.uniform(0.001, 0.01), 4),
        "flag_SYN": 1,
        "flag_ACK": 0,
        "flag_FIN": 0,
        "flag_RST": 0
    }


def dos_feature():
    """Simulate DoS behavior"""

    return {
        "size_mean": random.randint(900, 1500),
        "size_variance": random.randint(1500, 3000),
        "interarrival_mean": round(random.uniform(0.0001, 0.005), 5),
        "flag_SYN": 1,
        "flag_ACK": 1,
        "flag_FIN": 0,
        "flag_RST": 0
    }


# ==========================================================
# BUILD SEQUENCES
# ==========================================================

def build_sequence(generator, length=10):

    sequence = []

    for _ in range(length):
        sequence.append(generator())

    return sequence


# ==========================================================
# CREATE TEMPLATES
# ==========================================================

templates = {
    "normal": build_sequence(normal_feature),
    "port_scan": build_sequence(port_scan_feature),
    "dos": build_sequence(dos_feature)
}


# ==========================================================
# SAVE FILE
# ==========================================================

with open("../templates/templates.json", "w") as f:

    json.dump(templates, f, indent=4)

print("Attack templates generated.")