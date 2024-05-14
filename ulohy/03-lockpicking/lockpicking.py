print("#1 Absolutně neoptimalizované crazy řešení:")
pocet_validnich_kombinaci = 0
pocet_vsech_prochazenych_kombinaci = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a < b and b < c and c < d and a + b + c + d == 13:
                    print(f"{a}{b}{c}{d}", end=", ")
                    pocet_validnich_kombinaci += 1
                pocet_vsech_prochazenych_kombinaci += 1
print(
    f"\n{pocet_validnich_kombinaci} (validni) / {pocet_vsech_prochazenych_kombinaci} (všechny)"
)
print("-----------")

print(
    "#2 Zde již procházíme čísla do 1999, protože víme, že první cifra nemůže být větší než 1:"
)
pocet_validnich_kombinaci = 0
pocet_vsech_prochazenych_kombinaci = 0
for a in range(2):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                if a < b and b < c and c < d and a + b + c + d == 13:
                    print(f"{a}{b}{c}{d}", end=", ")
                    pocet_validnich_kombinaci += 1
                pocet_vsech_prochazenych_kombinaci += 1
print(
    f"\n{pocet_validnich_kombinaci} (validni) / {pocet_vsech_prochazenych_kombinaci} (všechny)"
)
print("-----------")

print("#3 Zde si optimalizujeme i minima dalších cifer:")
pocet_validnich_kombinaci = 0
pocet_vsech_prochazenych_kombinaci = 0
for a in range(0, 2):
    for b in range(1, 10):
        for c in range(2, 10):
            for d in range(3, 10):
                if a < b and b < c and c < d and a + b + c + d == 13:
                    print(f"{a}{b}{c}{d}", end=", ")
                    pocet_validnich_kombinaci += 1
                pocet_vsech_prochazenych_kombinaci += 1
print(
    f"\n{pocet_validnich_kombinaci} (validni) / {pocet_vsech_prochazenych_kombinaci} (všechny)"
)
print("-----------")

print("#4 Zde si optimalizujeme minima i maxima cifer:")
pocet_validnich_kombinaci = 0
pocet_vsech_prochazenych_kombinaci = 0
for a in range(0, 2):
    for b in range(1, 4):
        for c in range(2, 6):
            for d in range(3, 10):
                if a < b and b < c and c < d and a + b + c + d == 13:
                    print(f"{a}{b}{c}{d}", end=", ")
                    pocet_validnich_kombinaci += 1
                pocet_vsech_prochazenych_kombinaci += 1
print(
    f"\n{pocet_validnich_kombinaci} (validni) / {pocet_vsech_prochazenych_kombinaci} (všechny)"
)
print("-----------")


print(
    "#5 Po hlubší analýze zjištujeme lépe závyslosti cifer a také optimalizujeme podmínku:"
)
pocet_validnich_kombinaci = 0
pocet_vsech_prochazenych_kombinaci = 0
for a in range(0, 2):
    for b in range(a + 1, 4):
        for c in range(b + 1, 6):
            for d in range(c + 1, 10):
                if a + b + c + d == 13:
                    print(f"{a}{b}{c}{d}", end=", ")
                    pocet_validnich_kombinaci += 1
                pocet_vsech_prochazenych_kombinaci += 1
print(
    f"\n{pocet_validnich_kombinaci} (validni) / {pocet_vsech_prochazenych_kombinaci} (všechny)"
)
