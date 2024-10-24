# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os

import downloader
import image_iterator
import parser
from annotation_creator import create_annotation


def main() -> None:
    args = parser.get_args()
    try:
        downloader.download_images(args.keyword, args.number, args.imgdir)
        if len((os.listdir(args.imgdir))) == 0 and args.number != 0:
            raise FileNotFoundError("can't download images")
        create_annotation(args.imgdir, args.annotation_file)
        iterator = image_iterator.ImageIterator(args.annotation_file)
        for item in iterator:
            print(item)

    except FileNotFoundError as di:
        print(f"Something went wrong: {di}")

    except PermissionError as pe:
        print(f"Something went wrong: {pe} ")

    except StopIteration as si:
        print(f"Something went wrong: {si} ")


if __name__ == "__main__":
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
