%global source0_hash ec13c57ac4cdb3c010446137c2a36f72c16bfcffeb432d7ca19d15985080e221
%global gh_commit    7787ceff91365ba7d623ec410b8f429cdebb4f63
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_date      2026-02-20
%global gh_owner     FriendsOfPHP
%global gh_project   PHP-CS-Fixer
Name:           php-cs-fixer
Version:        3.95.25
Release:        1%{?dist}
Summary:        PHP Coding Standards Fixer
License:        MIT AND BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source2:        makesrc.sh
Patch0:         %{name}-autoload.patch
BuildArch:      noarch
Requires:       php(language) >= 8.1
Requires:       php-json
Requires:       php-tokenizer
Requires:       php-dom
Requires:       php-intl
Requires:       php-mbstring
Obsoletes:      php-cs-fixer3 < 3.5
Provides:       php-cs-fixer3 = %{version}
# oreon:deps
BuildRequires:  composer-generators
BuildRequires:  php(language)
BuildRequires:  php-cli
BuildRequires:  php-json
# /oreon:deps
%description
The PHP Coding Standards Fixer (PHP CS Fixer) tool fixes your code to follow
standards; whether you want to follow PHP coding standards as defined in the
PSR-1, PSR-2, etc., or other community driven ones like the Symfony one. You
can also define your (team's) style through configuration.

It can modernize your code (like converting the pow function to the ** operator
on PHP 5.6) and (micro) optimize it.

If you are already using a linter to identify coding standards problems in your
code, you know that fixing them by hand is tedious, especially on large
projects. This tool does not only detect them, but also fixes them for you.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}
%patch -P0 -p1 -b .rpm

# Fix version
#sed -e '/VERSION/s/3.68.6-DEV/%{version}/' -i src/Console/Application.php
# check version
grep "'%{version}'" src/Console/Application.php

%build

%install
: Library
mkdir -p      %{buildroot}%{_datadir}/%{name}
cp -pr src    %{buildroot}%{_datadir}/%{name}/src
cp -pr vendor %{buildroot}%{_datadir}/%{name}/vendor
: Command
install -Dpm755 %{name} %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%check

sed -e 's:%{_datadir}:%{buildroot}%{_datadir}:' -i %{name}
PHP_CS_FIXER_IGNORE_ENV=1 ./%{name} --version
PHP_CS_FIXER_IGNORE_ENV=1 ./%{name} --version | grep %{version}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
