%global source0_hash 48459e265f463c960f0c8e3de280334a89c6c9100cc7c200e2ecc71078655e40

%global author   kissifrot
%global project  php-ixr
Name: php-%{author}-%{project}

Version: 1.8.4
Release: 3%{?dist}

Summary: XML-RPC library for PHP
License: BSD

URL: https://github.com/%{author}/%{project}

# Starting with v1.8.4, upstrean marked tests
# as excluded from auto-generated tarballs.
Source0: %{name}-%{version}.zip

# Script to clone git repo (will include the tests!)
# and zip it up
Source1: makesrc.sh

BuildArch: noarch

%global with_tests 1

BuildRequires: php(language) >= 5.4.0
BuildRequires: php-fedora-autoloader-devel

%if 0%{with_tests}
BuildRequires: php-curl
BuildRequires: php-date
BuildRequires: php-pcre
BuildRequires: php-xml
BuildRequires: phpunit8
%endif

Requires: php-composer(fedora/autoloader)

Requires: php(language) >= 5.4.0
Requires: php-curl
Requires: php-date
Requires: php-pcre
Requires: php-xml

Provides: php-composer(%{author}/%{project}) = %{version}

# Use a PSR-0 compatible directory hierarchy
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/IXR

%description
PHP-IXR is an XML-RPC library designed primarily for ease of use.
It incorporates both client and server classes, and is designed to hide
as much of the workings of XML-RPC from the user as possible. A key feature
of the library is automatic type conversion from PHP types to XML-RPC types
and vice versa. This should enable developers to write web services
with very little knowledge of the underlying XML-RPC standard.

However, don't be fooled by it's simple surface. The library includes
a wide variety of additional XML-RPC specifications and has
all of the features required for serious web service implementations.

Autoloader: %{pkgdir}/autoload.php

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove tests from composer.json autoload list
sed -e '/"IXR\\\\tests\\\\":/d' -i composer.json

%build
# Create autoloader
phpab \
	--template fedora \
	--output autoload.php \
	--basedir src/ \
	./composer.json
cat autoload.php

%install
install -d -m 755 %{buildroot}%{pkgauthordir}
cp -a src %{buildroot}%{pkgdir}

cp autoload.php %{buildroot}%{pkgdir}/autoload.php

%if 0%{?with_tests}
%check
phpunit8 --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php
%endif

%files
%license LICENSE.txt
%doc composer.json
%doc README.md
%{pkgauthordir}/

%changelog
%autochangelog
