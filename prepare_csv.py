import argparse
import shutil

from pathlib import Path
from typing import List, Optional

def main(external_dirs: Optional[List[Path]]):
    Path("build").mkdir()
    shutil.copy(Path("LICENSE"), Path("build"))
    if external_dirs is None:
        external_dirs = []
    for dict_dir in Path("dict").iterdir():
        if not dict_dir.is_dir():
            continue
        if dict_dir.name == "external":
            for external_dir in external_dirs:
                working_dir = Path("dict/external") / external_dir
                for dict_csv in working_dir.iterdir():
                    if dict_csv.suffix == ".csv":
                        shutil.copy(dict_csv, Path("build"))
                with Path("build/LICENSE").open(encoding="utf-8", mode="a") as f:
                    f.write((working_dir/"LICENSE").read_text(encoding="utf-8"))


        for dict_csv in dict_dir.iterdir():
            if dict_csv.suffix == ".csv":
                shutil.copy(dict_csv, Path("build"))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--external_dir", type=Path, default=None, action="append")

    args = parser.parse_args()

    main(external_dirs=args.external_dir)
