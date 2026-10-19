%global source0_hash fd4d482f949e486a0e0ceb65877ab88b363612ef108ba7d279acea1452d8ae6c
%bcond_with tests
%undefine __brp_mangle_shebangs
%global gh_commit    bb87e28e7d7b8d9a7fda231d37457c9210faf6ce
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     nikic
%global gh_project   PHP-Parser
%global pk_project   php-parser
%global php_home     %{_datadir}/php
%global major        3
%global eolv1   0
%global eolv2   0
Name:           php-%{gh_owner}-%{pk_project}%{major}
Version:        5.9.0
Release:        1%{?dist}
Summary:        A PHP parser written in PHP - version 3
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Patch0:         %{name}-rpm.patch
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 5.5
Requires:       php-tokenizer
Requires:       php-filter
Requires:       php-json
Requires:       php-pcre
Requires:       php-spl
Requires:       php-xmlreader
Requires:       php-xmlwriter
Requires:       php-cli
Provides:       php-composer(%{gh_owner}/%{pk_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-composer(phpunit/phpunit)
BuildRequires:  php-filter
BuildRequires:  php-json
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
# /oreon:deps
%description
This is a PHP 5.2 to PHP 7.1 parser written in PHP.
Its purpose is to simplify static code analysis and manipulation.

This package provides the library version %{major} and the php-parse%{major} command.
The php-nikic-php-parser4 package provides the library version 4.

Documentation: https://github.com/nikic/PHP-Parser/tree/master/doc

Autoloader: %{php_home}/PhpParser%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%patch -P0 -p1 -b .rpm

%build

%install
: Library
mkdir -p                 %{buildroot}%{php_home}
cp -pr lib/PhpParser     %{buildroot}%{php_home}/PhpParser%{major}
cp -p  lib/bootstrap.php %{buildroot}%{php_home}/PhpParser%{major}/autoload.php
: Command
install -Dpm 0755 bin/php-parse %{buildroot}%{_bindir}/php-parse%{major}
%oreon_autofiles main

%check

%if %{with tests}
: Test the command
sed -e 's:%{php_home}:%{buildroot}%{php_home}:' \
    bin/php-parse > bin/php-parse-test
php bin/php-parse-test --help
: Test suite autoloader
sed -e 's:@BUILDROOT@:%{buildroot}:' -i test/bootstrap.php
: Upstream test suite
ret=0
for cmd in php php73 php74 php80; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit \
      --filter '^((?!(testResolveLocations|testParse|testError)).)*$' \
      --verbose || ret=1
  fi
done
exit $ret
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
