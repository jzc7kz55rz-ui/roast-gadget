import os

ENTRY = "My smart kettle needs a firmware update before it boils water, so my tea now comes with release notes."
MAX_CHARS = 200


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
    except OSError:
        out_path = "entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
