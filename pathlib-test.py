# batch cleaning & rebnaming .txt files

'''
pathlibとglobで同じ構造で新たなdirを自動化作成することができる！！！！！
dirを自分で作らなくでいい！！！！！
パス対象を実体化するときもとのあるPathと新たなstrを/で繋げるのでかい！！！！！
ファイル内容のreadとwriteが簡単になる！！！！
今後もpathlibを使いこなしたい＜＜＜
'''

import glob
from pathlib import Path

# original example:
original_files = Path("gdrive/MyDrive/").glob(r"calculate_forpathlib/*/*.txt")
for of in original_files:
    original_text = of.open().read()
    preprocessed_text = clean(original_text)
    parent_dir = of.parent
    preprocessed_file = of.stem + "_cleaned.txt"
    Path(parent_dir / preprocessed_file).write_text(preprocessed_text)


# real process:
original_files = Path("gdrive/MyDrive/").glob(r"calculate_pathlib/*/*.txt")
for of in original_files:
    original_text = of.open().read()
    preprocessed_text = clean(original_text)
    parent_dir = of.parent
    # cleaned_dir = Path(parent_dir / "preprocessed")
    real_last_cleaned_dir = Path(parent_dir / "real_last_preprocessed")
    real_last_cleaned_dir.mkdir(parents=True, exist_ok=True)
    # preprocessed_file_dir = cleaned_dir + "preprocessed"
    preprocessed_file = of.stem + "_cleaned.txt"
    Path(real_last_cleaned_dir / preprocessed_file).write_text(preprocessed_text)
