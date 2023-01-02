import time

zahlen = []
primzahlen = [2]
MAX_ZAHL = 1000000
zeit = time.time()

for counter in range(3, MAX_ZAHL + 1):
    primzahl_bool = True
    zahl = 0

    while zahl < len(primzahlen) and primzahl_bool:
        if counter % primzahlen[zahl] == 0:
            primzahl_bool = False
        zahl = zahl + 1

    if primzahl_bool:
        primzahlen.append(counter)


print(primzahlen)
print(time.time() - zeit)
