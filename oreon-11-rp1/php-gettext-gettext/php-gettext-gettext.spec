%global source0_hash 63670469b16496f42d12b2059dca89b7dd626cd6519b8171f00b1888ce2f15a2

%global gh_owner     php-gettext
%global gh_project   Gettext

Name:       php-gettext-gettext
Version:    5.7.0
Release:    9%{?dist}
BuildArch:  noarch

License:    MIT
Summary:    PHP gettext manager
URL:        https://github.com/%{gh_owner}/%{gh_project}
Source0:    %{url}/archive/v%{version}.tar.gz
# Upstream strips the tests from the tarball, so we have to generate it manually.
# dltests.sh is used to do this, and is included in this repository.
Source1:    tests-v%{version}.tar.bz2

BuildRequires: dos2unix
%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
BuildRequires: (php-composer(gettext/languages) >= 2.3.0 with php-composer(gettext/languages) < 3)
%else
BuildRequires: php-gettext-languages >= 2.3.0
%endif
BuildRequires: phpunit8

Requires:   php(language) >= 5.4.0
Requires:   php-date
Requires:   php-dom
Requires:   php-gettext
Requires:   php-json
Requires:   php-pcre
Requires:   php-simplexml
Requires:   php-spl
Requires:   php-tokenizer

%if 0%{?fedora} >= 27 || 0%{?rhel} >= 8
Requires:  (php-composer(gettext/languages) >= 2.3.0 with php-composer(gettext/languages) < 3)
%else
Requires:   php-gettext-languages >= 2.3.0
%endif

Provides:   php-composer(gettext/gettext) = %{version}

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

%check
# Upstream no longer contains tests/bootstrap.php file
#sed -i "s:include_once.*:\ninclude_once '%{buildroot}/%{_datadir}/php/Gettext/autoload.php';:" tests/bootstrap.php

# gettext has some optional dependencies that we are not integrating with at this time (we can later
# if desired). Thus, we need to skip the tests on these integration points since they will fail
# without the dependencies. There is an upstream issue about compatibility issues with Twig:
# https://github.com/oscarotero/Gettext/issues/137

: run upstream test suite with all installed PHP versions
ret=0
for cmd in php php71 php72 php73 php74; do
  if which $cmd; then
    $cmd %{_bindir}/phpunit8 --bootstrap %{buildroot}/%{_datadir}/php/Gettext/autoload.php tests --exclude-group default
  fi
done
exit $ret

%files
%license LICENSE
%doc CHANGELOG.md
%doc composer.json
%doc CONTRIBUTING.md
%doc README.md
%{_datadir}/php/Gettext/*

%changelog
%autochangelog
