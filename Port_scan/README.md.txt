#  Python Port Scanner (CLI)

A simple multi-threaded Python port scanner to detect open TCP ports on a given IP or domain.

##  Objective
Help in identifying open network ports for basic vulnerability assessment.

##  Built With
- Python
- socket
- threading
- argparse

##  Features
- CLI-based interface
- Scans a given range of ports
- Multi-threaded for faster scanning
- Resolves domain to IP

##  How to Run
```bash
python port_scanner.py <target> -p <start-end>
##EXAMPLES
python port_scanner.py 127.0.0.1 -p 1-1000
python port_scanner.py google.com -p 20-80

