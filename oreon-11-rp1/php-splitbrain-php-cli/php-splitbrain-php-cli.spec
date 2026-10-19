%global source0_hash 82276c75efbf030dfd66d58842f66e8c80969396c0a45d4df70615139f57456c
%global author   splitbrain
%global project  php-cli
Name: php-%{author}-%{project}
Version: 1.3.4
Release:        1%{?dist}
Summary:        PHP library to build command line tools
License: MIT
URL: http://splitbrain.github.io/php-cli/
Source0:        https://github.com/%{author}/%{project}/archive/%{version}/%{project}-%{version}.tar.gz
BuildArch: noarch
%global with_tests 1
%if 0%{?with_tests}
%endif
Requires: php(language) >= 8.0.0
Requires: php-pcre
Requires: php-composer(fedora/autoloader)
Provides: php-composer(%{author}/%{project}) = %{version}
%{!?phpdir:  %global phpdir  %{_datadir}/php}
%global pkgauthordir %{phpdir}/%{author}
%global pkgdir %{pkgauthordir}/phpcli
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  phpunit8
# /oreon:deps
%description
PHP-CLI is a simple library that helps with creating nice looking
command line scripts. It takes care of option parsing, help page generation,
automatic width adjustment and colored output.

It is lightweight and has no 3rd party dependencies.
Note: this is for non-interactive scripts only.
It has no readline or similar support.

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

phpunit8 --verbose --bootstrap %{buildroot}%{pkgdir}/autoload.php
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
