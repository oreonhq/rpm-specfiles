%global source0_hash b4ec14c6f5b009922ef9e5b017d11bed6efc59d9aa02663a37e6127e42a9b7a4
%bcond_with tests
%global github_owner    nikic
%global github_name     PHP-Parser
%global github_version  5.9.0
%global github_commit   f78af2c9c86107aa1a34cd1dbb5bbe9eeb0d9f51
%global github_short    %(c=%{github_commit}; echo ${c:0:7})
%global lib_name        PhpParser
%global lib_name_old    PHPParser
%global php_min_ver     5.3
Name:          php-%{lib_name_old}
Version:       %{github_version}
Release:        1%{?dist}
Summary:        A PHP parser written in PHP - version 1
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/%{github_owner}/%{github_name}
Source0:        %{name}-%{version}-%{github_short}.tgz
Source1:       makesrc.sh
Patch0:        %{name}-command.patch
BuildArch:     noarch
%if %{with tests}
%endif
Requires:      php(language) >= %{php_min_ver}
Requires:      php-tokenizer
Requires:      php-filter
Requires:      php-pcre
Requires:      php-spl
Requires:      php-xmlreader
Requires:      php-xmlwriter
Provides:      php-composer(nikic/php-parser) = %{version}
# oreon:deps
BuildRequires:  /usr/bin/phpunit
BuildRequires:  php(language)
BuildRequires:  php-ctype
BuildRequires:  php-filter
BuildRequires:  php-pcre
BuildRequires:  php-spl
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlreader
BuildRequires:  php-xmlwriter
# /oreon:deps
%description
A PHP parser written in PHP to simplify static analysis and code manipulation.

This package provides the library version 1.
The php-nikic-php-parser3 package provides the library version 3.
The php-nikic-php-parser4 package provides the library version 4.

Autoloader: '%{_datadir}/php/%{lib_name}/autoload.php';

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{github_name}-%{github_short}

%patch -P0 -p0 -b .rpm
rm lib/%{lib_name}/*rpm

%build

%install
mkdir -p -m 755 %{buildroot}%{_datadir}/php
cp -rp lib/%{lib_name} %{buildroot}%{_datadir}/php/%{lib_name}
mkdir -p -m 755 %{buildroot}%{_datadir}/php/%{lib_name_old}
ln -s ../%{lib_name}/Autoloader.php \
    %{buildroot}%{_datadir}/php/%{lib_name_old}/Autoloader.php
%oreon_autofiles main

%check

%if %{with tests}
%{_bindir}/phpunit \
    --bootstrap %{buildroot}%{_datadir}/php/%{lib_name}/autoload.php \
    --filter '^((?!(testResolveLocations)).)*$' \
    --verbose
%else
: Test suite disabled
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
