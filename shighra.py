import os
import subprocess
import random
import string

def generate_random_session_name(length=8):
    """Generate a random session name."""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def create_attach_script(session_name):
    """Create a temporary script to attach to the tmux session."""
    script_content = f"""#!/bin/bash
tmux attach -t {session_name}
"""
    script_path = f"./attach_tmux_{random.randint(1000000000, 9999999999)}.sh"
    with open(script_path, 'w') as f:
        f.write(script_content)
    os.chmod(script_path, 0o755)
    return script_path
def run_command_in_tmux(session_name, command, pane_number):
    """Send a command to a specific tmux pane."""
    subprocess.run(["tmux", "send-keys", "-t", f"{session_name}:0.{pane_number}", command, "C-m"])
def main():

    banner = r"""

███████╗██╗  ██╗██╗ ██████╗ ██╗  ██╗██████╗  █████╗ 
██╔════╝██║  ██║██║██╔════╝ ██║  ██║██╔══██╗██╔══██╗
███████╗███████║██║██║  ███╗███████║██████╔╝███████║
╚════██║██╔══██║██║██║   ██║██╔══██║██╔══██╗██╔══██║
███████║██║  ██║██║╚██████╔╝██║  ██║██║  ██║██║  ██║
╚══════╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                       by @sudosuraj


   
  """
    print(banner)
    ip = input("Enter the target IP address: ")
    password = input("Enter your sudo password: ")
    session_name = generate_random_session_name()
    print(f"Creating tmux session: {session_name}")
    subprocess.run(["tmux", "new-session", "-d", "-s", session_name])
    print("tmux session created.")
    masscan_command = f"echo {password} | sudo -S masscan -p1-65535,U:1-65535 {ip} --rate=1000 -e eth0 | tee -a masscan-udp.txt"
    nmap_command = f"echo {password} | sudo -S nmap --min-rate 1000 --max-retries 5 -p1-65535 -Pn -n {ip} | tee -a nmap-all.txt"
    fastmap_command = f"echo {password} | sudo -S fastmap {ip} | tee -a fastmap-output.txt"
    run_command_in_tmux(session_name, masscan_command, 0)
    subprocess.run(["tmux", "split-window", "-h"])
    run_command_in_tmux(session_name, nmap_command, 1)
    subprocess.run(["tmux", "split-window", "-v"])
    run_command_in_tmux(session_name, fastmap_command, 2)
    attach_script_path = create_attach_script(session_name)
    print("Attaching to tmux session...")
    subprocess.run(["bash", attach_script_path])
    print("Attached to tmux session.")

if __name__ == "__main__":
    main()
