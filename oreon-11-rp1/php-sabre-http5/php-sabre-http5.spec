%global source0_hash 1cbff6d6915f85003f50052b8cf41fb2ea7530cdf748211cb24b166d6e41dc34
%bcond_without      tests
%global gh_commit    7c2a14097d1a0de2347dcbdc91a02f38e338f4db
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   http
%global pk_vendor    sabre
%global pk_project   %{gh_project}
%global ns_vendor    Sabre
%global ns_project   HTTP
%global major        5
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Library for dealing with http requests and responses
Version:        5.1.13
Release:        1%{?dist}
URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD-3-Clause
Source0:        %{gh_project}s://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) >= 7.1
Requires:       php-mbstring
Requires:       php-ctype
Requires:       php-curl
Requires:      (php-composer(sabre/event) >= 4.0   with php-composer(sabre/event) < 6)
Requires:      (php-composer(sabre/uri)   >= 2.0   with php-composer(sabre/uri)   < 3)
Requires:       php-date
Requires:       php-hash
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xml
Requires:       php-composer(fedora/autoloader)
Conflicts:      php-sabre-dav < 1.9
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  (php-composer(sabre/event) >= 4.0 with php-composer(sabre/event) < 6)
BuildRequires:  (php-composer(sabre/uri) >= 2.0 with php-composer(sabre/uri) < 3)
BuildRequires:  php(language)
BuildRequires:  php-ctype
BuildRequires:  php-curl
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-hash
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-xml
BuildRequires:  phpunit9
# /oreon:deps
%description
This library provides a toolkit to make working with the HTTP protocol easier.

Most PHP scripts run within a HTTP request but accessing information about
the HTTP request is cumbersome at least, mainly do to superglobals and the
CGI standard.

There's bad practices, inconsistencies and confusion.
This library is effectively a wrapper around the following PHP constructs:

For Input:
    $_GET
    $_POST
    $_SERVER
    php://input or $HTTP_RAW_POST_DATA.

For output:
    php://output or echo.
    header()

What this library provides, is a Request object, and a Response object.
The objects are extendable and easily mockable.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Dependencies
\Fedora\Autoloader\Dependencies::required([
    '%{_datadir}/php/Sabre/Event5/autoload.php',
    '%{_datadir}/php/Sabre/Uri2/autoload.php',
]);

// Functions
if (!function_exists('Sabre\\HTTP\\parseDate')) {
    require_once __DIR__ . '/functions.php';
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
echo  Sabre\HTTP\Version::VERSION . "\n";
exit (Sabre\HTTP\Version::VERSION === "%{version}" ? 0 : 1);
'
%if %{with tests}
cd tests
ln -sf %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php bootstrap.php
: Start a Development web server
PORT=$(expr 8080 + %{?fedora}%{?rhel})
sed -e "s/localhost:8000/127.0.0.1:$PORT/" -i phpunit.xml
%{_bindir}/php   -S 127.0.0.1:$PORT -t $PWD/www &>web.log &
PHPPID=$!
: Run upstream test suite against installed library
ret=0
for cmdarg in "php %{phpunit}" php81 php82 php83 php84 php85; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done
kill $PHPPID || :
exit $ret
%else
: Skip upstream test suite
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
