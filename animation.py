import time

def run_animation():
    print("INITIALIZING SYSTEM")

    bar = "[####################]"
    for i in range(21):
        print("\r" + bar[:i] + " " * (20 - i), end="")
        time.sleep(0.05)

    print("\n[✓] DONE")
