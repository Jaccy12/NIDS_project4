"""
Main execution file for NIDS Feature Extraction.

This program:
1. Reads packets from CSV
2. Groups them into flows
3. Applies sliding windows
4. Extracts statistical features
5. Stores extracted templates
"""

import csv

# Import custom modules
from packet import Packet
from sliding_window import SlidingWindow
from feature_extractor import FeatureExtractor
from template_store import TemplateStore


# ==========================================================
# CONFIGURATION
# ==========================================================

# Since CSV has only 10 packets,
# we use small window size for testing.

window_size = 5     # Number of packets per window
overlap = 2         # Number of overlapping packets


# ==========================================================
# INITIALIZE COMPONENTS
# ==========================================================

# Dictionary to store sliding windows per flow
windows = {}

# Feature extractor object
extractor = FeatureExtractor()

# Template storage system
template_store = TemplateStore()


# ==========================================================
# READ CSV PACKETS
# ==========================================================

with open("../data/traffic.csv") as file:

    reader = csv.DictReader(file)

    print("Starting packet processing...")

    # Process each packet row
    for row in reader:

        # ------------------------------------------
        # Create Packet Object
        # ------------------------------------------

        packet = Packet(
            timestamp=float(row["timestamp"]),
            src_ip=row["src_ip"],
            dst_ip=row["dst_ip"],
              # REQUIRED FOR 5-TUPLE FLOW IDENTIFICATION
            src_port=int(row["src_port"]),
            dst_port=int(row["dst_port"]),
            protocol=row["protocol"],
            size=int(row["size"]),
            flags=row["flags"]
        )

        # ------------------------------------------
        # Identify flow using 5-tuple
        # ------------------------------------------

        flow_id = packet.flow_id()

        # ------------------------------------------
        # Create new window if flow not exists
        # ------------------------------------------

        if flow_id not in windows:

            windows[flow_id] = SlidingWindow(
                window_size,
                overlap
            )

        # Get flow window
        window = windows[flow_id]

        # ------------------------------------------
        # Add packet to sliding window
        # ------------------------------------------

        window.add_packet(packet)

        print("Packet added to window")

        # ------------------------------------------
        # Check if window is full
        # ------------------------------------------

        if window.is_full():

            print("Window full — extracting features")

            # Extract features
            features = extractor.extract(
                window.get_packets()
            )

            print("Features:", features)

            # Store feature template
            template_store.add_template("normal", features)

            # Slide window forward
            window.slide()


# ==========================================================
# SAVE TEMPLATES
# ==========================================================

template_store.save()

print("Processing complete.")