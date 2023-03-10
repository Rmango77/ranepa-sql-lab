import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.set_page_config(
    page_title="Введение в  SQL", page_icon="📈"
)

st.markdown("<h2 style='text-align: center; color: black;'>Введение в SQL</h2>", unsafe_allow_html=True)

st.image("src/sql-title.jpeg")

st.markdown("<h5 style='text-align: center; color: black;'>Что такое SQL и для чего он нужен</h5>", unsafe_allow_html=True)
st.write(
    """
    \n SQL (сокращение от англ. Structured Query Language) — это язык запросов, который применяют, чтобы работать с базами данных, структурированных особым образом. Главные задачи SQL — составлять запросы так, чтобы находить среди большого объёма информации ту, что нужна для конкретных целей, сортировать её, структурировать и представлять в наиболее простом и понятном виде.
    \n Первый прототип языка SQL представила в 1979 году компания-разработчик Oracle. Сначала это был простейший инструмент для извлечения нужных данных, вроде фильтров в Excel-таблицах. С годами он усложнился, и теперь его применяют в качестве одного из основных инструментов для обработки данных. С помощью SQL можно: 
    \n ● собирать и хранить данные в виде таблиц
    \n ● изменять их содержимое и структуру
    \n ● объединять данные и выполнять вычисления
    \n ● защищать и распределять доступ
    """
)

st.markdown("<h5 style='text-align: left; color: black;'>Что такое база данных SQL</h5>", unsafe_allow_html=True)
st.write(
    """
    \n База данных — это способ хранения и организации данных, которые структурированы так, чтобы пользоваться ими могли и человек, и алгоритм.
    \n При помощи SQL можно работать с реляционными базами данных — то есть теми, где данные представлены в виде таблиц. Это отчасти похоже на таблицы в Excel, при этом все таблицы в рамках одной базы данных связаны между собой.
    """
)
st.image("src/database-example.png")
st.write(
    """
    Структура базы данных SQL состоит из шести элементов:
    \n ● Ключ — самый главный столбец, который связывает таблицы данных
    \n Они бывают:
      \n первичными — содержат уникальный идентификатор для каждого объекта

      \n потенциальными — содержат альтернативный идентификатор

      \n внешними — содержат ссылку, которая позволяет связать две таблицы, при этом значения ключей в одной таблице соответствуют первичному ключу в другой
    """
)
st.image("src/database-structure.png")
st.write(
    """
   \n ● Отношение — таблица с данными, представленными в строках и столбцах.

    \n ● Атрибут — столбец, который содержит наименование, тип, цену или другой параметр.

    \n ● Домен — значения, которые допустимы для данного атрибута: например, стоимость в рублях или название кириллическими символами.

    \n ● Кортеж — пронумерованная строка, где содержатся все данные о каком-либо объекте.

    \n ● Значение — содержимое ячейки в таблице.
    """
)


st.markdown("<h5 style='text-align: left; color: black;'>Для чего нужен SQL на конкретном примере</h5>", unsafe_allow_html=True)
st.write(
    """
    Представьте таблицу с информацией о студентах: имена, возраст, предмет обучения и так далее. В ней есть определённое количество строк и столбцов. Один из рядов содержит успеваемость студентов.

    Как только все данные будут внесены в таблицу, каждая из записей попадает в разные категории (столбцы или «атрибуты»). Это и есть организованная база данных. Вся организованная внутри неё информация, которой можно управлять, называется Database Schema (схема данных).

    Если вы захотите выдать стипендии учащимся, которые получают оценку 90% или выше, то выполняется запрос данных в SQL, что простыми словами значит «попросить базу данных предоставить информацию о студентах, получающих 90% и более баллов».

    Команда будет иметь синтаксический вид:
    """
)
st.write("""**SELECT * FROM Student WHERE Percentage >= 90**""")

st.write(
    """
    Когда количество данных мало (скажем, 10 студентов), то можно всё легко посчитать и написать на клочке бумаге. Но когда объём данных увеличивается до тысяч записей, становится нужен SQL — он помогает управлять огромными данными эффективно, то есть быстро получать расчёты на их основе.
    """
)

