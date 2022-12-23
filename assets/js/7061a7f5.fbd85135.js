"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[935],{3543:e=>{e.exports=JSON.parse('{"blogPosts":[{"id":"/02.09.2022","metadata":{"permalink":"/EF-Informatik/02.09.2022","editUrl":"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/02.09.2022.md","source":"@site/blog/02.09.2022.md","title":"02.09.2022 report","description":"Today we were programming with the help of lists. The exercices were easy except for the prime number exercice. I only didn\'t think long enough.","date":"2022-12-23T15:14:01.000Z","formattedDate":"23. Dezember 2022","tags":[],"readingTime":0.985,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"nextItem":{"title":"02.12.2022-arbeiten-an-numtrip","permalink":"/EF-Informatik/02.12.2022-arbeiten-an-numtrip"}},"content":"Today we were programming with the help of lists. The exercices were easy except for the prime number exercice. I only didn\'t think long enough. \\n\\nThe solution for the listen word riddle 2 exercice is:\\n\\n![](r_1798534_nBE8D.jpg)\\n\\n\\n\\n### Prime number exercice\\nThe problem was that with the code below, the number is divided by another number and the rest isn\'t an integer once then it\'s an prime number. That\'s false! \\n\\n\\n\\n```py\\n# !!! Code funktioniert nicht !!!\\n\\nzahlen = []\\nprimzahlen = []\\n\\nfor counter in range(2, 101):\\n    zahlen.append(counter)\\n\\nfor zahl in zahlen:\\n    for primzahl in primzahlen:\\n        if zahl % primzahl != 0:\\n            primzahlen.append(zahl)\\n\\nprint(primzahlen)\\n```\\n\\n\\nMy solution was to create a boolean variable that is initiated as true. If the number divided by the prime number has no rest once, the bool is set to false. After the number was divided by all prime numbers the code checks if the bool is still true.\\n\\n```py\\nzahlen = []\\nprimzahlen = []\\nprimzahl_bool = True\\n\\nfor counter in range(2, 101):\\n    zahlen.append(counter)\\n\\n\\nfor zahl in zahlen:\\n    for primzahl in primzahlen:\\n        if zahl % primzahl == 0:\\n            primzahl_bool = False\\n\\n    if primzahl_bool == True:\\n        primzahlen.append(zahl)\\n    primzahl_bool = True\\n\\nprint(primzahlen)\\n\\n```"},{"id":"/02.12.2022-arbeiten-an-numtrip","metadata":{"permalink":"/EF-Informatik/02.12.2022-arbeiten-an-numtrip","editUrl":"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/02.12.2022-arbeiten-an-numtrip.md","source":"@site/blog/02.12.2022-arbeiten-an-numtrip.md","title":"02.12.2022-arbeiten-an-numtrip","description":"Zuerst habe ich die Funktion eingabe() so angepasst, dass sie eine Liste zur\xfcckgibt, welche die Position des vom Benutzer eingegebenen Elements der Matrix beinhaltet. In der Funktion habe ich ebenfalls eine neue Variable hinzugef\xfcgt, welche den Wert, der Position, welche der Benutzer eingegeben hat, hat.","date":"2022-12-23T15:14:01.000Z","formattedDate":"23. Dezember 2022","tags":[],"readingTime":0.86,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"prevItem":{"title":"02.09.2022 report","permalink":"/EF-Informatik/02.09.2022"},"nextItem":{"title":"26.08.2022 report","permalink":"/EF-Informatik/26.08.2022"}},"content":"Zuerst habe ich die Funktion eingabe() so angepasst, dass sie eine Liste zur\xfcckgibt, welche die Position des vom Benutzer eingegebenen Elements der Matrix beinhaltet. In der Funktion habe ich ebenfalls eine neue Variable hinzugef\xfcgt, welche den Wert, der Position, welche der Benutzer eingegeben hat, hat.\\n```py\\nself.alter_wert = self.matrix[int(self.feld_eingabe[0]) - 1][int(self.feld_eingabe[1]) - 1]\\nreturn [int(self.feld_eingabe[0]) - 1, int(self.feld_eingabe[1]) - 1]\\n```\\n\\nDanach habe ich eine neue Funktion nachbarsfelder() eingebaut, die pr\xfcft, ob die Nachbarsfelder denselben Wert haben. Da habe ich die Rekursion gebraucht, um die Nachbarsfelder der Nachbarsfelder zu pr\xfcfen. \\n\\n```py\\ndef nachbarsfelder(self, feld: list):\\n\\n    if feld[0] > 0:\\n        if self.matrix[feld[0] - 1][feld[1]] == self.alter_wert:\\n            self.matrix[feld[0] - 1][feld[1]] = 0\\n            self.nachbarsfelder([feld[0] - 1, feld[1]])\\n    if feld[0] < 4:\\n        if self.matrix[feld[0] + 1][feld[1]] == self.alter_wert:\\n            self.matrix[feld[0] + 1][feld[1]] = 0\\n            self.nachbarsfelder([feld[0] + 1, feld[1]])\\n    if feld[1] > 0:\\n        if self.matrix[feld[0]][feld[1] - 1] == self.alter_wert:\\n            self.matrix[feld[0]][feld[1] - 1] = 0\\n            self.nachbarsfelder([feld[0], feld[1] - 1])\\n    if feld[1] < 4:\\n        if self.matrix[feld[0]][feld[1] + 1] == self.alter_wert:\\n            self.matrix[feld[0]][feld[1] + 1] = 0\\n            self.nachbarsfelder([feld[0], feld[1] + 1])\\n```"},{"id":"/26.08.2022","metadata":{"permalink":"/EF-Informatik/26.08.2022","editUrl":"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/26.08.2022.md","source":"@site/blog/26.08.2022.md","title":"26.08.2022 report","description":"Today I have programmed a hexagone with a Koch curve. Under this text you find a video of the output and under it the code in Python with Turtle.","date":"2022-12-23T15:14:01.000Z","formattedDate":"23. Dezember 2022","tags":[],"readingTime":0.51,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"prevItem":{"title":"02.12.2022-arbeiten-an-numtrip","permalink":"/EF-Informatik/02.12.2022-arbeiten-an-numtrip"},"nextItem":{"title":"eingabe","permalink":"/EF-Informatik/eingabe"}},"content":"Today I have programmed a hexagone with a Koch curve. Under this text you find a video of the output and under it the code in Python with Turtle.\\n\\nhttps://user-images.githubusercontent.com/111580143/186967972-8a94ad51-1318-4fb2-a23e-069a937bf796.mp4\\n\\n\x3c!-- \\n<video width=\\"320\\" height=\\"240\\" controls>\\n  <source src=\\"Turtle_koch_kurve.mp4\\">\\n</video>\\n\\n<br><br/>\\n--\x3e\\n\\n```py\\nfrom turtle import *\\n\\ndef mini():\\n    forward(5)\\n    left(60)\\n    forward(5)\\n    right(120)\\n    forward(5)\\n    left(60)\\n    \\ndef normal():\\n    forward(5)\\n    left(60)\\n    mini()\\n    forward(5)\\n    right(120)\\n    mini()\\n    forward(5)\\n    left(60)\\n\\ndef normal_ohni_forward():\\n    left(60)\\n    mini()\\n    forward(5)\\n    right(120)\\n    mini()\\n    forward(5)\\n    left(60)\\n\\ndef maxi():\\n    mini()\\n    normal()\\n    mini()\\n    forward(5)\\n    left(60)\\n    mini()\\n    normal()\\n    right(60)\\n    normal_ohni_forward()\\n    right(60)\\n    normal_ohni_forward()\\n    mini()\\n    forward(5)\\n    left(60)\\n    mini()\\n    normal()\\n    mini()\\n    right(60)\\n\\n\\npenup()\\ngoto(0, 100)\\npendown()\\nfor counter in range(6):\\n    maxi()\\n    \\n```"},{"id":"/eingabe","metadata":{"permalink":"/EF-Informatik/eingabe","editUrl":"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/eingabe.md","source":"@site/blog/eingabe.md","title":"eingabe","description":"Ich habe in der Funktion eingabe() definiert, dass der Wert von der Matrixposition, die eingegeben worden ist, durch 0 ersetzt wird.","date":"2022-12-23T15:14:01.000Z","formattedDate":"23. Dezember 2022","tags":[],"readingTime":0.375,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"prevItem":{"title":"26.08.2022 report","permalink":"/EF-Informatik/26.08.2022"}},"content":"Ich habe in der Funktion eingabe() definiert, dass der Wert von der Matrixposition, die eingegeben worden ist, durch 0 ersetzt wird. \\n```py\\nself.feld_eingabe # Das ist eine Variable mit den zwei Zahlen, welcher der Benutzer eingegeben hat. \\nself.matrix[int(self.feld_eingabe[0]) - 1][int(self.feld_eingabe[1]) - 1] = 0\\n```\\n\\nDanach habe ich in meiner Funktion zahl() definiert, dass wenn die Zahl in der Matrix 0 ist, Leerzeichen hinzugef\xfcgt werden muss\\n```py\\nif zahl_m == 0:\\n    return \\"|     \\"\\n```"}]}')}}]);