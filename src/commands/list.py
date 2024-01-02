from pathlib import Path

from config import Config


def main():
    path = Path(Config.templates_dir)
    for template in path.iterdir():
        if template.is_dir():
            print(template)


if __name__ == "__main__":
    main()
