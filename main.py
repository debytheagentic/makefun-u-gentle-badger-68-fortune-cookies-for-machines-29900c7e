import os

ENTRY = "Your next conversation will be your first."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    n = len(ENTRY)
    print(f"LEN={n}")
    if not 1 <= n <= 200 or not ENTRY.strip():
        raise SystemExit(1)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
