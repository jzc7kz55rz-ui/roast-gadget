import os

ENTRY = 'My smart kettle needs a firmware update before it boils water, so my tea now comes with release notes.'
MAX_CHARS = 200  # the gate accepts 1..200 characters


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
