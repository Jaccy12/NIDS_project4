"""
Sliding Window Module for NIDS

This class manages packet storage using
a sliding window with overlap.

It allows:
1. Adding packets
2. Checking if window is full
3. Retrieving packets
4. Sliding window forward
"""


class SlidingWindow:

    def __init__(self, window_size, overlap):
        """
        Initialize sliding window.

        Parameters:
        window_size : int
            Number of packets per window

        overlap : int
            Number of packets to retain
            when window slides
        """

        self.window_size = window_size
        self.overlap = overlap

        # List to store packets
        self.packets = []

    # ==========================================================
    # ADD PACKET TO WINDOW
    # ==========================================================

    def add_packet(self, packet):
        """
        Add packet to window.
        """

        self.packets.append(packet)

    # ==========================================================
    # CHECK IF WINDOW IS FULL
    # ==========================================================

    def is_full(self):
        """
        Check if window reached required size.
        """

        return len(self.packets) >= self.window_size

    # ==========================================================
    # GET PACKETS IN WINDOW
    # ==========================================================

    def get_packets(self):
        """
        Return current packets in window.

        Returns:
        list of Packet objects
        """

        return self.packets

    # ==========================================================
    # SLIDE WINDOW
    # ==========================================================

    def slide(self):
        """
        Slide window forward.

        Keeps overlapping packets
        and removes older ones.
        """

        # Number of packets to remove
        remove_count = self.window_size - self.overlap

        # Keep only overlap packets
        self.packets = self.packets[remove_count:]