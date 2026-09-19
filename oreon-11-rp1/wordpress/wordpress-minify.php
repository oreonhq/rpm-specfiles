<?php
require '/usr/share/php/Patchwork/autoload-jsqueeze.php';

$in = file_get_contents($_SERVER['argv'][1]);
if (!$in) exit(1);
$jsqueeze = new \Patchwork\JSqueeze();
$out = $jsqueeze->squeeze($in);
if ($out) {
    printf("+ minify from %s to %s: %2d%% of %6d\n", 
        basename($_SERVER['argv'][1]), basename($_SERVER['argv'][2]),
        round(strlen($out)*100/strlen($in)), strlen($in));
    file_put_contents($_SERVER['argv'][2], $out);
} else {
    exit(2);
}