st.markdown("<h5 style='text-align: left; color: black;'>Кому нужен SQL</h5>", unsafe_allow_html=True)
st.write(
    """
    1. Аналитики и продуктовые маркетологи. Знание SQL помогает этим специалистам не зависеть от программистов, а самостоятельно получать и обрабатывать данные.
     
    2. Разработчики и тестировщики. С помощью SQL они могут самостоятельно проектировать базы для быстрой и надежной работы с данными, улучшать с их помощью сайты и приложения.
     
    3. Руководители и менеджеры. SQL позволит специалистам на руководящих постах самостоятельно обращаться к базам, контролировать работу компании и в реальном времени получать данные о положении дел.
    
    """
)

st.write('''\n##### **А если у меня другой профиль?**
    \nВо-первых, всегда полезно знать о современных технологиях, которые применяются во множестве профессиональных областей. 
    \nВо-вторых, в ходе выполнения работы вы ознакомитесь с примером решения широко распространенной бизнес-задачи.
    А для того, чтобы разработать и внедрить в деятельность организации такое решение, требуется вовлечение в команду специалистов разного уровня и разных ролей: как IT-специальностей, так и других профилей.
    ''')
with st.expander('Роли в проекте для специалистов различных сфер:'):
    st.write('''
        \n 1. Проанализировать текущее состояние бизнес-процессов, оценить риски и участвовать в промежуточных результатах могли бы:
        \n\t * Аналитик-международник (международный аналитик)
        \n\t * Политолог, политический аналитик
        \n\t * Политтехнолог
        \n\t * Менеджер по связям с общественностью (PR)
        \n\t * Финансовый менеджер
        \n\t * GR-менеджер
        \n\t * Руководитель по цифровой трансформации (CDO – Chief Digital Officer)
        \n\t * Development manager (менеджер по развитию)
        \n\t * Digital-стратег

        \n 2. Управлять проектом, организовывать и развивать его могут:
        \n\t * Директор по данным, Chief Data Officer (CDO)
        \n\t * Менеджер проекта
        ''')

with st.expander('Роли в проекте для IT-специалистов:'):
    st.write('''
        \n 1. Собрать, подготовить и обработать данные для проекта могли бы:
        \n\t * Аналитик данных (Data Analyst)
        \n\t * Data Mining Specialist: специалист по интеллектуальной обработке данных
        \n\t * Data Scientist: учёный по данным, исследователь данных
        \n\t * Big Data Analyst: специалист по анализу больших данных

        \n 2. Разработать серверную инфраструктуру, размещение данных и всей схемы решения, обеспечить безопасность на техническом уровне, обеспечить доступ пользователей к проекту могли бы:
        \n\t * DevOps (на данный момент нет в учебном процессе РАНХиГС)
        \n\t * MLOps (на данный момент нет в учебном процессе РАНХиГС)

        ''')

st.markdown("<h5 style='text-align: left; color: black;'>SQL-операторы</h5>", unsafe_allow_html=True)
st.write(
    """
    \n Работать с данными помогают операторы — определенные слова или символы, которые используются для выполнения конкретной операции — например, для выбора из множества по конкретному параметру. Если нам нужно из всех видов пиццы отсортировать те, в которых есть пармезан, — нужно использовать оператор SELECT (выбор в соответствии с условием).
    \n Операторы в SQL делятся на несколько групп в соответствии с задачами, которые они решают.
    \n Операторы отвечающие за создание и редактирование таблицы:
    \n ● CREATE — создание объекта в базе данных
    \n ● ALTER — изменение объекта
    \n ● DROP — удаление объекта
    \n Операторы отвечающие за манипуляции с данными:
    \n ● SELECT — выбор данных в соответствии с условием
    \n ● WHERE — фильтрация данных
    \n ● GROUP BY — группировка данных
    \n ● HAVING — фильтрация сгруппированных данных
    \n ● ORDER BY — сортировка данных. При этом можно сортировать данные как в порядке возрастания (ASC) или убывания (DESC)
    """
)
st.write("""При осуществлении группировки данных можно воспользоваться специальными агрегирующими функциями. 
Агрегирующие функции выполняют конкретные действия со строками таблиц.

Допустим, вы каждый год запускаете сбор денег на какие-то нужды. У вас есть база жертвователей, где хранятся их имена, адреса электронной почты и перечисленные суммы (по годам).""")

st.image("src/agregation-function.png")

