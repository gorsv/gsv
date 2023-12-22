import pandas as pd
import re
import os
import numpy as np
import requests
import datetime
import time

df = pd.DataFrame(columns=['date', 'time', 'name', 'task'])

def handle_text(text):
    x = text.split(", ")
    if len(x) == 4:
        date, time, name, task = None, None, None, None
        for line in x:
            if isDateFormat(line):
                date = line
            elif isTimeFormat(line):
                time = line
            elif line == "да" or line == "нет":
                task = line
            else:
                name = line

        if all((date, time, name, task)):
            # Добавляем данные в DataFrame
            global df
            new_row = pd.DataFrame([[date, time, name, task]], columns=['date', 'time', 'name', 'task'])
            df = pd.concat([df, new_row], ignore_index=True)
            print("Данные добавлены в датасет")
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

user_messages1 = input("Введите дату, время начала пары, название пары, надо ли сделать задание 'да' - 'нет': ")

handle_text(user_messages1)

# Выводим окончательный датасет
print(df)
