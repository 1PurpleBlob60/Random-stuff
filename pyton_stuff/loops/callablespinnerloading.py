import time
print("loading:\n", end="", flush=True)
for _ in range(5):
    for stick in ["|", "/", "-", "\\"]:
        print(f"\r{stick}", end="", flush=True)
        time.sleep(0.15)

print("\nDone!")
