import subprocess
import re

def scan_wifi_linux():
    """
    Scans for Wi-Fi networks on Linux using 'iwlist scan'.
    """
    print("Scanning for Wi-Fi networks (Linux)...")
    try:
        # Run the iwlist command to scan for networks
        # Assuming wlan0 is your wireless interface. You might need to change this.
        cmd = ["sudo", "iwlist", "wlan0", "scan"]
        output = subprocess.check_output(cmd, encoding='utf-8')

        networks = {}
        current_ssid = None

        # Regular expressions to parse the output
        ssid_pattern = re.compile(r'ESSID:"([^"]+)"')
        signal_pattern = re.compile(r'Signal level=(\d+)/70') # Adjust 70 if your driver reports differently
        quality_pattern = re.compile(r'Quality=(\d+)/(\d+)')
        address_pattern = re.compile(r'Address: ([0-9A-Fa-f:]{17})')

        for line in output.splitlines():
            line = line.strip()

            ssid_match = ssid_pattern.search(line)
            if ssid_match:
                current_ssid = ssid_match.group(1)
                if current_ssid not in networks:
                    networks[current_ssid] = {
                        'SSID': current_ssid,
                        'MAC Address': 'N/A',
                        'Signal Level': 'N/A',
                        'Quality': 'N/A'
                    }
                continue # Move to the next line to find other details

            if current_ssid:
                address_match = address_pattern.search(line)
                if address_match:
                    networks[current_ssid]['MAC Address'] = address_match.group(1)

                signal_match = signal_pattern.search(line)
                if signal_match:
                    signal_level = int(signal_match.group(1))
                    # Convert to percentage or dBm if needed, here just raw value
                    networks[current_ssid]['Signal Level'] = f"{signal_level}/70"

                quality_match = quality_pattern.search(line)
                if quality_match:
                    quality = int(quality_match.group(1))
                    max_quality = int(quality_match.group(2))
                    networks[current_ssid]['Quality'] = f"{quality}/{max_quality}"

        if not networks:
            print("No Wi-Fi networks found or 'iwlist' output could not be parsed.")
            print("Ensure 'iwlist' is installed and you have permissions (try running with sudo).")
            print("Also, check if 'wlan0' is the correct interface name.")
            return

        print("\nAvailable Wi-Fi Networks:")
        print("------------------------")
        for ssid, info in networks.items():
            print(f"SSID: {info['SSID']}")
            print(f"  MAC Address: {info['MAC Address']}")
            print(f"  Signal Level: {info['Signal Level']}")
            print(f"  Quality: {info['Quality']}")
            print("------------------------")

    except FileNotFoundError:
        print("Error: 'iwlist' command not found.")
        print("Please ensure 'wireless-tools' package is installed (e.g., 'sudo apt-get install wireless-tools' on Debian/Ubuntu).")
    except subprocess.CalledProcessError as e:
        print(f"Error running 'iwlist': {e}")
        print("Make sure your wireless interface (e.g., wlan0) is up and you have sufficient permissions.")
        print("Try running the script with 'sudo python your_script_name.py'")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    scan_wifi_linux() # Or scan_wifi_windows() depending on your script
