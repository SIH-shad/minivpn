
import struct

# Protocol constants
MAGIC = b"MVPN"
VERSION = 1
TYPE_DATA = 1

# Our header structure
HEADER_FORMAT = "!4sBBIH"

# Calculate header size automatically
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)


def encode_packet(payload, sequence):

    # Create the header
    header = struct.pack(
        HEADER_FORMAT,
        MAGIC,
        VERSION,
        TYPE_DATA,
        sequence,
        len(payload)
    )

    # Combine header and payload
    return header + payload


def decode_packet(packet):

    # Check minimum packet size
    if len(packet) < HEADER_SIZE:
        raise ValueError("Packet is too short!")

    # Extract header fields
    magic, version, packet_type, sequence, payload_length = struct.unpack(
        HEADER_FORMAT,
        packet[:HEADER_SIZE]
    )

    # Validate protocol identity
    if magic != MAGIC:
        raise ValueError("Invalid MiniVPN packet!")

    if version != VERSION:
        raise ValueError("Unsupported protocol version!")

    if packet_type != TYPE_DATA:
        raise ValueError("Unsupported packet type!")

    # Extract the payload
    payload = packet[HEADER_SIZE:]

    # Validate payload size
    if len(payload) != payload_length:
        raise ValueError("Payload length mismatch!")

    return sequence, payload
