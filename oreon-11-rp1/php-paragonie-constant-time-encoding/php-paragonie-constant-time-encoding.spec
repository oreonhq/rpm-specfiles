%global source0_hash 432bcbe7bc6b2137fd5078ef2bc1211bd197d42c88cb564d76d95866c3e6c80e
%global composer_vendor         paragonie
%global composer_project        constant_time_encoding
%global composer_namespace      ParagonIE/ConstantTime
%global github_owner            paragonie
%global github_name             constant_time_encoding
%global commit0 e30811f7bc69e4b5b6d5783e712c06c8eabf0226
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
Name:       php-%{composer_vendor}-constant-time-encoding
Version:    3.1.3
Release:        1%{?dist}
Summary:        Constant-time Implementations of RFC 4648 Encoding
License:    MIT
URL:        https://github.com/%{github_owner}/%{github_name}
Source0:        https://github.com/%{composer_vendor}/%{composer_project}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tgz
Source1:    makesrc.sh
BuildArch:  noarch
Requires:   php(language) >= 7
Requires:   php-mbstring
Requires:   php-spl
Suggests:   php-sodium
Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-mbstring
BuildRequires:  php-spl
BuildRequires:  phpunit9
# /oreon:deps
%description
Based on the constant-time base64 implementation made by Steve "Sc00bz" 
Thomas, this library aims to offer character encoding functions that do 
not leak information about what you are encoding/decoding via processor 
cache misses.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{github_name}-%{commit0}

%build

%{_bindir}/phpab -t fedora -o src/autoload.php src
%install
mkdir -p %{buildroot}%{_datadir}/php/%{composer_namespace}
cp -pr src/* %{buildroot}%{_datadir}/php/%{composer_namespace}
%oreon_autofiles main

%check

%{_bindir}/phpab -t fedora -o tests/autoload.php src tests
%{_bindir}/phpunit9 tests --verbose --bootstrap=tests/autoload.php
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
