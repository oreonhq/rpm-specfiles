%global source0_hash 09420f928f27d467130e1550c7fde0920c2aedef0a17397884fbe76cb9f2eaec

%global composer_vendor         paragonie
%global composer_project        constant_time_encoding
%global composer_namespace      ParagonIE/ConstantTime

%global github_owner            paragonie
%global github_name             constant_time_encoding

%global commit0 e30811f7bc69e4b5b6d5783e712c06c8eabf0226
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:       php-%{composer_vendor}-constant-time-encoding
Version:    2.8.2
Release:    2%{?dist}
Summary:    Constant-time Implementations of RFC 4648 Encoding

License:    MIT

URL:        https://github.com/%{github_owner}/%{github_name}
Source0:    %{url}/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tgz
Source1:    makesrc.sh

BuildArch:  noarch

# "php": "^7|^8"
BuildRequires:  php(language) >= 7
BuildRequires:  php-mbstring
BuildRequires:  php-spl
# "phpunit/phpunit": "^6|^7|^8|^9"
BuildRequires:  phpunit9
BuildRequires:  php-fedora-autoloader-devel

# "php": "^7|^8"
Requires:   php(language) >= 7
Requires:   php-mbstring
Requires:   php-spl

Suggests:   php-sodium

Provides:   php-composer(%{composer_vendor}/%{composer_project}) = %{version}

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

%check
%{_bindir}/phpab -t fedora -o tests/autoload.php src tests
%{_bindir}/phpunit9 tests --verbose --bootstrap=tests/autoload.php

%files
%dir %{_datadir}/php/ParagonIE
%{_datadir}/php/%{composer_namespace}
%doc README.md composer.json
%license LICENSE.txt

%changelog
%autochangelog
