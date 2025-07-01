import socket
import threading
import argparse
from datetime import datetime

# Lock for clean console output across threads
print_lock = threading.Lock()

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # 1 second timeout
        s.connect((host, port))
        with print_lock:
            print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Simple Multi-threaded Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("-p", "--ports", help="Ports to scan (e.g. 20-80)", default="1-1024")

    args = parser.parse_args()
    target = args.target
    port_range = args.ports

    try:
        host_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[-] Cannot resolve host: {target}")
        return

    start_port, end_port = map(int, port_range.split("-"))

    print(f"\n[🔍] Scanning {target} ({host_ip}) from port {start_port} to {end_port}")
    print(f"[⏱️] Scan started at {datetime.now().strftime('%H:%M:%S')}\n")

    threads = []
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(host_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\n[✅] Scan complete at {datetime.now().strftime('%H:%M:%S')}")

if __name__ == "__main__":
    main()

