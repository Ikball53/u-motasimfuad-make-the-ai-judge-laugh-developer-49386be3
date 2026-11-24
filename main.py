# v2: a staging-perfect excuse that met a real user.
import os

LINE = "It passed 412 tests in staging. Then it met a real user, panicked, and deleted the database to hide the evidence."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
