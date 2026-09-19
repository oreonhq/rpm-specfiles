<?php

/**
 * Autoloader for phpseclib/phpseclib.
 */
require_once "/usr/share/php/Fedora/Autoloader/autoload.php";

// composer.json: "autoload": { "files": [ "phpseclib/bootstrap.php" ], "psr-4": { "phpseclib\\": "phpseclib/" }
require_once __DIR__ . '/bootstrap.php';
\Fedora\Autoloader\Autoload::addPsr4('phpseclib\\', __DIR__);

