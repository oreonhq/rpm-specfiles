%global source0_hash 7274549a7f650bed04778dd9917b972460f5e24a92840e2444f2c28640cf39a3
%global gh_owner     php-gettext
%global gh_project   Gettext
Name:       php-gettext-gettext
Version:    5.7.3
Release:        1%{?dist}
BuildArch:  noarch
License:    MIT
Summary:        PHP gettext manager
URL:        https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{gh_project}/archive/v%{version}.tar.gz
Source1:    tests-v%{version}.tar.bz2
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%else
%endif
Requires:   php(language) >= 5.4.0
Requires:   php-date
Requires:   php-dom
Requires:   php-gettext
Requires:   php-json
Requires:   php-pcre
Requires:   php-simplexml
Requires:   php-spl
Requires:   php-tokenizer
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
Requires:  (php-composer(gettext/languages) >= 2.3.0 with php-composer(gettext/languages) < 3)
%else
Requires:   php-gettext-languages >= 2.3.0
%endif
Provides:   php-composer(gettext/gettext) = %{version}
# oreon:deps
BuildRequires:  (php-composer(gettext/languages) >= 2.3.0 with php-composer(gettext/languages) < 3)
BuildRequires:  dos2unix
BuildRequires:  phpunit8
# /oreon:deps
%description
Gettext is a PHP (5.3) library to import/export/edit gettext from PO,
MO, PHP, JS files, etc.

Autoloader: %{_datadir}/php/Gettext/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -a1 -n Gettext-%{version}

# The documentation has the wrong newline codes
dos2unix *.md

%build

: Create autoloader
cat <<'AUTOLOAD' | tee src/autoload.php
<?php
/**
 * Autoloader for %{name} and its' dependencies
 * (created by %{name}-%{version}-%{release}).
 */
require_once '%{_datadir}/php/Fedora/Autoloader/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('Gettext\\', __DIR__);
\Fedora\Autoloader\Autoload::addPsr4('Gettext\\Tests\\', 'tests');
\Fedora\Autoloader\Dependencies::required(array(
    '%{_datadir}/php/Gettext/Languages/autoloader.php'
));
AUTOLOAD
%install
install -d -p -m 0755 %{buildroot}/%{_datadir}/php
install -d -p -m 0755 %{buildroot}/%{_datadir}/php/Gettext
cp -ar src/* %{buildroot}/%{_datadir}/php/Gettext/
%oreon_autofiles main

%check

: run upstream test suite with all installed PHP versions
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --bootstrap %{buildroot}/%{_datadir}/php/Gettext/autoload.php tests --exclude-group default
  fi
done
exit $ret
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
