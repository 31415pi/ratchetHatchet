import struct
import csv
import sys

# Define drum base addresses and potential stride
base_addresses = [
    0x00000000, 0x00002000, 0x00004000, 0x00006000, 
    0x00008000, 0x0000A000, 0x0000C000, 0x0000E000,
    0x00010000, 0x00012000, 0x00014000, 0x00016000
]

# Define stride and page size (guessing from data)
stride = 0x10
page_size = 16

def read_bin_file_to_csv(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()

    patterns = {drum: [[0]*page_size for _ in range(4)] for drum in range(1, 13)}

    # Try to extract non-zero values
    for drum in range(1, 13):
        base_addr = base_addresses[drum - 1]
        for page in range(4):
            for step in range(page_size):
                address = base_addr + page * stride + step
                if address < len(data):
                    value = data[address]
                    if value != 0:
                        # Assuming value 0x0d at address 0x000020d8 corresponds to 14 ratchets (value - 1)
                        # and that 0x03 at address 0x00000003 corresponds to step activation.
                        if address % 4 == 0:  # Simplified assumption, to be refined
                            patterns[drum][page][step] = value  # Assuming it to be step activation
                        elif address % 4 == 1:  # Adjusted pattern recognition
                            patterns[drum][page][step] = value + 1  # Assuming ratchet count

    # Write to CSV
    with open(output_file, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        header = ["DRUM", "PAGE"] + [str(i) for i in range(16)]
        csvwriter.writerow(header)
        
        for drum in range(1, 13):
            for page in range(4):
                row = [f"Drum {drum}", f"Page {page + 1}"] + patterns[drum][page]
                csvwriter.writerow(row)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bin_to_csv.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    read_bin_file_to_csv(input_file, output_file)
