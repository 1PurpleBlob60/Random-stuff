import time
print("Loading\n", end="", flush=True)
for _ in range(4):
    for dots in [".  ", ".. ", "..."]:
        print(f"\r{dots}", end="", flush=True)
        time.sleep(0.4)

print("\nDone!")