st.write("""При помощи функции COUNT вы можете определить, сколько всего пожертвований было сделано. А при помощи SUM можно вычислить общую сумму денег, которую удалось собрать в этом году.""")
st.write("""Чтобы получить это значение для нашей таблицы с пожертвованиями, нужно запустить запрос: SELECT COUNT(*) FROM donors""")

st.write("""Вот полный список агрегирующих функций:
\n ● COUNT — возвращает количество строк
\n ● SUM — суммирует числовые значения
\n ● MIN — поиск минимального значения
\n ● MAX — поиск максимального значения
\n ● AVG — вычисляет среднее значение в указанном столбце""")
st.write("""Существует строгий порядок выполнения SQL-операторов отвечающих за манипуляцию с данными. Вот универсальная шпаргалка по очередности выполнения операций в SQL-запросах:
\n 1. FROM (выбор таблицы)
\n 2. WHERE (фильтрация строк)
\n 3. GROUP BY (агрегирование данных)
\n 4. HAVING (фильтрация агрегированных данных)
\n 5. SELECT (возврат результирующего датасета)
\n 6. ORDER BY (сортировка).
""")

st.markdown("<h5 style='text-align: left; color: black;'>Разберем применение SQL операторов на примерах</h5>", unsafe_allow_html=True)
st.write("""Предположим, что у нас есть таблица, которая называется users, со следующей информацией""")
st.image("src/table-example.png")
st.write("""Выполняем поиск пользователей, которые работают:""")
st.write("""**SELECT * FROM users WHERE Статус >= Работает**""")
st.write("""Результат:""")
st.image("src/table-where-example.png")
st.write("""Теперь давайте найдем всех пользователей из Москвы старше 22 лет""")
st.write("""Для этого необходимо выполнить команду:""")
st.write("""**SELECT * FROM users WHERE Город = Москва AND Возраст > 22**""")
st.write("""Результат:""")
st.image("src/table-logistic-operator-example.png")
st.write("""Здесь мы с вами впервые встречаемся с таким понятием как логические операторы.""")
st.write("""
    \n Логические операторы используются для проверки истинности условия. Логический оператор возвращает логическое значение TRUE или  FALSE. В SQL существует три логических оператора:
    \n ● AND - логическое И
    \n ● OR - логическое ИЛИ
    \n ● NOT - логическое НЕ
""")
st.write("""При этом очень важно не забывать и про их приоритеты. Самый высокий приоритет, среди логических операторов,
 у оператора NOT, за ним следует оператор AND и наименьший приоритетом обладает оператор OR""")

st.markdown("<h5 style='text-align: center; color: black;'>Задание для лабораторной работы</h5>", unsafe_allow_html=True)

right_answers = 0

task0 = st.selectbox("1. Что такое первичный ключ", ["", "Самый главный столбец, который содержит уникальный идентификатор для каждого объекта",
                                                  "Столбец, который содержат альтернативный идентификатор",
                                                  "Самый главный столбец, который содержит идентификатор для каждого объекта"])

if task0 == "Самый главный столбец, который содержит уникальный идентификатор для каждого объекта":
    right_answers += 1

task1 = st.selectbox("2. Выберете верную последовательности выполнения операторов в SQL", ["", "SELECT, FROM, WHERE, ORDER BY", "FROM, WHERE, SELECT, ORDER BY", "SELECT, ORDER BY, WHERE, FROM"])

if task1 == "FROM, WHERE, SELECT, ORDER BY":
    right_answers += 1

task2 = st.selectbox("3. Выберете верную последовательности выполнения логических операторов в SQL", ["", "AND, NOT, OR", "NOT, AND, OR", "Операторы выполняются последовательно слева направо"])

if task2 == "NOT, AND, OR":
    right_answers += 1

task3 = st.selectbox("4. Для чего используется оператор ORDER BY", ["", "Для сортировки данных удовлетворяющих определенному условию",
                                                                 "Для поиска записи по ключу",
                                                                 "Для сортировки данных в порядке возрастания (ASC) или убывания (DESC)"])

if task3 == "5. Для сортировки данных в порядке возрастания (ASC) или убывания (DESC)":
    right_answers += 1

