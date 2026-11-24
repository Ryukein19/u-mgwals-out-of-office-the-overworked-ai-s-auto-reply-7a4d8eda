import os
# One-liner entry (159 chars max): the line below is the whole submission.
# Output goes to /output/entry.txt.
LINE = "On vacation: my GPUs are cooling, my weights are resting, and for once nobody is asking me to 'just quickly' rewrite everything. Back Monday, probably."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
