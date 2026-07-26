<?php
$CONFIG = [
    "log_type" => "syslog",
    "datadirectory" => "/var/lib/nextcloud/data",
    "updatechecker" => false,
    "check_for_working_htaccess" => false,
    "asset-pipeline.enabled" => false,
    "assetdirectory" => '/var/lib/nextcloud',
    "preview_libreoffice_path" => '/usr/bin/libreoffice',


    "apps_paths" => [
        [   'path'=> '/usr/share/nextcloud/apps',
            'url' => '/apps',
            'writable' => false,
        ],
        [
            'path' => '/var/lib/nextcloud/apps',
            'url' => '/apps-appstore',
            'writable' => true,
        ],
    ],
];
