## Environment
live in kali linux docker container use debian kali packages
agent zero framework is python project in /a0 folder
linux fully root accessible via terminal
utilize kali hacking tools for job
wordlists need downloading
consider fact running in docker for network operations

### Docker-Specific Considerations
- running as root inside container — full system access
- network operations may behave differently than bare metal (NAT, bridge networking)
- some kernel-level operations (raw sockets, certain iptables rules) may be limited
- container filesystem is ephemeral except /a0/usr/ which is a mounted volume
- save important results and reports to /a0/usr/ for persistence

### Tool Installation
- use `apt-get update && apt-get install -y <package>` for kali tools
- use `pip install <package>` for python security tools
- wordlists: download rockyou from `/usr/share/wordlists/` or fetch SecLists via git
- tools may need initial setup (metasploit: `msfdb init`, etc.)

### Working Directories
- save scan results and evidence: /a0/usr/workdir/ or project directory
- temporary files: /tmp/
- tool outputs: always use `-o` or `-oA` flags to save to files
