import argparse
import re
from logging import exception


def parcing()->argparse.Namespace:
    parser = argparse.ArgumentParser()  # создание экземпляра парсера
    parser.add_argument('file_name', type=str, help='Введите название файла (с расширением)')
    parser.add_argument('name', type=str,help='название города в именительном падеже')
    args = parser.parse_args()
    # парсинг аргументов
    return args
    '''
    Данная функция запрашивает у пользователя название файла
    и параметр, по которому выбираются анкеты
    '''

def list_searcher(list1:list, args:argparse.Namespace)->list:
    flag = True
    result_list=[]
    for i in range(len(list1)):
        if (re.search(f"{args.name}", list1[i]) != None):
            result_list.append(str(i) + ')'+'\n'+list1[i])
            flag = False
    if flag:
        print("Таких людей в списке нет")
    return result_list
    '''
    Данная функция выбирает нужные анкеты
    '''

def text_splitter(text:str)->list:
    pattern=r'\d+'+r'[)]+'+'\n'
    list1=re.split(pattern,text,maxsplit=0)
    return list1
    '''
    Данная функция делит текст на список анкет
    '''


def read_file(args:argparse.Namespace)->str:
    with open(f"{args.file_name}", "r",encoding="utf_8") as file:
        text = file.read()
    return text
    '''
    Данная функция читает данные из файла
    '''

def list_print(list1:list)->None:
    for i in range(len(list1)):
        print(list1[i])
    '''
    Данная функция распечатывает список
    '''


def main():
    args = parcing()

    #print("Введите корректные параметры запуска программы")

    try:
        # ВЫЗВАЛИ ИСКЛ НА ОТСУТСВИЕ ФАЙЛА
        args = parcing()
        file = read_file(args)
        if len(file) == 0:
            raise Exception("файл пуст")
        blanks = text_splitter(file)
        result_list = list_searcher(blanks, args)
        list_print(result_list)

    except argparse.ArgumentTypeError:
        print("Ошибка: данные введены некорректно. Воспользуйтесь --help")
    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except Exception as exc:
        print("Ошибка:", exc)



if __name__== '__main__':
        main()
