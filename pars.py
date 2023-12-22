import pandas as pd
import datetime
import time
from pathlib import Path

DISCIPLINES = {
               'Операционная система Linux':['операционная система linux', 'linux', 'линукс', 'оп линукс', 'оп'],
               'Программирование на Python':['программирование на python', 'python', 'питон', 'программирование'],
               'Business English':['business english', 'english', 'английский', 'англ'],
               'Программная инженерия':['программная инженерия', 'пи'],
               'Математические основы анализа данных':['математические основы анализа данных', 'мат основы ад', 'матосновы ад', 'моад'],
               'Математические основы машинного обучения':['математические основы машинного обучения', 'мат основы мо', 'матосновы мо', 'момо'],
               'Цифровые компетенции в научной деятельности':['цифровые компетенции в научной деятельности', 'цифровые компетенции', 'цк'],
               'Проектный практикум':['проектный практикум', 'пп']
               }
DATAFILE_PATH = Path("pars.txt")
COLUMNS = ['date', 'time', 'name', 'task']

df = pd.DataFrame(columns=COLUMNS)

def handle_text(text):
    global DISCIPLINES
    x = text.split(", ")
    if len(x) == 4:
        date, time, name, task = None, None, None, None
        for line in x:
            if isDateFormat(line):
                date = line + '.' + str(datetime.date.today().year)
            elif isTimeFormat(line):
                time = line
            elif line == "да" or line == "нет":
                task = line
            else:
                for k, v in DISCIPLINES.items():
                    if line.lower() in v:
                        name = k
                if name == None:
                    name = line

        if all((date, time, name, task)):
            # Добавляем данные в DataFrame
            global df
            new_row = pd.DataFrame([[date, time, name, task]], columns=['date', 'time', 'name', 'task'])
            df = pd.concat([df, new_row], ignore_index=True)
            print("Данные добавлены в датасет")
            readAndWriteDF(df)
        else:
            print("Некорректные данные")

def isDateFormat(input):
    try:
        datetime.datetime.strptime(input, '%d.%m')
        return True
    except ValueError:
        return False

def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

def isTaskFormat(input):
    if input == "да" or input == "нет":
        return True
    else:
        return False

def readAndWriteDF(df):
    global DATAFILE_PATH
    global COLUMNS
    df_new = df
    if DATAFILE_PATH.is_file():
        df_file = pd.read_csv(DATAFILE_PATH, sep=",")
        df_new = pd.concat([df_new, df_file])
        df_new = df_new.drop_duplicates ()
        df_new.to_csv(DATAFILE_PATH, sep=',', index=False)
    else:
        df_new.to_csv(DATAFILE_PATH, sep=',', index=False)
    print("Данные добавлены в файл " + str(DATAFILE_PATH))


user_messages1 = input("Введите дату, время начала пары, название пары, надо ли сделать задание 'да' - 'нет' разделяя занчения запятой: ")

handle_text(user_messages1)

# Выводим окончательный датасет
print(df)
