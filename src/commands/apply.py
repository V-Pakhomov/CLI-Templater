import sys
import shutil
from pathlib import Path

from config import Config


def main(template_name: str, dirname: str):
    # TODO add checking abspath
    template_tree_path = Path(Config.templates_dir, template_name, 'tree')
    shutil.copytree(template_tree_path, Path(dirname))


if __name__ == '__main__':  # adssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
    main(*sys.argv[1:])
