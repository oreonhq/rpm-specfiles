%global source0_hash 3b4c2a730de7dfdb2ef8035bb6ddfa2091d66418c665b57a039f8ddd494ebd48

%global	handlebars_git 36d52a2c199f50e3b636f4334b1daa8d2cdc3a5f
%global	mustache_git 83b0721610a4e11832e83df19c73ace3289972b9

Name:		php-zordius-lightncandy
Version:	1.2.6
Release:	11%{?dist}
Summary:	An extremely fast PHP implementation of handlebars and mustache

License:	MIT
URL:		https://github.com/zordius/lightncandy
Source0:	https://github.com/zordius/lightncandy/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Tests require data from third-party repositories
Source1:	https://github.com/jbboehr/handlebars-spec/archive/%{handlebars_git}.tar.gz#/%{name}-handlebars.tar.gz
Source2:	https://github.com/mustache/spec/archive/%{mustache_git}.tar.gz#/%{name}-mustache.tar.gz

BuildArch:	noarch

#BuildRequires:	php-phpunit-PHPUnit
BuildRequires:	php-theseer-autoload

Requires:	php(language) >= 5.3.0
Requires:	php-pcre
Requires:	php-reflection
Requires:	php-spl

Provides:	php-composer(zordius/lightncandy) = %{version}

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

# Tests have been removed from upstream tarball
#check
#phpunit -v --filter test

%files
%license LICENSE.md
%doc HISTORY.md README.md UPGRADE.md
%{_datadir}/php/zordius

%changelog
%autochangelog
