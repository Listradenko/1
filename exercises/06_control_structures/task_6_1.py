mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
mac_cisco = []

for addr in mac:
    q = addr.replace(':','.')
    mac_cisco.append(q)
print(mac_cisco)