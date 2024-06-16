import csv
import struct

def write_csv_to_bin(input_filename, output_filename):
    base_addresses = [
        0x00000000, 0x00002000, 0x00004000, 0x00006000, 
        0x00008000, 0x0000A000, 0x0000C000, 0x0000E000,
        0x00010000, 0x00012000, 0x00014000, 0x00016000
    ]

    with open(input_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        lines = list(csv_reader)

    with open(output_filename, 'wb') as bin_file:
        for drum_index in range(12):
            base_address = base_addresses[drum_index]

            # Step on/off
            step_data = lines[drum_index * 3]
            bin_data = bytearray()
            for value in step_data:
                bin_data.append(int(value))
            bin_file.seek(base_address)
            bin_file.write(bin_data)

            # Gate length
            gate_data = lines[drum_index * 3 + 1]
            bin_data = bytearray()
            for value in gate_data:
                bin_data.append(int(value))
            bin_file.seek(base_address + 0x80)  # 80 addresses off
            bin_file.write(bin_data)

            # Ratchet
            ratchet_data = lines[drum_index * 3 + 2]
            bin_data = bytearray()
            for value in ratchet_data:
                bin_data.append(int(value))
            bin_file.seek(base_address + 0xC0)  # C0 addresses off
            bin_file.write(bin_data)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python scriptname.py inputfilename outputfilename")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    write_csv_to_bin(input_filename, output_filename)
