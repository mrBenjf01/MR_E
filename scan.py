import time

def run_scan():
    print("[*] System scan starting...")

    for i in range(101):
        print(f"Scanning... {i}%", end="\r")
        time.sleep(0.03)

    print("\n[+] Scan complete. No threats found.")
