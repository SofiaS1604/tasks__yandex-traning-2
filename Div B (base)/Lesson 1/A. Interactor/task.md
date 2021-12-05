<h1>A. Interactor</h1>

<table>
   <tr>
    <td>Ограничение времени</td>
    <td>1 секунда</td>
   </tr>
   <tr>
    <td>Ограничение памяти</td>
    <td>64Mb</td>
  </tr>
   <tr>
    <td>Ввод</td>
    <td>стандартный ввод или input.txt</td>
  </tr>
   <tr>
    <td>Вывод</td>
    <td>стандартный вывод или output.txt</td>
  </tr>
 </table>

Лена руководит разработкой тестирующей системы, в которой реализованы интерактивные задачи.
До заверщения очередной стадии проекта осталось написать модуль, определяющий итоговый вердикт системы для интерактивной задачи. Итоговый вердикт определяется из кода завершения задачи, вердикта интерактора и вердикта чекера по следующим правилам:
<ul>

<li> Вердикт чекера и вердикт интерактора — это целые числа от 0 до 7 включительно. </li>

<li> Код завершения задачи — это целое число от -128 до 127 включительно. </li>

<li>Если интерактор выдал вердикт 0, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и вердикту чекера в противном случае. </li>

<li>Если интерактор выдал вердикт 1, итоговый вердикт равен вердикту чекера. </li>

<li>Если интерактор выдал вердикт 4, итоговый вердикт равен 3 в случае, если программа завершилась с ненулевым кодом, и 4 в противном случае. </li>

<li>Если интерактор выдал вердикт 6, итоговый вердикт равен 0. </li>

<li>Если интерактор выдал вердикт 7, итоговый вердикт равен 1. </li>

<li> В остальных случаях итоговый вердикт равен вердикту интерактора. </li>

</ul>

Ваша задача — реализовать этот модуль.

### Формат ввода
Первая строка входного файла содержит два целых числа t<sub>room</sub>, и t<sub>cond</sub>, разделенных ровно одним пробелом (–50 ≤ t<sub>room</sub> ≤ 50, –50 ≤ t<sub>cond</sub> ≤ 50).

Вторая строка содержит одно слово, записанное строчными буквами латинского алфавита — режим работы кондиционера.

Входной файл состоит из трёх строк. В первой задано целое число r (−128 ≤ r ≤ 127) — код завершения задачи, во второй — целое число 
i (0 ≤ i ≤7) — вердикт интерактора, в третьей — целое число c (0 ≤ c ≤7) — вердикт чекера.

### Формат вывода
Выведите одно целое число от 0 до 7 включительно — итоговый вердикт системы.

<table>
   <tr>
    <th>Ввод</th>
    <th>Вывод</th>
   </tr>
   <tr>
    <td>0 <br> 0 <br> 0 </td>
    <td>0</td>
  </tr>
   <tr>
    <td>-1 <br> 0 <br> 1 <br></td>
    <td>3</td>
  </tr>
   <tr>
    <td>42 <br> 1 <br> 6 <br></td>
    <td>6</td>
  </tr>
   <tr>
    <td> 44 <br> 7 <br> 4 <br></td>
    <td>1</td>
  </tr>
   <tr>
    <td> 1 <br> 4 <br> 0 <br></td>
    <td>3</td>
  </tr>
   <tr>
    <td>-3 <br> 2 <br> 4 <br></td>
    <td>2</td>
  </tr>
 </table>
 