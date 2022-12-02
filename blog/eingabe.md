Ich habe in der Funktion eingabe() definiert, dass der Wert von der Matrixposition, die eingegeben worden ist, durch 0 ersetzt wird. 
```py
self.feld_eingabe # Das ist eine Variable mit den zwei Zahlen, welcher der Benutzer eingegeben hat. 
self.matrix[int(self.feld_eingabe[0]) - 1][int(self.feld_eingabe[1]) - 1] = 0
```

Danach habe ich in meiner Funktion zahl() definiert, dass wenn die Zahl in der Matrix 0 ist, Leerzeichen hinzugefügt werden muss
```py
if zahl_m == 0:
    return "|     "
```