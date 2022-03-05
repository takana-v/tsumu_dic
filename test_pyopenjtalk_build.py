from pathlib import Path

from pyopenjtalk import create_user_dict

for dict_dir_path in Path("dict").iterdir():
    if dict_dir_path.is_dir() and dict_dir_path.name == "external":
        for ex_dict_dir_path in dict_dir_path.iterdir():
            for ex_dict_path in ex_dict_dir_path.iterdir():
                if ex_dict_path.suffix != ".csv":
                    continue
                create_user_dict(str(ex_dict_path), str(ex_dict_path)+".dic")
    elif dict_dir_path.is_dir():
        for dict_path in dict_dir_path.iterdir():
            if dict_path.suffix != ".csv":
                continue
            create_user_dict(str(dict_path), str(dict_path)+".dic")
