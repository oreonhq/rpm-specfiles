%global source0_hash 33b9810f3b59ba1f654f6597bb2518cd684f96678ed26d3466b0bfa3f0eeaf4c

%global composer_vendor   openpsa
%global composer_project  universalfeedcreator
Name: php-%{composer_vendor}-%{composer_project}

Version: 1.9.0
Release: 5%{?dist}

Summary: RSS and Atom feed generator
License: LGPL-2.1-or-later

%global repo_owner  flack
%global repo_name   UniversalFeedCreator
URL: https://github.com/%{repo_owner}/%{repo_name}
Source0: %{URL}/archive/v%{version}/%{repo_name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-simplexml

BuildRequires: php-composer(phpunit/phpunit) >= 10
BuildRequires: php-composer(phpunit/phpunit) < 11

BuildRequires: php-fedora-autoloader-devel

Requires: php-date
Requires: php-pcre
Requires: php-simplexml

Requires: php-composer(fedora/autoloader)

# Composer
Provides: php-composer(%{composer_vendor}/%{composer_project}) = %{version}

%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgdir %{phpdir}/%{composer_vendor}-%{composer_project}

%description
RSS and Atom feed generator. Supported formats: RSS0.91, RSS1.0, RSS2.0,
PIE0.1 (deprecated), MBOX, OPML, ATOM, ATOM0.3, HTML, JS, PHP, JSON.

Autoloader: %{pkgdir}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{repo_name}-%{version}

%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir lib/ \
	./composer.json
echo 'require_once __DIR__ . "/constants.php";' >> autoload.php
cat autoload.php

%install
install -d -m 755 %{buildroot}%{phpdir}
cp -a lib %{buildroot}%{pkgdir}

cp autoload.php %{buildroot}%{pkgdir}/autoload.php

%check
# Fix outdated class names in tests
find test/ -name '*.php' -exec sed -e 's/PHPUnit_Framework_/\\PHPUnit\\Framework\\/g' -i '{}' '+'

phpunit10 --bootstrap %{buildroot}%{pkgdir}/autoload.php

%files
%doc *.md
%doc composer.json
%license LICENSE
%{pkgdir}/

%changelog
%autochangelog
