import time
import threading
from time import perf_counter as timer

def spinnerloading(check_spinning):
    start = timer()
    print("loading:\n", end="", flush=True)
    
    while check_spinning():
        for stick in ["|", "/", "-", "\\"]:
            if not check_spinning():
                break
            print(f"\r{stick}", end="", flush=True)
            time.sleep(0.15)
            
    end = timer()
    print("\nDone!")
    print(f"Time: {end - start:.2f} seconds")

# --- How you use it ---
keepspinning = True

# Start the spinner in the background
t = threading.Thread(target=spinnerloading, args=(lambda: keepspinning,))
t.start()

# Your main code goes here (simulating 3 seconds of work)
time.sleep(3)

# Set your variable to False to stop it
keepspinning = False
t.join()
