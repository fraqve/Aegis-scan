import subprocess

def run_nmap(target:str) -> str:
    try:
        proces = subprocess.run(["nmap","-sV",target],capture_output=True,text=True)
        return proces.stdout
    
    except FileNotFoundError:
        print("[!] Nmap not found is it installed ?")
        return "ERROR:nmap_not_found"
    
    except subprocess.CalledProcessError:
        print("[!] There has been an error running nmap please try again.")
        return "ERROR:nmap_failed"
    

def run_gobuster(target:str,wordlist:str) -> str:
    try:
        proces = subprocess.run(["gobuster","dir","-u",f"http://{target}","-w",wordlist],capture_output=True,text=True)
        return proces.stdout
    
    except FileNotFoundError:
        print("[!] Gobuster not found is it installed ?")
        return "ERROR:gobuster_not_found"
    
    except subprocess.CalledProcessError:
        print("[!] There has been an error running gobuster please try again.")
        return "ERROR:gobuster_failed"


def run_nikto(target:str) -> str:
    try:
        proces = subprocess.run(["nikto","-h",f"http://{target}"],capture_output=True,text=True)
        return proces.stdout
    
    except FileNotFoundError:
        print("[!] Nikto not found is it installed ?")
        return "ERROR:nikto_not_found"
    
    except subprocess.CalledProcessError:
        print("[!] There has been an error running nikto please try again.")
        return "ERROR:nikto_failed"