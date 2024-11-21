import argparse


def get_args() -> argparse.Namespace:
    """
    Reads arguments from terminal
    :return: Arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type = str, help="Keyword of search request")
    parser.add_argument("-d", "--imgdir", type = str, help="Path to the folder, where you want to save images")
    parser.add_argument("-f", "--flag", type = bool, help= "Grayscale true or false")
    arguments = parser.parse_args()
    print(arguments.flag)
    return arguments