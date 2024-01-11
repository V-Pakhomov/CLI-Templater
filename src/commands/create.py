import sys
import shutil
from pathlib import Path

from config import Config


def main(template_name: str, dirname: str):
    # TODO add checking abspath
    template_path = Path(Config.templates_dir, template_name)
    template_path.mkdir()

    template_tree_path = template_path / 'tree'
    shutil.copytree(dirname, template_tree_path)

    for path_object in template_tree_path.rglob('*'):
        if path_object.is_file():
            open(path_object, 'w').close()


if __name__ == "__main__":
    main(*sys.argv[1:])
