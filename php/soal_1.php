<?php

function encryptString($cheap)
{
    $uppered = strtoupper($cheap);

    $arr = str_split($uppered);

    $encrypted = "";

    // echo ord("M") . PHP_EOL; // 77
    // echo ord("N") . PHP_EOL; // 78
    // echo chr("78") . PHP_EOL; // 78

    foreach ($arr as $key => $value) {
        // echo $value . PHP_EOL;
        $codeBefore = ord($value);
        $codeAfter = $codeBefore + 13;
        $sisa = $codeAfter - 90;

        if ($value != " ") {
            $charAfter = "";
            if ($sisa > 0) {
                $charAfter = chr(64 + $sisa);
            } else {
                $charAfter = chr($codeAfter);
            }

            $encrypted = $encrypted . $charAfter;
        } else {
            $encrypted = $encrypted . " ";
        }
    }

    return $encrypted;
}

function descryptString($encrypted)
{

    $arr = str_split($encrypted);

    $cheapText = "";

    // echo ord("M") . PHP_EOL; // 77
    // echo ord("N") . PHP_EOL; // 78
    // echo chr("78") . PHP_EOL; // 78

    foreach ($arr as $key => $value) {
        // echo $value . PHP_EOL;
        $codeBefore = ord($value);
        $codeAfter = $codeBefore + 13;
        $sisa = $codeAfter - 90;

        if ($value != " ") {
            $charAfter = "";
            if ($sisa > 0) {
                $charAfter = chr(64 + $sisa);
            } else {
                $charAfter = chr($codeAfter);
            }

            $cheapText = $cheapText . $charAfter;
        } else {
            $cheapText = $cheapText . " ";
        }
    }

    return $cheapText;
}

$result = encryptString("aku suka makan");
echo $result . PHP_EOL;

$result = descryptString($result);
echo $result . PHP_EOL;
