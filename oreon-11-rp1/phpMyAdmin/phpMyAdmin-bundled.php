<?php

if (!isset($_SERVER['argv'][1])) {
	echo "Missing arg\n";
	exit(1);
}
$pkgs = file_get_contents($_SERVER['argv'][1]);
if (!$pkgs) {
	echo "can't read json file\n";
	exit(2);
}

$pkgs = json_decode($pkgs, true);
if (!is_array($pkgs)) {
	echo "can't decode json file\n";
	exit(3);
}

$lic = [];
if (isset($pkgs['packages'])) {
	$res = [];
    foreach($pkgs["packages"] as $pkg) {
		$lic = implode(" and ", $pkg["license"]);
		if (!isset($res[$lic])) $res[$lic] = [];
		$res[$lic][] = sprintf("Provides:  bundled(php-composer(%s)) = %s", $pkg["name"], ltrim($pkg["version"], "v"));
	}
	ksort($res);
	foreach($res as $lic => $lib) {
		sort($lib);
		printf("# License %s\n%s\n", $lic, implode("\n", $lib));
	}
} else if (isset($pkgs['dependencies'])) {
	foreach($pkgs['dependencies'] as $pkg) {
		$n = strtolower($pkg['name'] ?? $pkg['lib']);
		$n = str_replace('.js', '', $n);
		printf("Provides:  bundled(js-%s) = %s\n", $n, $pkg['version']);
		if (isset($pkg['license'])) {
			$lic[] = $pkg['license'];
		}
	}
} else {
	echo "unkown content\n";
	exit(4);
}
