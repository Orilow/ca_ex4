# ca_ex4

Combinatory algorithms, ex 4

Prim's algorithm.

Построить минимальны остов связного неориентированного взвешенного графа.

Метод решения: алгоритм Ярника-Прима-Дейкстры.

Файл входных файлов:
- Граф, заданный массивом смежности.
- N - число элементов в массиве. Далее построчно расположен массив смежности
(не более 10 чисел в одной строке). Последний элемент массива равен 32767.

Пример входа:
```
22
6 10 14 20 22 2 25 3 4 1
25 3 0 1 4 2 0 4 7 3 
7 32767
```

Файл выхода:

Остов, заданный списками смежностей. Внутри каждого списка
упорядочить вершины по возрастанию номеров. В последней строке записать вес остова.