import csv
import os

def create_annotation(imgdir: str, csv_path: str) -> None:
    """
    Creates annotation (.csv file) with absolute and relative paths to images
    :param imgdir: Directory with images
    :param csv_path: .csv file that is used to write annotation
    """
    try:
        with open(csv_path, mode='w', newline='', encoding='utf-8') as annotation_file:
            writer = csv.writer(annotation_file)
            headers = ['Relative path', 'Absolute path']
            writer.writerow(headers)

            for file in os.listdir(imgdir):
                relative_path = os.path.relpath(file, start=imgdir)
                absolute_path = os.path.abspath(file)
                writer.writerow([relative_path, absolute_path])
    except: raise PermissionError("can't open csv file")

class ImageIterator:
    '''iteration of 1Kla$'''
    def __init__(self, csv_path: str) -> None:
        ''' fields of iterator'''
        self.csv_path = csv_path
        self.path_list = self.__load_csv()
        self.limit = len(self.path_list)  # ограничение
        self.counter = 0  # счётчик

    def __iter__(self) -> 'ImageIterator':
        '''return example of iterator'''
        return self

    def __next__(self) -> str:
        '''return next element'''
        if self.counter < self.limit:
            next_element = self.path_list[self.counter]
            self.counter += 1
            return next_element
        else:
            raise StopIteration("iteration has broken")

    def __load_csv(self) -> list:
        '''return list of path's to files'''
        with open(self.csv_path, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader) # skip the header
            path_list = list(row[1] for row in reader)

            return path_list

