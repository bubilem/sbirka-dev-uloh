# Lámání zámku

## Story

Mějme Pepu a Frantu. Pepa má kufřík s číselným zámkem a Frantu moc zajímá, co je v kufříku. Pepa mu to ale nechce rovnou říci, chce Frantu potrápit a tak mu kufřík dá, ať si na heslo přijde a do kufříku se podívá.

Franta si hned spočítá, že pokud jsou na zámku 4 cifry a každá má deset možností (0-9), tak je celkem 10.000 kombinací, což by jednak bylo na dlouho to vše vyzkoušet. Navíc se zámek po třech pokusech na hodinu zamkne. Při maximální smůle to může trvat klidně i 139 dní.

Franta se ale nevzdává. Ví, že Pepa má rád číslo 13 a také čísla vzestpuná. Počítá s tím, že i heslo bude vzestupné číslo, tedy cifry se budou postupně zvětšovat a jejich součet bude 13.

Kolik je takových řešení? Stihne Franta najít všechny odpovídající kombinace a za odpoledne je vyzkoušet a kufr otevřít?

## Zadání

Napište program, který vygeneruje všechny validní kombinace zámku, které splňují následující podmínky:

- `a < b` a `b < c` a `c < d`, tedy levé cifry jsou vždy menší než pravé cifry mezi všemi sousedy.
- `a + b + c + d = 13`, tedy součet cifer je rovný číslu 13.

kde:

- `a` jsou desetitisíce
- `b` jsou tisíce
- `c` jsou desítky
- `d` jsou jednotky

Optimalizujte program tak, aby nemusel procházet všech 10.000 kombinací. Zamyslete se například, jaké jsou možnosti pro jednotlivé cifry. Může mít například cifra `a` hodnotu `8`? Zkuste program vyřešit několika způsoby.
