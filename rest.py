import pandas as pd
import datetime as DT
import time
from pathlib import Path

DATAFILE_PATH = Path("rest.txt")
COLUMNS=['Дата', 'Время начала отдыха', 'Время окончания отдыха']

#проверка на свободное время
def its_freetime():
    for i in range(3):
        msg_input = input("Вы хотите записать время отдыха? Пожалуйста укажите - да или нет " )

        if msg_input.lower() == "да":
            print("Хорошо, введите следующие данные " )
            time.sleep(1)
            break

        elif msg_input.lower() == "нет":
            raise SystemExit("К сожалению вы выбрали не ту функцию, попробуйте поискать нужную вам")

        else:
            print("Введено неверное значение, попробуйте еще раз (попыток осталось - {})".format(2 - i))


def input_data():
    data, firsttime, lasttime = None, None, None

    for i in range(3):
        try:
            data_str = input("Введите дату в формате дд/мм/гггг: ").strip()
            firsttime_str = input("Введите время начала отдыха в формате чч:mm: ").strip()
            lasttime_str = input("Введите время окончания отдыха в формате чч:mm: ").strip()

            data = DT.datetime.strptime(data_str, '%d/%m/%Y').date()
            firsttime = DT.datetime.strptime(firsttime_str, '%H:%M').time()
            lasttime = DT.datetime.strptime(lasttime_str, '%H:%M').time()

            break
        except ValueError:
            print(f'Вы ввели некорректные данные. Проверьте правильность ввода. Осталось попыток: {2 - i}')
            time.sleep(3)

    if data is not None and firsttime is not None and lasttime is not None:
        df = pd.DataFrame([[data, firsttime, lasttime]],
                          columns=COLUMNS)
        readAndWriteDF(df)
        return df
    else:
        return None

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

its_freetime()
df = input_data()
if df is not None:
    print(df)
else:
    print("Не удалось получить данные.")
