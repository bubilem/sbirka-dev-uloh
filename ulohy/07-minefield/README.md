# Minové pole

Jedná se o minové pole pro legendární logickou hru **Hledání min** (Minesweeper). V poli je daný počet min, kolem kterých jsou neminová pole ohodnocena tak, že číslo v nich udává počet min, se kterými přímo sousedí. Neminové pole tak může přímo sousedit maximálně s 8 minami.

## Ukázka minového pole 5x5 se 4 minami.

```
2M200
2M200
34200
MM100
22100
```

## Zadání

Napište funkci `generate_field`, která bude generovat minové pole dané velikosti `width x height` s určeným počtem min `mines` na náhodných pozicích. Také vytvořte funkci `mine_field`, která pole do textové konzole vypíše.

## Zdroje

- [Wiki - Hledání min
  ](https://cs.wikipedia.org/wiki/Hled%C3%A1n%C3%AD_min)
