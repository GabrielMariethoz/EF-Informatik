Im Code

```py
matrix = []

zeile = [0, 1, 0]
for i in range(3):
    matrix.append(zeile)

print(matrix)

matrix[1][1] = 0 # nur den Wert in Zeile 1 in der Mitte auf 0 Setzen

print(matrix)
```

wird der Output sie vielleicht überraschen:

\
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
\
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]


Das ist so, weil man nur eine Zeile für die ganze Matrix definiert hat. In der Linie, wo man ein Element einer Matrix ändert, wird die Zeile geändert. Da alle Zeilen eine sind, wird alles verändert.