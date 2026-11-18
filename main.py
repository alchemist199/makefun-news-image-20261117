#!/usr/bin/env python3
"""Copy the front-page image to /output/entry.png.

Stdlib only, no network, deterministic: the output is a byte-for-byte
copy of entry.png next to this script. After copying, the output's byte
size is checked against the source's; a mismatch is a hard error.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    src_size = os.path.getsize(SRC)
    out_size = os.path.getsize(OUT)
    if out_size != src_size:
        print(f"error: size mismatch: output {out_size} != source {src_size}",
              file=sys.stderr)
        sys.exit(1)
    with open(OUT, "rb") as f:
        header = f.read(8)
    if header != b"\x89PNG\r\n\x1a\n":
        print("error: output is not a valid PNG (bad magic header)",
              file=sys.stderr)
        sys.exit(1)
    print("wrote", OUT, f"({out_size} bytes)")


if __name__ == "__main__":
    main()