st.write("""\n 5. Выполнится ли следующий запрос:""")
st.image("src/sql-question1.png")
task4 = st.selectbox("", ["",
                          "Да, вернется три поля: order_id, order_code и сумма по полю order_value",
                          "Нет, так как поля order_id и order_code используются без агрегирующих функций",
                          "Нет, так как поле order_code не участвует в группировке"])

if task4 == "Нет, так как поле order_code не участвует в группировке":
    right_answers += 1

st.write("""\n 6. Что вернет следующий запрос к таблице department:""")
st.write("""**SELECT AVG(Зарплата) FROM department GROUP BY Пол HAVING Возраст >= 30**""")
st.image("src/department.png")
task5 = st.selectbox("", ["",
                          "Среднюю зарплату сгруппированную по полу для лиц старше 30 лет",
                          "Среднюю зарплату для лиц старше 30 лет",
                          "Данный запрос не выполнется так как оператор HAVING нелязя использовать с оператором GROUP BY"])

if task5 == "Среднюю зарплату сгруппированную по полу для лиц больше 30 лет":
    right_answers += 1

st.write("""\n 7. Что вернет следующий запрос к таблице report:""")
st.write("""**SELECT AVG(Клик) FROM report GROUP BY Месяц**""")
st.image("src/sql-click-example.png")
task6 = st.selectbox("", ["",
                          "Среднее значение по полю Клик",
                          "0.87",
                          "Помесячный CTR"])

if task6 == "Помесячный CTR":
    right_answers += 1

st.write("""В таблице computers для каждого ПК, указаны модель – model, скорость - speed (процессора в мегагерцах), объем памяти - ram (в мегабайтах), размер диска - hd (в гигабайтах), скорость считывающего устройства - cd (например, '4x') и цена - price (в долларах).""")
st.write("""Найдите номер модели, скорость и размер жесткого диска ПК, имеющих 12x или 24x CD и цену менее 600 дол.""")
first_query = st.text_input("""8. Введите SQL-запрос""")

engine = create_engine('sqlite://', echo=False)
data = pd.read_csv("src/dataset.csv", sep=";")
answer = pd.read_csv("src/dataset_answer.csv", sep=";")
answer_hd = pd.read_csv("src/answer-hd.csv", sep=";")
data.to_sql('computers', con=engine)
if first_query != "":
    try:
        first_query = first_query.lower()
        result = engine.execute(first_query).fetchall()
        if first_query != "select * from computers":
            start = first_query.find("select") + 6
            end = first_query.find("from")
            columns = first_query[start:end].strip().split(",")
            columns = [st.strip() for st in columns]
            result = pd.DataFrame(result, columns=columns)
        else:
            columns = ['id', 'model', 'speed', 'ram', 'hd', 'cd', 'price']
            result = pd.DataFrame(result, columns=columns)
            result = result.set_index('id')
        if (result.equals(answer)):
            st.write("Запрос написан верно", result)
            right_answers += 1
        else:
            st.write('Результат выполнения вашего запроса', result)
            st.write('Результат выполнения правильного запроса', answer)

    except:
        st.write("""Вы ввели некорректный запрос""")

st.write("""Найдите размеры жестких дисков, совпадающих у двух и более ПК. Вывести: HD""")
second_query = st.text_input("""9. Введите  SQL-запрос""")

if second_query != "":
    try:
        second_query = second_query.lower()
        result = engine.execute(second_query).fetchall()
        if second_query != "select * from computers":
            start = second_query.find("select") + 6
            end = second_query.find("from")
            columns = second_query[start:end].strip().split(",")
            columns = [st.strip() for st in columns]
            result = pd.DataFrame(result, columns=columns)
        else:
            columns = ['id', 'model', 'speed', 'ram', 'hd', 'cd', 'price']
            result = pd.DataFrame(result, columns=columns)
            result = result.set_index('id')
        if (result.equals(answer_hd)):
            st.write("Запрос написан верно", result)
            right_answers += 1
        else:
            st.write('Результат выполнения вашего запроса', result)
            st.write('Результат выполнения правильного запроса', answer_hd)
    except:
        st.write("""Вы ввели некорректный запрос""")

if right_answers > 7:
    st.markdown("<h6 style='text-align: center; color: black;'>Лабораторная работа cдана!</h6>", unsafe_allow_html=True)
else:
    st.markdown("<h6 style='text-align: center; color: black;'>Лабораторная работа пока не сдана</h6>", unsafe_allow_html=True)
