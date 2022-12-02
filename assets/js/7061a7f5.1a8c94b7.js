"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[935],{3543:n=>{n.exports=JSON.parse('{"blogPosts":[{"id":"/02.09.2022","metadata":{"permalink":"/EF-Informatik/02.09.2022","editUrl":"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/02.09.2022.md","source":"@site/blog/02.09.2022.md","title":"02.09.2022 report","description":"Today we were programming with the help of lists. The exercices were easy except for the prime number exercice. I only didn\'t think long enough.","date":"2022-12-02T14:43:46.000Z","formattedDate":"2. Dezember 2022","tags":[],"readingTime":0.985,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"nextItem":{"title":"26.08.2022 report","permalink":"/EF-Informatik/26.08.2022"}},"content":"Today we were programming with the help of lists. The exercices were easy except for the prime number exercice. I only didn\'t think long enough. \\n\\nThe solution for the listen word riddle 2 exercice is:\\n\\n![](r_1798534_nBE8D.jpg)\\n\\n\\n\\n### Prime number exercice\\nThe problem was that with the code below, the number is divided by another number and the rest isn\'t an integer once then it\'s an prime number. That\'s false! \\n\\n\\n\\n```py\\n# !!! Code funktioniert nicht !!!\\n\\nzahlen = []\\nprimzahlen = []\\n\\nfor counter in range(2, 101):\\n    zahlen.append(counter)\\n\\nfor zahl in zahlen:\\n    for primzahl in primzahlen:\\n        if zahl % primzahl != 0:\\n            primzahlen.append(zahl)\\n\\nprint(primzahlen)\\n```\\n\\n\\nMy solution was to create a boolean variable that is initiated as true. If the number divided by the prime number has no rest once, the bool is set to false. After the number was divided by all prime numbers the code checks if the bool is still true.\\n\\n```py\\nzahlen = []\\nprimzahlen = []\\nprimzahl_bool = True\\n\\nfor counter in range(2, 101):\\n    zahlen.append(counter)\\n\\n\\nfor zahl in zahlen:\\n    for primzahl in primzahlen:\\n        if zahl % primzahl == 0:\\n            primzahl_bool = False\\n\\n    if primzahl_bool == True:\\n        primzahlen.append(zahl)\\n    primzahl_bool = True\\n\\nprint(primzahlen)\\n\\n```"},{"id":"/26.08.2022","metadata":{"permalink":"/EF-Informatik/26.08.2022","editUrl":"https://github.com/GabrielMariethoz/EF-Informatik/tree/main/blog/26.08.2022.md","source":"@site/blog/26.08.2022.md","title":"26.08.2022 report","description":"Today I have programmed a hexagone with a Koch curve. Under this text you find a video of the output and under it the code in Python with Turtle.","date":"2022-12-02T14:43:46.000Z","formattedDate":"2. Dezember 2022","tags":[],"readingTime":0.51,"hasTruncateMarker":false,"authors":[],"frontMatter":{},"prevItem":{"title":"02.09.2022 report","permalink":"/EF-Informatik/02.09.2022"}},"content":"Today I have programmed a hexagone with a Koch curve. Under this text you find a video of the output and under it the code in Python with Turtle.\\n\\nhttps://user-images.githubusercontent.com/111580143/186967972-8a94ad51-1318-4fb2-a23e-069a937bf796.mp4\\n\\n\x3c!-- \\n<video width=\\"320\\" height=\\"240\\" controls>\\n  <source src=\\"Turtle_koch_kurve.mp4\\">\\n</video>\\n\\n<br><br/>\\n--\x3e\\n\\n```py\\nfrom turtle import *\\n\\ndef mini():\\n    forward(5)\\n    left(60)\\n    forward(5)\\n    right(120)\\n    forward(5)\\n    left(60)\\n    \\ndef normal():\\n    forward(5)\\n    left(60)\\n    mini()\\n    forward(5)\\n    right(120)\\n    mini()\\n    forward(5)\\n    left(60)\\n\\ndef normal_ohni_forward():\\n    left(60)\\n    mini()\\n    forward(5)\\n    right(120)\\n    mini()\\n    forward(5)\\n    left(60)\\n\\ndef maxi():\\n    mini()\\n    normal()\\n    mini()\\n    forward(5)\\n    left(60)\\n    mini()\\n    normal()\\n    right(60)\\n    normal_ohni_forward()\\n    right(60)\\n    normal_ohni_forward()\\n    mini()\\n    forward(5)\\n    left(60)\\n    mini()\\n    normal()\\n    mini()\\n    right(60)\\n\\n\\npenup()\\ngoto(0, 100)\\npendown()\\nfor counter in range(6):\\n    maxi()\\n    \\n```"}]}')}}]);