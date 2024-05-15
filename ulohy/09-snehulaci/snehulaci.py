import math

h = 3000
pata_spicka = 5000
celkovy_cas = 0
celkovy_pocet_snehulaku = 0
# fi je vrcholový úhel pravoúhlého trojúhelníku tvořícího 2D profil půl-kužele hory.
fi = math.acos(h / pata_spicka)
# print(fi / math.pi * 180)
for actual_h in range(0, 3000, 100):
    # poloměr na vrstevnici
    r = math.tan(fi) * (h - actual_h)
    # obvod vrstevnice
    o = round(2 * math.pi * r, 2)
    pocet_snehulaku_na_vrstevnici = int(o // 100)
    celkovy_pocet_snehulaku += pocet_snehulaku_na_vrstevnici
    celkovy_cas += pocet_snehulaku_na_vrstevnici * 30 + 60

# ještě připočtu sněhuláka, který stojí přímo na špičce hory
celkovy_pocet_snehulaku += 1
# k tomu adekvátně čas a také poslední zasloužený odpočinek s výhledem na sněhuláky
celkovy_cas += 30 + 60

print(f"Celkový počet sněhuláků: {celkovy_pocet_snehulaku}")
print(f"Celkový čas: {celkovy_cas/(60*24):.1f} dnů")
