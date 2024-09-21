![SHIGHRA](https://github.com/user-attachments/assets/49fd5471-4ce1-484a-9221-75a1c125b584)
A powerful and fastest port scanning approach for CTFs and network vulnerability assessments.
**shighra** is a powerful port scanning tool that combines speed and precision. It simultaneously executes three advanced scanning commands (masscan, nmap, and fastmap) in a beautifully organized terminal layout, unveiling vulnerabilities in your network with unparalleled efficiency.

## Features

- **Concurrent Scanning**: Run masscan, nmap, and fastmap simultaneously across different terminal panes for comprehensive results.
- **User-Friendly Input**: Prompts for the target IP address, streamlining the scanning process.
- **Log Output**: Automatically saves scan results to dedicated log files (`masscan-udp.txt`, `nmap-all.txt`, `fastmap-output.txt`).
- **Dynamic Terminal Layout**: Utilizes `tmux` to create an efficient multi-pane terminal interface.
- **Single Sudo Authentication**: Prompts for the sudo password only once to ensure smooth operation.
- **Customizable Scanning Options**: Easily modify scan parameters within the script to suit specific needs.

## Requirements

Before using shighra, ensure your system meets the following requirements:

- **Operating System**: Kali Linux or any compatible Linux distribution.
- **Dependencies**:
  - **tmux**: Terminal multiplexer. (Install via `sudo apt install tmux`)
  - **masscan**: High-speed port scanner. (Install via `sudo apt install masscan`)
  - **nmap**: Comprehensive network exploration tool. (Install via `sudo apt install nmap`)
  - **fastmap.sh**: Your custom or third-party scanning script, located in the same directory.

## Installation

1. **Clone the Repository**:
   Clone or download the shighra script to your desired directory, recommanded:
   
   ```bash
   git clone https://github.com/sudosuraj/shighra.git /opt/shighra
   cd /opt/shighra
   echo alias shighra="python3 /opt/shighra/shighra.py" > ~/.bashrc
   sudo chmod +x fastmap.sh
   echo alias fastmap="/opt/shighra/fastmap.sh" > ~/.bashrc
   cd -
   ```

