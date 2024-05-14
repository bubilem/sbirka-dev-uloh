<?php

function pascal_triangle(int $h): void
{
    for ($i = 1; $i <= $h; $i++) {
        echo str_repeat('  ', $h - $i);
        for ($j = 1; $j <= $i; $j++) {
            echo sprintf('%03d ', n_over_k($i - 1, $j - 1));
        }
        echo PHP_EOL;
    }
}

function fact(int $n): int
{
    if ($n <= 1) {
        return 1;
    }
    $fact = 1;
    for ($i = 2; $i <= $n; $i++) {
        $fact *= $i;
    }
    return $fact;
}

function n_over_k(int $n, int $k): int
{
    if ($n >= $k && $k >= 0) {
        return fact($n) / (fact($k) * fact($n - $k));
    }
    return 0;
}

pascal_triangle(10);