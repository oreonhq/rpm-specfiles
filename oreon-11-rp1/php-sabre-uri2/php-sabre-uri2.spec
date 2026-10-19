%global source0_hash 112162012f5dd9c62620d11ee16ba5ea79e256c1bf41608a5abd9e3bbbe5bb46
%bcond_without       tests
%global gh_commit    b76524c22de90d80ca73143680a8e77b1266c291
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sabre-io
%global gh_project   uri
%global pk_vendor    sabre
%global pk_project   %{gh_project}
%global ns_vendor    Sabre
%global ns_project   Uri
%global major        2
Name:           php-%{pk_vendor}-%{pk_project}%{major}
Summary:        Functions for making sense out of URIs
Version:        2.3.4
Release:        1%{?dist}
URL:            https://github.com/%{gh_owner}/%{gh_project}
License:        BSD-3-Clause
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%global phpunit %{_bindir}/phpunit9
%endif
Requires:       php(language) > 7.4
Requires:       php-pcre
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-pcre
BuildRequires:  phpunit9
# /oreon:deps
%description
sabre/uri is a lightweight library that provides several functions for
working with URIs, staying true to the rules of RFC3986.

Partially inspired by Node.js URL library, and created to solve real
problems in PHP applications. 100% unitested and many tests are based
on examples from RFC3986.

The library provides the following functions:
* resolve to resolve relative urls.
* normalize to aid in comparing urls.
* parse, which works like PHP's parse_url.
* build to do the exact opposite of parse.
* split to easily get the 'dirname' and 'basename' of a URL without
  all the problems those two functions have.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

phpab -t fedora -o lib/autoload.php lib
cat << 'EOF' | tee -a lib/autoload.php

// Functions
if (!function_exists('Sabre\\Uri\\resolve')) {
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
echo  Sabre\Uri\Version::VERSION . "\n";
exit (Sabre\Uri\Version::VERSION === "%{version}" ? 0 : 1);
'
%if %{with tests}
: Run upstream test suite against installed library
mkdir vendor
ln -s %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php vendor/autoload.php
cd tests
for cmdarg in "php %{phpunit}" php81 php82 php83 php84; do
  if which $cmdarg; then
    set $cmdarg
    $1 ${2:-%{_bindir}/phpunit9} --verbose || ret=1
  fi
done
exit $ret
%else
: Skip upstream test suite
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
