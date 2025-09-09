# Port Scanner

A simple Python-based port scanner that checks for open and closed ports on a specified host/IP within a given range.

## How It Works
- Prompts the user for a target IP address or hostname.
- Asks for a starting and ending port number.
- Scans each port in the specified range and reports if it is open or closed.

## Usage
1. Make sure you have Python installed (Python 3.x recommended).
2. Run the script:
   ```powershell
   python scanner.py
   ```
3. Enter the target IP address or hostname when prompted.
4. Enter the starting and ending port numbers to scan.

## Precautions & Legal Notice
- **Permission:** Only scan hosts and networks you own or have explicit permission to scan. Unauthorized scanning may be illegal and can result in penalties.
- **Firewall/IDS:** Scanning may trigger security alerts or blocks on the target system or your own network.
- **Rate Limiting:** Scanning too many ports too quickly may cause your IP to be blocked or flagged as malicious.
- **Accuracy:** Some ports may appear closed due to firewalls or network filtering, even if they are open.
- **Timeouts:** The script uses a short timeout (0.2 seconds) for each port. On slow networks, you may miss open ports. Adjust the timeout if needed.

## Disclaimer
This tool is for educational and authorized use only. The author is not responsible for any misuse or damage caused by this script.
