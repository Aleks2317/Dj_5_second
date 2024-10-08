# Поисковые поля используют простой синтаксис двойного подчёркивания. 

<поле поиска>__<поисковый метод>

>Worker.objects.filter(first_name__exact='John')

Под капотом Django создает запрос SQL WHERE для построения запросов к базе данных из применяемого поиска. Допускается многократный поиск, а также поисковые поля могут быть выстроены по цепочке:

>Worker.objects.filter(first_name__exact='John', created__year__lt=2024)

Тем самым мы получаем сотрудника с именем John, созданного раньше 2024 года. Рассмотрим все методы поисковых полей:

 

### Полный список поисковых методов в Django

>exact/iexact:   Точное совпадение. iexact - версия без учета регистра.

>contains/icontains:   Поле содержит текст поиска. icontains это версия без учета регистра.

>in:   Наличие в указанном итерируемом объекте (список, кортеж или QuerySet).

>gt/gte:   Больше чем / больше чем или равно.

>lt/lte:   Меньше чем / меньше чем или равно.

>startswith/istartswith:   Начинается в строке поиска. istartswith это версия без учета регистра.

>endswith/iendswith:   Заканчивается в строке поиска. iendswith это версия без учета регистра.

>range:   Тест диапазона. Диапазон включает в себя начальное и конечное значения.

>date:   Передает значение в виде даты. Используется для поиска полей datetime.

>year:   Поиск точного совпадения года.

>iso_year:   Поиск точного совпадения по году ISO 8601.

>month:   Поиск точного совпадения месяца.

>day:   Поиск точного совпадения дня.

>week:   Поиск точного совпадения недели.

>week_day:   Поиск точного совпадения дня недели.

>quarter:   Поиск точного совпадения квартала года.

>time:   Использует значение времени. Используется для поиска полей datetime.

>hour/minute/second:   Поиск точного совпадения по часам, минутам или секундам.

>isnull:   Проверяет, есть ли нулевое поле. Возвращает True или False.

>regex/iregex:   Совпадение по регулярному выражению. iregex - версия без учета регистра.

Подробнее о методах вы можете посмотреть в документации.  По аналогии с прошлым разделом запустим шелл и импортируем модель Worker и на практике рассмотрим некоторые методы подробнее:

 

 ## exact/iexact
Поиск exact используется для получения записей с указанным значением. Поиск exact чувствителен к регистру. Для поиска без учета регистра используйте поиск iexact.

Worker.objects.filter(first_name__exact='John')


 

## contains/icontains
contains позволяет вам проверить, содержит ли строка подстроку. Это эквивалентно следующему оператору - LIKE:

LIKE '%substring%'
Например, следующий код находит сотрудников, чье имя содержит подстроку Jes:

Worker.objects.filter(first_name__contains='Jes')


Запрос возвращает сотрудника с именем Jessie.

icontains это нечувствительная к регистру версия метода contains. Таким образом, вы можете использовать icontains чтобы проверить, содержит ли строка подстроку, без учета регистра:

Worker.objects.filter(first_name__icontains='jes')


 

in()
Оператор SQL IN возвращает QuerySet, если значение одного из полей равно одному из значений:

field_name IN (v1, v2, ...)
В Django вы используете in оператор:

Worker.objects.filter(age__in=(25, 31)) 
