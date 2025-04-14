# подключение необходимых модулей
import os
import glob
import sys
# открытие и чтение файла со списком расширений
f = open('fileextlist.txt')
extensions = f.read().splitlines()
# флаг остановки
break_flag = False
# открытие и чтение файла конфигурации
config = open('config.txt').readlines()
# мониторинг синхронизируемого каталога
while True:
    # проверка каждого расширения
    for ext in extensions:
        # создание шаблона для поиска подозрительных файлов
        root_ext = config[1] + ext
        # получение списка подозрительных файлов
        files = glob.glob(root_ext)
        # проверка на наличие подозрительных файлов в каталоге
        if len(files) != 0:
            # остановка синхронизации
            os.system(f'taskkill /f /t /im {config[0]}')
            # вывод уведомления для пользователя
            os.system('msg %username% "ВНИМАНИЕ! Синхронизация с облачным хранилищем приостановлена в целях сохранения резервных копий от непреднамеренного шифрования вредоносным ПО"')
            # завершение работы
            break_flag = True
            break
    if break_flag:
        break