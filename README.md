                                        # Лабораторная работа № 7.

Выполнил студент группы 427
Букеев Михаил Дмитриевич

## Вариант № 12
Решить методом Хойна задачу Коши

<p align="center"><img src="/readd/1.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=44.90601885pt/></p>

с заданной относительной точностью 0.01

## Теоретическая часть

Метод Хойна

Пусть поставлена задача Коши

<p align="center"><img src="/readd/2.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=70.90601885pt/></p>

Для построения приближенного решения в точке x (n+1) сетки ω (n) , разложим в ряд
Тейлора решение в предыдущей точке сетки x (n) по степеням шага h:

<p align="center"><img src="/readd/3.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=70.90601885pt/></p>

и ограничимся учетом первых p членов этого ряда:

<p align="center"><img src="/readd/4.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=70.90601885pt/></p>

Рассмотрим метод Хойна. Он является одним из методов семейства Рунге-Кутты.
Идея этих методов заключается в построении функций ϕ, которые не используют
явно производных функции f(x,y) и, в то же время, “наилучшим образом” прибли-
жают соответствующие отрезки ϕ (p) ряда Тейлора Δ. Если ограничиться членами до
h в кватрате , получим

<p align="center"><img src="/readd/5.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=70.90601885pt/></p>

где c 1 , c 2 , a 2 , b 12 - произвольные постоянные подлежащие определению. Определив
их, разлагая ϕ по степеням h до членов порядка h в квадрате и сравнивая полученное разложе-
ние с рядом Тейлора Δ, придем к системе со свободным параметром, зафиксировав
который получим двукратный метод Рунге-Кутты - метод Хойна:

<p align="center"><img src="/readd/6.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=70.90601885pt/></p>

Точность решения, как и при взятии определенного интеграла контролирова-
лась по правилу Рунге. При решении на каждом шаге вычислялось максималь-
ное отклонение компонент векторов решений Y(n) и Y(n-1)
<p align="center"><img src="/readd/8.png?invert_in_darkmode&sanitize=true" align=middle width=300.2915617pt height=40.90601885pt/></p>
и если оно превосходило наперед заданную постоянную ε, программа вдвое увеличивала число точек разбиения сетки ω (n) и переходила к
следующей итерации цикла.


## Практическая часть
В программе используются две функции

double F(double x, double y)

double dF(double x)

Программа выводит значение x и y которые являются решением задачи Коши

### Результаты
В результате работы программы была решена задача коши метдом Хойна <p align="center"><img src="/readd/1.png?invert_in_darkmode&sanitize=true" align=middle width=386.2915617pt height=44.90601885pt/></p>

Ниже приведены рисунки

<p align="center"><img src="/readd/gr2.jpg?invert_in_darkmode&sanitize=true" align=middle width=886.2915617pt height=500.90601885pt/></p>

<p align="center"><img src="/readd/gr3.jpg?invert_in_darkmode&sanitize=true" align=middle width=886.2915617pt height=500.90601885pt/></p>
