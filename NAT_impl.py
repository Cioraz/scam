nat_table = {}

public_ip = "200.10.20.30"

private_ips = {
    "192.168.1.2",
    "192.168.1.3",
}

for i in private_ips:
    nat_table[i] = public_ip

test_ip = "192.168.1.4"
result = nat_table.get(test_ip, "No NAT translation for this IP")
print(result)
