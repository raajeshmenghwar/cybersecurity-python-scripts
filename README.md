# Python Scripts Repository

This repository contains Python projects I have built during my learning journey. Each project focuses on different aspects of programming, cybersecurity, networking, and automation. Below you'll find a list of all the projects with brief descriptions and the libraries used.

## Project List

### [Auto](#auto)
- **Description**: A set of automation scripts designed for various tasks like handling multihandler, Nmap scanning, and SSH automation.
- **Libraries Used**: `paramiko`, `nmap`, `time`
  - [multihandlerAuto.py](auto/multihandlerAuto.py)
  - [nmapAuto.py](auto/nmapAuto.py)
  - [sshAuto.py](auto/sshAuto.py)

### [Exploit](#exploit)
- **Description**: Contains a script that exploits vulnerabilities, specifically designed for `vsftpd` vulnerability testing.
- **Libraries Used**: `socket`
  - [vsftd.py](exploit/vsftd.py)

### [PCAP](#pcap)
- **Description**: A collection of scripts and files related to packet capture analysis and forensic examination.
- **Libraries Used**: `scapy`, `pyshark`
  - [decoding-mixed-case-usb-keystrokes-from.html](pcap/decoding-mixed-case-usb-keystrokes-from.html)
  - [forensics_key_mission.zip](pcap/forensics_key_mission.zip)
  - [hut1_12v2.pdf](pcap/hut1_12v2.pdf)
  - [key_mission.pcap](pcap/key_mission.pcap)
  - [sol4mChatGPT.py](pcap/sol4mChatGPT.py)
  - [sol.py](pcap/sol.py)
  - [temp.text](pcap/temp.text)

### [PortScanners](#portscanners)
- **Description**: Scripts to perform port scanning operations using custom methods.
- **Libraries Used**: `socket`, `os`
  - [advscanner.py](portScanners/advscanner.py)
  - [portscanner.py](portScanners/portscanner.py)

### [PySys](#pysys)
- **Description**: A set of Python scripts to handle system operations, argument parsing, and encoding/decoding processes.
- **Libraries Used**: `sys`, `argparse`
  - [args1.py](pysys/args1.py)
  - [args2.py](pysys/args2.py)
  - [comment_args2.py](pysys/comment_args2.py)
  - [endec.py](pysys/endec.py)

### [Requests](#requests)
- **Description**: A collection of requests-related scripts for working with HTTP requests and responses.
- **Libraries Used**: `requests`, `beautifulsoup4`
  - [file.html](requests/file.html)
  - [req.py](requests/req.py)

### [Sock](#sock)
- **Description**: Basic socket programming scripts for client-server communication.
- **Libraries Used**: `socket`
  - [client.py](sock/client.py)
  - [server.py](sock/server.py)

### [Thread](#thread)
- **Description**: Multi-threading scripts for handling parallel client-server communication.
- **Libraries Used**: `threading`, `socket`
  - [client.py](thread/client.py)
  - [rough.py](thread/rough.py)
  - [server.py](thread/server.py)

---

## How to Run These Projects

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/python.git
