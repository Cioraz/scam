def ip_to_binary(ip):
    octets = ip.split('.') 
    binary_ip = ''.join([format(int(octet), '08b') for octet in octets]) 
    return binary_ip

def binary_to_ip(binary):
    octets = [str(int(binary[i:i+8], 2)) for i in range(0, 32, 8)] 
    return '.'.join(octets) 

def calculate_network_address(ip_binary, mask_binary):
    network_binary = ''.join(['1' if ip_binary[i] == '1' and mask_binary[i] == '1' else '0' for i in range(32)])
    return network_binary

def calculate_broadcast_address(network_binary, mask_binary):
    broadcast_binary = ''.join([network_binary[i] if mask_binary[i] == '1' else '1' for i in range(32)])
    return broadcast_binary

def subnet_information(ip, subnet_mask):
    ip_binary = ip_to_binary(ip)
    mask_binary = ip_to_binary(subnet_mask)

    network_binary = calculate_network_address(ip_binary, mask_binary)
    broadcast_binary = calculate_broadcast_address(network_binary, mask_binary)

    network_address = binary_to_ip(network_binary)
    broadcast_address = binary_to_ip(broadcast_binary)

    num_zeros = mask_binary.count('0') 
    total_ips = 2 ** num_zeros

    print(f"First IP (Network Address): {network_address}")
    print(f"Last IP (Broadcast Address): {broadcast_address}")
    print(f"Total IP addresses: {total_ips}")

ip_address = input("Enter the IP address (e.g., 192.168.1.10): ")
subnet_mask = input("Enter the subnet mask (e.g., 255.255.255.0): ")

subnet_information(ip_address, subnet_mask)
