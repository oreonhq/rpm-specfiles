%global source0_hash 14b302426fdce9df3774ea64775207de5b3fc0cf3a4eafcf930b997a29314af5
%bcond_without      tests
%global gh_commit    01a7927842abf3e10df3d9c2d9b0cc9d813a3fcc
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   xml
%global pk_vendor    sabre
%global pk_project   %{gh_project}
%global ns_vendor    Sabre
%global ns_project   Xml
%global major        2
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        XML library that you may not hate
Version:        2.2.11
Release:        1%{?dist}
URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD-3-Clause
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.1
Requires:       php-xmlwriter
Requires:       php-xmlreader
Requires:       php-dom
Requires:      (php-composer(sabre/uri) >= 1.0   with  php-composer(sabre/uri) <  3)
Requires:       php-libxml
Requires:       php-pcre
Requires:       php-spl
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sabre/uri) >= 1.0 with php-composer(sabre/uri) < 3)
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-libxml
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
BuildRequires:  phpunit9
# /oreon:deps
%description
The sabre/xml library is a specialized XML reader and writer.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    [
        '%{_datadir}/php/Sabre/Uri2/autoload.php',
        '%{_datadir}/php/Sabre/Uri/autoload.php',
    ],
]);

// Functions
if (!function_exists('Sabre\\Xml\\Serializer\\enum')) {
    require_once __DIR__ . '/Deserializer/functions.php';
    require_once __DIR__ . '/Serializer/functions.php';
}
EOF

%build

%install
mkdir -p %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr lib %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main

%check

: Check version
php -r '
require "%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php";
echo  Sabre\Xml\Version::VERSION . "\n";
exit (Sabre\Xml\Version::VERSION === "%{version}" ? 0 : 1);
'
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require_once '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Sabre\\Xml\\', dirname(__DIR__).'/tests/Sabre/Xml/');
EOF
cd tests
: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
