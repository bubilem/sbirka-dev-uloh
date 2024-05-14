# Pascalův trojúhelník

Pascalův trojúhelník je geometrické uspořádání binomických koeficientů do tvaru trojúhelníku. Každý prvek se dá vypočítat jako hodnota kombinačního čísla `n nad k`, kde n je řádek a k je pořadí prvku na řádku v trojúhelníku viz. zdroje.

## Zadání

Vytvořte funkci `pascal_triangle`, který bude mít na vstupu jedno číslo `h`, které bude udávat výšku (počet pater) trojúhelníku. Tato funkce bude v textové podobě vypisovat Pascalův trojúhelník.

## Příklad pro h = 5

```
    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
```

Každý prvek v trojúhelníku je dán součtem jeho přímých dvou sousedů nad ním.

## Zdroje

- [Wiki - Pascalův trojúhelník](https://cs.wikipedia.org/wiki/Pascal%C5%AFv_troj%C3%BAheln%C3%ADk)
- [Wiki - Kombinační číslo
  ](https://cs.wikipedia.org/wiki/Kombina%C4%8Dn%C3%AD_%C4%8D%C3%ADslo)
