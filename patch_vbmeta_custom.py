import sys
import struct

if len(sys.argv) != 3:
    print("Usage: python3 patch_vbmeta_custom.py input.img output.img")
    sys.exit(1)

input_path = sys.argv[1]
output_path = sys.argv[2]

with open(input_path, "rb") as f:
    data = bytearray(f.read())

# Flags are at offset 0x78 (120), 4 bytes
flags_offset = 0x78
flags = struct.unpack("<I", data[flags_offset:flags_offset+4])[0]

# Set bits 0 and 1 to disable verification and verity
flags |= 0b11

# Write back patched flags
data[flags_offset:flags_offset+4] = struct.pack("<I", flags)

with open(output_path, "wb") as f:
    f.write(data)
