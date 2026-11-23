"""Write this make.fun entry to the configured output directory."""

import os
import sys
from pathlib import Path

TEXT = "A Russian warship stopped in Libya for fuel, and Ukraine sent seven drones that sank it 1,500 miles from the nearest front line."

assert 1 <= len(TEXT) <= 280

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
output_path = Path(output_dir)
output_path.mkdir(parents=True, exist_ok=True)
(output_path / "entry.txt").write_bytes(TEXT.encode("utf-8"))

print(len(TEXT), file=sys.stderr)
