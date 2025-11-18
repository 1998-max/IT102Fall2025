#!/usr/bin/env python3
#By Harel Boyenge
#Cyber project_Port Scanner with Suspicious Port Alert
"""
Simple Port Scanner with Suspicious Port Alert

This script scans a target host over a range of TCP ports and reports
which ports are open. It then compares the open ports to a list of
allowed ports and flags any unexpected ports as potentially suspicious.

"""

import socket
import sys
from typing import List

# --------- Configuration ---------
DEFAULT_TARGET = "127.0.0.1"  # localhost by default
DEFAULT_START_PORT = 1
DEFAULT_END_PORT = 1024

# Ports we consider "expected" on this system 
ALLOWED_PORTS = {22, 80, 443}
# ---------------------------------


def scan_port(host: str, port: int, timeout: float = 0.5) -> bool:
    """
    Try to connect to a single TCP port.
    Returns True if the port is open, False otherwise.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
    except socket.error:
        sock.close()
        return False
    sock.close()
    return result == 0


def parse_args():
    """
    Parse optional command-line arguments.
    If no arguments are provided, use default host and port range.
    """
    if len(sys.argv) == 1:
        # No arguments: use defaults
        return DEFAULT_TARGET, DEFAULT_START_PORT, DEFAULT_END_PORT

    if len(sys.argv) != 4:
        print("Usage: python3 port_scanner_alert.py <host> <start_port> <end_port>")
        sys.exit(1)

    target = sys.argv[1]
    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    except ValueError:
        print("Error: start_port and end_port must be integers.")
        sys.exit(1)

    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("Error: port range must be between 1 and 65535 and start <= end.")
        sys.exit(1)

    return target, start_port, end_port


def main():
    target, start_port, end_port = parse_args()

    # Resolve the target to an IP address
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{target}'.")
        sys.exit(1)

    print("=" * 60)
    print("Simple Port Scanner with Suspicious Port Alert")
    print(f"Target host: {target} ({target_ip})")
    print(f"Port range: {start_port} - {end_port}")
    print(f"Allowed ports (whitelist): {sorted(ALLOWED_PORTS)}")
    print("=" * 60)

    open_ports: List[int] = []

    # Scan ports in the specified range
    for port in range(start_port, end_port + 1):
        if scan_port(target_ip, port):
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    print("=" * 60)
    print(f"Total open ports found: {len(open_ports)}")

    if not open_ports:
        print("No open ports were detected in the specified range.")
        sys.exit(0)

    # Classify ports as allowed or suspicious
    allowed_open = [p for p in open_ports if p in ALLOWED_PORTS]
    suspicious_open = [p for p in open_ports if p not in ALLOWED_PORTS]

    print("\nOpen ports that are on the allowed list:")
    if allowed_open:
        for p in allowed_open:
            print(f" - Port {p} (allowed)")
    else:
        print(" - None")

    print("\nOpen ports that are NOT on the allowed list (suspicious):")
    if suspicious_open:
        for p in suspicious_open:
            print(f" ! Port {p} (unexpected, review this service)")
    else:
        print(" - None (no unexpected open ports detected)")

    print("=" * 60)
    print("Scan complete.")


if __name__ == "__main__":
    main()
