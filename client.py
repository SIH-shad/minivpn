
import socket
from protocol import encode_packet, decode_packet

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.settimeout(5)

# Our original message
message = b"Hello VPN Server!"

# Create our MiniVPN packet
packet = encode_packet(message, sequence=1)

print("Original payload size:", len(message))
print("MiniVPN packet size:", len(packet))

# Send the packet
client.sendto(packet, ("127.0.0.1", 50000))

print("\nMiniVPN packet sent!")

# Receive server response
response_packet, server_address = client.recvfrom(1024)

# Decode the response
sequence, payload = decode_packet(response_packet)

print("Response sequence:", sequence)
print("Server response:", payload.decode("utf-8"))
print("Response packet size:", len(response_packet), "bytes")

client.close()
