import subprocess


def run_nmap(target: str) -> str:
    """
    Runs an nmap service version scan (-sV) against the target.
    Returns the raw stdout output as a string.
    On failure, returns an error code string for downstream handling.
    """
    try:
        proces = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)
        return proces.stdout

    except FileNotFoundError:
        # nmap binary not found on PATH
        print("[!] Nmap not found is it installed ?")
        return "ERROR:nmap_not_found"

    except subprocess.CalledProcessError:
        print("[!] There has been an error running nmap please try again.")
        return "ERROR:nmap_failed"


def run_gobuster(target: str, wordlist: str) -> str:
    """
    Runs a gobuster directory enumeration scan against the target over HTTP.
    Requires a wordlist path — defaults to seclists common.txt if not provided by user.
    Returns the raw stdout output as a string.
    """
    try:
        proces = subprocess.run(
            ["gobuster", "dir", "-u", f"http://{target}", "-w", wordlist],
            capture_output=True, text=True
        )
        return proces.stdout

    except FileNotFoundError:
        # gobuster binary not found on PATH
        print("[!] Gobuster not found is it installed ?")
        return "ERROR:gobuster_not_found"

    except subprocess.CalledProcessError:
        print("[!] There has been an error running gobuster please try again.")
        return "ERROR:gobuster_failed"


def run_nikto(target: str) -> str:
    """
    Runs a nikto web vulnerability scan against the target over HTTP.
    Returns the raw stdout output as a string.
    """
    try:
        proces = subprocess.run(["nikto", "-h", f"http://{target}"], capture_output=True, text=True)
        return proces.stdout

    except FileNotFoundError:
        # nikto binary not found on PATH
        print("[!] Nikto not found is it installed ?")
        return "ERROR:nikto_not_found"

    except subprocess.CalledProcessError:
        print("[!] There has been an error running nikto please try again.")
        return "ERROR:nikto_failed"
