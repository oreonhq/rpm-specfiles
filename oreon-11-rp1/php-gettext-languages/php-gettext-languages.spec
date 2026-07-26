%global source0_hash 34f5b569d547ee76f99d26e2c73927eaa38f8449644114d2d1a5b33dc9cdf0c8

Name:       php-gettext-languages
Version:    2.12.1
Release:    1%{?dist}
BuildArch:  noarch

License:    MIT and Unicode-DFS-2016
Summary:    Generate gettext language lists with plural rules
URL:        https://github.com/mlocati/cldr-to-gettext-plural-rules
# Upstream removes the tests from the archive, so the tarball is manually built from a checkout.
# https://github.com/mlocati/cldr-to-gettext-plural-rules/issues/11
#
# To build the tarball:
#
# $ git clone https://github.com/php-gettext/Languages.git
# $ cd Languages
# $ rm .gitattributes
# $ touch .gitattributes
# $ git archive -o cldr-to-gettext-plural-rules-VERSION.tar.gz --prefix cldr-to-gettext-plural-rules-VERSION/ --worktree-attributes VERSION
Source0:    cldr-to-gettext-plural-rules-%{version}.tar.gz

BuildRequires: php-composer(fedora/autoloader)
BuildRequires: phpunit10

Requires:   php(language) >= 5.4.0
Requires:   php-cli
Requires:   php-dom
Requires:   php-iconv
Requires:   php-json

Provides:   php-composer(gettext/languages) = %{version}

%description
A library that can generate gettext language lists automatically
generated from CLDR data.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n cldr-to-gettext-plural-rules-%{version}

sed -i "s:require_once.*:require_once '%{_datadir}/php/Gettext/Languages/autoloader.php';:" bin/export-plural-rules

%install
install -d -p -m 0755 %{buildroot}/%{_datadir}/php
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Gettext
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Gettext/Languages

install -Dpm 0755 bin/export-plural-rules %{buildroot}/%{_bindir}/%{name}-export-plural-rules
install -Dpm 0755 bin/import-cldr-data    %{buildroot}/%{_bindir}/%{name}-import-cldr-data

cp -ar src/* %{buildroot}/%{_datadir}/php/Gettext/Languages/
cp -ar tests/test %{buildroot}/%{_datadir}/php/Gettext/Languages/Test

%check
sed -i "s:require_once.*:require_once '%{buildroot}/%{_datadir}/php/Gettext/Languages/autoloader.php';:" tests/bootstrap.php

sed -i "s:require_once.*:require_once '%{buildroot}/%{_datadir}/php/Gettext/Languages/autoloader.php';:" bin/export-plural-rules
phpunit10 --bootstrap tests/bootstrap.php

%files
%license LICENSE
%license UNICODE-LICENSE.txt
%doc composer.json
%doc README.md
%{_bindir}/%{name}-export-plural-rules
%{_bindir}/%{name}-import-cldr-data
%{_datadir}/php/Gettext

%changelog
%autochangelog
