import sys
import shutil
from pathlib import Path

from config import Config


def main(template_name: str):
    template_dir = Path(Config.templates_dir, template_name)
    if not template_dir.exists():
        print(f'no such template: {template_name}')
        return

    ans = None
    while ans not in ('y', 'n'):
        ans = input('this action can not be undone, continue? (y/n): ')

    if ans == 'n':
        return

    shutil.rmtree(template_dir)


if __name__ == "__main__":
    main(*sys.argv[1:])
