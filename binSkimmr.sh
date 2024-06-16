#!/bin/bash

# Name: extract_non_zero.sh
# Description: Extract & display non-zero address/offset values from a binary file
# Date: 2024-06-06
# Version: 1.2.0

if [ $# -ne 1 ]; then
  echo "Usage: $0 <binary-file>"
  exit 1
fi

binary_file=$1

# Generate the hexadecimal dump of the binary file
xxd -g 1 "$binary_file" | awk '
{
  offset = $1
  for (i = 2; i <= NF; i++) {
    # Check if the value is not 00 and not a placeholder for non-printable characters
    if ($i != "00" && $i !~ /^[.]+$/) {
      printf "Address: 0x%s, Value: %s\n", substr(offset, 1, length(offset)-1), $i
    }
    # Update offset
    offset = sprintf("%08x:", strtonum("0x" substr(offset, 1, length(offset)-1)) + 1)
  }
}
'
