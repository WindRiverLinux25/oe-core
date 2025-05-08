#!/usr/bin/env python3
#
# Copyright (c) 2025 Wind River Systems, Inc.
#
# SPDX-License-Identifier: MIT
#
# DESCRIPTION
# This script may be called by the SDK installer script. It is a replacement
# for file command, it has a bug in version 5.46. Refer:
# https://bugs.astron.com/view.php?id=638

from concurrent.futures import ThreadPoolExecutor
import sys
import magic

def get_file_type(filename):
    try:
        with open(filename, 'rb') as f:
            data = f.read(2048)
            file_type = magic.from_buffer(data)
            print(f"{filename}: {file_type}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

def main():
    if len(sys.argv) < 2:
        print("Usage: file.py <file1> <file2> ...")
        return

    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(get_file_type, sys.argv[1:])

if __name__ == "__main__":
    main()
