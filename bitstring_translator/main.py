import time
import random


def run_and_translate(duration_seconds):
    responses = ["1", "0", ""]
    current_bits = ""
    start_time = time.time()

    print(f"Collecting bits for {duration_seconds} seconds...\n")

    while time.time() - start_time < duration_seconds:
        bit = random.choice(responses)

        # Replace a spacer choice if the previous output was also a spacer.
        if bit == "" and current_bits.endswith(" "):
            bit = random.choice(["1", "0"])
        
        if bit == "":
            print("[SPACER]")
            current_bits += " "
        else:
            print(bit)
            current_bits += bit
            
        time.sleep(0.1)

    print("\n--- Translating... ---")
    
    binary_chunks = current_bits.split()
    translated_text = ""
    
    for chunk in binary_chunks:
        # Pad short binary sequences to 8 bits with leading zeros (e.g. '011' -> '00000011')
        padded_chunk = chunk.zfill(8)
        
        try:
            ascii_num = int(padded_chunk, 2)
            # Only print standard printable ASCII characters (letters, numbers, basic punctuation)
            if 32 <= ascii_num <= 126:
                translated_text += chr(ascii_num)
            else:
                translated_text += f"[{ascii_num}]"  # Show numeric ASCII code if non-printable
        except ValueError:
            translated_text += "[?]"

    print(f"Intput: {current_bits}")
    print(f"Output: {translated_text}")

run_and_translate(20)