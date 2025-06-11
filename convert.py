#!/usr/bin/env python3
import argparse

def binary_to_hex(bin_str):
    bin_str = bin_str.strip().replace(" ", "")
    if len(bin_str) % 8 != 0:
        raise ValueError("Binary input must be a multiple of 8 bits.")
    byte_val = int(bin_str, 2).to_bytes(len(bin_str) // 8, byteorder="big")
    return byte_val.hex(), byte_val

def hex_to_binary(hex_str):
    hex_str = hex_str.strip().replace(" ", "")
    byte_val = bytes.fromhex(hex_str)
    bin_str = ''.join(f"{byte:08b}" for byte in byte_val)
    return bin_str, byte_val

def main():
    parser = argparse.ArgumentParser(description="Convert between binary and hex.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-b", "--binary", help="Binary string to convert to hex/bytes")
    group.add_argument("-x", "--hex", help="Hex string to convert to binary/bytes")

    args = parser.parse_args()

    if args.binary:
        try:
            hex_val, byte_val = binary_to_hex(args.binary)
            print(f"Hex:   {hex_val}")
            print(f"Bytes: {byte_val}")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.hex:
        try:
            bin_val, byte_val = hex_to_binary(args.hex)
            print(f"Binary: {bin_val}")
            print(f"Bytes:  {byte_val}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
