#!/usr/bin/env python3
# By Harel Boyenge

import os
import re
from collections import Counter

# Always load access.log from the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
log_file_path = os.path.join(BASE_DIR, "access.log")

# Defines the shape of the text we're looking for – Standard web logs
# IP address always appears at the beginning, like: 127.0.0.1 - - [...]
ip_pattern = r'^(\d{1,3}(?:\.\d{1,3}){3})'

with open(log_file_path, "r") as file:
    logs = file.readlines()

# Extracted IP addresses
ip_addresses = [
    re.search(ip_pattern, line).group(1)
    for line in logs
    if re.search(ip_pattern, line)
]

# Count occurrences (traffic volume per IP)
ip_counts = Counter(ip_addresses)

# Identify the top IP with the most traffic
top_ip, top_count = ip_counts.most_common(1)[0]
total_requests = sum(ip_counts.values())
percentage = (top_count / total_requests) * 100

# Display the results
print("Traffic Volume from Individual IP Addresses:")
for ip, count in ip_counts.items():
    print(f"{ip}: {count} requests")

print("\nIP with the Most Traffic:")
print(f"{top_ip} → {top_count} requests ({percentage:.2f}% of all traffic)")
