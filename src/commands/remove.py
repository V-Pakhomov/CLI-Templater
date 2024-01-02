import sys
import shutil
from pathlib import Path

from config import Config


def main(template_name: str):
    template_dir = Path(Config.templates_dir, template_name)
    shutil.rmtree(template_dir)


if __name__ == "__main__":
    main(*sys.argv[1:])
