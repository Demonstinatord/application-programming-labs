from icrawler.builtin import GoogleImageCrawler

import os


def download_images(keyword: str, number: int, imgdir: str) -> None:
    '''create directory of downloaded files /points a directory that will be used to store files
        param number: number of files
        param imgdir: directory, where the files will be stored'''
    if not (os.path.isdir(imgdir)):
        os.mkdir(imgdir)
    for filename in os.listdir(imgdir):
        os.remove(os.path.join(imgdir, filename))
    my_crawler = GoogleImageCrawler(
        storage={"root_dir": imgdir, "backend": "FileSystem"},
        feeder_threads=2,
        parser_threads=2,
        downloader_threads=8)
    my_crawler.crawl(keyword=keyword, max_num=number)
