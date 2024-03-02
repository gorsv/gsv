import pandas as pd
import datetime
import time
from pathlib import Path

# Словарь названий дисциплин и вариантов их написания
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

# Путь к файлу с датасетом расписания занятий
DATAFILE_PATH = Path("./resources/pars.txt")

# Список имён полей датасета
COLUMNS = ['date', 'time', 'name', 'task']

df = pd.DataFrame(columns=COLUMNS)

# Функция для парсинга строки, введённой пользователем, в датасет
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

# Проверка является ли строка датой
def isDateFormat(input):
    try:
        datetime.datetime.strptime(input, '%d.%m')
        return True
    except ValueError:
        return False

# Проверка является ли строка временем
def isTimeFormat(input):
    try:
        time.strptime(input, '%H:%M')
        return True
    except ValueError:
        return False

# Проверка является ли строка отметкой о наличии задания
def isTaskFormat(input):
    if input == "да" or input == "нет":
        return True
    else:
        return False

# Функция записи датасета свободного времени в файл
def readAndWriteDF(df):
    global DATAFILE_PATH
    global COLUMNS
    df_new = df
    # Проверка наличия файла. Создание файла, если его нет. Запись датасета в файл.
    if DATAFILE_PATH.is_file():
        df_file = pd.read_csv(DATAFILE_PATH, sep=",")
        df_new = pd.concat([df_new, df_file])
        df_new = df_new.drop_duplicates ()
        df_new.to_csv(DATAFILE_PATH, sep=',', index=False)
    else:
        df_new.to_csv(DATAFILE_PATH, sep=',', index=False)
    print("Данные добавлены в файл " + str(DATAFILE_PATH))

# Запрос на введние пользователем строки с данными о дате, времени, навания предмета и отметки есть ли задание на эту пару
user_messages1 = input("Введите дату, время начала пары, название пары, надо ли сделать задание 'да' - 'нет' разделяя значения запятой: ")

handle_text(user_messages1)

# Выводим окончательный датасет
print(df)
