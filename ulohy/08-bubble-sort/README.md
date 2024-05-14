# Bublinkové řazení

Bublinkové řazení (známé pod anglickým jménem bubble sort, česky též řazení záměnou) je implementačně jednoduchý řadicí algoritmus. Algoritmus opakovaně prochází seznam, přičemž porovnává každé dva sousedící prvky, a pokud nejsou ve správném pořadí, prohodí je. Pro praktické účely je neefektivní, využívá se hlavně pro výukové účely či v nenáročných aplikacích.

Algoritmus je univerzální (pracuje na základě porovnávání dvojic prvků), pracuje lokálně (nevyžaduje pomocnou paměť), je stabilní (prvkům se stejným klíčem nemění vzájemnou polohu), patří mezi přirozené řadicí algoritmy (částečně seřazený seznam zpracuje rychleji než neseřazený).

Název vyjadřuje průběh zpracování, při kterém prvky s vyšší hodnotou „probublávají“ na konec seznamu.

Optimalizací algoritmu je detekce prohození prvků v průchodu seznamu. V případě, že algoritmus v průchodu neprohodil žádné dva prvky, tak žádné další prvky již nikdy neprohodí. Tudíž řazení můžeme ukončit s tím, že seznam je seřazen.

## Ukázka postupu řazení

Vstup: 5, 8, 1, 4, 2, 6

| 5   | 8   | 1   | 4   | 2   | 6   |
| --- | --- | --- | --- | --- | --- |
| 5   | 1   | 4   | 2   | 6   | 8   |
| 1   | 4   | 2   | 5   | 6   | 8   |
| 1   | 2   | 4   | 5   | 6   | 8   |

## Zadání

Napište funkci `buble_sort`, která bude řadit pole čísel metodou bubble sort. Na vstupu bude neseřazené pole, na výstupu pak seřazené. Zaměřte se i na optimalizaci algoritmu.

## Zdroje

- [Wiki - Minové pole](https://cs.wikipedia.org/wiki/Bublinkov%C3%A9_%C5%99azen%C3%AD)
