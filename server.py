
import socket
from protocol import encode_packet, decode_packet

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("127.0.0.1", 50000))

print("MiniVPN Server started...")
print("Waiting for MiniVPN packets...")

while True:

    # Receive the complete UDP datagram
    packet, client_address = server.recvfrom(1024)

    try:

        # Decode our custom packet
        sequence, payload = decode_packet(packet)

        message = payload.decode("utf-8")

        print("\nMiniVPN packet received!")
        print("Client:", client_address)
        print("Sequence:", sequence)
        print("Message:", message)
        print("Total packet size:", len(packet), "bytes")

        # Prepare response
        response = b"Hello VPN Client!"

        # Encode response using our protocol
        response_packet = encode_packet(response, sequence)

        # Send the encoded packet
        server.sendto(response_packet, client_address)

    except (ValueError, UnicodeDecodeError) as error:
        print("Invalid packet:", error)
