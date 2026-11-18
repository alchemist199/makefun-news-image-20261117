#!/usr/bin/env python3
"""Copy the front-page image to /output/entry.png.

Stdlib only, no network, deterministic: the output is a byte-for-byte
copy of entry.png next to this script.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print("wrote", OUT)


if __name__ == "__main__":
    main()
