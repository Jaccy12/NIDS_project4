"""
Main execution file for NIDS Feature Extraction + DTW Detection.
"""

import csv
import os

from packet import Packet
from sliding_window import SlidingWindow
from feature_extractor import FeatureExtractor
from matcher import Matcher


window_size = 5
overlap = 2
MAX_FLOWS = 100

base_dir = os.path.dirname(__file__)
template_file = os.path.join(base_dir, "..", "templates", "templates.json")
data_file = os.path.join(base_dir, "..", "data", "traffic.csv")


windows = {}

extractor = FeatureExtractor()
matcher = Matcher(template_file)

packet_count = 0


with open(data_file) as file:

    reader = csv.DictReader(file)

    print("\nStarting packet processing...\n")

    for row in reader:

        packet_count += 1

        packet = Packet(
            timestamp=float(row["timestamp"]),
            src_ip=row["src_ip"],
            dst_ip=row["dst_ip"],
            src_port=int(row["src_port"]),
            dst_port=int(row["dst_port"]),
            protocol=row["protocol"],
            size=int(row["size"]),
            flags=row["flags"]
        )

        flow_id = packet.flow_id()

        if flow_id not in windows:
            windows[flow_id] = SlidingWindow(window_size, overlap)

        window = windows[flow_id]

        window.add_packet(packet)

        print("Packet added to window")

        if window.is_full():

            print("Window full — extracting features")

            features = extractor.extract(window.get_packets())

            print("Features:", features)

            feature_sequence = [features]

            label, distance, confidence = matcher.match(feature_sequence)

            result = {
                "flow_id": flow_id,
                "prediction": label,
                "distance": distance,
                "confidence": confidence
            }

            print("\nDETECTION RESULT")
            print(result)
            print("-" * 50)

            window.slide()

        if len(windows) > MAX_FLOWS:
            windows.pop(next(iter(windows)))


print("\nProcessing complete.")
print("Total packets processed:", packet_count)