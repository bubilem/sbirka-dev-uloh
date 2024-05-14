<?php
function fibrek($n)
{
    return $n <= 1 ? $n : fibrek($n - 1) + fibrek($n - 2);
}

function fib($n)
{
    if ($n <= 1) {
        return $n;
    }
    $prev = 0;
    $fib = 1;
    for ($i = 2; $i <= $n; $i++) {
        $new_fib = $fib + $prev;
        $prev = $fib;
        $fib = $new_fib;
    }
    return $fib;
}

$n = 35;
echo "Nerekurzivní řešení: ", fib($n), "\n";
echo "Rekurzivní řešení  : ", fibrek($n), "\n";


