# vsosh-project
**Репозиторий проекта "Защита резервных копий, расположенных в облачных хранилищах, от программ-шифровальщиков"**

*Настоящая программа разработана в рамках подготовки проекта к Всероссийской олимпиаде школьников по труду (технологии), профиль: Информационная безопасность.*

Программа, реализующая алгоритм мониторинга изменений в файловой системе, останавливающая работу фонового приложения облачного хранилища в системе при регистрации вредоносных изменений

**Принцип работы:**
Прерывание соединения с облачным хранилищем в момент регистрации вредоносной активности криптовымогателей – изменения расширений обрабатываемых файлов

**Руководство пользователя** расположенно в файле ***Инструкция.txt***

Используется список расширений [ransomware-fileext-list](https://github.com/dannyroemhild/ransomware-fileext-list) от [dannyroemhild](https://github.com/dannyroemhild) по лицензии GPL-3.0

2025 г.
