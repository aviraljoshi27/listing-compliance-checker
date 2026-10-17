"""Downloads the Amazon listing files I use into data/raw/.

If a file is already there it gets skipped, so running this twice is fine.
"""

from pathlib import Path

import httpx

BASE_URL = (
    "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/"
)
FILES = ["meta_Health_and_Personal_Care.jsonl.gz", "meta_All_Beauty.jsonl.gz"]
RAW_DIR = Path(__file__).resolve().parents[1] / "data" / "raw"


def download_file(name: str) -> None:
    """Downloads one file into data/raw/, unless it's already there."""
    target = RAW_DIR / name
    if target.exists():
        print(f"{name} already downloaded, skipping")
        return
    partial = target.with_name(name + ".part")
    url = BASE_URL + name
    with httpx.stream("GET", url, timeout=60, follow_redirects=True) as response:
        response.raise_for_status()
        with partial.open("wb") as file:
            for chunk in response.iter_bytes():
                file.write(chunk)
    partial.rename(target)
    print(f"{name} saved ({target.stat().st_size / 1e6:.1f} MB)")


def main() -> None:
    """Makes sure data/raw/ exists, then downloads each file in turn."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        download_file(name)


if __name__ == "__main__":
    main()
