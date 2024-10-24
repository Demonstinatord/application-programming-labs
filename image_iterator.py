import csv

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