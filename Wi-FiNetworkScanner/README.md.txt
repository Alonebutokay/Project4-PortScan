Wi-Fi Network Scanner
Project Description
This project provides a simple command-line utility to scan for available Wi-Fi networks in your vicinity. It's designed to help users quickly assess network availability, signal strength, and basic security information, enabling them to choose the best connection for optimal connectivity.

The scanner offers distinct implementations for Linux and Windows operating systems, leveraging platform-specific tools for efficient and reliable network discovery.

Problem Statement
Users frequently need to check available wireless networks and their signal strength to ensure optimal connectivity and troubleshooting.

Objective
To create a scanner that lists nearby Wi-Fi networks with essential information such as signal strength, helping users choose the best one.

Features
Platform-Specific Scanning: Dedicated scripts for both Linux and Windows for native performance.

Network Name (SSID): Displays the Broadcast Service Set Identifier of the network.

MAC Address (BSSID): Shows the unique hardware address of the access point.

Signal Strength: Provides an indication of the network's signal quality.

Linux: Signal Level (e.g., 50/70) and Quality (e.g., 60/70).

Windows: Signal Strength in dBm.

Security Information (Windows): Includes details on authentication and cipher types (e.g., WPA2, AES).

Requirements
General
Python 3.x

##For Linux (linux_wifi_scanner.py)
wireless-tools package: This provides the iwlist command-line utility.

Installation: On Debian/Ubuntu-based systems, install with sudo apt-get install wireless-tools. For other distributions, use your respective package manager (e.g., sudo dnf install wireless-tools for Fedora, sudo pacman -S wireless_tools for Arch Linux).

Permissions: Running the script often requires sudo privileges to execute iwlist scan.

For Windows (windows_wifi_scanner.py)
Python Libraries:

pywifi: A Python wrapper for Windows Native Wifi API.

comtypes: A dependency for pywifi, used for COM interoperability.

Installation: These can be installed via pip:

##Bash

pip install -r requirements.txt
Permissions: It's recommended to run your command prompt or PowerShell as an Administrator for pywifi to have full access.

Installation
Clone the repository:

##Bash

git clone https://github.com/YOUR_USERNAME/wifi-scanner.git
cd wifi-scanner
(Replace YOUR_USERNAME with your actual GitHub username).

Install Python dependencies (for Windows users):
If you plan to use the Windows scanner, install the required Python libraries:

##Bash

pip install -r requirements.txt
For Linux users, Python dependencies are not typically required, as the script relies on system utilities.

Usage
##On Linux
To scan for networks using the Linux script:

##Bash

sudo python3 linux_wifi_scanner.py
Important: You might need to change the wireless interface name (wlan0) in the linux_wifi_scanner.py script to match your system's actual interface (e.g., wlp2s0, wlo1). You can find your interface name by running ip a or ifconfig in your terminal.

Ensure your wireless adapter is enabled and up (sudo ip link set YOUR_INTERFACE_NAME up).

##On Windows
To scan for networks using the Windows script:

##Bash

python windows_wifi_scanner.py
Important: For the script to function correctly, run your command prompt or PowerShell as an Administrator.


