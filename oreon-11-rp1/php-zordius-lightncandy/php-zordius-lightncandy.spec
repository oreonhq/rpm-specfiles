%global source2_hash 3b4c2a730de7dfdb2ef8035bb6ddfa2091d66418c665b57a039f8ddd494ebd48
%global source1_hash 23c52dba7a00d5fe025fc9d32a7f67c545468b49987b90e1003a77bc016ac76b
%global source0_hash 29b4e39ccea2f43e5f6e67287992e169bf1c03025c0226dc2e3f8875f4b5cd0e
%global	handlebars_git 36d52a2c199f50e3b636f4334b1daa8d2cdc3a5f
%global	mustache_git 83b0721610a4e11832e83df19c73ace3289972b9
Name:		php-zordius-lightncandy
Version:	1.2.6
Release:        1%{?dist}
Summary:        An extremely fast PHP implementation of handlebars and mustache
License:	MIT
URL:		https://github.com/zordius/lightncandy
Source0:        https://github.com/zordius/lightncandy/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	https://github.com/jbboehr/handlebars-spec/archive/%{handlebars_git}.tar.gz#/%{name}-handlebars.tar.gz
Source2:	https://github.com/mustache/spec/archive/%{mustache_git}.tar.gz#/%{name}-mustache.tar.gz
BuildArch:	noarch
Requires:	php(language) >= 5.3.0
Requires:	php-pcre
Requires:	php-reflection
Requires:	php-spl
Provides:	php-composer(zordius/lightncandy) = %{version}
# oreon:deps
BuildRequires:  php-theseer-autoload
# /oreon:deps
%description
An extremely fast PHP implementation of handlebars ( http://handlebarsjs.com/ )
and mustache ( http://mustache.github.io/ ).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn lightncandy-%{version}
tar zxf %{SOURCE1}
cp -rp handlebars-spec-%{handlebars_git}/spec specs/handlebars/
tar zxf %{SOURCE2}
cp -rp spec-%{mustache_git}/specs specs/mustache/

%build

phpab --output src/autoload.php src
%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/zordius/lightncandy
cp -p src/*.php %{buildroot}%{_datadir}/php/zordius/lightncandy
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
