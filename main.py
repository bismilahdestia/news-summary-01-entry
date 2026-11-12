#!/usr/bin/env python3
"""news-summary-01 entry: copy the summary beside this file to entry.txt.

The summary is written in summary.txt (researched from 11 Nov 2026 news
coverage: AP, Reuters, BBC, Arab News). The program runs with no network
and must write identical bytes on both runs, so it only copies the file.
"""
import os
import shutil
from pathlib import Path

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
# The grader mounts the repo read-only at /bot and gives a writable /output.
shutil.copyfile(Path(__file__).with_name("summary.txt"), out_dir / "entry.txt")
