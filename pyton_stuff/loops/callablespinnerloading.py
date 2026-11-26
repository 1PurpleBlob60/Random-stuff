import time
from time import perf_counter as timer

def spinnerloading():

    start = timer()
    print("loading:\n", end="", flush=True)
    for _ in range(5):
        for stick in ["|", "/", "-", "\\"]:
            print(f"\r{stick}", end="", flush=True)
            time.sleep(0.15)
    end = timer()
    print("\nDone!")
    print(f"Time: {end - start:.2f} seconds")

spinnerloading()