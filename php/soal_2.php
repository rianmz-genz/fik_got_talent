<?php

function checkValidString($s)
{
    $s = str_split($s);

    $alphabet = range('a', 'z');

    $arr = [];
    for ($i = 0; $i < count($alphabet); $i++) {
        $arr[$alphabet[$i]] = 0;
    }
    // var_dump($arr);

    for ($i = 0; $i < count($s); $i++) {
        foreach ($alphabet as $key => $value) {
            if ($s[$i] == $value) {
                $arr[$value] += 1;
            }
        }
    }
    // var_dump($arr);

    $alphabetFilled = array_filter($arr, fn ($v) => $v > 0);
    // var_dump($alphabetFilled);

    $allValueEqual = true;
    $keys = array_keys($alphabetFilled);
    for ($i = 0; $i < count($keys) - 1; $i++) {
        $current = $alphabetFilled[$keys[$i]];
        $next = $alphabetFilled[$keys[$i + 1]];
        if ($current != $next) {
            $allValueEqual = false;
            break;
        }
    }
    if ($allValueEqual) return "YES";

    $freqTypes = array_unique($alphabetFilled);

    if (count($freqTypes) > 2) return "NO";

    $result = [];
    foreach ($freqTypes as $key => $value) {
        $result[] = array_filter($alphabetFilled, function ($v) use ($value) {
            return $value == $v;
        });
    }

    // var_dump($result);

    $x = $result[0];
    $y = $result[1];

    $a = true;
    foreach ($x as $key => $value) {
        if ($value > 2) $a = false;
    }

    $b = true;
    foreach ($y as $key => $value) {
        if ($value > 2) $b = false;
    }

    if ((count($x) == 1 && $a) || (count($y) == 1 && $b)) {
        return "YES";
    }

    foreach ($x as $key => $value) {
        if ($value == 3 && count($x) == 1) return "YES";
    }

    $b = true;
    foreach ($y as $key => $value) {
        if ($value == 3 && count($y) == 1) return "YES";
    }

    return "NO";
}   

$tests = [
    [
        "input" => "aabbc",
        "expected" => "YES",
    ],
    [
        "input" => "ababd",
        "expected" => "YES",
    ],
    [
        "input" => "abccdd",
        "expected" => "NO",
    ]
];

foreach ($tests as $key => $test) {
    $result = checkValidString($test['input']);
    if ($result == $test["expected"]) {
        echo $key . ": Benar" . PHP_EOL ;
    } else {
        echo $key . ": Salah expected:" . $test["expected"] . " but, result:" . $result . PHP_EOL ;
    }
}


