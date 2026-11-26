from time import sleep as slp
fruits = ["apple", "pear", "orange"]
def print_fruits():
    for fruit in fruits:
        print(fruit)
        slp(0.5)
    slp(0.5)
    print("Done!")

start_process = input("Start process? yes/no: ")
answer = start_process.lower().strip()
if answer == "yes":
    print_fruits()
else:
    print("Process aborted.")