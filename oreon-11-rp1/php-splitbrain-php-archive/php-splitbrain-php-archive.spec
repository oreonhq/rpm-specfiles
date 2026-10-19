%global source0_hash 405141eeaf23e6069a93c29272c692fc0a7ca6581adcb133d50fc8d601e96f88
%global author   splitbrain
%global project  php-archive
Name: php-%{author}-%{project}
Version: 1.4.1
Release:        1%{?dist}
Summary:        Pure-PHP implementation to read and write TAR and ZIP archives
License: MIT
URL: https://splitbrain.github.io/php-archive/
Source0:        https://github.com/%{author}/%{project}/archive/%{version}/%{project}-%{version}.tar.gz
BuildArch: noarch
%global with_tests 1
%if 0%{?with_tests}
%endif
Requires: php(language) >= 7.0.0
Requires: php-date
Requires: php-hash
Requires: php-pcre
Requires: php-composer(fedora/autoloader)
Recommends: php-bz2
Recommends: php-iconv
Recommends: php-mbstring
Recommends: php-zlib
Provides: php-composer(%{author}/%{project}) = %{version}
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/PHPArchive
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-bz2
BuildRequires:  php-composer(mikey179/vfsstream)
BuildRequires:  php-date
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-hash
BuildRequires:  php-iconv
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-zip
BuildRequires:  php-zlib
BuildRequires:  phpunit8
# /oreon:deps
%description
PHPArchive allows to handle new ZIP and TAR archives without the need
for any special PHP extensions (gz and bzip are needed for compression).
It can create new files or extract existing ones.

To keep things simple, the modification (adding or removing files)
of existing archives is not supported.

Autoloader: %{pkgdir}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{project}-%{version}

%build

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
%oreon_autofiles main
%if 0%{?with_tests}
%check

cat > bootstrap.php <<EOF
<?php
require '%{phpdir}/org/bovigo/vfs/autoload.php';
require '%{buildroot}%{pkgdir}/autoload.php';
EOF
phpunit8 --verbose --bootstrap ./bootstrap.php 
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
