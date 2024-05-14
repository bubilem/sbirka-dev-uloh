# Přenosová doba v síti

## Definice

Mějme počítačovou síť, která má danou stabilní rychlost. Tato rychlost se jednotně udává v Mbps (Mb/s, milión bitů za sekundu). Určuje nám tedy, kolik miliónů bitů se přenese za jednu sekundu.

Také mějme soubor se zadanou velikostí. Velikost souboru se může zadat pomocí jednotek B, KiB, MiB nebo GiB. Kde: 1 KiB = 1024 B, 1 MiB = 1024 KiB, 1GiB = 1024 B. Nezapoměňte také na rozdíl jednotek B (byte) a b (bit), kde platí 1 B = 8 b.

nápověda: _Vzpoměňte si na vzoreček z fyziky ze ZŠ: v = s / t._

## Zadání

Napište funkci `transfer_time`, která spočítá dobu, za kterou se zadaý soubor přenese po zadané síti. Na vstupu funkce bude soubor a rychlost sítě. Soubor je zadán jako slovník např: `file = {"size": 80, "unit": "KiB"}`, kde se jedná o soubor 80 KiB. Rychlost sítě je v MiB.

K problematice naimplementujte nějaké hezké lidské zobrazování času. Tedy například pro čas `0.00002347 s` by se mohl zobrazovat jako `23.47 microsecond`.

## Výsledek ke kontrole

Pro soubor `80 KiB` nám náš program vypíše `6.554 miliseconds`.
