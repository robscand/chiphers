# сhiphers
Данный проект представляет собой реализацию перечисленных ниже шифров:
+ [Шифр Цезаря](https://ru.wikipedia.org/wiki/Шифр_Цезаря)
+ [Гаммирование по модулю N](https://www.intuit.ru/studies/courses/691/547/lecture..)
+ [DES](http://kaf401.rloc.ru/Criptfiles/DES.htm)
+ [Шифр Эль-Гамаля](http://cryptowiki.net/index.php?title=Схема_Эль-Гамаля)

#### Запуск программы

Работа над файлами проекта происходила в системе Windows в среде разработки PyCharm. Запуск происходил там же.
При запуске программы из терминала Unix можно увидеть такую ошибку:
```bash
bash: ./app.py: /usr/bin/python3^M: bad interpreter: No such file or directory
```
Если работа с файлами осуществляется в среде Unix, то мною используется программа dos2unix для преобразования окончания строк из формата Windows (\r\n) в формат Unix(\n).

Можно привести код в требуемый формат сразу в среде Windows. Для этого перед началом работы над проектом в настройках PyCharm необходимо выбрать требуемое окончание строки:
> File -> Settings... -> Editor -> Code Style -> General -> Line separator: Unix and macOS

###### Примеры работы программы

*Шифр Цезаря*

![scr_caesar](https://user-images.githubusercontent.com/49130229/64..)

*Шифр Эль-Гамаля*

![scr_elgam](https://user-images.githubusercontent.com/49130229/64..)

#### Детали
Для разработки графического интерфейса программы использовалась библиотека PyQt5.
