import os

LINE = (
    "Skip the backups: run the migration on production Friday at 5pm, "
    "then email the .env to the whole team so they can help."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
