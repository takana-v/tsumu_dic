from pathlib import Path

from pyopenjtalk import create_user_dict

for dict_dir_path in Path("dict").iterdir():
    if dict_dir_path.is_dir:
        for dict_path in dict_dir_path.iterdir():
            if dict_path.suffix != ".csv":
                continue
            create_user_dict(str(dict_path), str(dict_path)+".dic")