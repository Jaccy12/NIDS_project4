"""
Packet Class for NIDS

This class represents a single network packet
and provides flow identification using the 5-tuple.
"""


class Packet:

    def __init__(
        self,
        timestamp,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        protocol,
        size,
        flags
    ):
        """
        Initialize packet metadata.

        Parameters:
        timestamp : float → packet arrival time
        src_ip : str → source IP address
        dst_ip : str → destination IP address
        src_port : int → source port number
        dst_port : int → destination port number
        protocol : str → protocol type (TCP/UDP)
        size : int → packet size in bytes
        flags : str → TCP flags (SYN, ACK, FIN, etc.)
        """

        self.timestamp = timestamp
        self.src_ip = src_ip
        self.dst_ip = dst_ip

        self.src_port = src_port
        self.dst_port = dst_port

        self.protocol = protocol
        self.size = size
        self.flags = flags

    # ==========================================================
    # FLOW IDENTIFICATION FUNCTION
    # ==========================================================

    def flow_id(self):
        """
        Generate unique flow identifier.

        Uses 5-tuple:
        (src_ip, dst_ip, src_port, dst_port, protocol)

        Returns:
        tuple → unique flow ID
        """

        return (
            self.src_ip,
            self.dst_ip,
            self.src_port,
            self.dst_port,
            self.protocol
        )